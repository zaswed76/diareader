#!/usr/bin/env python
# -*- coding: utf-8 -*-


# !/usr/bin/python
# -*- coding: utf-8 -*-



import sqlite3

# Подключаемся к базе данных
con = sqlite3.connect('dbase1')

curs = con.cursor()
# Создаем таблицу
curs.execute(
    '''
create table diafilms(name text, path text, type text, )''')
