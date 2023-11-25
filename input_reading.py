import pyzed.sl as sl


class ZedCamera:
    def __init__(self) -> None:
        self.zed = sl.Camera()

        # Initialise factory calibration parameters.
        params = (
            self.zed.get_camera_information().camera_configuration.calibration_parameters
        )

        fx, fy = params.left_cam.fx, params.left_cam.fy
        cx, cy = params.left_cam.cx, params.left_cam.cy
        self.calibration_parameters = fx, fy, cx, cy

    def get_frame(self):
        image = sl.Mat()
        runtime_params = sl.RuntimeParameters()

        if self.zed.grab(runtime_params) == sl.ERROR_CODE.SUCCESS:
            self.zed.retrieve_image(image, sl.VIEW.LEFT)
            return image

    def get_calibration_parameters(self):
        """
        Returns a tuple of calibration parameters for the left camera in the following format:
        (focal length x, focal length y, principle point x, principle point y)
        """

        return self.calibration_parameters
