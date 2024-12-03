import face_recognition
import os
import pickle
import cv2

known_face_encodings = []
known_face_names = []

dataset_dir = "dataset"

for category in ["Leo", "famous_people"]:
    
    image = cv2.imread(image_path)
    rgb = cv2.cvtColor(image, cv2)
    
    category_folder = os.path.join(dataset_dir, category)
    for person_name in os.listdir(category_folder):
        person_folder = os.path.join(category_folder, person_name)
        if os.path.isdir(person_folder):  
            for filename in os.listdir(person_folder):
                image_path = os.path.join(person_folder, filename)
                image = face_recognition.load_image_file(image_path)
                encodings = face_recognition.face_encodings(image)
                if encodings:
                    known_face_encodings.append(encodings[0])
                    boxes = face_recognition.face_locations(rgb, model='hog')
                    known_face_names.append(f"{category}/{person_name}")

with open("known_faces.pkl", "wb") as f:
    pickle.dump((known_face_encodings, known_face_names), f)

print("Encoding complete. Encodings saved to 'known_faces.pkl'.")
