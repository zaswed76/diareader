#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PIL import Image
from glob import glob
import os
FILEEXTENSIONS = [ "jpg", "bmp"]


def resize(source, target, size):
    img = Image.open(source)
    img.thumbnail((size, size), Image.ANTIALIAS)
    img.save(target)


def collect_files(directory, exts):
    files_lst = []
    for extension in exts:
        files_lst.extend(glob("".join((directory, os.sep, "*", extension))))
    return sorted(files_lst)




def resize_dir(direct, target, size, ext=FILEEXTENSIONS):
    if os.path.isdir(direct):
        target_dir = os.path.join(target, os.path.basename(direct))
        if not os.path.isdir(target_dir):
            os.makedirs(target_dir)
        files = collect_files(direct, ext)
    else:
        print("Каталог - '{}' не найден".format(direct))
        return
    for file in files:
        target_path = os.path.join(target_dir, os.path.basename(file))
        resize(file, target_path, size)




if __name__ == '__main__':
    size = 300
    source_dir = "/home/serg/Документы/dia/Диафильмы_JPEG/Дракон и геркулесовая каша (1973)"
    target_dir = "/home/serg/project/diareader/program/resources/thumbnail"
    resize_dir(source_dir, target_dir, size)