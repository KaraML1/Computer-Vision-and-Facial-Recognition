# Computer-Vision-Face-Detection-and-Recognition
Repository for ICSI435/535 (Artificial Intelligence I) Project

# Face Recognition GUI Application

Face recognition application with a GUI that allows users to upload an image to identify if the person in the image matches any known faces stored in the application’s dataset. Known faces include famous individuals.

## Features
- GUI built with Tkinter for ease of use.
- Ability to add new images and identify if the person is in the stored dataset.
- Distinguishes between group members and famous individuals.

## Prerequisites

To run this project, ensure you have Python installed on your system (Python 3.10 or 3.11).

### Required Libraries
- Run "pip install -r requirements.txt"
    - Includes 
        - OpenCV
        - Tkinter
        - Pillow

- Install the following Python libraries using `pip`:
```bash
pip install face-recognition dlib opencv-python-headless
```

- **face-recognition**: For face encoding and face comparison.
- **dlib**: Core library for face detection and encoding.
  - **Windows users**: Installing `dlib` requires **CMake** and **Visual Studio Build Tools**.
    - Download and install [CMake](https://cmake.org/download/) and add it to your PATH.
    - Download [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/), then install `dlib`.
- **opencv-python-headless**: For image processing, using the headless version since there’s no need for OpenCV’s GUI functionalities.
- **pillow**: For handling and displaying images in Tkinter.


## Running the Application

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/KaraML1/Computer-Vision-and-Facial-Recognition.git
   cd Computer-Vision-Face-Detection-and-Recognition
   ```

2. **Directory Structure**:
    - Organize your dataset images under a `dataset` folder, with subfolders for each category:
        ```
        dataset/
        ├── famous_people/
        ├── group_members/
        ```

3. **Add Images**:
   - Place images of known individuals (e.g., famous people and group members) in the respective folders. Use clear, front-facing images for best results. Make sure to properly name the file (check the existing images as examples).

4. **Encoding Faces**:
   - Run the encoding script (provided in the repository) to generate face encodings from the images and save them as a `pickle` file. This script processes all images in `dataset/` and saves their encodings to `known_faces.pkl`.
   - **Run this script each time you update or add new images to the dataset** to keep `known_faces.pkl` up-to-date.

5. **Ensure `known_faces.pkl` is in the Project Directory**:
   - Make sure the `known_faces.pkl` file is in the same directory as the main GUI script after you run the encoding script.

6. **Run the GUI Application**:
    - Add the names of your images in line 31 of face_recognition_app.py
   - Start the application with:
     ```bash
     python face_recognition_app.py
     ```

7. **Using the Application**:
   - Click the **"Take Picture"** button to take a picture or the **"Upload Image"** button to upload an image. The app will display the name if a match is found or show "Unknown Person" if no match is found.

## Additional Notes
- Ensure good lighting and image quality for better recognition accuracy.
- For any new images added to the dataset, re-run the encoding script to update the `known_faces.pkl` file.

## Troubleshooting

If you encounter any issues, make sure:
- The `dataset` folder is correctly structured with the necessary images.
- `known_faces.pkl` exists and is up-to-date with the images you want to recognize.
- All necessary libraries are installed and imported.



