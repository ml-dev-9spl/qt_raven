from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QSizePolicy

from base.base_widget import BaseWidget
from widget.add_user_widget import AddUserWidget
from widget.camera_widget import CameraWidget
from utils.commons import get_icon


class AttendenceOptionWidget(BaseWidget):
    def init_ui(self):
        layout = QtWidgets.QGridLayout(self)

        self.item1 = QtWidgets.QVBoxLayout()

        self.btnQrCode = QtWidgets.QPushButton(self)
        self.btnQrCode.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Expanding)
        self.btnQrCode.setIcon(get_icon("base/qr-code.png"))
        self.btnQrCode.setIconSize(QSize(64, 64))

        self.item1.addWidget(self.btnQrCode)

        self.item2 = QtWidgets.QVBoxLayout()

        self.btnRfid = QtWidgets.QPushButton(self)
        self.btnRfid.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Expanding)
        self.btnRfid.setIcon(get_icon("base/rfid.png"))
        self.btnRfid.setIconSize(QSize(64, 64))

        self.item2.addWidget(self.btnRfid)

        self.item3 = QtWidgets.QVBoxLayout()

        self.btnFaceIdentification = QtWidgets.QPushButton(self)
        self.btnFaceIdentification.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Expanding)
        self.btnFaceIdentification.setIcon(get_icon("base/face-detection.png"))
        self.btnFaceIdentification.setIconSize(QSize(64, 64))

        self.item3.addWidget(self.btnFaceIdentification)

        self.item4 = QtWidgets.QVBoxLayout()

        self.btnAddUser = QtWidgets.QPushButton(self)
        self.btnAddUser.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Expanding)
        self.btnAddUser.setIcon(get_icon("base/add_user.png"))
        self.btnAddUser.setIconSize(QSize(64, 64))

        self.item4.addWidget(self.btnAddUser)

        layout.addLayout(self.item1, 0, 0, 1, 1)
        layout.addLayout(self.item2, 0, 1, 1, 1)
        layout.addLayout(self.item3, 1, 0, 1, 1)
        layout.addLayout(self.item4, 1, 1, 1, 1)

        self.btnQrCode.clicked.connect(self.on_qr_code_click)
        self.btnAddUser.clicked.connect(self.on_add_user_click)

    def on_qr_code_click(self):
        self.add_screen(CameraWidget())

    def on_add_user_click(self):
        self.add_screen(AddUserWidget())
