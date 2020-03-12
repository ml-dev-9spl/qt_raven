from PyQt5 import QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QPushButton, QHBoxLayout

from base.base_widget import BaseWidget
from utils.commons import get_icon


class BottomWidget(BaseWidget):
    home_click_listener = QtCore.pyqtSignal()
    logout_click_listener = QtCore.pyqtSignal()

    def init_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        btnBack = QPushButton("", self)
        btnBack.setFixedHeight(50)

        btnBack.setIcon(get_icon("base/return.png"))
        btnBack.setIconSize(QSize(24, 24))
        btnBack.clicked.connect(self.on_back_click)

        btnHome = QPushButton("", self)
        btnHome.setFixedHeight(50)
        btnHome.setIcon(get_icon("base/home.png"))
        btnHome.setIconSize(QSize(24, 24))
        btnHome.clicked.connect(self.on_home_click)

        btnLogout = QPushButton("", self)
        btnLogout.setFixedHeight(50)
        btnLogout.setIcon(get_icon("base/logout.png"))
        btnLogout.setIconSize(QSize(24, 24))
        btnLogout.clicked.connect(self.on_logout_click)

        layout.addWidget(btnBack)
        layout.addWidget(btnHome)
        layout.addWidget(btnLogout)
        self.setLayout(layout)

    def on_back_click(self):
        self.on_back_press()

    def on_home_click(self):
        self.home_click_listener.emit()

    def on_logout_click(self):
        self.logout_click_listener.emit()
