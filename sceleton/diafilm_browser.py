#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets


class ViewsStack(QtWidgets.QStackedLayout):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.widgets = []

    def add_widget(self, widget):
        self.widgets.append(widget.name)
        print(widget.name)
        self.addWidget(widget)

    def set_view(self, view_name):
        self.setCurrentIndex(self.widgets.index(view_name))





class DiafilmBrowser(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        box = QtWidgets.QHBoxLayout(self)
        self.stack_views = ViewsStack()
        box.addLayout(self.stack_views)

    def add_view(self, view):
        self.stack_views.add_widget(view)


    def select_view(self, view_name):
        self.stack_views.set_view(view_name)








