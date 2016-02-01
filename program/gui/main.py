#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

from PyQt5 import QtWidgets, QtCore, QtGui

from program.gui import diawidget


class EmptyWidget(QtWidgets.QWidget):
    def __init__(self, width=None, strech=0):
        super().__init__()
        if width is not None:
            self.setFixedWidth(width)
        elif strech:
            box = QtWidgets.QHBoxLayout(self)
            box.addStretch(strech)




        # spacer = QtWidgets.QSpacerItem(20, 40,
        #                                QtWidgets.QSizePolicy.Expanding,
        #                                QtWidgets.QSizePolicy.Expanding)
        # box.addSpacerItem(spacer)


class Action(QtWidgets.QAction):
    def __init__(self, *__args, obgect_name=None):
        super().__init__(*__args)
        self.setObjectName(obgect_name)


class ToolTeg(QtWidgets.QToolBar):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setAllowedAreas(
                QtCore.Qt.LeftToolBarArea | QtCore.Qt.RightToolBarArea)
        self.setFixedWidth(40)
        self.setFloatable(False)


class ToolControl(QtWidgets.QToolBar):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setFixedHeight(30)
        self.setAllowedAreas(
                QtCore.Qt.TopToolBarArea | QtCore.Qt.BottomToolBarArea)
        self.setFixedHeight(45)
        self.setFloatable(False)
        self.setIconSize(QtCore.QSize(24, 24))

        self.exit_act = Action(self, obgect_name="exit_program")
        self.exit_act.setIcon(
                QtGui.QIcon(
                    "resources/icons/png/icon_close_alt2.png"))

        self.collaps_window = Action(self, obgect_name="collaps_window")
        self.collaps_window.setIcon(
                QtGui.QIcon(
                    "resources/icons/png/arrow_condense.png"))

        self.addWidget(EmptyWidget(strech=1))
        self.addAction(self.collaps_window)
        self.addWidget(EmptyWidget(7))
        self.addAction(self.exit_act)
        self.addWidget(EmptyWidget(7))




class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = QtWidgets.QFrame()
        self.setCentralWidget(self.central_widget)
        self.resize(500, 500)

        self.dia_widget = diawidget.WidgetGrid(self)
        self.stack = QtWidgets.QStackedLayout(self.central_widget)
        self.stack.addWidget(self.dia_widget)

    def create_tool_teg(self):
        self.tool_teg = ToolTeg(self)
        self.addToolBar(QtCore.Qt.LeftToolBarArea, self.tool_teg)

    def create_tool_controll(self):
        self.tool_controll = ToolControl(self)
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.tool_controll)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(open('../css/base.css').read())
    main = Main()

    main = Main()
    main.dia_widget.ceate_gtrid(3, 4)
    main.dia_widget.next_page()
    main.show()
    main.create_tool_teg()
    main.create_tool_controll()
    sys.exit(app.exec_())
