#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from sceleton.main import Main
from sceleton.dbmanager import DbaseManager
from sceleton import browser_views as views
from sceleton import diafilm_browser as dia_browser





app = QtWidgets.QApplication(sys.argv)
browser = dia_browser.DiafilmBrowser()
list_view = views.ListView()
icon_view = views.IconView()
browser.add_view(list_view)
browser.add_view(icon_view)

db_manager = DbaseManager()
main = Main(db_manager, browser)
main.show()
app.exec()
