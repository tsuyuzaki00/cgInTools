# -*- coding: iso-8859-15 -*-

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import os
from maya import cmds
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance

import cgInTools as cit
from ...ui import scriptsRunUI as UI
from ..library import jsonLB as jLB
cit.reloads([jLB])

class MainWindow(UI.MainWindowBase):
    def __init__(self, parent):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("windowTitle")
        
        layouts=QFormLayout(self)
        self.centerWidget.setLayout(layouts)
        #widget = NewClassName(self)
        #layouts.addWidget(widget)

# mayaのメインウインドウを取得する
def getMayaMainWindow():
    ptr=omui.MQtUtil.mainWindow()
    widget=wrapInstance(int(ptr),QWidget)
    return widget

def main():
    # 依存関係のないウインドウを継承して作ったMaya用のボタンUI
    mayaWindow=MainWindow(parent=getMayaMainWindow())
    mayaWindow.show()