#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
этот модуль содержит инструменты для создания миниатюр
"""

import os

from PIL import Image


def resize(source, target, size):
    img = Image.open(source)
    img.thumbnail((size, size), Image.ANTIALIAS)
    img.save(target)


class Miniature:
    def __init__(self):
        self._file_exts = ["jpg", "bmp", 'jpeg', "JPG", 'JPEG']

    @property
    def file_exts(self):
        return self._file_exts

    def files_for_thumbnails(self, directory, namber, exts=None):
        if exts is None:
            exts = self.file_exts
        num_img_path = []
        diafilms = os.listdir(directory)
        diafilms_path = [os.path.join(directory, d) for d in diafilms]
        for d in diafilms_path:
            lst = [p for p in os.listdir(d) if p[-3:] in exts]
            if lst:
                pth = os.path.join(d, sorted(lst)[namber])
                num_img_path.append(pth)
        return num_img_path

    def create_thumbnails(self, file_lst, target_dir, size):
        for file in file_lst:
            dir_dia, name = os.path.split(file)
            name_dia = os.path.basename(dir_dia)
            ext = os.path.splitext(name)[1]

            target_path = os.path.join(target_dir, name_dia + ext)
            resize(file, target_path, size)


if __name__ == '__main__':
    dia_dir = "/media/sergk/WH/MEDIA/диафильмы/Диафильмы/Диафильмы_JPEG/"
    target_dir = "/home/sergk/Диафильмы/миниатюры"
    m = Miniature()
    files = m.files_for_thumbnails(dia_dir, 0)
    m.create_thumbnails(files, target_dir, 240)


