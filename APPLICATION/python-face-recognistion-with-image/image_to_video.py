import cv2
import face_recognition

# Load your profile picture and encode it
known_image = face_recognition.load_image_file("./img/adarsh.jpg")
known_face_encoding = face_recognition.face_encodings(known_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [known_face_encoding]
known_face_names = ["adarsh"]

# Initialize webcam
video_capture = cv2.VideoCapture(0)


def recognize_face(face_encoding):
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
            # See if the face is a match for the known face(s)q
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "unknown"

            # If a match was found in known_face_encodings, use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

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
    recognize_face(known_face_encodings)