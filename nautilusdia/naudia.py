#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import sys
from PyQt5 import QtWidgets


class Widget(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)

    def set_text(self, name):
        self.setText(name)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()

    main.show()
    name_dia = sys.argv[1]
    main.set_text(name_dia)

    sys.exit(app.exec_())

