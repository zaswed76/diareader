#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from program.libs import imagesize

_cfg = dict(
        thumbnail="/home/serg/project/diareader/program/resources/thumbnail/Дракон и геркулесовая каша (1973)"
)


class ThumbLabel(QtWidgets.QLabel):
    def __init__(self, num):
        super().__init__()
        # self.setScaledContents(True)
        self.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignRight)
        self.num = num
        police = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding)
        self.setSizePolicy(police)
        self.setNum(self.num)

    def set_image(self, pth):
        self.setPixmap(QtGui.QPixmap(pth))

        # pxm = QtGui.QPixmap(img)
        # self.setFixedSize(200, 200)
        # print(pxm.size())
        # self.setPixmap(pxm)

        # self.check = QtWidgets.QCheckBox(self)


class WidgetGrid(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.thumb_label = {}

    def ceate_gtrid(self, lines, column):
        grid = QtWidgets.QGridLayout(self)
        num_lab = 0
        for x in range(lines):
            for y in range(column):
                self.thumb_label[num_lab] = ThumbLabel(num_lab)
                grid.addWidget(self.thumb_label[num_lab], x, y)
                num_lab += 1

    def next_page(self):
        lst_file = imagesize.collect_files(_cfg["thumbnail"], ["jpg"])
        for n, widget in enumerate(self.thumb_label.values()):
            widget.set_image(lst_file[n])





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(open('../css/base.css').read())
    main = WidgetGrid()
    main.resize(500, 500)
    main.ceate_gtrid(3, 4)
    main.next_page()
    main.show()

    sys.exit(app.exec_())
