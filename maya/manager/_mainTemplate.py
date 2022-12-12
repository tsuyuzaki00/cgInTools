# -*- coding: iso-8859-15 -*-

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import os
from maya import cmds

import cgInTools as cit
from ...ui import scriptsRunUI as UI
from ..library import windowLB as wLB
from ..library import jsonLB as jLB
cit.reloads([UI,wLB,jLB])

class MainWindow(UI.MainWindowBase):
    def __init__(self, parent):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("windowTitle")
        
        self.custom_QGridLayout.addWidget()
        

def main():
    mayaWindow=MainWindow(parent=wLB.mayaMainWindow_query_widget())
    mayaWindow.show()