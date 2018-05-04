# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 16:30:50 2018

@author: Ana Lucia Diaz Leppe
"""

from PyQt5.QtWidgets import (
        QApplication,
        QLCDNumber
)

from PyQt5.QtCore import (
        QTimer,
        QTime
)

DURATION_INT = 10

class Clock(QLCDNumber):
    def __init__(self):
        super(Clock, self).__init__()
        self.setWindowTitle("Digital Clock")
        self.timer = QTimer()
        self.timer.timeout.connect(self._update)
        self.timer.start(1000)
        
    def _update(self):
        """Update display each """
        time = QTime.currentTime().toString()
        self.display(time)
if __name__== "__main__":
    import sys
    
    app= QApplication([])
    
    w = Clock()
    w.show()
    w.resize(807, 554)
    sys.exit(app.exec_())