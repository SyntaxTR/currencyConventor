# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets\ui\UI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_KurHesaplayici(object):
    def setupUi(self, KurHesaplayici):
        KurHesaplayici.setObjectName("KurHesaplayici")
        KurHesaplayici.resize(537, 526)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/img/UIlogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        KurHesaplayici.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(KurHesaplayici)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 111, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 50, 101, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 10, 191, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 150, 71, 21))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 90, 151, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 130, 47, 16))
        self.label_6.setObjectName("label_6")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(200, 150, 82, 101))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.widget = QtWidgets.QWidget(self.splitter_2)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_4 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_2.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout_2.addWidget(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_6.setObjectName("radioButton_6")
        self.verticalLayout_2.addWidget(self.radioButton_6)
        self.radioButton_10 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_10.setObjectName("radioButton_10")
        self.verticalLayout_2.addWidget(self.radioButton_10)
        self.radioButton_8 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_8.setObjectName("radioButton_8")
        self.verticalLayout_2.addWidget(self.radioButton_8)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(310, 190, 201, 41))
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 180, 71, 23))
        self.pushButton.setObjectName("pushButton")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(90, 150, 91, 101))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.widget1 = QtWidgets.QWidget(self.splitter_4)
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.widget1)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_7 = QtWidgets.QRadioButton(self.widget1)
        self.radioButton_7.setObjectName("radioButton_7")
        self.verticalLayout.addWidget(self.radioButton_7)
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget1)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton_9 = QtWidgets.QRadioButton(self.widget1)
        self.radioButton_9.setObjectName("radioButton_9")
        self.verticalLayout.addWidget(self.radioButton_9)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget1)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(190, 50, 191, 21))
        self.label_8.setObjectName("label_8")
        KurHesaplayici.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(KurHesaplayici)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 537, 26))
        self.menubar.setObjectName("menubar")
        KurHesaplayici.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(KurHesaplayici)
        self.statusbar.setObjectName("statusbar")
        KurHesaplayici.setStatusBar(self.statusbar)

        self.retranslateUi(KurHesaplayici)
        QtCore.QMetaObject.connectSlotsByName(KurHesaplayici)

    def retranslateUi(self, KurHesaplayici):
        _translate = QtCore.QCoreApplication.translate
        KurHesaplayici.setWindowTitle(_translate("KurHesaplayici", "Kur Hesaplayıcı"))
        self.label_2.setText(_translate("KurHesaplayici", "<html><head/><body><p><span style=\" font-size:12pt;\">Dolar</span></p></body></html>"))
        self.label_3.setText(_translate("KurHesaplayici", "<html><head/><body><p><span style=\" font-size:12pt;\">Euro</span></p></body></html>"))
        self.label_4.setText(_translate("KurHesaplayici", "<html><head/><body><p><span style=\" font-size:12pt;\">Gram Altın</span></p></body></html>"))
        self.label_5.setText(_translate("KurHesaplayici", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Dönüştürücü</span></p></body></html>"))
        self.label_6.setText(_translate("KurHesaplayici", "Miktar"))
        self.label_8.setText(_translate("KurHesaplayici", "<html><head/><body><p><span style=\" font-size:12pt;\">Gümüş</span></p></body></html>"))
        self.radioButton_4.setText(_translate("KurHesaplayici", "Gram Altın"))
        self.radioButton_5.setText(_translate("KurHesaplayici", "TL"))
        self.radioButton_6.setText(_translate("KurHesaplayici", "Dolar"))
        self.radioButton_8.setText(_translate("KurHesaplayici", "Euro"))
        self.radioButton_9.setText(_translate("KurHesaplayici", "Gümüş"))
        self.radioButton_10.setText(_translate("KurHesaplayici", "Gümüş"))
        self.label_7.setText(_translate("KurHesaplayici", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Sonuç: </span></p></body></html>"))
        self.pushButton.setText(_translate("KurHesaplayici", "Hesapla"))
        self.radioButton_3.setText(_translate("KurHesaplayici", "Gram Altın"))
        self.radioButton_7.setText(_translate("KurHesaplayici", "TL"))
        self.radioButton.setText(_translate("KurHesaplayici", "Dolar"))
        self.radioButton_2.setText(_translate("KurHesaplayici", "Euro"))

