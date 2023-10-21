import common_functions
import corner_detection_fast
import essential_matrix_computation
import featuretracking
import image_processing
import os
import cv2
import numpy as np
from tqdm import tqdm

cap = cv2.VideoCapture("20230605_163120.mp4")
if not cap.isOpened():
    print("Access error")
    exit()

idx = 0
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

# Store one frame behinds info
prevFrameCorners = ()
prevFrame = ()
rotationArr = np.zeros(shape=(3, 3))
translationArr = np.zeros(shape=(3, 3))
focal = 718.8560
pp = (607.1928, 185, 2157)
start = np.array([0, 0, 0])

for i in tqdm(range(int(frame_count))):
    ret, frame = cap.read()
    if not ret:
        print("Unable to read the frame")
        continue

    # Always do extraction
    currentFrameCorners = extract_features(frame, True)

    if i != 0:
        # logic with prevFrameCorners which would be i-1 frame, and currentFrameCorners
        prevFrameCorners, currentFrameCorners = feature_tracking(
            prevFrame, frame, prevFrameCorners, currentFrameCorners
        )
        rotationArr, translationArr = essential_matrix_computation(
            rotationArr,
            translationArr,
            currentFrameCorners,
            prevFrameCorners,
            focal,
            pp,
            i,
            poseInfo,
        )

        # Matrixes updated, and corners updated
        # plot result of our matrix change

    prevFrameCorners = currentFrameCorners  # Save i-1 frame
    prevFrame = frame
    # cv2.imwrite(f"frame_{idx}.jpg", frame)
    idx += 1

cap.release()
