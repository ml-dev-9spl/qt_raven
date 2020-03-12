# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/add_user.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(240, 320)
        Frame.setMinimumSize(QtCore.QSize(0, 320))
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_3 = QtWidgets.QGridLayout(Frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(Frame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(Frame)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_3.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Frame)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(Frame)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_3.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 4, 1, 1, 1, QtCore.Qt.AlignRight)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "TextLabel"))
        self.label_2.setText(_translate("Frame", "TextLabel"))
        self.label_3.setText(_translate("Frame", "TextLabel"))
        self.label_4.setText(_translate("Frame", "TextLabel"))
        self.pushButton.setText(_translate("Frame", "PushButton"))
