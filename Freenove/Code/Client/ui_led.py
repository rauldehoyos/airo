# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_led(object):
    def setupUi(self, led):
        led.setObjectName("led")
        led.resize(630, 280)
        led.setStyleSheet("QWidget{\n"
"background:#484848;\n"
"}\n"
"QAbstractButton{\n"
"border-style:none;\n"
"border-radius:0px;\n"
"padding:5px;\n"
"color:#DCDCDC;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #858585,stop:1 #383838);\n"
"}\n"
"QAbstractButton:hover{\n"
"color:#000000;\n"
"background-color:#008aff;\n"
"}\n"
"QAbstractButton:pressed{\n"
"color:#DCDCDC;\n"
"border-style:solid;\n"
"border-width:0px 0px 0px 4px;\n"
"padding:4px 4px 4px 2px;\n"
"border-color:#008aff;\n"
"background-color:#444444;\n"
"}\n"
"\n"
"QLabel{\n"
"color:#DCDCDC;\n"
"\n"
"\n"
"}\n"
"QLabel:focus{\n"
"border:1px solid #00BB9E;\n"
"\n"
"}\n"
"\n"
"QLineEdit{\n"
"border:1px solid #242424;\n"
"border-radius:3px;\n"
"padding:2px;\n"
"background:none;\n"
"selection-background-color:#484848;\n"
"selection-color:#DCDCDC;\n"
"}\n"
"QLineEdit:focus,QLineEdit:hover{\n"
"border:1px solid #242424;\n"
"}\n"
"QLineEdit{\n"
"border:1px solid #242424;\n"
"border-radius:3px;\n"
"padding:2px;\n"
"background:none;\n"
"selection-background-color:#484848;\n"
"selection-color:#DCDCDC;\n"
"}\n"
"\n"
"QLineEdit:focus,QLineEdit:hover{\n"
"border:1px solid #242424;\n"
"}\n"
"QLineEdit{\n"
"lineedit-password-character:9679;\n"
"}")
        self.label_4 = QtWidgets.QLabel(led)
        self.label_4.setGeometry(QtCore.QRect(301, 155, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(led)
        self.label_6.setGeometry(QtCore.QRect(340, 20, 30, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.radioButtonOne = QtWidgets.QRadioButton(led)
        self.radioButtonOne.setGeometry(QtCore.QRect(20, 55, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.radioButtonOne.setFont(font)
        self.radioButtonOne.setObjectName("radioButtonOne")
        self.label_10 = QtWidgets.QLabel(led)
        self.label_10.setGeometry(QtCore.QRect(410, 20, 30, 20))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.radioButtonFour = QtWidgets.QRadioButton(led)
        self.radioButtonFour.setGeometry(QtCore.QRect(20, 190, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.radioButtonFour.setFont(font)
        self.radioButtonFour.setObjectName("radioButtonFour")
        self.label_8 = QtWidgets.QLabel(led)
        self.label_8.setGeometry(QtCore.QRect(255, 20, 30, 20))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.lineEdit_H = QtWidgets.QLineEdit(led)
        self.lineEdit_H.setGeometry(QtCore.QRect(145, 20, 30, 20))
        self.lineEdit_H.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_H.setObjectName("lineEdit_H")
        self.widget = QtWidgets.QWidget(led)
        self.widget.setGeometry(QtCore.QRect(320, 35, 290, 230))
        self.widget.setObjectName("widget")
        self.radioButtonFive = QtWidgets.QRadioButton(led)
        self.radioButtonFive.setGeometry(QtCore.QRect(20, 235, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.radioButtonFive.setFont(font)
        self.radioButtonFive.setObjectName("radioButtonFive")
        self.lineEdit_L = QtWidgets.QLineEdit(led)
        self.lineEdit_L.setGeometry(QtCore.QRect(285, 20, 30, 20))
        self.lineEdit_L.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_L.setObjectName("lineEdit_L")
        self.lineEdit_G = QtWidgets.QLineEdit(led)
        self.lineEdit_G.setGeometry(QtCore.QRect(440, 20, 30, 20))
        self.lineEdit_G.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_G.setObjectName("lineEdit_G")
        self.dial_color = QtWidgets.QDial(led)
        self.dial_color.setGeometry(QtCore.QRect(141, 95, 160, 140))
        self.dial_color.setStyleSheet("QDial {\n"
"image: url(:/Picture/hsl.png);\n"
"}\n"
"")
        self.dial_color.setObjectName("dial_color")
        self.label = QtWidgets.QLabel(led)
        self.label.setGeometry(QtCore.QRect(211, 235, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit_B = QtWidgets.QLineEdit(led)
        self.lineEdit_B.setGeometry(QtCore.QRect(510, 20, 30, 20))
        self.lineEdit_B.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_B.setObjectName("lineEdit_B")
        self.radioButtonThree = QtWidgets.QRadioButton(led)
        self.radioButtonThree.setGeometry(QtCore.QRect(20, 145, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.radioButtonThree.setFont(font)
        self.radioButtonThree.setObjectName("radioButtonThree")
        self.label_2 = QtWidgets.QLabel(led)
        self.label_2.setGeometry(QtCore.QRect(211, 75, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(led)
        self.label_5.setGeometry(QtCore.QRect(115, 20, 30, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(led)
        self.label_7.setGeometry(QtCore.QRect(185, 20, 30, 20))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.lineEdit_R = QtWidgets.QLineEdit(led)
        self.lineEdit_R.setGeometry(QtCore.QRect(370, 20, 30, 20))
        self.lineEdit_R.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_R.setObjectName("lineEdit_R")
        self.radioButtonTwo = QtWidgets.QRadioButton(led)
        self.radioButtonTwo.setGeometry(QtCore.QRect(20, 100, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.radioButtonTwo.setFont(font)
        self.radioButtonTwo.setObjectName("radioButtonTwo")
        self.lineEdit_S = QtWidgets.QLineEdit(led)
        self.lineEdit_S.setGeometry(QtCore.QRect(215, 20, 30, 20))
        self.lineEdit_S.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_S.setObjectName("lineEdit_S")
        self.label_9 = QtWidgets.QLabel(led)
        self.label_9.setGeometry(QtCore.QRect(480, 20, 30, 20))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_3 = QtWidgets.QLabel(led)
        self.label_3.setGeometry(QtCore.QRect(121, 155, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButtonLightsOut = QtWidgets.QPushButton(led)
        self.pushButtonLightsOut.setGeometry(QtCore.QRect(120, 55, 70, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pushButtonLightsOut.setFont(font)
        self.pushButtonLightsOut.setObjectName("pushButtonLightsOut")
        self.label_11 = QtWidgets.QLabel(led)
        self.label_11.setGeometry(QtCore.QRect(555, 20, 70, 25))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")

        self.retranslateUi(led)
        QtCore.QMetaObject.connectSlotsByName(led)

    def retranslateUi(self, led):
        _translate = QtCore.QCoreApplication.translate
        led.setWindowTitle(_translate("led", "Led"))
        self.label_4.setText(_translate("led", "270"))
        self.label_6.setText(_translate("led", "R"))
        self.radioButtonOne.setText(_translate("led", "Mode 1"))
        self.label_10.setText(_translate("led", "G"))
        self.radioButtonFour.setText(_translate("led", "Mode 4"))
        self.label_8.setText(_translate("led", "L"))
        self.lineEdit_H.setText(_translate("led", "0"))
        self.radioButtonFive.setText(_translate("led", "Mode 5"))
        self.lineEdit_L.setText(_translate("led", "1"))
        self.lineEdit_G.setText(_translate("led", "255"))
        self.label.setText(_translate("led", "0"))
        self.lineEdit_B.setText(_translate("led", "255"))
        self.radioButtonThree.setText(_translate("led", "Mode 3"))
        self.label_2.setText(_translate("led", "180"))
        self.label_5.setText(_translate("led", "H"))
        self.label_7.setText(_translate("led", "S"))
        self.lineEdit_R.setText(_translate("led", "255"))
        self.radioButtonTwo.setText(_translate("led", "Mode 2"))
        self.lineEdit_S.setText(_translate("led", "0"))
        self.label_9.setText(_translate("led", "B"))
        self.label_3.setText(_translate("led", "90"))
        self.pushButtonLightsOut.setText(_translate("led", "Turn off"))
        self.label_11.setText(_translate("led", "Brightness"))
