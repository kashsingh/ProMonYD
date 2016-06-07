# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\dialogUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(655, 412)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("C:\Users\Alxetraz\Documents\Canopy\Python Advanced\youtube-downloader\icon\PMYD.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.pushButtonDownload = QtGui.QPushButton(Dialog)
        self.pushButtonDownload.setGeometry(QtCore.QRect(160, 360, 301, 41))
        self.pushButtonDownload.setDefault(False)
        self.pushButtonDownload.setFlat(False)
        self.pushButtonDownload.setObjectName(_fromUtf8("pushButtonDownload"))

        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 161, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.listWidget = QtGui.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(20, 30, 621, 321))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "PMYD", None))
        self.pushButtonDownload.setText(_translate("Dialog", "Download", None))
        self.label.setText(_translate("Dialog", "Select format:", None))




