import cv2
import numpy as np
import pyzbar
from PyQt5 import QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem
from pyzbar import pyzbar

from base.base_widget import BaseWidget
#from utils.open_cv_camera import OpenCvCamera
from utils.csi_camera import CsiCamera

class CameraWidget(BaseWidget):
    def __init__(self):
        super().__init__()
        self.start_camera()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.image_frame = QLabel()

        self.attendence_table = QTableWidget(self)
        self.attendence_table.setColumnCount(2)

        self.attendence_table.horizontalHeader().setStretchLastSection(True)
        self.attendence_table.setHorizontalHeaderLabels(['Device Type', 'ID'])

        layout.addWidget(self.image_frame)
        layout.addWidget(self.attendence_table)

        self.setLayout(layout)

    def start_camera(self):
        self.camera_thread = CameraThread()
        self.camera_thread.current_frame.connect(self.update_current_frame)
        self.camera_thread.camera_video_shape.connect(self.update_camera_scale)
        self.camera_thread.start_camera()

    def update_current_frame(self, frame):
        frame = self.detect_barcode(frame)
        frame = self.rescale_image(frame)

        frame = self._build_image(frame)
        self.image_frame.setPixmap(QPixmap(frame))

    def update_camera_scale(self, camera_shape):
        self.scale_percent = 35000 / camera_shape[0]

    def detect_barcode(self, frame):
        barcodes = pyzbar.decode(frame)

        for barcode in barcodes:
            # extract the bounding box location of the barcode and draw the
            # bounding box surrounding the barcode on the image
            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            # the barcode data is a bytes object so if we want to draw it on
            # our output image we need to convert it to a string first
            barcodeData = barcode.data.decode("utf-8")
            barcodeType = barcode.type
            # draw the barcode data and barcode type on the image
            text = "{} ({})".format(barcodeData, barcodeType)
            cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 0, 255), 2)
            # print the barcode type and data to the terminal
            print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
            self.add_attendence_item(barcodeType, barcodeData)
        return frame

    def rescale_image(self, image):
        if self.scale_percent:
            width = int(image.shape[1] * self.scale_percent / 100)
            height = int(image.shape[0] * self.scale_percent / 100)
            dim = (width, height)
            # resize image
            return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        else:
            return image

    def _build_image(self, frame):
        height, width, channel = frame.shape
        bytesPerLine = 3 * width
        return QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()

    def add_attendence_item(self, type, value):
        print(self.attendence_table.rowCount())
        self.attendence_table.insertRow(self.attendence_table.rowCount())
        self.attendence_table.setItem(self.attendence_table.rowCount() - 1, 0, QTableWidgetItem(type))
        self.attendence_table.setItem(self.attendence_table.rowCount() - 1, 1, QTableWidgetItem(value))
        self.attendence_table.scrollToBottom()


class CameraThread(QtCore.QObject):
    current_frame = QtCore.pyqtSignal(np.ndarray)
    camera_video_shape = QtCore.pyqtSignal(tuple)

    def __init__(self):
        super().__init__()
        self.camera = CsiCamera()
        self.timer = QtCore.QBasicTimer()

    def start_camera(self):
        self.camera_video_shape.emit(self.camera.get_video_shape())
        self.timer.start(50, self)

    def timerEvent(self, event):
        if (event.timerId() != self.timer.timerId()):
            return

        frame = self.camera.get_frame()
        self.current_frame.emit(frame)

    def disconnect(self):
        pass
