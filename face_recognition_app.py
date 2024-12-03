import tkinter as tk
from tkinter import filedialog, messagebox
import face_recognition
import pickle
import cv2
from PIL import Image, ImageTk

with open("known_faces.pkl", "rb") as f:
    known_face_encodings, known_face_names = pickle.load(f)

vid = cv2.VideoCapture(0)

def identify_face(unknown_encoding):
    face_distances = face_recognition.face_distance(known_face_encodings, unknown_encoding)
    min_distance = min(face_distances)
    threshold = 0.6  
    if min_distance < threshold:
        match_index = face_distances.tolist().index(min_distance)
        name = known_face_names[match_index]

        if name.startswith("group_members"):
            message = f"Identified as: ({name.split('/')[-1]})"
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

def capture_image():
    result, frame = vid.read()
    if not result:
        messagebox.showerror("Error", "Failed to capture image from camera.")
        return

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    try:
        unknown_encoding = face_recognition.face_encodings(rgb_frame)[0]
        identify_face(unknown_encoding)
    except IndexError:
        messagebox.showerror("Error", "No face detected in the image.")

def open_camera():
    result, frame = vid.read()
    if result:
        opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        captured_image = Image.fromarray(opencv_image)
        photo_image = ImageTk.PhotoImage(image=captured_image)

        label_widget.photo_image = photo_image
        label_widget.configure(image=photo_image)

    label_widget.after(10, open_camera)

root = tk.Tk()
root.title("Face Recognition App")

label_widget = tk.Label(root)
label_widget.pack()

take_picture_button = tk.Button(root, text="Take Picture", command=capture_image)
take_picture_button.pack(pady=5)

upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack(pady=5)

open_camera()

root.geometry("900x1000")
root.mainloop()

vid.release()
cv2.destroyAllWindows()