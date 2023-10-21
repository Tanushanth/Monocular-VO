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


for i in tqdm(range(int(frame_count))):
    ret, frame = cap.read()
    if not ret:
        print("Unable to read the frame")
        continue
    
    #Whatever we want here


    # cv2.imwrite(f"frame_{idx}.jpg", frame)
    idx+=1

cap.release()