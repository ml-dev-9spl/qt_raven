import os
from sys import path

from PyQt5.QtGui import QIcon, QPixmap


def get_icon(image_path):
    icon = QIcon()
    image_path = os.path.join("icons", image_path)
    icon.addPixmap(QPixmap(image_path), QIcon.Normal, QIcon.Off)
    return icon
