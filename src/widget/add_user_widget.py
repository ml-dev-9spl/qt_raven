from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from base.base_widget import BaseWidget


class AddUserWidget(BaseWidget):
    def init_ui(self):
        self.layout = QtWidgets.QFormLayout(self)

        self.lblFName = QtWidgets.QLabel(self)
        self.lblFName.setText("First Name")

        self.lblLName = QtWidgets.QLabel(self)
        self.lblLName.setText("Last Name")

        self.lblQrCode = QtWidgets.QLabel(self)
        self.lblQrCode.setText("QRCode")

        self.lblRfid = QtWidgets.QLabel(self)
        self.lblRfid.setText("RFID")

        self.leFName = QtWidgets.QLineEdit(self)
        self.leFName.setPlaceholderText("Enter First Name")

        self.leLName = QtWidgets.QLineEdit(self)
        self.leLName.setPlaceholderText("Enter Second Name")

        self.leQrCode = QtWidgets.QLineEdit(self)
        self.leQrCode.setPlaceholderText("Enter QRCode")

        self.leRfid = QtWidgets.QLineEdit(self)
        self.leRfid.setPlaceholderText("Enter RFID")

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setText("Submit")

        self.layout.addRow(self.lblFName)
        self.layout.addRow(self.leFName)
        self.layout.addRow(self.lblLName)
        self.layout.addRow(self.leLName)
        self.layout.addRow(self.lblQrCode)
        self.layout.addRow(self.leQrCode)
        self.layout.addRow(self.lblRfid)
        self.layout.addRow(self.leRfid)
        self.layout.addRow(self.pushButton)

        self.pushButton.clicked.connect(self.on_submit_click)

    def on_submit_click(self):
        if (self.is_valid()):
            print(self.leFName.displayText())

    def is_valid(self):
        if (not self.leFName.displayText()):
            QMessageBox.critical(self, "Alert", "Please enter first name")
            return False
        if (not self.leLName.displayText()):
            QMessageBox.critical(self, "Alert", "Please enter last name")
            return False
        if (not self.leQrCode.displayText()):
            QMessageBox.critical(self, "Alert", "Please enter QRCode")
            return False
        if (not self.leRfid.displayText()):
            QMessageBox.critical(self, "Alert", "Please enter RFID")
            return False
        return True
