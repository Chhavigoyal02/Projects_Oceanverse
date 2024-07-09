import os
import cv2
from ultralytics import YOLO

# Path to the model
model_path = 'yolov8n.pt'

# Load the model
model = YOLO(model_path)

# Open a connection to the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

def is_hand_raised(keypoints):
    left_shoulder_y = keypoints[5][1]
    right_shoulder_y = keypoints[6][1]
    left_wrist_y = keypoints[9][1]
    right_wrist_y = keypoints[10][1]

    # Check if either of the wrists are above the respective shoulders
    if (left_wrist_y < left_shoulder_y) or (right_wrist_y < right_shoulder_y):
        return True
    return False


while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        break

    # Perform object detection
    results = model(frame)

    keypoints = results[0].keypoints 

    if keypoints is not None:
        for keypoint in keypoints:
            keypoint = keypoint.detach().cpu().numpy()
            if is_hand_raised(keypoint):
                cv2.putText(frame, "Hand Raised", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            else:
                cv2.putText(frame, "Hand Not Raised", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    # Display the results
    annotated_frame = results[0].plot()  # Use results[0].plot() to get the annotated frame

    cv2.imshow('Live Object Detection', annotated_frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

