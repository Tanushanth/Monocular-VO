import numpy as np
import cv2
import os

#calculate the essential matrix and the new rotation and translation vectors
#input
#R: rotation matrix
#t: translation vector
#new: points in new image
#old: points in old image
#focal: focal length
#pp: principal point
#id: index of the image
#poseInfo: pose information
#output
#newR: new rotation matrix
#newt: new translation vector
def essential_matrix_computation(inputR, inputt, new, old, focal, pp, id, poseInfo):
        E,_ = cv2.findEssentialMat(new, old, focal, pp, cv2.RANSAC, 0.999, 1.0, None)
        _, R, t, _ = cv2.reversePose(E, old, new, inputR, inputt, focal, pp, None)
        if id  >= 2:
            absolute_scale = get_absolute_scale(poseInfo, id)
            if (absolute_scale > 0.1 and abs(t[2][0]) > abs(t[0][0]) and abs(t[2][0]) > abs(t[1][0])):
                inputt = inputt + absolute_scale*inputR.dot(t)
                inputR = R.dot(inputR)
        return inputR, inputt

def get_absolute_scale(poseInfo, id):
    pose = poseInfo[id - 1].strip().split()
    x_prev = float(pose[3])
    y_prev = float(pose[7])
    z_prev = float(pose[11])
    pose = poseInfo[id].strip().split()
    x = float(pose[3])
    y = float(pose[7])
    z = float(pose[11])

    true_vect = np.array([[x], [y], [z]])
    prev_vect = np.array([[x_prev], [y_prev], [z_prev]])
    
    return np.linalg.norm(true_vect - prev_vect)
