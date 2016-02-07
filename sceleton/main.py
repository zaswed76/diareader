#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtWidgets, QtCore


class Main(QtWidgets.QMainWindow):
    def __init__(self, db_manager=None, browser=None):
        super().__init__()
        self.resize(500, 500)

        self.browser = browser
        self.db_manager = db_manager

        self.center = QtWidgets.QWidget()
        self.setCentralWidget(self.center)
        box = QtWidgets.QHBoxLayout(self.center)
        box.addWidget(self.browser)


    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == QtCore.Qt.Key_1:
            self.select_view("List")
        elif QKeyEvent.key() == QtCore.Qt.Key_2:
            self.select_view("Icon")



    def select_view(self, view_name):
        self.browser.select_view(view_name)
