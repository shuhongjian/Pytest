# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Pytest\实用脚本\pyQt\综合工具组\12.27_dome2\CaiDan_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(565, 219)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 561, 211))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(270, 20, 181, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(310, 140, 41, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(80, 50, 141, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 130, 141, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 90, 101, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 90, 51, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(310, 60, 54, 12))
        self.label_5.setObjectName("label_5")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(420, 90, 51, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 20, 71, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 90, 101, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 140, 41, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(250, 90, 41, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(360, 130, 151, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(360, 50, 151, 30))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "默认值"))
        self.label_3.setText(_translate("Form", "时间戳："))
        self.label_6.setText(_translate("Form", "时间戳："))
        self.pushButton_3.setText(_translate("Form", "13位（毫秒级）"))
        self.pushButton_2.setText(_translate("Form", "转换"))
        self.label_5.setText(_translate("Form", "时间："))
        self.pushButton_4.setText(_translate("Form", "转换"))
        self.label.setText(_translate("Form", "当前时间："))
        self.pushButton.setText(_translate("Form", "13位（毫秒级）"))
        self.label_4.setText(_translate("Form", "时间："))
        self.pushButton_5.setText(_translate("Form", "刷新"))
