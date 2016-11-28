# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sat Nov 26 15:58:54 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(409, 123)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/app-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.macButton = QtGui.QPushButton(Dialog)
        self.macButton.setGeometry(QtCore.QRect(20, 30, 111, 61))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/mac-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.macButton.setIcon(icon1)
        self.macButton.setIconSize(QtCore.QSize(32, 32))
        self.macButton.setObjectName("macButton")
        self.fedoraButton = QtGui.QPushButton(Dialog)
        self.fedoraButton.setGeometry(QtCore.QRect(150, 30, 111, 61))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/fedora-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fedoraButton.setIcon(icon2)
        self.fedoraButton.setIconSize(QtCore.QSize(32, 32))
        self.fedoraButton.setObjectName("fedoraButton")
        self.windowsButton = QtGui.QPushButton(Dialog)
        self.windowsButton.setGeometry(QtCore.QRect(280, 30, 111, 61))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/windows-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.windowsButton.setIcon(icon3)
        self.windowsButton.setIconSize(QtCore.QSize(32, 32))
        self.windowsButton.setObjectName("windowsButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.macButton.setText(QtGui.QApplication.translate("Dialog", "Load Mac", None, QtGui.QApplication.UnicodeUTF8))
        self.fedoraButton.setText(QtGui.QApplication.translate("Dialog", "Load Fedora", None, QtGui.QApplication.UnicodeUTF8))
        self.windowsButton.setText(QtGui.QApplication.translate("Dialog", "Load Windows", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
