#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sqlite3

conn = sqlite3.connect('dbase1')

def read_dir(dir):
    pass

class Data:
    def __init__(self, data_path):
        self.data_path = data_path
        self.conn = sqlite3.connect(self.data_path)

    def create_table(self):
        curs = self.conn.cursor()
        tblcmd = '''create table book(names,  path,  image_path)'''
        curs.execute(tblcmd)


if __name__ == '__main__':
    data = Data("/home/serg/project/diareader/program/data/lib1.bd")
    # data.create_table()







