#!/usr/bin/env python
# -*- coding: utf-8 -*-

data = (
    ('nam1', 'ru', 'path1'),
    ('nam2', 'ru', 'path2'))


class DbaseManager:
    def __init__(self):
        self._data = ()

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data
