# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Tabs.Dynamical_systems.neuron_models.Huxly.sin_plot.plot import canvas_widget



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(708, 519)
        self.widget = canvas_widget(Form)
        self.widget.setGeometry(QtCore.QRect(40, 20, 611, 381))
        self.widget.setObjectName("widget")
        self.amp_lineEdit = QtWidgets.QLineEdit(Form)
        self.amp_lineEdit.setGeometry(QtCore.QRect(470, 430, 111, 25))
        self.amp_lineEdit.setObjectName("amp_lineEdit")
        self.freq_line_Edit = QtWidgets.QLineEdit(Form)
        self.freq_line_Edit.setGeometry(QtCore.QRect(470, 460, 111, 25))
        self.freq_line_Edit.setObjectName("freq_line_Edit")
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(41, 430, 411, 58))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.amp_slider = QtWidgets.QSlider(self.widget1)
        self.amp_slider.setOrientation(QtCore.Qt.Horizontal)
        self.amp_slider.setObjectName("amp_slider")
        self.gridLayout.addWidget(self.amp_slider, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.freq_slider = QtWidgets.QSlider(self.widget1)
        self.freq_slider.setOrientation(QtCore.Qt.Horizontal)
        self.freq_slider.setObjectName("freq_slider")
        self.gridLayout.addWidget(self.freq_slider, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Amplitude"))
        self.label_2.setText(_translate("Form", "Freqeuncy"))
