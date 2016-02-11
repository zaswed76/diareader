#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
join = os.path.join

from PIL import Image


def resize(source, target, size):
    img = Image.open(source)
    img.thumbnail((size, size), Image.ANTIALIAS)
    img.save(target)

def filter_ext(lst_names, ext_lst):
    return [x for x in lst_names if x[-3:] in ext_lst]


def files_for_thumbnails(directory, ext_lst):
    lst = []
    for dn in sorted(os.listdir(directory)):
        d = join(directory, dn)
        lst.append(
            join(d, min(filter_ext(os.listdir(d), ext_lst))))
    return lst



if __name__ == '__main__':
    DIA_DIR = "/media/windows/media/диафильмы/Диафильмы_JPEG"
    TARGET_DIR = "/home/sergk/Диафильмы/миниатюры"
    EXT = ("jpg", "jpeg")

    img_list = files_for_thumbnails(DIA_DIR, EXT)
    print(img_list)
