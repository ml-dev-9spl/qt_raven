from PyQt5.QtWidgets import QVBoxLayout, QPushButton

from base.base_widget import BaseWidget


class HomeWidget(BaseWidget):

    def init_ui(self):
        layout = QVBoxLayout()

        btnLogin = QPushButton("Home", self)
        btnLogin.clicked.connect(self.on_click)

        layout.addWidget(btnLogin)

    def on_click(self):
        self.on_back_press()
        pass
