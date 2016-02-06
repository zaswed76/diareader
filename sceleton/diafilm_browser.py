#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets





class DiafilmBrowser(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        box = QtWidgets.QHBoxLayout(self)
        self.stack_views = QtWidgets.QStackedLayout()
        box.addLayout(self.stack_views)

    def add_view(self, view):
        self.stack_views.addWidget(view())










