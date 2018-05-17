# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logo.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from main2 import Ui_ProyectoHCI
from helps import Ui_MainWindow
from main2 import QLCDCountDown
from instrucciones import Ui_Main
import PyQt5.QtMultimedia as M
import sys



class Ui_Logo(object):
    
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Main()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(683, 437)
        MainWindow.setStyleSheet("border-image: url(:/newPrefix/pantallainicio.JPG);")
    
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.iniciarprograma = QtWidgets.QPushButton(self.centralwidget)
        self.iniciarprograma.setGeometry(QtCore.QRect(250, 360, 201, 71))
        self.iniciarprograma.setStyleSheet("border-image: url(:/newPrefix/iniciodeprograma.JPG);")
        self.iniciarprograma.setText("")
        self.iniciarprograma.setObjectName("iniciarprograma")
        self.iniciarprograma.clicked.connect(self.openWindow)
        #self.iniciarprograma.clicked.connect(self.music)
        MainWindow.setCentralWidget(self.centralwidget)
      
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OCCHIO VARMO"))
        url= QtCore.QUrl.fromLocalFile("./orange.mp3")
        content= M.QMediaContent(url)
        player = M.QMediaPlayer()
        player.setMedia(content)
        player.play()
        
    #def music(self):
        #url= QtCore.QUrl.fromLocalFile("./orange.mp3")
        #content= M.QMediaContent(url)
        #player = M.QMediaPlayer()
       # player.setMedia(content)
        #player.play()


import iniciar_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Logo()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

