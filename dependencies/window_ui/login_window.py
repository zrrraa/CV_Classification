# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(1200, 800)
        login.setStyleSheet("")
        self.zhanghao = QtWidgets.QLineEdit(login)
        self.zhanghao.setGeometry(QtCore.QRect(520, 240, 231, 51))
        self.zhanghao.setStyleSheet("background-color: rgba(255, 132, 139, 0);")
        self.zhanghao.setObjectName("zhanghao")
        self.mima = QtWidgets.QLineEdit(login)
        self.mima.setGeometry(QtCore.QRect(520, 340, 231, 41))
        self.mima.setStyleSheet("background-color: rgba(255, 132, 139, 0);")
        self.mima.setObjectName("mima")
        self.label = QtWidgets.QLabel(login)
        self.label.setGeometry(QtCore.QRect(360, 240, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(login)
        self.label_2.setGeometry(QtCore.QRect(360, 320, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setObjectName("label_2")
        self.login_button = QtWidgets.QPushButton(login)
        self.login_button.setGeometry(QtCore.QRect(400, 610, 371, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.login_button.setFont(font)
        self.login_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon.fromTheme("applications-accessories")
        self.login_button.setIcon(icon)
        self.login_button.setIconSize(QtCore.QSize(24, 24))
        self.login_button.setCheckable(False)
        self.login_button.setObjectName("login_button")
        self.signup_button = QtWidgets.QPushButton(login)
        self.signup_button.setGeometry(QtCore.QRect(400, 700, 371, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        self.signup_button.setFont(font)
        self.signup_button.setObjectName("signup_button")
        self.backup = QtWidgets.QPushButton(login)
        self.backup.setGeometry(QtCore.QRect(1020, 730, 81, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        self.backup.setFont(font)
        self.backup.setObjectName("backup")
        self.label_3 = QtWidgets.QLabel(login)
        self.label_3.setGeometry(QtCore.QRect(220, 60, 221, 131))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(login)
        self.label_4.setGeometry(QtCore.QRect(510, 100, 281, 91))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Form"))
        self.label.setText(_translate("login", "账号"))
        self.label_2.setText(_translate("login", "密码"))
        self.login_button.setText(_translate("login", "登录"))
        self.signup_button.setText(_translate("login", "注册"))
        self.backup.setText(_translate("login", "退出"))
        self.label_3.setText(_translate("login", "TextLabel"))
        self.label_4.setText(_translate("login", "TextLabel"))