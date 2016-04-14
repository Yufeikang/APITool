# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windows.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(691, 514)
        self.lineEdit_Url = QtWidgets.QLineEdit(Form)
        self.lineEdit_Url.setGeometry(QtCore.QRect(60, 20, 541, 20))
        self.lineEdit_Url.setObjectName("lineEdit_Url")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 31, 16))
        self.label.setObjectName("label")
        self.pushButton_go = QtWidgets.QPushButton(Form)
        self.pushButton_go.setGeometry(QtCore.QRect(610, 20, 51, 23))
        self.pushButton_go.setObjectName("pushButton_go")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(25, 61, 571, 421))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "URL:"))
        self.pushButton_go.setText(_translate("Form", "Go"))

