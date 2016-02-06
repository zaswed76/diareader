#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtWidgets


class Main(QtWidgets.QMainWindow):
    def __init__(self, db_manager=None):
        super().__init__()
        self.db_manager = db_manager
        self.center = QtWidgets.QWidget()
        self.setCentralWidget(self.center)
        self.resize(500, 500)




