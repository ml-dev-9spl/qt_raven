from abc import abstractmethod

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget


class BaseWidget(QWidget):
    add_screen_listener = QtCore.pyqtSignal(QWidget)
    on_back_press_listener = QtCore.pyqtSignal()

    def __init__(self, title="Raven"):
        super().__init__()
        self.title = title
        self.init_ui()

    def show(self):
        super().show()

    @abstractmethod
    def init_ui(self):
        raise Exception("method init_ui() not implemented")

    def add_screen(self, screen):
        self.add_screen_listener.emit(screen)

    def on_back_press(self):
        self.on_back_press_listener.emit()


