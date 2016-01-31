#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets, QtGui, QtCore

from program.libs import imagesize

_cfg = dict(
        thumbnail="/home/vostro/project/diareader/program/resources/thumbnail/Гном Гномыч и Изюмка (1986)"
)

class ThumbControll(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(30)
        self.setMaximumWidth(45)


class ThumbLabel(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        # self.setScaledContents(True)
        self.setAlignment(QtCore.Qt.AlignCenter)

        # police = QtWidgets.QSizePolicy(
        #         QtWidgets.QSizePolicy.Maximum,
        #         QtWidgets.QSizePolicy.Maximum)
        # self.setSizePolicy(police)

class TextLabel(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.setScaledContents(True)
        self.setAlignment(QtCore.Qt.AlignCenter)

        police = QtWidgets.QSizePolicy(
                QtWidgets.QSizePolicy.Minimum,
                QtWidgets.QSizePolicy.Minimum)
        self.setSizePolicy(police)
        # self.setStyleSheet("background-color: grey")


class ThumbBox(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.thumb = ThumbLabel()
        self.label = TextLabel()
        self.controller = ThumbControll()
        self.box = QtWidgets.QHBoxLayout(self)
        self.box.setSpacing(0)
        self.box.setContentsMargins(0, 0, 0, 0)

        self.create_widget()

    @property
    def label_box(self):
        box = QtWidgets.QVBoxLayout()
        box.setSpacing(0)
        box.setContentsMargins(0, 0, 0, 0)

        box.addWidget(self.thumb, stretch=7)
        box.addWidget(self.label, stretch=1)
        return box

    @property
    def controller_box(self):
        return self.controller

    def create_widget(self):
        self.box.addWidget(self.controller_box)
        self.box.addLayout(self.label_box)

    def set_image(self, pth):
        self.thumb.setPixmap(QtGui.QPixmap(pth))

    def set_text(self, text):
        self.label.setText(text)








class WidgetGrid(QtWidgets.QWidget):
    def __init__(self, *args):
        super().__init__(*args)
        self.thumb_label = {}

    def ceate_gtrid(self, lines, column):
        grid = QtWidgets.QGridLayout(self)
        grid.setSpacing(8)
        num_lab = 0
        for x in range(lines):
            for y in range(column):
                self.thumb_label[num_lab] = ThumbBox()
                grid.addWidget(self.thumb_label[num_lab], x, y)
                num_lab += 1

    def next_page(self):
        lst_file = imagesize.collect_files(_cfg["thumbnail"], ["jpg"])
        for n, widget in enumerate(self.thumb_label.values()):
            widget.set_image(lst_file[n])
            widget.set_text("Гном Гномыч и Изюмка (1986)\nГном Гномыч и Изюмка (1986)")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(open('../css/base.css').read())
    main = WidgetGrid()
    main.resize(500, 500)
    main.ceate_gtrid(3, 4)
    main.next_page()
    main.show()

    sys.exit(app.exec_())
