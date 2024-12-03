#this file just verifies if the script created the encodings

import pickle

with open("known_faces.pkl", "rb") as f:
    known_face_encodings, known_face_names = pickle.load(f)

print("Loaded known faces:")
for name in known_face_names:
    print(name)
