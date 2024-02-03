import pyzed.sl as sl
import numpy as np
import cv2
class ZedCamera:
    def __init__(self) -> None:
        self.zed = sl.Camera()

        # Initialise factory calibration parameters.
        # params = (
        #     self.zed.get_camera_information().camera_configuration.calibration_parameters
        # )
        # fx, fy = params.left_cam.fx, params.left_cam.fy
        # cx, cy = params.left_cam.cx, params.left_cam.cy
        # self.camera_matrix = np.matrix([(fx,0,cx),(0,fy,cy),(0,0,1)])
        # self.dist = 0
        # self.new_camera_mtx = np.ones(3)
            # Create a Camera object

        # Create a InitParameters object and set configuration parameters
        init_params = sl.InitParameters()
        init_params.sdk_verbose = 0

        # Open the camera
        err = self.zed.open(init_params)
        if err != sl.ERROR_CODE.SUCCESS:
            exit(1)



    def get_frame(self):
        image = sl.Mat()
        runtime_params = sl.RuntimeParameters()

        if self.zed.grab(runtime_params) == sl.ERROR_CODE.SUCCESS:
            self.zed.retrieve_image(image, sl.VIEW.LEFT)
            return image.get_data()

    def get_calibration_parameters(self):
        """
        Returns a tuple of calibration parameters for the left camera in the following format:
        (focal length x, focal length y, principle point x, principle point y)
        """

        return self.calibration_parameters
    
    def close(self):
        self.zed.close()
