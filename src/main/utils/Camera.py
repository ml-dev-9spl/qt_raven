import cv2


class Camera:
    def __init__(self, video_url):
        self.cap = cv2.VideoCapture(video_url)
        if self.cap.isOpened():
            self.video_width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # float
            self.video_height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float
        else:
            self.video_width = 1
            self.video_height = 1

    def get_video_shape(self):
        return (self.video_width, self.video_height)

    def get_frame(self):
        id, frame = self.cap.read()
        if id:
            return frame
        else:
            return False

    def stop_camera(self):
        self.cap.release()
