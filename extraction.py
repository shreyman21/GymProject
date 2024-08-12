import cv2
import os

# Define the mapping of video files to exercise labels
video_labels = {
    'burpee.mp4': 6,
    'squat.mp4': 1,
    'pushups.mp4': 0,
    'lunges.mp4': 2,
    'highknees.mp4': 7,
    'jumpingjack.mp4': 3,
    'mountainclimber.mp4': 8,
    'plank.mp4': 4,
    'sideplank.mp4': 9,
    'situp.mp4': 5
}

# Create directories for each exercise class
for label in video_labels.values():
    if not os.path.exists(f'data/{label}'):
        os.makedirs(f'data/{label}')

# Extract frames and save them with labels
for video_file, label in video_labels.items():
    cap = cv2.VideoCapture(video_file)
    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_path = os.path.join(f'data/{label}',
                                  f"{video_file.split('.')[0]}"
                                  f"_frame_{count}.jpg")
        cv2.imwrite(frame_path, frame)
        count += 1
    cap.release()

print("Frames extracted and labeled.")
