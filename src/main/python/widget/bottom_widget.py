from PyQt5 import QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QPushButton, QHBoxLayout

from src.main.python.base.base_widget import BaseWidget


class BottomWidget(BaseWidget):
    home_click_listener = QtCore.pyqtSignal()
    logout_click_listener = QtCore.pyqtSignal()

    def init_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        btnBack = QPushButton("", self)
        btnBack.setFixedHeight(50)

        iconBack = QIcon()
        iconBack.addPixmap(QPixmap("../icons/base/return.png"), QIcon.Normal, QIcon.Off)
        btnBack.setIcon(iconBack)
        btnBack.setIconSize(QSize(24, 24))
        btnBack.clicked.connect(self.on_back_click)

        btnHome = QPushButton("", self)
        btnHome.setFixedHeight(50)
        iconHome = QIcon()
        iconHome.addPixmap(QPixmap("../icons/base/home.png"), QIcon.Normal, QIcon.Off)
        btnHome.setIcon(iconHome)
        btnHome.setIconSize(QSize(24, 24))
        btnHome.clicked.connect(self.on_home_click)

        btnLogout = QPushButton("", self)
        btnLogout.setFixedHeight(50)
        iconLogout = QIcon()
        iconLogout.addPixmap(QPixmap("../icons/base/logout.png"), QIcon.Normal, QIcon.Off)
        btnLogout.setIcon(iconLogout)
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
