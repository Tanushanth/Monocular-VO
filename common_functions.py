import cv2
from tqdm import tqdm


def show_image(window_name, image):
    cv2.imshow(window_name, image)
    if cv2.waitKey(0) == "q":
        cv2.destroyWindow(window_name)


def get_frames(video_name, num_frames):
    cap = cv2.VideoCapture(video_name)

    if not cap.isOpened():
        print("Access error")
        exit()

    idx = 0
    frame_count = num_frames

    for _ in tqdm(range(int(frame_count))):
        ret, frame = cap.read()
        if not ret:
            print("Unable to read the frame")
            continue
        cv2.imwrite(f"frame_{idx}.jpg", frame)
        idx += 1

    cap.release()


if __name__ == "__main__":
    get_frames("20230605_163120.mp4", 10)
