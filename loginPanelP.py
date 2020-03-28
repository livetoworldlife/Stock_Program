# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/hackyourfuture/Documents/Python3/DERSLER/PyQt5/d/loginPanel.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import time
from mudurPanelP import Ui_MainWindow_2s
from kasaPanelP import Ui_MainWindow_3k


class Ui_MainWindow_L(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(600, 400))
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget.setStyleSheet("#centralwidget{\n"
                                         "background-color: rgb(255, 255, 255);\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.formFrameKullanici = QtWidgets.QFrame(self.centralwidget)
        self.formFrameKullanici.setGeometry(QtCore.QRect(140, 120, 501, 300))
        self.formFrameKullanici.setMinimumSize(QtCore.QSize(400, 300))
        self.formFrameKullanici.setMaximumSize(QtCore.QSize(600, 400))
        self.formFrameKullanici.setStyleSheet("#formFrameKullanici{\n"
                                              "background-color: rgb(138, 167, 227);\n"
                                              "}\n"
                                              "")
        self.formFrameKullanici.setMidLineWidth(70)
        self.formFrameKullanici.setObjectName("formFrameKullanici")
        self.formLayout = QtWidgets.QFormLayout(self.formFrameKullanici)
        self.formLayout.setObjectName("formLayout")
        spacerItem = QtWidgets.QSpacerItem(
            20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.label = QtWidgets.QLabel(self.formFrameKullanici)
        self.label.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color:rgb(255, 255, 255);")
        self.label.setLineWidth(8)
        self.label.setMidLineWidth(10)
        self.label.setObjectName("label")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.formFrameKullanici)
        self.lineEdit.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color:rgb(138, 167, 227);\n"
                                    "")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formFrameKullanici)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("color:rgb(138, 167, 227);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(
            5, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.formFrameKullanici)
        self.label_2.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setStyleSheet("color:rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(
            QtCore.QRect(140, 430, 501, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(600, 400))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color:rgb(0, 117, 0);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar_K = QtWidgets.QStatusBar(MainWindow)
        self.statusBar_K.setMinimumSize(QtCore.QSize(0, 30))
        self.statusBar_K.setObjectName("statusBar_K")
        MainWindow.setStatusBar(self.statusBar_K)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "   LOGIN SCREEN"))
        self.label.setText(_translate("MainWindow", "   🆔   ID: "))
        self.label_2.setText(_translate("MainWindow", "   🔐  PASSWORD : "))
        self.pushButton.setText(_translate("MainWindow", " ✅ LOGIN"))
        ##########################111#####################
        self.pushButton.clicked.connect(self.Login)

    def Login(self):
        self.baglanti = sqlite3.connect('stock_database.db')
        self.cur = self.baglanti.cursor()

        self.cur.execute('SELECT * From user')
        data = self.cur.fetchall()
        if len(data) == 0:
            self.statusBar_K.showMessage("data connection error")
            self.statusBar_K.setStyleSheet("color:rgb(116, 3, 3)")

        id = self.lineEdit.text()
        password = self.lineEdit_2.text()

        print(id, password)
        for i in data:
            if id == str(i[2]) and password == str(i[1]):
                if i[3] == "M":
                    self.statusBar_K.showMessage(
                        "WELCOME!!!")
                    self.statusBar_K.setStyleSheet("color:rgb(1, 1, 119)")
                    time.sleep(1)
                    self.ui = Ui_MainWindow_2s()
                    self.ui.setupUi(MainWindow)
                elif i[3] == "C":
                    self.statusBar_K.showMessage(
                        "WELCOME!!!")
                    self.statusBar_K.setStyleSheet("color:rgb(1, 1, 119)")
                    time.sleep(1)
                    self.ui = Ui_MainWindow_3k()
                    self.ui.setupUi(MainWindow)
            else:
                self.statusBar_K.showMessage(
                    "Wrong id or password!!! Try again...")
                self.statusBar_K.setStyleSheet("color:rgb(116, 3, 3)")
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_L()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
