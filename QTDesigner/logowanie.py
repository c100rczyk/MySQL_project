# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(549, 419)
        self.pushButton_zaloguj_sie = QtWidgets.QPushButton(Dialog)
        self.pushButton_zaloguj_sie.setGeometry(QtCore.QRect(200, 240, 141, 41))
        self.pushButton_zaloguj_sie.setObjectName("pushButton_zaloguj_sie")
        self.label_login = QtWidgets.QLabel(Dialog)
        self.label_login.setGeometry(QtCore.QRect(200, 90, 151, 21))
        self.label_login.setObjectName("label_login")
        self.label_haslo = QtWidgets.QLabel(Dialog)
        self.label_haslo.setGeometry(QtCore.QRect(200, 160, 67, 17))
        self.label_haslo.setObjectName("label_haslo")
        self.lineEdit_login = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_login.setGeometry(QtCore.QRect(200, 120, 141, 25))
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.lineEdit_haslo = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_haslo.setGeometry(QtCore.QRect(200, 190, 141, 25))
        self.lineEdit_haslo.setObjectName("lineEdit_haslo")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 310, 121, 21))
        self.label.setObjectName("label")
        self.pushButton_Zarejestruj_sie = QtWidgets.QPushButton(Dialog)
        self.pushButton_Zarejestruj_sie.setGeometry(QtCore.QRect(200, 340, 141, 41))
        self.pushButton_Zarejestruj_sie.setObjectName("pushButton_Zarejestruj_sie")
        self.LOGO = QtWidgets.QGraphicsView(Dialog)
        self.LOGO.setGeometry(QtCore.QRect(130, 10, 301, 71))
        self.LOGO.setObjectName("LOGO")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_zaloguj_sie.setText(_translate("Dialog", "Zaloguj się"))
        self.label_login.setText(_translate("Dialog", "Login:"))
        self.label_haslo.setText(_translate("Dialog", "Hasło:"))
        self.label.setText(_translate("Dialog", "Nie masz konta?"))
        self.pushButton_Zarejestruj_sie.setText(_translate("Dialog", "Zarejestruj się"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
