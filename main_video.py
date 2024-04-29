

def Recongntion(user):
    import Encryption_Folder
    import Decryption_Folder   
    import cv2
    from simple_facerec import SimpleFacerec

    # Encode faces from a folder
    sfr = SimpleFacerec()
    sfr.load_encoding_images(r"E:\Codeing\Python Language\Projects\Project_12_Folder_Encryption_(LOCK)\images")

    # Load Camera
    cap = cv2.VideoCapture(0)

    name = ""  # Initialize the name variable outside the loop

    while True:
        ret, frame = cap.read()

        # Detect Faces
        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, detected_name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

            cv2.putText(frame, detected_name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 2)

            # Update the 'name' variable with the detected name
            name = detected_name

        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if key == 27:
            break

        # Check if the recognized name is "Raiden"
        if name == "Raiden":
            if user == 'N':
                Encryption_Folder.Encrypt()
            elif user == 'D':
                Decryption_Folder.Decrypt()
                

    cap.release()
    cv2.destroyAllWindows()
