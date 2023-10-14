import numpy as np
import cv2
from matplotlib import pyplot as plt
import common_functions

# Read image in grayscale.
image = cv2.imread("cuboid.jpeg", cv2.IMREAD_GRAYSCALE)

# Instantiate FAST detector.
fast_feature_detector = cv2.FastFeatureDetector_create()

# Get corners.
corners = fast_feature_detector.detect(image, None)
cornered_image_nms = cv2.drawKeypoints(image, corners, None, color=(255,0,0))

fast_feature_detector.setNonmaxSuppression(0)
corners = fast_feature_detector.detect(image, None)
cornered_image = cv2.drawKeypoints(image, corners, None, color=(255,0,0))

common_functions.show_image("cornered_image_nms", cornered_image_nms)
common_functions.show_image("cornered_image", cornered_image)

