# -*- coding: utf-8 -*-
"""
Created on Wed May  2 13:44:36 2018

@author: Ana Lucia Diaz Leppe
"""

import PyQt5.QtCore as C
import PyQt5.QtMultimedia as M
import sys

app=C.QCoreApplication(sys.argv)

url= C.QUrl.fromLocalFile("./orange.mp3")
content= M.QMediaContent(url)
player = M.QMediaPlayer()
player.setMedia(content)
player.play()

player.stateChanged.connect( app.quit )
app.exec()