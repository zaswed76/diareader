#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from sceleton.main import Main
from sceleton.dbmanager import DbaseManager
from sceleton import browser_views as views
from sceleton import diafilm_browser as dia_browser


browser = dia_browser.DiafilmBrowser()
list_view = views.ListView
icon_view = views.IconView
browser.add_view(list_view)
browser.add_view(icon_view)

app = QtWidgets.QApplication(sys.argv)

db_manager = DbaseManager()
main = Main(db_manager)
main.show()
app.exec()
