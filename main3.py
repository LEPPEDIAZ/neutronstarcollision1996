# -*- coding: utf-8 -*-
"""
Created on Wed May 16 18:13:43 2018

@author: Ana Lucia Diaz Leppe
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import os

from datetime import datetime



from PyQt5.QtCore import QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
#import PyQt5.QtCore as C
import PyQt5.QtMultimedia as M
#from PyQt5 import  QtGui, QtWidgets
from PyQt5.QtCore import QBasicTimer
from pprint import pprint
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import QPalette, QBrush, QImage
from helps import Ui_MainWindow
import sys
import serial

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from PyQt5.QtWidgets import (
        QApplication,
        QLCDNumber
)

from PyQt5.QtCore import (
        QTimer,
        QTime
)

DURATION_INT = 10
ser = 0
dato = 0
COUNT = 100

"""
# ------ Inicializar la variable ser ------------------------------------------
def init_serial():
    global ser
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = "COM4"
    ser.bytesize = serial.EIGHTBITS
    ser.parity = serial.PARITY_NONE
    ser.stopbits = 1
    ser.timeout = 0.25
    ser.open()
    
init_serial()
# -----------------------------------------------------------------------------
"""
class QLCDCountDown(QLCDNumber):



    """Custom QLCDNumber with a CountDown based on argument datetime."""



    def __init__(self, parent=None, background_image=None, until=None, *args):

        """Init class custom tab bar."""

        super(QLCDCountDown, self).__init__(parent=None, *args)

        self.parent, self.timer, self.palete = parent, QTimer(self), QPalette()

        self.setNumDigits(5)

        if background_image and os.path.isfile(background_image):

            self.palete.setBrush(QPalette.Background,

                                 QBrush(QImage(background_image)))

            self.setPalette(self.palete)

        if until and isinstance(until, datetime) and until > datetime.now():

            self.timer.timeout.connect(lambda: self.display(

               self.seconds_time_to_human_string(

                   (until - datetime.now()).total_seconds())))

            self.timer.start(1000)

        else:

            self.display("0" * 24)



    def seconds_time_to_human_string(self, time_on_seconds=0):

        """Calculate time, with precision from seconds to days."""

        minutes, seconds = divmod(int(time_on_seconds), 60)

        hours, minutes = divmod(minutes, 60)

        days, hours = divmod(hours, 24)

        human_time_string = ""

        if days:

            human_time_string += "%02dD " % days

        if hours:

            human_time_string += "%02d" % hours

        else:

            human_time_string += "00"

        if minutes:

            human_time_string += ":%02d" % minutes

        else:

            human_time_string += ":00"

        human_time_string += ":%02d" % seconds

        return human_time_string

class Ui_ProyectoHCI(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        #ProyectoHCI.hide()
        self.window.show()
    def setupUi(self, ProyectoHCI):
        ProyectoHCI.setObjectName("ProyectoHCI")
        ProyectoHCI.resize(807, 554)
        font = QtGui.QFont()
        font.setPointSize(60)
        ProyectoHCI.setFont(font)
        ProyectoHCI.setStyleSheet("border-image: url(:/backgroud/fondopantalla2.JPG);")
        
        # ------ Variables dentro de la Interfaz ------------------------------
        self.escritura = 0
        # ---------------------------------------------------------------------
        
        self.temp=24
        self.tiempo=0
        self.timer = QBasicTimer()
        self.step=0
        self.time_left_int = DURATION_INT
        self.widget_counter_int = 0
        self.centralwidget = QtWidgets.QWidget(ProyectoHCI)
        self.centralwidget.setObjectName("centralwidget")
        self.debajotemperatura = QtWidgets.QPushButton(self.centralwidget)
        self.debajotemperatura.setGeometry(QtCore.QRect(80, 290, 91, 71))
        self.debajotemperatura.setStyleSheet("image: url(:/backgroud/boton2.JPG);\n"
"border-image: url(:/backgroud/boton2.JPG);")
        self.debajotemperatura.setText("")
        self.debajotemperatura.setObjectName("debajotemperatura")
        self.debajotemperatura.clicked.connect(self.on_click)
        self.abajotiempo = QtWidgets.QPushButton(self.centralwidget)
        self.abajotiempo.setGeometry(QtCore.QRect(360, 290, 91, 71))
        self.abajotiempo.setStyleSheet("border-image: url(:/backgroud/boton2.JPG);")
        self.abajotiempo.setText("")
        self.abajotiempo.setObjectName("abajotiempo")
        self.abajotiempo.clicked.connect(self.on_click4)
        self.Encendido = QtWidgets.QPushButton(self.centralwidget)
        self.Encendido.setGeometry(QtCore.QRect(560, 150, 221, 91))
        self.Encendido.move(560,150)
        self.Encendido.setStyleSheet("border-image: url(:/backgroud/encendido.JPG);")
        self.Encendido.setText("")
        self.Encendido.setObjectName("Encendido")
        self.Encendido.clicked.connect(self.startchange)
        #self.Encendido.clicked.connect(self.doAction)
        #self.Encendido.clicked.connect(self.music)
        self.Pausa = QtWidgets.QPushButton(self.centralwidget)
        self.Pausa.setGeometry(QtCore.QRect(560, 150, 221, 91))
        self.Pausa.setStyleSheet("border-image: url(:/backgroud/pausa1.JPG);\n"
"image: url(:/backgroud/pausa1.JPG);")
        self.Pausa.setText("")
        self.Pausa.setObjectName("Pausa")
        self.nada = QtWidgets.QPushButton(self.centralwidget)
        self.nada.setGeometry(QtCore.QRect(570, 50, 121, 71))
        self.nada.setStyleSheet("border-image: url(:/backgroud/blanck.JPG);")
        self.nada.setText("")
        self.nada.setObjectName("nada")
        self.grafica = QtWidgets.QPushButton(self.centralwidget)
        self.grafica.setGeometry(QtCore.QRect(560, 370, 221, 131))
        self.grafica.setStyleSheet("border-image: url(:/backgroud/graficacaliente.JPG);")
        self.grafica.setText("")
        self.grafica.setObjectName("grafica")
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
        self.help.clicked.connect(self.openWindow)
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
        self.gradoalto = QtWidgets.QPushButton(self.centralwidget)
        self.gradoalto.setGeometry(QtCore.QRect(30, 140, 201, 151))
        self.gradoalto.setStyleSheet("border-image: url(:/backgroud/gradospausa.JPG);")
        self.gradoalto.setText("")
        self.gradoalto.setObjectName("gradoalto")
        self.tiempopausa = QtWidgets.QPushButton(self.centralwidget)
        self.tiempopausa.setGeometry(QtCore.QRect(290, 140, 211, 151))
        self.tiempopausa.setStyleSheet("border-image: url(:/backgroud/tiempopausa.JPG);")
        self.tiempopausa.setText("")
        self.tiempopausa.setObjectName("tiempopausa")
        self.gradoinactivo = QtWidgets.QPushButton(self.centralwidget)
        self.gradoinactivo.setGeometry(QtCore.QRect(30, 140, 201, 151))
        self.gradoinactivo.setStyleSheet("border-image: url(:/backgroud/gradorun.JPG);")
        self.gradoinactivo.setText("")
        self.gradoinactivo.setObjectName("gradoinactivo")
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
        #LCD Number 2
        self.timenumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.timenumber.setGeometry(QtCore.QRect(310, 170, 121, 81))
        self.timenumber.setStyleSheet("border-image: url(:/backgroud/blanck.JPG);\n"
"font: 36pt \"MS Shell Dlg 2\";")
        self.timenumber.setObjectName("lcdNumber2")
        self.timer, QTimer(self)
        self.setNumDigits(14)
        
        #self.timer.clicked.connect(self._update)
        #self.timer = QTimer()
        #self.timer.timeout.connect(self._update)
        #self.timer.start(1000)
        #end lcd number 2
        self.temperaturadeseada = QtWidgets.QPushButton(self.centralwidget)
        self.temperaturadeseada.setGeometry(QtCore.QRect(0, 370, 257, 181))
        self.temperaturadeseada.setStyleSheet("border-image: url(:/backgroud/temperaturadeseada.JPG);")
        self.temperaturadeseada.setText("")
        self.temperaturadeseada.setObjectName("temperaturadeseada")
        self.nadass = QtWidgets.QPushButton(self.centralwidget)
        self.nadass.setGeometry(QtCore.QRect(0, 370, 257, 184))
        self.nadass.setStyleSheet("border-image: url(:/backgroud/blanck.JPG);")
        self.nadass.setText("")
        self.nadass.setObjectName("nadass")
        self.subirtemperatura = QtWidgets.QPushButton(self.centralwidget)
        self.subirtemperatura.setGeometry(QtCore.QRect(80, 70, 91, 71))
        self.subirtemperatura.setStyleSheet("border-image: url(:/backgroud/botondearriba.JPG);")
        self.subirtemperatura.setText("")
        self.subirtemperatura.setObjectName("subirtemperatura")
        self.subirtemperatura.clicked.connect(self.on_click2)
        
        self.arribatiempo = QtWidgets.QPushButton(self.centralwidget)
        self.arribatiempo.setGeometry(QtCore.QRect(360, 70, 91, 71))
        self.arribatiempo.setStyleSheet("border-image: url(:/backgroud/botondearriba.JPG);")
        self.arribatiempo.setText("")
        self.arribatiempo.setObjectName("arribatiempo")
        self.arribatiempo.clicked.connect(self.on_click3)
        self.oktemperatura = QtWidgets.QPushButton(self.centralwidget)
        self.oktemperatura.setGeometry(QtCore.QRect(70, 500, 111, 41))
        self.oktemperatura.setStyleSheet("border-image: url(:/backgroud/ok.JPG);")
        self.oktemperatura.setText("")
        self.oktemperatura.setObjectName("oktemperatura")
        self.temperaturacargando = QtWidgets.QPushButton(self.centralwidget)
        self.temperaturacargando.setGeometry(QtCore.QRect(0, 370, 257, 184))
        self.temperaturacargando.setStyleSheet("border-image: url(:/backgroud/cargandotemperaturafinal.JPG);")
        self.temperaturacargando.setText("")
        self.temperaturacargando.setObjectName("temperaturacargando")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 460, 211, 31))
        self.progressBar.setStyleSheet("background-image: url(:/backgroud/blanck.JPG);\n"
"border-image: url(:/backgroud/blanck.JPG);\n"
"image: url(:/backgroud/blanck.JPG);")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        #timer
        #self.timer2 = QBasicTimer()
        #self.step = 0
        #end timer
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(720, 120, 47, 13))
        self.label_3.setStyleSheet("border-image: url(:/backgroud/blanck.JPG);")
        self.label_3.setObjectName("label_3")
        self.nuevaconsulta = QtWidgets.QPushButton(self.centralwidget)
        self.nuevaconsulta.setGeometry(QtCore.QRect(560, 250, 221, 91))
        self.nuevaconsulta.setStyleSheet("border-image: url(:/backgroud/nuevaconsulta2.JPG);")
        self.nuevaconsulta.setText("")
        self.nuevaconsulta.setObjectName("nuevaconsulta")
        self.nuevaconsulta.clicked.connect(self.nuevac)
        
        self.oktemperatura_2 = QtWidgets.QPushButton(self.centralwidget)
        self.oktemperatura_2.setGeometry(QtCore.QRect(70, 500, 111, 41))
        self.oktemperatura_2.setStyleSheet("border-image: url(:/backgroud/ok.JPG);")
        self.oktemperatura_2.setText("")
        self.oktemperatura_2.setObjectName("oktemperatura_2")
        self.pushButton_2.raise_()
        self.debajotemperatura.raise_()
        self.abajotiempo.raise_()
        self.Pausa.raise_()
        #self.QBasicTimer.raise_()
        self.nada.raise_()
        self.grafica.raise_()
        self.Encendido.raise_()
        self.nada2.raise_()
        self.nada3.raise_()
        self.help.raise_()
        self.gradoactivo.raise_()
        self.pushButton_4.raise_()
        self.gradoalto.raise_()
        self.tiempopausa.raise_()
        self.gradoinactivo.raise_()
        self.tiemporun.raise_()
        self.lcdNumber.raise_()
        self.label.raise_()
        self.pushButton_5.raise_()
        self.label_2.raise_()
        self.nadass.raise_()
        #self.temperaturadeseada.raise_()
        self.subirtemperatura.raise_()
        self.arribatiempo.raise_()
        #self.oktemperatura.raise_()
        #self.temperaturacargando.raise_()
        #self.progressBar.raise_()
        self.label_3.raise_()
        self.nuevaconsulta.raise_()
        #self.oktemperatura_2.raise_()
        self.timenumber.raise_()
        #self.QTimer.raise_()
        ProyectoHCI.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProyectoHCI)
        QtCore.QMetaObject.connectSlotsByName(ProyectoHCI)

    def retranslateUi(self, ProyectoHCI):
        _translate = QtCore.QCoreApplication.translate
        ProyectoHCI.setWindowTitle(_translate("ProyectoHCI", "OCCHIO VARMO"))
        self.label.setText(_translate("ProyectoHCI", "℃"))
        self.label_3.setText(_translate("ProyectoHCI", "  Ayuda"))
    def on_click(self):
        self.temp= self.temp -1
        self.lcdNumber.display(self.temp)
        self.escritura = self.temp +40
        ser.write(bytes([self.escritura]))
        print(self.escritura)
    
    def on_click2(self):
        self.temp = self.temp +1
        self.lcdNumber.display(self.temp)
        self.escritura = self.temp +40
        ser.write(bytes([self.escritura]))
        print(self.escritura)
    def on_click3(self):
        self.tiempo = self.tiempo +1
        self.timenumber.display(self.tiempo)
        
    def on_click4(self):
        self.tiempo= self.tiempo -1
        self.timenumber.display(self.tiempo)


        

    #def _update(self):
     #   """Update display each """
     #   time = QTime.currentTime().toString()
      #  self.display(time)
    
    def startchange(self):
        self.gradoinactivo.lower()
        self.tiemporun.lower()
        self.temperaturacargando.raise_()
        self.progressBar.raise_()
        self.oktemperatura.raise_()
        self.oktemperatura_2.raise_()
        
    def nuevac(self):
        self.gradoinactivo.raise_()
        self.tiemporun.raise_()
        self.temperaturacargando.lower()
        self.progressBar.lower()
        self.oktemperatura.lower()
        self.oktemperatura_2.lower()
        self.pushButton_5.raise_()
        self.lcdNumber.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.timenumber.raise_()
        self.tiempo= self.tiempo  = 0
        self.temp= self.temp=0
        self.timenumber.display(self.tiempo)
        self.lcdNumber.display(self.temp)
    def timerEvent(self, e):
      
        if self.step >= 100:
            
            self.timer.stop()
            self.Encendido.setText('Finished')
            return
            
        self.step = self.step + 1
        self.progressBar.setValue(self.step)
        

    def doAction(self):
      
        if self.timer.isActive():
            self.timer.stop()
            self.Encendido.setText('Start')
        else:
            #self.timer.start(self, 100, QBasicTimer)
            self.timer.start(self, 100,QBasicTimer,ProyectoHCI)

            self.Encendido.setText('Stop')
    
    def music(self):
        app=QtCore.QCoreApplication(sys.argv)
        url= QtCore.QUrl.fromLocalFile("./fairydust.mp3")
        content= M.QMediaContent(url)
        player = M.QMediaPlayer()
        player.setMedia(content)
        player.play()
        
 


import new2_rc

if __name__ == "__main__":
    import sys
    #app = QtWidgets.QApplication(sys.argv)
    from PyQt5.QtWidgets import QApplication

    app = QApplication([])

    #gui1 = QLCDDateTime(None)

    gui2 = QLCDCountDown(None, None, datetime.strptime('Jun 2020', '%b %Y'))

    #gui1.show()  # date and time

    gui2.show()  # count down
    ProyectoHCI = QtWidgets.QMainWindow()
    #yo anadi pprint
    pprint("input parameters = " + str(sys.argv))
    ui = Ui_ProyectoHCI()
    ui.setupUi(ProyectoHCI)
    ProyectoHCI.show()
    sys.exit(app.exec_())