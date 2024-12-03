import tkinter as tk
from tkinter import filedialog, messagebox
import face_recognition
import pickle
import cv2
from PIL import Image, ImageTk
import numpy as np

with open("known_faces.pkl", "rb") as f:
    known_face_encodings, known_face_names = pickle.load(f)

def identify_face(unknown_encoding):
    face_distances = face_recognition.face_distance(known_face_encodings, unknown_encoding)
    min_distance = min(face_distances)
    threshold = 0.6  
    if min_distance < threshold:
        match_index = face_distances.tolist().index(min_distance)
        name = known_face_names[match_index]

        if name.startswith("group_members"):
            message = f"Identified as: Group Member ({name.split('/')[-1]})"
        elif name.startswith("famous_people"):
            message = f"Identified as: Famous Person ({name.split('/')[-1]})"
    else:
        message = "Unknown face"

    messagebox.showinfo("Identification Result", message)

def upload_image():
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.jpg *.jpeg *.png *.JPG")])
    if not file_path:
        return

    try:
        unknown_image = face_recognition.load_image_file(file_path)
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
        identify_face(unknown_encoding)
    except IndexError:
        messagebox.showerror("Error", "No face detected in the image.")

def open_camera():
    video_capture = cv2.VideoCapture(0)
    while True:
        ret, frame = video_capture.read()
        # convert the input frame from BGR to RGB
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb,model='hog')
        # the facial encodings for faces in the frame
        encodings = face_recognition.face_encodings(rgb,boxes,model='large')
        
        for (top, right, bottom, left), face_encoding in zip(boxes, encodings):
            #for top, right, bottom, left in boxes: # draw box around face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.6)
            name = "Unknown"
            #Use the known face with smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                cv2.rectangle(frame, (left, top), (right,bottom), (0, 255, 0), 2)
                cv2.putText(frame, name, (left+6, top-12), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
        
        cv2.imshow("ICSI 435 Project", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): # click 'q' to close program
            break
        
    video_capture.release()
    cv2.destroyAllWindows()
    
open_camera()