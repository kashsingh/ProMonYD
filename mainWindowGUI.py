# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI files\firstUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(789, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(".\icon\PMYD.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBoxVideo = QtGui.QGroupBox(self.centralwidget)
        self.groupBoxVideo.setGeometry(QtCore.QRect(10, 20, 761, 101))
        self.groupBoxVideo.setObjectName(_fromUtf8("groupBoxVideo"))
        self.videoDown = QtGui.QPushButton(self.groupBoxVideo)
        self.videoDown.setGeometry(QtCore.QRect(660, 50, 75, 23))
        self.videoDown.setObjectName(_fromUtf8("videoDown"))
        self.videoURL = QtGui.QLineEdit(self.groupBoxVideo)
        self.videoURL.setGeometry(QtCore.QRect(10, 50, 621, 20))
        self.videoURL.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.videoURL.setInputMask(_fromUtf8(""))
        self.videoURL.setText(_fromUtf8(""))
        self.videoURL.setObjectName(_fromUtf8("videoURL"))
        self.label_3 = QtGui.QLabel(self.groupBoxVideo)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 411, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.groupBoxPlaylist = QtGui.QGroupBox(self.centralwidget)
        self.groupBoxPlaylist.setGeometry(QtCore.QRect(10, 140, 761, 121))
        self.groupBoxPlaylist.setObjectName(_fromUtf8("groupBoxPlaylist"))
        self.playlistDown = QtGui.QPushButton(self.groupBoxPlaylist)
        self.playlistDown.setGeometry(QtCore.QRect(660, 40, 75, 23))
        self.playlistDown.setObjectName(_fromUtf8("playlistDown"))
        self.startValue = QtGui.QSpinBox(self.groupBoxPlaylist)
        self.startValue.setGeometry(QtCore.QRect(480, 70, 42, 22))
        self.startValue.setMinimum(1)
        self.startValue.setMaximum(200)
        self.startValue.setObjectName(_fromUtf8("startValue"))
        self.endValue = QtGui.QSpinBox(self.groupBoxPlaylist)
        self.endValue.setGeometry(QtCore.QRect(560, 70, 42, 22))
        self.endValue.setMinimum(2)
        self.endValue.setMaximum(200)
        self.endValue.setObjectName(_fromUtf8("endValue"))
        self.label = QtGui.QLabel(self.groupBoxPlaylist)
        self.label.setGeometry(QtCore.QRect(430, 70, 61, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBoxPlaylist)
        self.label_2.setGeometry(QtCore.QRect(530, 70, 31, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.playlistURL = QtGui.QLineEdit(self.groupBoxPlaylist)
        self.playlistURL.setGeometry(QtCore.QRect(10, 40, 621, 20))
        self.playlistURL.setObjectName(_fromUtf8("playlistURL"))
        self.label_4 = QtGui.QLabel(self.groupBoxPlaylist)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 411, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.groupBoxOutput = QtGui.QGroupBox(self.centralwidget)
        self.groupBoxOutput.setGeometry(QtCore.QRect(10, 280, 761, 111))
        self.groupBoxOutput.setObjectName(_fromUtf8("groupBoxOutput"))
        self.outputDir = QtGui.QLineEdit(self.groupBoxOutput)
        self.outputDir.setGeometry(QtCore.QRect(10, 40, 621, 20))
        self.outputDir.setInputMask(_fromUtf8(""))
        self.outputDir.setObjectName(_fromUtf8("outputDir"))
        self.outputBrowse = QtGui.QPushButton(self.groupBoxOutput)
        self.outputBrowse.setGeometry(QtCore.QRect(660, 40, 75, 23))
        self.outputBrowse.setObjectName(_fromUtf8("outputBrowse"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(False)
        self.progressBar.setGeometry(QtCore.QRect(20, 460, 751, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.statuslabel = QtGui.QLabel(self.centralwidget)
        self.statuslabel.setGeometry(QtCore.QRect(20, 430, 41, 16))
        self.statuslabel.setObjectName(_fromUtf8("statuslabel"))
        self.statusValuelabel = QtGui.QLabel(self.centralwidget)
        self.statusValuelabel.setGeometry(QtCore.QRect(60, 430, 711, 16))
        self.statusValuelabel.setText(_fromUtf8(""))
        self.statusValuelabel.setObjectName(_fromUtf8("statusValuelabel"))
        self.stopButton = QtGui.QPushButton(self.centralwidget)
        self.stopButton.setEnabled(False)
        self.stopButton.setGeometry(QtCore.QRect(670, 500, 75, 23))
        self.stopButton.setAutoDefault(False)
        self.stopButton.setDefault(False)
        self.stopButton.setFlat(False)
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 789, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ProMon YD", None))
        self.groupBoxVideo.setTitle(_translate("MainWindow", "Video Download", None))
        self.videoDown.setText(_translate("MainWindow", "Download", None))
        self.videoURL.setPlaceholderText(_translate("MainWindow", "URL", None))
        self.label_3.setText(_translate("MainWindow", "Paste video URL below.", None))
        self.groupBoxPlaylist.setTitle(_translate("MainWindow", "Playlist Download", None))
        self.playlistDown.setText(_translate("MainWindow", "Download", None))
        self.label.setText(_translate("MainWindow", "Start from", None))
        self.label_2.setText(_translate("MainWindow", "End", None))
        self.playlistURL.setPlaceholderText(_translate("MainWindow", "Playlist URL", None))
        self.label_4.setText(_translate("MainWindow", "Paste playlist URL below.", None))
        self.groupBoxOutput.setTitle(_translate("MainWindow", "Output Folder", None))
        self.outputDir.setText(_translate("MainWindow", "C:\\PMYD", None))
        self.outputBrowse.setText(_translate("MainWindow", "Browse", None))
        self.statuslabel.setText(_translate("MainWindow", "Status:", None))
        self.stopButton.setText(_translate("MainWindow", "Stop", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))

