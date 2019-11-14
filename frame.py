# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frame.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5.sip

class Ui_windows(object):
    def setupUi(self, windows):
        windows.setObjectName("windows")
        windows.resize(179, 167)
        self.centralwidget = QtWidgets.QWidget(windows)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_up = QtWidgets.QPushButton(self.centralwidget)
        self.bt_up.setGeometry(QtCore.QRect(60, 10, 51, 51))
        self.bt_up.setObjectName("bt_up")
        self.bt_down = QtWidgets.QPushButton(self.centralwidget)
        self.bt_down.setGeometry(QtCore.QRect(60, 110, 51, 51))
        self.bt_down.setObjectName("bt_down")
        self.bt_right = QtWidgets.QPushButton(self.centralwidget)
        self.bt_right.setGeometry(QtCore.QRect(110, 60, 61, 51))
        self.bt_right.setObjectName("bt_right")
        self.bt_left = QtWidgets.QPushButton(self.centralwidget)
        self.bt_left.setGeometry(QtCore.QRect(10, 60, 51, 51))
        self.bt_left.setObjectName("bt_left")
        windows.setCentralWidget(self.centralwidget)

        self.retranslateUi(windows)
        QtCore.QMetaObject.connectSlotsByName(windows)

    def retranslateUi(self, windows):
        _translate = QtCore.QCoreApplication.translate
        windows.setWindowTitle(_translate("windows", "MainWindow"))
        self.bt_up.setText(_translate("windows", "↑"))
        self.bt_down.setText(_translate("windows", "↓"))
        self.bt_right.setText(_translate("windows", "→"))
        self.bt_left.setText(_translate("windows", "←"))

