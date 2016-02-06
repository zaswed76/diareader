#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtWidgets, QtGui

class Widget(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.setScaledContents(True)
        self.resize(500, 500)
        self.setStyleSheet("background-color: white")
        self.setPixmap(QtGui.QPixmap("/home/serg/project/diareader/program/resources/car.jpg"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())