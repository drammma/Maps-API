# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DesignUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 883)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.picture = QtWidgets.QLabel(self.centralwidget)
        self.picture.setGeometry(QtCore.QRect(110, 260, 600, 381))
        self.picture.setMaximumSize(QtCore.QSize(600, 450))
        self.picture.setStyleSheet("background-color: rgb(230, 230, 230);\n"
"border-color: rgb(0, 0, 0);")
        self.picture.setText("")
        self.picture.setObjectName("picture")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 660, 801, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.Button = QtWidgets.QPushButton(self.centralwidget)
        self.Button.setGeometry(QtCore.QRect(330, 220, 121, 31))
        self.Button.setStyleSheet("font: 14pt \"Comic Sans MS\";\n"
"background-color: rgb(0, 170, 255);")
        self.Button.setObjectName("Button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -20, 1501, 861))
        self.label.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.99005, y2:0.972, stop:0.129353 rgba(46, 132, 178, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setText("")
        self.label.setObjectName("label")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(110, 260, 600, 1))
        self.line_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(110, 640, 600, 1))
        self.line_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(710, 260, 1, 381))
        self.line_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(110, 260, 1, 381))
        self.line_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(680, 810, 121, 31))
        self.label_5.setStyleSheet("font: italic 11pt \"Sitka Heading\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 5, 801, 41))
        self.label_6.setStyleSheet("font: 16pt \"Segoe Script\";")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.keyboard = QtWidgets.QCheckBox(self.centralwidget)
        self.keyboard.setGeometry(QtCore.QRect(690, 680, 101, 20))
        self.keyboard.setStyleSheet("font: 8pt \"Comic Sans MS\";")
        self.keyboard.setObjectName("keyboard")
        self.type_cart = QtWidgets.QComboBox(self.centralwidget)
        self.type_cart.setGeometry(QtCore.QRect(20, 710, 111, 22))
        self.type_cart.setObjectName("type_cart")
        self.type_cart.addItem("")
        self.type_cart.addItem("")
        self.type_cart.addItem("")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 680, 91, 31))
        self.label_7.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"text-decoration: underline;")
        self.label_7.setObjectName("label_7")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 30, 761, 161))
        self.tabWidget.setObjectName("tabWidget")
        self.Coordibate = QtWidgets.QWidget()
        self.Coordibate.setObjectName("Coordibate")
        self.label_9 = QtWidgets.QLabel(self.Coordibate)
        self.label_9.setGeometry(QtCore.QRect(10, 0, 151, 61))
        self.label_9.setStyleSheet("font: 14pt \"Comic Sans MS\";\n"
"text-decoration: underline;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.Coordibate)
        self.label_10.setGeometry(QtCore.QRect(10, 40, 151, 61))
        self.label_10.setStyleSheet("font: 14pt \"Comic Sans MS\";\n"
"text-decoration: underline;")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.Coordibate)
        self.label_11.setGeometry(QtCore.QRect(10, 80, 121, 61))
        self.label_11.setStyleSheet("font: 14pt \"Comic Sans MS\";\n"
"text-decoration: underline;")
        self.label_11.setObjectName("label_11")
        self.coordY = QtWidgets.QLineEdit(self.Coordibate)
        self.coordY.setGeometry(QtCore.QRect(160, 60, 591, 22))
        self.coordY.setObjectName("coordY")
        self.coordX = QtWidgets.QLineEdit(self.Coordibate)
        self.coordX.setGeometry(QtCore.QRect(160, 20, 591, 22))
        self.coordX.setObjectName("coordX")
        self.coordZ = QtWidgets.QSpinBox(self.Coordibate)
        self.coordZ.setGeometry(QtCore.QRect(160, 100, 591, 21))
        self.coordZ.setMaximum(17)
        self.coordZ.setObjectName("coordZ")
        self.tabWidget.addTab(self.Coordibate, "")
        self.Text = QtWidgets.QWidget()
        self.Text.setObjectName("Text")
        self.Address_line = QtWidgets.QLineEdit(self.Text)
        self.Address_line.setGeometry(QtCore.QRect(150, 50, 591, 22))
        self.Address_line.setObjectName("Address_line")
        self.label_8 = QtWidgets.QLabel(self.Text)
        self.label_8.setGeometry(QtCore.QRect(40, 30, 101, 61))
        self.label_8.setStyleSheet("font: 14pt \"Comic Sans MS\";\n"
"text-decoration: underline;")
        self.label_8.setObjectName("label_8")
        self.tabWidget.addTab(self.Text, "")
        self.label.raise_()
        self.picture.raise_()
        self.line.raise_()
        self.Button.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.line_5.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.keyboard.raise_()
        self.type_cart.raise_()
        self.label_7.raise_()
        self.tabWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button.setText(_translate("MainWindow", "\'OK\'"))
        self.label_5.setText(_translate("MainWindow", "[by drammma]"))
        self.label_6.setText(_translate("MainWindow", "- Maps API -"))
        self.keyboard.setText(_translate("MainWindow", "Клавиатура"))
        self.type_cart.setItemText(0, _translate("MainWindow", "Спутник"))
        self.type_cart.setItemText(1, _translate("MainWindow", "Гибрид"))
        self.type_cart.setItemText(2, _translate("MainWindow", "Схема"))
        self.label_7.setText(_translate("MainWindow", "тип карты:"))
        self.label_9.setText(_translate("MainWindow", "X coordinate:"))
        self.label_10.setText(_translate("MainWindow", "Y coordinate:"))
        self.label_11.setText(_translate("MainWindow", "Scale < 17:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Coordibate), _translate("MainWindow", "Coordinate"))
        self.label_8.setText(_translate("MainWindow", "Address:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Text), _translate("MainWindow", "Text"))
