#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from program.gui import main as base

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(open('./css/base.css').read())
    main = base.Main()
    main.dia_widget.ceate_gtrid(3, 4)
    main.dia_widget.next_page()
    main.show()
    main.create_tool_teg()
    main.create_tool_controll()
    sys.exit(app.exec_())


main()