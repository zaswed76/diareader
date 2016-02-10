#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import subprocess
import sys
DIA_DIR = "/media/windows/media/диафильмы/Диафильмы_JPEG"



def open_diafilm(path):
    command = ["mcomix", "-f"]
    base = os.path.basename(path)
    name = os.path.splitext(base)[0]
    target = os.path.join(DIA_DIR, name)
    command.append(target)
    subprocess.call(command)



if __name__ == '__main__':
    name_dia = sys.argv[1]
    open_diafilm(name_dia)


