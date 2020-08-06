# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_image.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1023, 552)
        self.openGLWidget = QtWidgets.QOpenGLWidget(Dialog)
        self.openGLWidget.setGeometry(QtCore.QRect(350, 30, 581, 441))
        self.openGLWidget.setObjectName("openGLWidget")
        self.verticalSlider = QtWidgets.QSlider(Dialog)
        self.verticalSlider.setGeometry(QtCore.QRect(30, 40, 16, 171))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.verticalSlider_2 = QtWidgets.QSlider(Dialog)
        self.verticalSlider_2.setGeometry(QtCore.QRect(150, 40, 16, 177))
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.verticalSlider_3 = QtWidgets.QSlider(Dialog)
        self.verticalSlider_3.setGeometry(QtCore.QRect(270, 40, 16, 174))
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(17, 234, 64, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(127, 234, 64, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(257, 234, 64, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(390, 180, 511, 121))
        self.label_4.setObjectName("label_4")
        self.dial = QtWidgets.QDial(Dialog)
        self.dial.setGeometry(QtCore.QRect(175, 363, 50, 64))
        self.dial.setObjectName("dial")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(124, 509, 91, 17))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(142, 314, 41, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(141, 436, 41, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(245, 371, 41, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(56, 373, 41, 41))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Contrast"))
        self.label_2.setText(_translate("Dialog", "Threshold"))
        self.label_3.setText(_translate("Dialog", "Zoom"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:20pt; color:#eeeeec;\">The Image Will be Rendered Here ...</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "Fine Adjust"))
        self.pushButton.setText(_translate("Dialog", "Up"))
        self.pushButton_2.setText(_translate("Dialog", "Down"))
        self.pushButton_3.setText(_translate("Dialog", "Right"))
        self.pushButton_4.setText(_translate("Dialog", "Left"))
