# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helps.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#import sys

class Ui_MainWindow(object):
    def setupUi(self, HelpsWindow):
        HelpsWindow.setObjectName("HelpsWindow")
        HelpsWindow.resize(823, 567)
        HelpsWindow.setStyleSheet("border-image: url(:/newPrefix/helps final 2.JPG);")
        self.centralwidget = QtWidgets.QWidget(HelpsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.English = QtWidgets.QPushButton(self.centralwidget)
        self.English.setGeometry(QtCore.QRect(620, 210, 101, 41))
        self.English.setStyleSheet("border-image: url(:/newPrefix/English.JPG);")
        self.English.setText("")
        self.English.setObjectName("English")
        self.cambiaridioma = QtWidgets.QPushButton(self.centralwidget)
        self.cambiaridioma.setGeometry(QtCore.QRect(610, 370, 141, 61))
        self.cambiaridioma.setStyleSheet("border-image: url(:/newPrefix/cambiar.JPG);")
        self.cambiaridioma.setText("")
        self.cambiaridioma.setObjectName("cambiaridioma")
        self.Spanish = QtWidgets.QPushButton(self.centralwidget)
        self.Spanish.setGeometry(QtCore.QRect(620, 300, 121, 41))
        self.Spanish.setStyleSheet("border-image: url(:/newPrefix/spanish.JPG);")
        self.Spanish.setText("")
        self.Spanish.setObjectName("Spanish")
        #self.backtomain = QtWidgets.QPushButton(self.centralwidget)
        #self.backtomain.setGeometry(QtCore.QRect(10, 10, 81, 61))
        #self.backtomain.setStyleSheet("border-image: url(:/newPrefix/backtomain.JPG);")
        #self.backtomain.setText("")
        #self.backtomain.setObjectName("backtomain")
        #self.backtomain.clicked.connect(self.hide)
        HelpsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(HelpsWindow)
        QtCore.QMetaObject.connectSlotsByName(HelpsWindow)

    def retranslateUi(self, HelpsWindow):
        _translate = QtCore.QCoreApplication.translate
        HelpsWindow.setWindowTitle(_translate("HelpsWindow", "OCCHIO VARMO"))
    def hide(self, HelpsWindow):
        sys.exit(app.exec_())
        #HelpsWindow.hide()

import helps_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HelpsWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(HelpsWindow)
    HelpsWindow.show()
    sys.exit(app.exec_())

