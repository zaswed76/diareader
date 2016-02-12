#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import subprocess
import sys
from PyQt5 import QtWidgets

import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('logger1.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)






class Message(QtWidgets.QMessageBox):
    def __init__(self, *__args):
        super().__init__(*__args)



def dia_dir(path):
    d = os.path.dirname(path)

    file = os.path.join(d, 'config.txt')

    try:
        with open(file, "r") as f:
            return f.readlines()[0].strip()
    except FileNotFoundError as mass:
        logger.info(mass)
        sys.exit()


def open_diafilm(path):
    command = ["mcomix", "-f"]
    base = os.path.basename(path)
    name = os.path.splitext(base)[0]
    target = os.path.join(dia_dir(path), name)
    command.append(target)
    subprocess.call(command)


if __name__ == '__main__':

    # name_dia = sys.argv[1]
    name_dia = '/home/sergk/Диафильмы/миниатюры/Ай да молодец! (1987).jpg'
    open_diafilm(name_dia)


