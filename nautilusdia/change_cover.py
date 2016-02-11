#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
from PyQt5.QtCore import pyqtSignal
import sys
from PyQt5 import QtWidgets, QtGui

import thumb

_file_exts = ["jpg", "bmp", 'jpeg', "JPG", 'JPEG']

EXT = ".jpg"
DIA_DIR = "/media/windows/media/диафильмы/Диафильмы_JPEG"
MINIATURES = "/home/vostro/Изображения/диафильмы_миниатюры"

def create_miniature(sourse, size):
    dir_name = os.path.dirname(sourse)
    name = os.path.basename(dir_name)
    target = os.path.join(MINIATURES, name + EXT)
    thumb.resize(sourse, target, size)
    print("создан файл - {}".format(target))
    return target

def collect_files(dir, exts):
    files_lst = [os.path.join(dir, p) for p in os.listdir(dir)]
    jpg_list = [p for p in files_lst if p[-3:] in exts]
    return sorted(jpg_list)

def dia_dir_path(miniature, dia_dir):
    base = os.path.basename(miniature)
    name = os.path.splitext(base)[0]
    return os.path.join(dia_dir, name)

class Cell(QtWidgets.QLabel):
    click = pyqtSignal(str)
    def __init__(self, path_image=None):
        super().__init__()
        self.path_image = path_image

        self.setScaledContents(True)
        if path_image is not None:
            pixmap = QtGui.QPixmap(path_image).scaled(280, 280, 1, 1)
            self.setPixmap(pixmap)
        else:
            self.resize(280, 280)
            self.setStyleSheet("background-color: lightgrey")

    def mousePressEvent(self, QMouseEvent):
        self.click.emit(self.path_image)


class Widget(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        # self.setFixedSize(600, 600)
        self.grid = QtWidgets.QGridLayout(self)
        self.grid.setSpacing(15)

    def change_image(self, path):
        create_miniature(path, 240)
        self.close()


    def create_grid(self, source_path):
        dir_dia = dia_dir_path(source_path, DIA_DIR)
        n = 0
        lst = collect_files(dir_dia, _file_exts)


        for x in range(3):
            for y in range(4):
                try:
                    img = lst[n]
                    n += 1
                except IndexError:
                    img = None
                label = Cell(img)
                label.click.connect(self.change_image)
                self.grid.addWidget(label, x, y)


if __name__ == '__main__':
    with open("file.txt", "w") as f:
        pass

    app = QtWidgets.QApplication(sys.argv)
    main = Widget()
    main.show()
    name_dia = sys.argv[1]
    # name_dia = "/home/vostro/Изображения/диафильмы_миниатюры/Али - мореплаватель (1988) [2ч].jpg"
    main.create_grid(name_dia)
    sys.exit(app.exec_())





