import face_recognition

def compare_faces():
    # 1. Load the known image and learn how to recognize it
    known_image = face_recognition.load_image_file("./img/adarsh.jpg")
    # Get the 128-dimensional face embedding for the image
    known_encoding = face_recognition.face_encodings(known_image)[0]
    # 2. Load the unknown image to test
    unknown_image = face_recognition.load_image_file("./img/random.jpg")
    try:
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
        
        # 3. Compare the faces
        # tolerance=0.6 is the default (lower means stricter matching)
        results = face_recognition.compare_faces([known_encoding], unknown_encoding, tolerance=0.6)

        if results[0]:
            print("Match Found! This is the known person.")
        else:
            print("No Match. This is a different person.")
            
    except IndexError:
        print("No faces were detected in one of the images.")

if __name__ == "__main__":
    compare_faces()