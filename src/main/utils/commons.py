from PyQt5.QtGui import QIcon, QPixmap


def get_icon(path):
    icon = QIcon()
    icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)
    return icon
