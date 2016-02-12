#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os



join = os.path.join

import argparse

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--diafilm')
    parser.add_argument('-m', '--miniature')
    parser.add_argument('-s', '--size')
    parser.add_argument ('-e', '--extlist', nargs='*', default=['jpg', 'jpeg', 'png', 'JPG', 'JPEG', 'PNG'])
    return parser





def filter_ext(lst_names, ext_lst):
    return [x for x in lst_names if x[-3:] in ext_lst]


def files_for_thumbnails(directory, ext_lst):
    """

    :param directory: str путь к каталогу с диафильмами
    :param ext_lst:
    :return:
    """
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

