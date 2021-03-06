from PyQt5.QtWidgets import QVBoxLayout, QPushButton

from base.base_widget import BaseWidget
from widget.home_widget import HomeWidget


class LoginWidget(BaseWidget):

    def init_ui(self):
        layout = QVBoxLayout()

        btnLogin = QPushButton("Hi", self)
        btnLogin.clicked.connect(self.on_click)

        layout.addWidget(btnLogin)

    def on_click(self):
        print("on_click")
        self.add_screen(HomeWidget(self))
