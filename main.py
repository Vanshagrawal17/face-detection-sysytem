import cv2
import time
import os

# Load Haar cascade files
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Check if cascades are loaded properly
if face_cascade.empty() or smile_cascade.empty() or eye_cascade.empty():
    print("Error loading Haar cascade files!")
    exit()

# Create folder to save detected faces
os.makedirs("saved_faces", exist_ok=True)

# Open the webcam
video_capture = cv2.VideoCapture(0)
if not video_capture.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Start video writer for recording
frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('output_with_detections.avi', fourcc, 20.0, (frame_width, frame_height))

# Toggle detection features
detect_face = True
detect_smile = True
detect_eyes = True
highlight_faces = False
start_time = time.time()

print("Press 'q' to quit.")
print("Press 'f' to toggle face detection.")
print("Press 's' to toggle smile detection.")
print("Press 'e' to toggle eye detection.")
print("Press 'h' to toggle face highlighting.")
print("Press 'c' to capture a screenshot.")

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Convert the frame to grayscale for detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if detect_face:
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(50, 50))

        for i, (x, y, w, h) in enumerate(faces):
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

            if highlight_faces:
                # Apply blur or highlight effect
                face_blurred = cv2.GaussianBlur(roi_color, (51, 51), 30)
                frame[y:y + h, x:x + w] = face_blurred

            # Save detected face as an image
            face_path = os.path.join("saved_faces", f"face_{int(time.time())}_{i}.png")
            cv2.imwrite(face_path, roi_color)

            # Draw rectangle around the face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            if detect_eyes:
                # Detect eyes within the face
                eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 255), 2)

            if detect_smile:
                # Detect smiles within the face
                smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20)
                for (sx, sy, sw, sh) in smiles:
                    cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)

    # Display face count and elapsed time
    face_count = len(faces) if detect_face else 0
    cv2.putText(frame, f"Faces: {face_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    elapsed_time = int(time.time() - start_time)
    cv2.putText(frame, f"Time: {elapsed_time}s", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # Record the video frame
    output.write(frame)

    # Display the frame
    cv2.imshow('Face, Smile, and Eye Detection', frame)

    # Handle keypress events
    key = cv2.waitKey(1)
    if key == ord('q'):  # Quit
        break
    elif key == ord('f'):  # Toggle face detection
        detect_face = not detect_face
        print(f"Face detection {'enabled' if detect_face else 'disabled'}.")
    elif key == ord('s'):  # Toggle smile detection
        detect_smile = not detect_smile
        print(f"Smile detection {'enabled' if detect_smile else 'disabled'}.")
    elif key == ord('e'):  # Toggle eye detection
        detect_eyes = not detect_eyes
        print(f"Eye detection {'enabled' if detect_eyes else 'disabled'}.")
    elif key == ord('h'):  # Toggle face highlighting
        highlight_faces = not highlight_faces
        print(f"Face highlighting {'enabled' if highlight_faces else 'disabled'}.")
    elif key == ord('c'):  # Capture a screenshot
        screenshot_path = f"screenshot_{int(time.time())}.png"
        cv2.imwrite(screenshot_path, frame)
        print(f"Screenshot saved as {screenshot_path}.")

# Release resources
video_capture.release()
output.release()
cv2.destroyAllWindows()
