#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyunpack import Archive

rar = "/home/serg/Документы/dia/Диафильмы_JPEG/Дракон и геркулесовая каша (1973).rar"

# Archive(rar).extractall("/home/serg/Документы/dia")
#
# from rarfile import RarFile


from rarfile import RarFile
#
# def unrar(file, to_dir):
#     with RarFile(file) as rf:
#         rf.extractall(path=to_dir)


class Rar(RarFile):
    def __init__(self, rarfile):
        super().__init__(rarfile)


class Unrar_directory:
    def __init__(self, dir):
        pass
