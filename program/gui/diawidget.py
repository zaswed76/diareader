#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import textwrap

from PyQt5 import QtWidgets, QtGui, QtCore

from program.libs import imagesize

_cfg = dict(
        thumbnail="resources/thumbnail"
)

class TegPanel(QtWidgets.QFrame):
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
        # self.setScaledContents(True)
        self.setAlignment(QtCore.Qt.AlignCenter)

        police = QtWidgets.QSizePolicy(
                QtWidgets.QSizePolicy.Minimum,
                QtWidgets.QSizePolicy.Expanding)
        # self.setSizePolicy(police)
        # self.setStyleSheet("background-color: grey")
    def _setText(self, p_str):
        text_obj = textwrap.TextWrapper(width=25, max_lines=2, placeholder="...")
        dedented_text = textwrap.dedent(p_str).strip()
        t = text_obj.fill(dedented_text)
        if len(t) <= 25:
            t += "\n "

        self.setText(t)


class DiaFilm(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.thumb = ThumbLabel()
        self.label = TextLabel()
        self._teg_panel = TegPanel()
        self.box = QtWidgets.QHBoxLayout(self)
        self.box.setSpacing(0)
        self.box.setContentsMargins(0, 0, 0, 0)

        self._create_widget()

    @property
    def label_box(self):
        box = QtWidgets.QVBoxLayout()
        box.setSpacing(0)
        box.setContentsMargins(0, 0, 0, 0)

        box.addWidget(self.thumb, stretch=10)
        box.addWidget(self.label, stretch=3)
        return box

    @property
    def teg_panel(self):
        return self._teg_panel

    def _create_widget(self):
        self.box.addWidget(self.teg_panel)
        self.box.addLayout(self.label_box)

    def set_image(self, pth):
        self.thumb.setPixmap(QtGui.QPixmap(pth))

    def set_text(self, text):
        self.label._setText(text)








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
                self.thumb_label[num_lab] = DiaFilm()
                grid.addWidget(self.thumb_label[num_lab], x, y)
                num_lab += 1

    def next_page(self):
        lst_file = os.listdir(_cfg["thumbnail"])
        for n, widget in enumerate(self.thumb_label.values()):
            name = os.path.splitext(lst_file[n])[0]
            widget.set_image(os.path.join(_cfg["thumbnail"], lst_file[n]))
            widget.create_grid(name)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(open('../css/base.css').read())
    main = WidgetGrid()
    main.resize(500, 500)
    main.ceate_gtrid(3, 4)
    # main.next_page()
    main.show()

    sys.exit(app.exec_())
