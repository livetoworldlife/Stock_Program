# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/hackyourfuture/Documents/Python3/DERSLER/PyQt5/kasaPanel.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


import buy_rc
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_MainWindow_3k(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 800)
        MainWindow.setMinimumSize(QtCore.QSize(600, 800))
        MainWindow.setMaximumSize(QtCore.QSize(600, 800))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
                                         "background-color: rgb(255, 255, 255);\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(150, 320, 421, 341))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.formFrame = QtWidgets.QFrame(self.centralwidget)
        self.formFrame.setGeometry(QtCore.QRect(20, 20, 431, 271))
        self.formFrame.setStyleSheet("#formFrame{\n"
                                     "background-color: rgb(138, 167, 227);\n"
                                     "}\n"
                                     "")
        self.formFrame.setObjectName("formFrame")
        self.formLayout = QtWidgets.QFormLayout(self.formFrame)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formFrame)
        self.label.setMinimumSize(QtCore.QSize(100, 40))
        self.label.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.formFrame)
        self.lineEdit.setMinimumSize(QtCore.QSize(250, 40))
        self.lineEdit.setMaximumSize(QtCore.QSize(250, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.formFrame)
        self.label_2.setMinimumSize(QtCore.QSize(100, 40))
        self.label_2.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formFrame)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(250, 40))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(250, 40))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.formFrame)
        self.label_3.setMinimumSize(QtCore.QSize(100, 40))
        self.label_3.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formFrame)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(250, 40))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(250, 40))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.formFrame)
        self.label_4.setMinimumSize(QtCore.QSize(100, 40))
        self.label_4.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:white;")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formFrame)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(250, 40))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(250, 40))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        spacerItem = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(
            5, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.verticalFrame = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame.setGeometry(QtCore.QRect(490, 20, 80, 260))
        self.verticalFrame.setMinimumSize(QtCore.QSize(80, 260))
        self.verticalFrame.setMaximumSize(QtCore.QSize(80, 260))
        self.verticalFrame.setStyleSheet("#verticalFrame{\n"
                                         "background-color:rgb(245,245,245);\n"
                                         "border-radius: 4px;\n"
                                         "}")
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalFrame)
        self.pushButton.setMinimumSize(QtCore.QSize(68, 60))
        self.pushButton.setMaximumSize(QtCore.QSize(68, 60))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/sorgu/icons/barkod.png"),
                       QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(48, 48))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalFrame)
        self.pushButton_2.setMinimumSize(QtCore.QSize(68, 60))
        self.pushButton_2.setMaximumSize(QtCore.QSize(68, 60))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/temiz/icons/clean.png"),
                        QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalFrame)
        self.pushButton_3.setMinimumSize(QtCore.QSize(68, 60))
        self.pushButton_3.setMaximumSize(QtCore.QSize(68, 60))
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ekle/icons/ekle copy.png"),
                        QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.horizontalFrame = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame.setGeometry(QtCore.QRect(20, 680, 551, 92))
        self.horizontalFrame.setStyleSheet("#horizontalFrame{\n"
                                           "background-color: rgb(55, 99, 99);\n"
                                           "}")
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.horizontalFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:white;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.textBrowser = QtWidgets.QTextBrowser(self.horizontalFrame)
        self.textBrowser.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)
        self.label_6 = QtWidgets.QLabel(self.horizontalFrame)
        self.label_6.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:white;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.horizontalFrame)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(80, 69))
        self.lineEdit_5.setMaximumSize(QtCore.QSize(80, 80))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout.addWidget(self.lineEdit_5)
        self.label_7 = QtWidgets.QLabel(self.horizontalFrame)
        self.label_7.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:white;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.horizontalFrame)
        self.textBrowser_2.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout.addWidget(self.textBrowser_2)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 319, 121, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(110, 110))
        self.pushButton_4.setMaximumSize(QtCore.QSize(120, 120))
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/ekle/icons/shop.png"),
                        QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(110, 110))
        self.pushButton_5.setMaximumSize(QtCore.QSize(120, 120))
        self.pushButton_5.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/buy/icons/odeme.png"),
                        QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(110, 110))
        self.pushButton_6.setMaximumSize(QtCore.QSize(120, 120))
        self.pushButton_6.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/buy/icons/receipt,png.png"),
                        QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "CASHREGISTER SCREEN"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "PRODUCT"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "COST"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "PIECE"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "P TOTAL"))
        self.label.setText(_translate("MainWindow", "BARKOD"))
        self.label_2.setText(_translate("MainWindow", "PRODUCT"))
        self.label_3.setText(_translate("MainWindow", "COST"))
        self.label_4.setText(_translate("MainWindow", "PIECE"))
        self.label_5.setText(_translate("MainWindow", "TOTAL"))
        self.label_6.setText(_translate("MainWindow", "GIVEN"))
        self.label_7.setText(_translate("MainWindow", "CHANGE"))

        ##########yaz###
        self.pushButton.clicked.connect(self.Query)  # sorgula
        self.pushButton_3.clicked.connect(self.Clist)  # alim
        self.pushButton_4.clicked.connect(self.Cbuy)  # al
        self.pushButton_5.clicked.connect(self.CPayment)  # odeme
        self.pushButton_2.clicked.connect(self.CClean)  # temizle

    def Query(self):
        self.baglanti = sqlite3.connect('stock_database.db')
        self.cur = self.baglanti.cursor()

        barkod = self.lineEdit.text()

        self.cur.execute("""SELECT 'clean' AS tablo,price,kind 
        FROM clean 
        WHERE code=?
        UNION ALL
        SELECT 'fruit' AS tablo,price,kind
        FROM fruit 
        WHERE code=?
        UNION ALL
        SELECT 'meat' AS tablo,price,kind
        FROM meat 
        WHERE code=?
        UNION ALL
        SELECT 'legumes' AS tablo,price,kind
        FROM legumes 
        WHERE code=?""", (int(barkod), int(barkod), int(barkod), int(barkod)))
        data = self.cur.fetchall()
        if len(data) == 0:
            self.statusbar.showMessage("data connection error")
            self.statusbar.setStyleSheet("color:rgb(116, 3, 3)")
        else:
            self.statusbar.showMessage("data was found in the database")
            self.statusbar.setStyleSheet("color:rgb(1, 1, 119)")
            self.lineEdit_2.setText(data[0][2])
            self.lineEdit_3.setText(str(data[0][1]))

    def Clist(self):
        kind = self.lineEdit_2.text()
        price = self.lineEdit_3.text()
        piece = self.lineEdit_4.text()
        table = []
        table_list = []
        table.append(kind)
        table.append(price)
        table.append(piece)
        table.append(int(price)*int(piece))
        table = tuple(table)
        table_list.append(table)

        self.tableWidget.insertRow(0)
        for row, form in enumerate(table_list):
            for column, item in enumerate(form):
                self.tableWidget.setItem(
                    row, column, QtWidgets.QTableWidgetItem(str(item)))
                column += 1
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)

        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")

    def Cbuy(self):
        number_rows = self.tableWidget.rowCount()/2
        payment = 0

        for i in range(int(number_rows)):
            pay = int(self.tableWidget.item(i, 3).text())
            payment += pay
        print(payment)
        self.textBrowser.setText(str(payment))

    def CClean(self):
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
        self.textBrowser.setText("")

    def CPayment(self):
        from datetime import datetime
        date = datetime.now().strftime("%x")
        time = datetime.now().strftime("%X")

        self.baglanti_c = sqlite3.connect('stock_database.db')
        self.cur_c = self.baglanti_c.cursor()

        payment = self.textBrowser.toPlainText()

        self.cur_c.execute("INSERT INTO amount VALUES (?,?,?)",
                           (int(payment), str(date), str(time)))

        self.baglanti_c.commit()

        data = []
        allRows = self.tableWidget.rowCount()/2
        for row in range(int(allRows)):
            c = []
            cins = self.tableWidget.item(row, 0).text()
            miktar = self.tableWidget.item(row, 2).text()
            c.append(cins)
            c.append(miktar)
            data.append(c)

        for i in data:
            kind = i[0]

            self.cur_c.execute("""SELECT 'clean' AS tablo,code,piece 
                                FROM clean 
                                WHERE kind=?
                                UNION ALL
                                SELECT 'fruit' AS tablo,code,piece 
                                FROM fruit 
                                WHERE kind=?
                                UNION ALL
                                SELECT 'meat' AS tablo,code,piece 
                                FROM meat 
                                WHERE kind=?
                                UNION ALL
                                SELECT 'legumes' AS tablo,code,piece
                                FROM legumes 
                                WHERE kind=?""", (kind, kind, kind, kind))
            data_ = self.cur_c.fetchall()
            print(data_)

            if data_[0][0] == "clean":
                self.cur_c.execute(
                    "UPDATE clean Set piece=piece=? WHERE code=?", (int(i[1]), data_[0][1]))
                self.baglanti_c.commit()
            elif data_[0][0] == "fruit":
                self.cur_c.execute(
                    "UPDATE fruit Set piece=piece=? WHERE code=?", (int(i[1]), data_[0][1]))
                self.baglanti_c.commit()
            elif data_[0][0] == "meat":
                self.cur_c.execute(
                    "UPDATE meat Set piece=piece=? WHERE code=?", (int(i[1]), data_[0][1]))
                self.baglanti_c.commit()
            elif data_[0][0] == "legumes":
                self.cur_c.execute(
                    "UPDATE legumes Set piece=piece=? WHERE code=?", (int(i[1]), data_[0][1]))
                self.baglanti_c.commit()

        self.statusbar.showMessage("updated the stock successfully")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_3k()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
