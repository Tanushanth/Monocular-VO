import numpy as np
import cv2
import os

def feature_tracking(image1, image2, corners1, corners2):
    corners2, status, err = cv2.calcOpticalFlowPyrLK(image1, image2, corners1, corners2, dict(winSize = (21,21), criteria = (cv2.TERM_CRITERIA_EPS | cv2. TERM_CRITERIA_COUNT , 30, 0.01)))
    #To get rid of points for the KLT tracking where the status is 0 or if they are not in the frame
    index_correction = 0
    for i in range(len(status)):
        pt = corners2[i - index_correction]
        if status[i] == 0 or pt[0] < 0 or pt[1] < 0:
            if pt[0] < 0 or pt[1] < 0:
                status[i] = 0
            corners1.pop(i - index_correction)
            corners2.pop(i - index_correction)
            index_correction += 1

    return corners1, corners2
