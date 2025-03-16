import cv2
import os

def extract_frames(video_path, output_path):
    # Opens the video
    video = cv2.VideoCapture(video_path)

    # Verify the video
    if not video.isOpened():
        print("Error opening the video")
        return

    # Start the count for every frame
    frame_count = 0

    # Reads and save every second of the video
    while True:
        # Reads the next frame
        ret, frame = video.read()

        # If ret is false the video is finished
        if not ret:
            break

        # Save the frame
        if frame_count % 2 == 0:
            output_file = os.path.join(output_path, f"frame_{frame_count}.jpg")
            cv2.imwrite(output_file, frame)

        frame_count += 1

    # Closes the video
    video.release()

    print(f"Saved {frame_count//2} frames in {output_path}.")

video_path = r"route"  # Video route
output_path = r"route"  # Route to save the frames

extract_frames(video_path, output_path)
