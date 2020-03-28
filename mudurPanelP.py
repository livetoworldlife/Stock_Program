# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/hackyourfuture/Documents/Python3/DERSLER/PyQt5/mudurPanel.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import sqlite3
import add_rc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_2s(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget.setStyleSheet("#centralwidget{\n"
                                         "background-color: rgb(255, 255, 255);\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(90, 10, 591, 521))
        self.tabWidget.setStyleSheet("#tabWidget{\n"
                                     "background-color: rgb(138, 167, 227);\n"
                                     "}\n"
                                     "")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("#tab{\n"
                               "background-color: rgb(138, 167, 227);\n"
                               "}\n"
                               "")
        self.tab.setObjectName("tab")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(60, 130, 461, 291))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(115, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setMinimumSize(QtCore.QSize(256, 40))
        self.comboBox.setMaximumSize(QtCore.QSize(256, 40))
        self.comboBox.setBaseSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setAcceptDrops(False)
        self.comboBox.setMaxVisibleItems(10)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setMinimumSize(QtCore.QSize(115, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:white;")
        self.label_9.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(250, 40))
        self.lineEdit_7.setMaximumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(115, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(250, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(115, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(250, 40))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(115, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:white;")
        self.label_4.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(
            6, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(250, 40))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(
            6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        spacerItem = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(
            7, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.horizontalFrame = QtWidgets.QFrame(self.tab)
        self.horizontalFrame.setGeometry(QtCore.QRect(20, 30, 541, 81))
        self.horizontalFrame.setStyleSheet("#horizontalFrame{\n"
                                           "background-color:rgb(245,245,245);\n"
                                           "border-radius: 4px;\n"
                                           "}")
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalFrame)
        self.pushButton.setMinimumSize(QtCore.QSize(64, 64))
        self.pushButton.setMaximumSize(QtCore.QSize(64, 64))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/seacrh/icons/research.png"),
                       QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalFrame)
        self.pushButton_2.setMinimumSize(QtCore.QSize(64, 64))
        self.pushButton_2.setMaximumSize(QtCore.QSize(64, 64))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/save/icons/Save-icon.png"),
                        QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalFrame)
        self.pushButton_3.setMinimumSize(QtCore.QSize(64, 64))
        self.pushButton_3.setMaximumSize(QtCore.QSize(64, 64))
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/delete/icons/delete.png"),
                        QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalFrame)
        self.pushButton_7.setMinimumSize(QtCore.QSize(64, 64))
        self.pushButton_7.setMaximumSize(QtCore.QSize(64, 64))
        self.pushButton_7.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/refresh/icons/Refresh.png"),
                        QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.pushButton_7.setIcon(icon3)
        self.pushButton_7.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setStyleSheet("#tab_2{\n"
                                 "background-color: rgb(138, 167, 227);\n"
                                 "}\n"
                                 "")
        self.tab_2.setObjectName("tab_2")
        self.horizontalFrame_2 = QtWidgets.QFrame(self.tab_2)
        self.horizontalFrame_2.setGeometry(QtCore.QRect(20, 30, 541, 81))
        self.horizontalFrame_2.setStyleSheet("#horizontalFrame_2{\n"
                                             "background-color:rgb(245,245,245);\n"
                                             "border-radius: 4px;\n"
                                             "}")
        self.horizontalFrame_2.setObjectName("horizontalFrame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalFrame_2)
        self.pushButton_4.setMinimumSize(QtCore.QSize(64, 64))
        self.pushButton_4.setMaximumSize(QtCore.QSize(64, 64))
        self.pushButton_4.setText("")
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalFrame_2)
        self.pushButton_5.setMinimumSize(QtCore.QSize(64, 64))
        self.pushButton_5.setMaximumSize(QtCore.QSize(64, 64))
        self.pushButton_5.setText("")
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalFrame_2)
        self.pushButton_6.setMinimumSize(QtCore.QSize(64, 64))
        self.pushButton_6.setMaximumSize(QtCore.QSize(64, 64))
        self.pushButton_6.setText("")
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.pushButton_12 = QtWidgets.QPushButton(self.horizontalFrame_2)
        self.pushButton_12.setMinimumSize(QtCore.QSize(64, 64))
        self.pushButton_12.setMaximumSize(QtCore.QSize(64, 64))
        self.pushButton_12.setText("")
        self.pushButton_12.setIcon(icon3)
        self.pushButton_12.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_3.addWidget(self.pushButton_12)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(29, 140, 521, 291))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(250, 40))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(250, 40))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_5.setMinimumSize(QtCore.QSize(140, 40))
        self.label_5.setMaximumSize(QtCore.QSize(140, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:white;")
        self.label_5.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(250, 40))
        self.lineEdit_5.setMaximumSize(QtCore.QSize(250, 40))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout_2.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_6.setMinimumSize(QtCore.QSize(160, 40))
        self.label_6.setMaximumSize(QtCore.QSize(160, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:white;")
        self.label_6.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(250, 40))
        self.lineEdit_6.setMaximumSize(QtCore.QSize(250, 40))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout_2.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_8.setMinimumSize(QtCore.QSize(160, 40))
        self.label_8.setMaximumSize(QtCore.QSize(160, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:white;")
        self.label_8.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.comboBox_2 = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.comboBox_2.setMinimumSize(QtCore.QSize(256, 40))
        self.comboBox_2.setMaximumSize(QtCore.QSize(256, 40))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.formLayout_2.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_7.setMinimumSize(QtCore.QSize(140, 40))
        self.label_7.setMaximumSize(QtCore.QSize(140, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:white;")
        self.label_7.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.label_7)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(
            0, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(
            5, QtWidgets.QFormLayout.FieldRole, spacerItem3)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar_s = QtWidgets.QStatusBar(MainWindow)
        self.statusbar_s.setMinimumSize(QtCore.QSize(0, 30))
        self.statusbar_s.setObjectName("statusbar_s")
        MainWindow.setStatusBar(self.statusbar_s)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MANAGER SCREEN"))
        self.label.setText(_translate("MainWindow", "★ KIND : "))
        self.comboBox.setItemText(0, _translate("MainWindow", " "))
        self.comboBox.setItemText(1, _translate("MainWindow", "GREENGROCERY"))
        self.comboBox.setItemText(2, _translate("MainWindow", "BUTCHER"))
        self.comboBox.setItemText(3, _translate("MainWindow", "CLEANING"))
        self.comboBox.setItemText(4, _translate("MainWindow", "LEGUMES"))
        self.label_9.setText(_translate("MainWindow", "∅ PRODUCT : "))
        self.label_2.setText(_translate("MainWindow", "∎ STOCK CODE : "))
        self.label_3.setText(_translate("MainWindow", "☖☗ PIECE : "))
        self.label_4.setText(_translate("MainWindow", "＄ COST : "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab), _translate("MainWindow", "STOCK OPERATIONS"))
        self.label_5.setText(_translate("MainWindow", "🛅   ID : "))
        self.label_6.setText(_translate("MainWindow", "🚹  NAME : "))
        self.label_8.setText(_translate("MainWindow", "🈳   PASSWORD : "))
        self.comboBox_2.setItemText(0, _translate("MainWindow", " "))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "CASHIER"))
        self.comboBox_2.setItemText(
            2, _translate("MainWindow", "MANAGER"))
        self.label_7.setText(_translate("MainWindow", " 🛃  POSITION : "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_2), _translate("MainWindow", "STAFF OPERATIONS"))
        # calisan islemleri sorgula butonu
        self.pushButton_4.clicked.connect(self.Query)
        # calisan islemleri kaydet butonu
        self.pushButton_5.clicked.connect(self.Save)
        # calisan islemleri sil butonu
        self.pushButton_6.clicked.connect(self.Delete)
        self.pushButton_12.clicked.connect(self.Refresh)
        ##########################2.ONLINE DERS############
        # stok islemleri sorgula butonu
        self.pushButton.clicked.connect(self.SQuery)
        # stok islemleri kaydet butonu
        self.pushButton_2.clicked.connect(self.SSave)
        # stok islemleri sil butonu
        self.pushButton_3.clicked.connect(self.SDelete)
        self.pushButton_7.clicked.connect(self.SRefresh)

    def Query(self):
        self.baglanti = sqlite3.connect('stock_database.db')
        self.cur = self.baglanti.cursor()

        self.cur.execute("SELECT * FROM user")
        data = self.cur.fetchall()
        # print(data)

        id = self.lineEdit_4.text()  # calsina islemleri sicil yanindaki text kismi
        k = 1
        for i in data:
            if id == str(i[2]):
                # print(i)
                # calsina islemleri adsoyad yanindaki text kismi
                self.lineEdit_5.setText(str(i[0]))
                # calsina islemleri sifre yanindaki text kismi
                self.lineEdit_6.setText(str(i[1]))
                self.statusbar_s.showMessage(
                    "This ID was found in the database")
                self.statusbar_s.setStyleSheet("color:rgb(1, 1, 119)")

                if i[3] == "M":
                    self.comboBox_2.setCurrentText("MANAGER")
                else:
                    self.comboBox_2.setCurrentText("CASHIER")

                break

            if k == len(data):
                self.lineEdit_5.setText("")
                self.lineEdit_6.setText("")
                # calisan islmler ksiminda en alttaki buyuk alan
                self.statusbar_s.showMessage(
                    "This ID could not be found in the database")
                self.statusbar_s.setStyleSheet("color:rgb(116, 3, 3)")

            k += 1

    def Save(self):
        self.baglanti_ = sqlite3.connect('stock_database.db')
        self.cur_ = self.baglanti_.cursor()

        id_list = []
        self.cur_.execute("SELECT * FROM user")
        data_ = self.cur_.fetchall()

        for i in data_:
            id_list.append(i[2])

        id = self.lineEdit_4.text()  # calsina islemleri sicil yanindaki text kismi
        name = self.lineEdit_5.text()
        password = self.lineEdit_6.text()
        position = self.comboBox_2.currentText()
        if position == "CASHIER":
            position_ = "C"
        else:
            position_ = "M"
        # print(position_)
        if int(id) in id_list:
            self.cur_.execute("UPDATE user SET name=?,password=?,position=? WHERE id=?", (name, int(
                password), position_, int(id)))
            self.baglanti_.commit()
            self.lineEdit_4.setText("")
            self.lineEdit_5.setText("")
            self.lineEdit_6.setText("")
            self.statusbar_s.showMessage(
                "User information was updated in the database")
            self.statusbar_s.setStyleSheet("color:rgb(1, 94, 21)")
        else:
            self.cur_.execute("INSERT INTO user VALUES (?,?,?,?)",
                              (name, int(password), int(id), position_))
            # DEGISIKLIGI GOSTERME
            self.lineEdit_4.setText("")
            self.lineEdit_5.setText("")
            self.lineEdit_6.setText("")
            self.statusbar_s.showMessage(
                "New staff was added in the database")
            self.statusbar_s.setStyleSheet("color:rgb(1,1,119)")

            self.baglanti_.commit()

    def Delete(self):
        self.baglanti_d = sqlite3.connect('stock_database.db')
        self.cur_d = self.baglanti_d.cursor()
        id = self.lineEdit_4.text()  # calsina islemleri sicil yanindaki text kismi
        self.cur_d.execute("DELETE FROM user WHERE id=?", (int(id),))

        # DEGISIKLIGI GOSTERME
        self.Refresh()
        self.statusbar_s.showMessage(
            "A staff was deleted from the database")
        self.statusbar_s.setStyleSheet("color:rgb(1,1,119)")
        self.baglanti_d.commit()

    def Refresh(self):
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.statusbar_s.showMessage("")
        self.comboBox_2.setCurrentText(" ")

    def SQuery(self):  # 2.online ders
        self.baglanti_sq = sqlite3.connect('stock_database.db')
        self.cur_sq = self.baglanti_sq.cursor()

        kind = self.comboBox.currentText()
        stok = self.lineEdit.text()

        if kind == "GREENGROCERY":
            self.cur_sq.execute("SELECT * FROM fruit")
            data_sq = self.cur_sq.fetchall()

            id_list = []

            for i in data_sq:
                id_list.append(i[0])

            if int(stok) in id_list:
                for i in data_sq:
                    if int(stok) == i[0]:
                        self.lineEdit_7.setText(i[3])
                        self.lineEdit_2.setText(str(i[1]))
                        self.lineEdit_3.setText(str(i[2]))

                        break
            else:
                self.lineEdit_7.setText("")
                self.lineEdit_2.setText("")
                self.lineEdit_3.setText("")
                self.statusbar_s.showMessage(
                    "This stock could not be found in the database")
                self.statusbar_s.setStyleSheet("color:rgb(116,3,3)")

        elif kind == "CLEANING":
            self.cur_sq.execute("SELECT * FROM clean")
            data_sq = self.cur_sq.fetchall()

            id_list = []

            for i in data_sq:
                id_list.append(i[0])

            if int(stok) in id_list:
                for i in data_sq:
                    if int(stok) == i[0]:
                        self.lineEdit_7.setText(i[3])
                        self.lineEdit_2.setText(str(i[1]))
                        self.lineEdit_3.setText(str(i[2]))

                        break
            else:
                self.lineEdit_7.setText("")
                self.lineEdit_2.setText("")
                self.lineEdit_3.setText("")
                self.statusbar_s.showMessage(
                    "This stock could not be found in the database")
                self.statusbar_s.setStyleSheet("color:rgb(116,3,3)")

        elif kind == "LEGUMES":
            self.cur_sq.execute("SELECT * FROM legumes")
            data_sq = self.cur_sq.fetchall()

            id_list = []

            for i in data_sq:
                id_list.append(i[0])

            if int(stok) in id_list:
                for i in data_sq:
                    if int(stok) == i[0]:
                        self.lineEdit_7.setText(i[3])
                        self.lineEdit_2.setText(str(i[1]))
                        self.lineEdit_3.setText(str(i[2]))

                        break
            else:
                self.lineEdit_7.setText("")
                self.lineEdit_2.setText("")
                self.lineEdit_3.setText("")
                self.statusbar_s.showMessage(
                    "This stock could not be found in the database")
                self.statusbar_s.setStyleSheet("color:rgb(116, 3, 3)")

        elif kind == "BUTCHER":
            self.cur_sq.execute("SELECT * FROM meat")
            data_sq = self.cur_sq.fetchall()

            id_list = []

            for i in data_sq:
                id_list.append(i[0])

            if int(stok) in id_list:
                for i in data_sq:
                    if int(stok) == i[0]:
                        self.lineEdit_7.setText(i[3])
                        self.lineEdit_2.setText(str(i[1]))
                        self.lineEdit_3.setText(str(i[2]))

                        break
            else:
                self.lineEdit_7.setText("")
                self.lineEdit_2.setText("")
                self.lineEdit_3.setText("")
                self.statusbar_s.showMessage(
                    "This stock could not be found in the database")
                self.statusbar_s.setStyleSheet("color:rgb(116,3,3)")

    def EkranYazdirStok(self, cesit, kod, adet, fiyat, ekran):
        self.lineEdit_7.setText(cesit)
        self.lineEdit.setText(kod)
        self.lineEdit_2.setText(adet)
        self.lineEdit_3.setText(fiyat)
        self.statusbar_s.showMessage(ekran)
        self.statusbar_s.setStyleSheet("color:rgb(1,94,21)")

    def SRefresh(self):
        self.lineEdit_7.setText("")
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.comboBox.setCurrentText(" ")
        self.statusbar_s.showMessage("")
        self.statusbar_s.setStyleSheet("color:rgb(1,94,21)")

    def SSave(self):

        self.baglanti_ss = sqlite3.connect('stock_database.db')
        self.cur_ss = self.baglanti_ss.cursor()

        kind = self.comboBox.currentText()
        kind_ces = self.lineEdit_7.text()
        stok = self.lineEdit.text()
        piece = self.lineEdit_2.text()
        price = self.lineEdit_3.text()

        if kind == "GREENGROCERY":
            self.cur_ss.execute("SELECT * FROM fruit")
            data_ss = self.cur_ss.fetchall()

            id_list = []

            for i in data_ss:
                id_list.append(i[0])

            if int(stok) in id_list:
                self.cur_ss.execute(
                    "UPDATE fruit SET piece=?,price=?,kind=? WHERE code=?", (int(piece), int(price), kind_ces, int(stok)))
                self.baglanti_ss.commit()

                self.EkranYazdirStok("", "", "", "", "stock is updated")

            else:
                self.cur_ss.execute(
                    "INSERT INTO fruit VALUES(?,?,?,?)", (int(stok), int(piece), int(price), kind_ces))
                self.baglanti_ss.commit()

                self.EkranYazdirStok("", "", "", "", "new stock is added")

        elif kind == "CLEANING":
            self.cur_ss.execute("SELECT * FROM clean")
            data_ss = self.cur_ss.fetchall()

            id_list = []

            for i in data_ss:
                id_list.append(i[0])

            if int(stok) in id_list:
                self.cur_ss.execute(
                    "UPDATE clean SET piece=?,price=?,kind=? WHERE code=?", (int(piece), int(price), kind_ces, int(stok)))
                self.baglanti_ss.commit()

                self.EkranYazdirStok("", "", "", "", "stock is updated")

            else:
                self.cur_ss.execute(
                    "INSERT INTO clean VALUES(?,?,?,?)", (int(stok), int(piece), int(price), kind_ces))
                self.baglanti_ss.commit()

                self.EkranYazdirStok("", "", "", "", "new stock is added")

        elif kind == "LEGUMES":
            self.cur_ss.execute("SELECT * FROM legumes")
            data_ss = self.cur_ss.fetchall()

            id_list = []

            for i in data_ss:
                id_list.append(i[0])

            if int(stok) in id_list:
                self.cur_ss.execute(
                    "UPDATE legumes SET piece=?,price=?,kind=? WHERE code=?", (int(piece), int(price), kind_ces, int(stok)))
                self.baglanti_ss.commit()

                self.EkranYazdirStok("", "", "", "", "stock is updated")

            else:
                self.cur_ss.execute(
                    "INSERT INTO legumes VALUES(?,?,?,?)", (int(stok), int(piece), int(price), kind_ces))
                self.baglanti_ss.commit()

                self.EkranYazdirStok("", "", "", "", "new stock is added")

        elif kind == "BUTCHER":
            self.cur_ss.execute("SELECT * FROM meat")
            data_ss = self.cur_ss.fetchall()

            id_list = []

            for i in data_ss:
                id_list.append(i[0])

            if int(stok) in id_list:
                self.cur_ss.execute(
                    "UPDATE meat SET piece=?,price=?,kind=? WHERE code=?", (int(piece), int(price), kind_ces, int(stok)))
                self.baglanti_ss.commit()

                self.EkranYazdirStok("", "", "", "", "stock is updated")

            else:
                self.cur_ss.execute(
                    "INSERT INTO meat VALUES(?,?,?,?)", (int(stok), int(piece), int(price), kind_ces))
                self.baglanti_ss.commit()

                self.EkranYazdirStok("", "", "", "", "new stock is added")

    def SDelete(self):
        self.baglanti_sd = sqlite3.connect('stock_database.db')
        self.cur_sd = self.baglanti_sd.cursor()

        kind = self.comboBox.currentText()
        stok = self.lineEdit.text()

        if kind == "GREENGROCERY":
            self.cur_sd.execute("DELETE FROM fruit WHERE code=?", (int(stok),))
            self.baglanti_sd.commit()
            self.EkranYazdirStok("", "", "", "", "the stock is deleted")
        elif kind == "CLEANING":
            self.cur_sd.execute("DELETE FROM clean WHERE code=?", (int(stok),))
            self.baglanti_sd.commit()
            self.EkranYazdirStok("", "", "", "", "the stock is deleted")
        elif kind == "LEGUMES":
            self.cur_sd.execute(
                "DELETE FROM legumes WHERE code=?", (int(stok),))
            self.baglanti_sd.commit()
            self.EkranYazdirStok("", "", "", "", "the stock is deleted")
        elif kind == "BUTCHER":
            self.cur_sd.execute("DELETE FROM meat WHERE code=?", (int(stok),))
            self.baglanti_sd.commit()
            self.EkranYazdirStok("", "", "", "", "the stock is deleted")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_2s()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
