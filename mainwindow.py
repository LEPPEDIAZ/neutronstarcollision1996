# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
        QApplication, QLCDNumber
        )
from PyQt5.QtCore import(
        QTimer,
        QTime
)

class Ui_ProyectoHCI(object):
    def setupUi(self, ProyectoHCI):
        ProyectoHCI.setObjectName("ProyectoHCI")
        ProyectoHCI.resize(807, 554)
        font = QtGui.QFont()
        font.setPointSize(60)
        ProyectoHCI.setFont(font)
        ProyectoHCI.setStyleSheet("border-image: url(:/backgroud/fondopantalla2.JPG);")
        self.temp=0
        self.centralwidget = QtWidgets.QWidget(ProyectoHCI)
        self.centralwidget.setObjectName("centralwidget")
        self.subirtemperatura = QtWidgets.QPushButton(self.centralwidget)
        self.subirtemperatura.setGeometry(QtCore.QRect(80, 70, 81, 71))
        self.subirtemperatura.setStyleSheet("color: rgb(85, 85, 255);\n"
"border-image: url(:/backgroud/boton.JPG);\n"
"image: url(:/backgroud/boton.JPG);")
        self.subirtemperatura.setText("")
        self.subirtemperatura.setObjectName("subirtemperatura")
        self.subirtemperatura.clicked.connect(self.on_click2)
        self.arribatiempo = QtWidgets.QPushButton(self.centralwidget)
        self.arribatiempo.setGeometry(QtCore.QRect(360, 70, 81, 71))
        self.arribatiempo.setStyleSheet("image: url(:/backgroud/boton.JPG);\n"
"border-image: url(:/backgroud/boton.JPG);\n"
"background-image: url(:/backgroud/boton.JPG);")
        self.arribatiempo.setText("")
        self.arribatiempo.setObjectName("arribatiempo")
         # ------ Boton DISMINUIR ------
        self.debajotemperatura = QtWidgets.QPushButton(self.centralwidget)
        self.debajotemperatura.setGeometry(QtCore.QRect(80, 290, 91, 71))
        self.debajotemperatura.setStyleSheet("image: url(:/backgroud/boton2.JPG);\n"
"border-image: url(:/backgroud/boton2.JPG);")
        self.debajotemperatura.setText("")
        self.debajotemperatura.setObjectName("debajotemperatura")
        self.debajotemperatura.clicked.connect(self.on_click)
        
        self.abajotiempo = QtWidgets.QPushButton(self.centralwidget)
        self.abajotiempo.setGeometry(QtCore.QRect(350, 290, 91, 71))
        self.abajotiempo.setStyleSheet("border-image: url(:/backgroud/boton2.JPG);")
        self.abajotiempo.setText("")
        self.abajotiempo.setObjectName("abajotiempo")
        # -----------------------------
        self.Encendido = QtWidgets.QPushButton(self.centralwidget)
        self.Encendido.setGeometry(QtCore.QRect(560, 120, 231, 91))
        self.Encendido.setStyleSheet("border-image: url(:/backgroud/encendido.JPG);")
        self.Encendido.setText("")
        self.Encendido.setObjectName("Encendido")
        self.nuevaconsulta = QtWidgets.QPushButton(self.centralwidget)
        self.nuevaconsulta.setGeometry(QtCore.QRect(560, 320, 231, 91))
        self.nuevaconsulta.setStyleSheet("border-image: url(:/backgroud/nuevaconsulta.JPG);")
        self.nuevaconsulta.setText("")
        self.nuevaconsulta.setObjectName("nuevaconsulta")
        self.Pausa = QtWidgets.QPushButton(self.centralwidget)
        self.Pausa.setGeometry(QtCore.QRect(560, 220, 231, 91))
        self.Pausa.setStyleSheet("border-image: url(:/backgroud/pausa1.JPG);\n"
"image: url(:/backgroud/pausa1.JPG);")
        self.Pausa.setText("")
        self.Pausa.setObjectName("Pausa")
        self.nada = QtWidgets.QPushButton(self.centralwidget)
        self.nada.setGeometry(QtCore.QRect(570, 50, 121, 71))
        self.nada.setStyleSheet("border-image: url(:/backgroud/blanck.JPG);")
        self.nada.setText("")
        self.nada.setObjectName("nada")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 420, 181, 131))
        self.pushButton.setStyleSheet("border-image: url(:/backgroud/graficacaliente.JPG);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 120, 231, 251))
        self.pushButton_2.setStyleSheet("border-image: url(:/backgroud/blanck.JPG);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.nada2 = QtWidgets.QPushButton(self.centralwidget)
        self.nada2.setGeometry(QtCore.QRect(30, 50, 181, 23))
        self.nada2.setStyleSheet("image: url(:/backgroud/blanck.JPG);\n"
"border-image: url(:/backgroud/blanck.JPG);")
        self.nada2.setText("")
        self.nada2.setObjectName("nada2")
        self.nada3 = QtWidgets.QPushButton(self.centralwidget)
        self.nada3.setGeometry(QtCore.QRect(310, 50, 181, 23))
        self.nada3.setStyleSheet("border-image: url(:/backgroud/blanck.JPG);")
        self.nada3.setText("")
        self.nada3.setObjectName("nada3")
        self.help = QtWidgets.QPushButton(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(700, 50, 81, 71))
        self.help.setStyleSheet("border-image: url(:/backgroud/help.JPG);")
        self.help.setText("")
        self.help.setObjectName("help")
        self.gradoactivo = QtWidgets.QPushButton(self.centralwidget)
        self.gradoactivo.setGeometry(QtCore.QRect(30, 140, 201, 151))
        self.gradoactivo.setStyleSheet("border-image: url(:/backgroud/gradoactivo.JPG);")
        self.gradoactivo.setText("")
        self.gradoactivo.setObjectName("gradoactivo")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(294, 142, 201, 151))
        self.pushButton_4.setStyleSheet("border-image: url(:/backgroud/tiempoactivo.JPG);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 140, 201, 151))
        self.pushButton_3.setStyleSheet("border-image: url(:/backgroud/gradospausa.JPG);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.tiempopausa = QtWidgets.QPushButton(self.centralwidget)
        self.tiempopausa.setGeometry(QtCore.QRect(290, 140, 211, 151))
        self.tiempopausa.setStyleSheet("border-image: url(:/backgroud/tiempopausa.JPG);")
        self.tiempopausa.setText("")
        self.tiempopausa.setObjectName("tiempopausa")
        self.gradoactivo_2 = QtWidgets.QPushButton(self.centralwidget)
        self.gradoactivo_2.setGeometry(QtCore.QRect(30, 140, 201, 151))
        self.gradoactivo_2.setStyleSheet("border-image: url(:/backgroud/gradorun.JPG);")
        self.gradoactivo_2.setText("")
        self.gradoactivo_2.setObjectName("gradoactivo_2")
        self.tiemporun = QtWidgets.QPushButton(self.centralwidget)
        self.tiemporun.setGeometry(QtCore.QRect(290, 140, 211, 151))
        self.tiemporun.setStyleSheet("border-image: url(:/backgroud/tiemporun.JPG);")
        self.tiemporun.setText("")
        self.tiemporun.setObjectName("tiemporun")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(50, 170, 121, 81))
        self.lcdNumber.setStyleSheet("border-image: url(:/backgroud/blanck.JPG);\n"
"font: 36pt \"MS Shell Dlg 2\";")
        self.lcdNumber.setObjectName("lcdNumber")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 170, 31, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("border-image: url(:/backgroud/blanck.JPG);\n"
"font: 8pt \"Copperplate Gothic Light\";\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"font: 8pt \"Century Gothic\";\n"
"font: 75 22pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(170, 200, 31, 51))
        self.pushButton_5.setStyleSheet("border-image: url(:/backgroud/blanck.JPG);")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 170, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-image: url(:/backgroud/blanck.JPG);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        #self.label_2.clicked.connect(self._init)
        # ------ clock  ------
        # ------ end clock ------
        self.pushButton_2.raise_()
        self.subirtemperatura.raise_()
        self.arribatiempo.raise_()
        self.debajotemperatura.raise_()
        self.abajotiempo.raise_()
        self.nuevaconsulta.raise_()
        self.Pausa.raise_()
        self.nada.raise_()
        self.pushButton.raise_()
        self.Encendido.raise_()
        self.nada2.raise_()
        self.nada3.raise_()
        self.help.raise_()
        self.gradoactivo.raise_()
        self.pushButton_4.raise_()
        self.pushButton_3.raise_()
        self.tiempopausa.raise_()
        self.gradoactivo_2.raise_()
        self.tiemporun.raise_()
        self.lcdNumber.raise_()
        self.label.raise_()
        self.pushButton_5.raise_()
        self.label_2.raise_()
        ProyectoHCI.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProyectoHCI)
        QtCore.QMetaObject.connectSlotsByName(ProyectoHCI)

    def retranslateUi(self, ProyectoHCI):
        _translate = QtCore.QCoreApplication.translate
        ProyectoHCI.setWindowTitle(_translate("ProyectoHCI", "MainWindow"))
        self.label.setText(_translate("ProyectoHCI", "℃"))
    def _update(self):
        time = QTime.currentTime().toString()
        self.display(time)
    #def tick():
        #time_string = time.strftime ("%H: %M :%S")
        #clock.config(text=time_string)
        #clock.after(200, tick)
    def _init_(self, digits=8, parent=None):
        super(Ui_ProyectoHCI, self)._init_(digits, parent)
        self.label_2 = QTimer()
        self.label_2.timeout.connect(self._update)
        self.timer.start(1000)
    
    def on_click(self):
        self.temp= self.temp -1
        self.lcdNumber.display(self.temp)
    
    def on_click2(self):
        self.temp = self.temp +1
        self.lcdNumber.display(self.temp)
        #print(self.temp)

    
import new_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProyectoHCI = QtWidgets.QMainWindow()
    ui = Ui_ProyectoHCI()
    ui.setupUi(ProyectoHCI)
    ProyectoHCI.show()
    sys.exit(app.exec_())
    w= Ui_ProyectoHCI()
    w.show()

