#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os


import sys
from PyQt5 import QtWidgets

import thumb

EXT = ".jpg"
DIA_DIR = "/media/sergk/WH/MEDIA/диафильмы/Диафильмы/Диафильмы_JPEG"
MINIATURES = "/home/sergk/Диафильмы/миниатюры"

def create_miniature(sourse, size):
    dir_name = os.path.dirname(sourse)
    name = os.path.basename(dir_name)
    target = os.path.join(MINIATURES, name + EXT) + "\n" + sourse
    thumb.resize(sourse, target, size)

class Widget(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)



    def set_text(self, text):
        source_path = text # файл из которого будем делать обожку
        name = create_miniature(source_path, 240)
        self.setText(name)


if __name__ == '__main__':
    with open("file.txt", "w") as f:
        pass

    app = QtWidgets.QApplication(sys.argv)
    main = Widget()
    main.show()
    name_dia = sys.argv[1]
    main.set_text(name_dia)


    sys.exit(app.exec_())





