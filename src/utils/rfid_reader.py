import numpy as np
from PyQt5 import QtCore

from .SimpleMFRC522 import SimpleMFRC522
import RPi.GPIO as GPIO


class RfidThread(QtCore.QObject):
    rfid_value = QtCore.pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.reader = SimpleMFRC522()
        self.timer = QtCore.QBasicTimer()
        self.timer.start(50, self)

    def start_reading(self):
        while True:
            id, text = self.read()
            if id:
                print(id)

    def disconnect(self):
        GPIO.cleanup()
        pass

    def read(self):
        print("Hold a tag near the reader")
        return self.reader.read()


    def timerEvent(self, event):
        if (event.timerId() != self.timer.timerId()):
            return

        id,text = self.reader.read()
        if id:
            self.rfid_value.emit(id)
