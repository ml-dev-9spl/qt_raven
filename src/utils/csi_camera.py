from utils.camera import Camera


class CsiCamera(Camera):
    def __init__(self):
        super().__init__(self.gstreamer_pipeline())

    def gstreamer_pipeline(self,
                           capture_width=1280,
                           capture_height=720,
                           display_width=1280,
                           display_height=720,
                           framerate=60,
                           flip_method=0,
                           ):
        return (
                "nvarguscamerasrc ! "
                "video/x-raw(memory:NVMM), "
                "width=(int)%d, height=(int)%d, "
                "format=(string)NV12, framerate=(fraction)%d/1 ! "
                "nvvidconv flip-method=%d ! "
                "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
                "videoconvert ! "
                "video/x-raw, format=(string)BGR ! appsink"
                % (
                    capture_width,
                    capture_height,
                    framerate,
                    flip_method,
                    display_width,
                    display_height,
                )
        )
