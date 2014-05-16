# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_help_window.ui'
#
# Created: Fri May 25 16:27:11 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_help_window(object):
    def setupUi(self, help_window):
        help_window.setObjectName(_fromUtf8("help_window"))
        help_window.resize(758, 511)
        self.frame = QtGui.QFrame(help_window)
        self.frame.setGeometry(QtCore.QRect(9, 9, 741, 491))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.webView = QtWebKit.QWebView(self.frame)
        self.webView.setGeometry(QtCore.QRect(0, 0, 741, 491))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))

        self.retranslateUi(help_window)
        QtCore.QMetaObject.connectSlotsByName(help_window)

    def retranslateUi(self, help_window):
        help_window.setWindowTitle(QtGui.QApplication.translate("help_window", "Grids for Atlas Help", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
