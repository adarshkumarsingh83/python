import os
import glob

import cv2
import numpy as np
import face_recognition

# Folder that holds one (or more) reference picture(s) per person.
# Each image filename (without extension) is used as that person's name,
# e.g. img/shakti.jpg -> "shakti", img/adarsh.jpg -> "adarsh".
KNOWN_FACES_DIR = "./img"


def load_known_faces(directory):
    """Load and encode every image in `directory` as a known person.

    Returns two parallel lists: the face encodings and their names.
    Images where no face can be detected are skipped with a warning.
    """
    known_face_encodings = []
    known_face_names = []

    image_paths = []
    for ext in ("*.jpg", "*.jpeg", "*.png"):
        image_paths.extend(glob.glob(os.path.join(directory, ext)))

    for image_path in sorted(image_paths):
        name = os.path.splitext(os.path.basename(image_path))[0]
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)

        if not encodings:
            print(f"[WARN] No face found in {image_path}, skipping.")
            continue

        # Use the first face found in each reference image.
        known_face_encodings.append(encodings[0])
        known_face_names.append(name)
        print(f"[INFO] Loaded known face: {name}")

    return known_face_encodings, known_face_names


def recognize_faces(known_face_encodings, known_face_names, tolerance=0.5):
    """Match every face in the live video against all known people."""
    # Initialize webcam
    video_capture = cv2.VideoCapture(0)

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()
        if not ret:
            break

        # Convert the image from BGR color (OpenCV default) to RGB color (face_recognition default)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        # Loop through each face found in this frame
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            name = "unknown"

            if known_face_encodings:
                # Compare this face against every known person and pick the closest match.
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = int(np.argmin(face_distances))

                # Only accept the match if it is within the tolerance threshold.
                if face_distances[best_match_index] <= tolerance:
                    name = known_face_names[best_match_index]

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.8, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video Face Recognition', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    known_face_encodings, known_face_names = load_known_faces(KNOWN_FACES_DIR)
    if not known_face_encodings:
        print("[ERROR] No known faces loaded. Add images to", KNOWN_FACES_DIR)
    else:
        recognize_faces(known_face_encodings, known_face_names)
