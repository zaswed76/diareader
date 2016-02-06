#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets



class ListView(QtWidgets.QLabel):
    name = "List"
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: green")

class IconView(QtWidgets.QLabel):
    name = "Icon"
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setStyleSheet("background-color: grey")
