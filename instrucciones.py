# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'instrucciones.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from helps import Ui_MainWindow
from main2 import Ui_ProyectoHCI

class Ui_Main(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ProyectoHCI()
        self.ui.setupUi(self.window)
        #MainWindow1.hide()
        #MainWindow1.setVisible(False)
        self.window.show()
    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.resize(1073, 665)
        MainWindow1.setStyleSheet("border-image: url(:/newPrefix/empezar.JPG);")
        self.centralwidget = QtWidgets.QWidget(MainWindow1)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 580, 1061, 91))
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/start.JPG);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openWindow)
        MainWindow1.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", "MainWindow1"))

import instrucciones_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(MainWindow1)
    MainWindow1.show()
    sys.exit(app.exec_())

