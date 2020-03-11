from PyQt5.QtWidgets import QWidget, QVBoxLayout, QStackedWidget

from src.main.python.base import base_widget
from src.main.python.widget.attendence_option_widget import AttendenceOptionWidget
from src.main.python.widget.bottom_widget import BottomWidget


class MainWindow(QWidget):
    def __init__(self, title="Raven"):
        super().__init__()
        self.window_width = 350
        self.window_height = 600
        self.setFixedSize(self.window_width, self.window_height)
        self.setWindowTitle(title)
        self.init_ui()

    def init_ui(self):
        bottom_bar = BottomWidget(self)
        bottom_bar.home_click_listener.connect(self.on_home_click)
        bottom_bar.logout_click_listener.connect(self.on_logout_click)

        self.fragment = QStackedWidget()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.fragment)

        bottom_bar.on_back_press_listener.connect(self.on_back_press)
        layout.addWidget(bottom_bar)

        self.setLayout(layout)
        # self.add_screen(LoginWidget("Login Screen"))
        # self.add_screen(CameraWidget())
        self.add_screen(AttendenceOptionWidget())

    def add_screen(self, screen: base_widget):
        screen.add_screen_listener.connect(self.add_screen)
        screen.on_back_press_listener.connect(self.on_back_press)

        self.fragment.addWidget(screen)
        self.fragment.setCurrentIndex(self.fragment.count() - 1)
        self.updateUi()

    def on_back_press(self):
        if self.fragment.count() > 1:
            widget = self.fragment.currentWidget()
            self.fragment.removeWidget(widget)
            widget.deleteLater()
            self.updateUi()

    def updateUi(self):
        widget: base_widget = self.fragment.currentWidget()
        self.setWindowTitle(widget.title)

    def on_home_click(self):
        self.remove_all_screen()

    def remove_all_screen(self):
        while self.fragment.count() > 1:
            widget = self.fragment.currentWidget()
            self.fragment.removeWidget(widget)
            widget.deleteLater()
            self.updateUi()

    def on_logout_click(self):
        print("On Logout Click")
