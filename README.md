# face-detection-sysytem

This Python-based application utilizes OpenCV to detect faces, smiles, and eyes in real-time from a webcam feed. It provides interactive controls to toggle detection features, highlight faces, capture screenshots, and record video with annotated frames. The project demonstrates the use of Haar cascade classifiers for facial feature detection and offers a simple yet effective way to analyze live video data.

## Features
- **Real-Time Detection:** Detect faces, smiles, and eyes from the webcam feed using Haar cascade classifiers.
- **Interactive Controls:** Toggle detection features, highlight faces, and capture screenshots with simple keyboard inputs.
- **Video Recording:** Record live webcam feed with detection annotations and save the output as an AVI file.
- **Face Storage:** Save detected faces as individual images for later analysis.
- **Screenshot Capture:** Capture and save high-resolution screenshots of the live feed with annotations.

## Requirements
- Python 3.x
- OpenCV
- Webcam

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Vanshagrawal17/face-detection-system.git
   cd face-detection
   ```

2. Install the required Python libraries:
   ```bash
   pip install opencv-python
   ```

3. Download the Haar cascade XML files:
   - [haarcascade_frontalface_default.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)
   - [haarcascade_smile.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_smile.xml)
   - [haarcascade_eye.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_eye.xml)

   Place these XML files in the project directory.

## Usage

1. Run the script:
   ```bash
   python main.py
   ```

2. Use the following keyboard inputs to interact with the application:
   - **'q'**: Quit the application.
   - **'f'**: Toggle face detection on/off.
   - **'s'**: Toggle smile detection on/off.
   - **'e'**: Toggle eye detection on/off.
   - **'h'**: Toggle face highlighting on/off.
   - **'c'**: Capture a screenshot.

3. The application will display the live webcam feed with detection annotations. Detected faces, smiles, and eyes will be highlighted in the frame, and video will be recorded in the background.

## Output
- **Video Output:** The recorded video is saved as `output_with_detections.avi` in the project directory.
- **Saved Faces:** Detected faces are saved as individual images in the `saved_faces` folder.
- **Screenshots:** Screenshots are saved as PNG files with timestamps in their filenames.

## Example
- When face detection is enabled, the application will draw a rectangle around detected faces.
- Smile and eye detections will highlight the corresponding features within the detected faces.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Make sure to update the repository link and adjust the `python face_detection.py` command if the script name differs in your project.
