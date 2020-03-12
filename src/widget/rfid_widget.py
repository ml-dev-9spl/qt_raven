import cv2
import numpy as np
import pyzbar
from PyQt5 import QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem
from pyzbar import pyzbar

from base.base_widget import BaseWidget
from utils.SimpleMFRC522 import SimpleMFRC522
from utils.open_cv_camera import OpenCvCamera


class RfidWidget(BaseWidget):
    def __init__(self):
        super().__init__()
        self.start_rfid()
        self.destroyed.connect(lambda: self.on_destroy())

    def on_destroy(self):
        self.rfid_thread.disconnect()
        pass

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.attendence_table = QTableWidget(self)
        self.attendence_table.setColumnCount(2)

        self.attendence_table.horizontalHeader().setStretchLastSection(True)
        self.attendence_table.setHorizontalHeaderLabels(['Device Type', 'ID'])

        layout.addWidget(self.attendence_table)

        self.setLayout(layout)

    def start_rfid(self):
        self.rfid_thread = RfidThread()
        self.rfid_thread.rfid_value.connect(self.on_rfid_read)
        self.rfid_thread.start_rfid()

    def on_rfid_read(self, value):
        self.add_attendence_item("RFID", str(value))

    def add_attendence_item(self, type, value):
        print(self.attendence_table.rowCount())
        self.attendence_table.insertRow(self.attendence_table.rowCount())
        self.attendence_table.setItem(self.attendence_table.rowCount() - 1, 0, QTableWidgetItem(type))
        self.attendence_table.setItem(self.attendence_table.rowCount() - 1, 1, QTableWidgetItem(value))
        self.attendence_table.scrollToBottom()


class RfidThread(QtCore.QObject):
    rfid_value = QtCore.pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.reader = SimpleMFRC522()
        self.timer = QtCore.QBasicTimer()

    def start_rfid(self):
        self.timer.start(50, self)
        print("Hold a tag near the reader")


    def read(self):
        return self.reader.read()

    def timerEvent(self, event):
        if (event.timerId() != self.timer.timerId()):
            return

        id, text = self.reader.read()
        if id:
            self.rfid_value.emit(id)
            

    def disconnect(self):
        if self.timer.isActive():
            self.timer.stop()
        GPIO.cleanup()
        pass
