# -*- coding: iso-8859-15 -*-
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import os
from maya import cmds
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance
import cgInTools as cit
from ...ui import tableUI as UI
from ..library import windowLB as wLB
from ..library import jsonLB as jLB
cit.reloads([UI,wLB,jLB])

class MainMenu(mainUI.MainWindowBase):
    def __init__(self, parent):
        super(MainMenu, self).__init__(parent)
        self.setWindowTitle("select_list_view")
        
        layouts = QFormLayout(self)
        self.centerWidget.setLayout(layouts)
        widget = ScriptsRunWindow(self)
        layouts.addWidget(widget)

class SelectionTextWindow(UI.PlainTextWindowBase):
    def __init__(self, parent):
        super(SelectionTextWindow, self).__init__(parent)
        self.setObjectName("selectView_list")
        self.setWindowTitle("selectView_list")
        self.left_button.setText("Selection")
        self.center_button.setText("Select Replace")
        self.right_button.setText("Select Add")

    def select_function(get_scripts):
        exec(get_scripts)
        cmds.ls(sl=True)

    def _planeText_create_func(self,objs,add=False):
        if add is True:
            pass
        self.textPlain_QPlainTextEdit.setPlainText("objs="+str(obj)+"\n")
        
    def left_button_onClicked(self):
        get_scripts = self.scripts_plain.toPlainText()
        self.list_scripts = get_scripts.splitlines()
        run_script = "selections="+str(self.list_scripts)+"\n"+"cmds.select(selections)"
        select_function(run_script)

    def center_button_onClicked(self):
        objs = cmds.ls(sl=True)
        self.scripts_plain.clear()
        self.view_scripts(objs)

    def right_button_onClicked(self):
        objs = cmds.ls(sl=True)
        self.view_scripts(objs)

    #Public Function
    def buttonLeftOnClicked(self):
        getText_str=self.textPlain_QPlainTextEdit.toPlainText()
        text_list=eval(getText_str)
        cmds.select(text_list)

    def buttonCenterOnClicked(self):
        objs=cmds.ls(sl=True)
        self._planeText_create_func(objs)

    def buttonRightOnClicked(self):
        objs=cmds.ls(sl=True)
        self._planeText_create_func(objs,add=True)

def main():
    viewWindow=SelectionTextWindow(parent=wLB.mayaMainWindow_query_widget())
    objs=cmds.ls(sl=True)
    viewWindow._planeText_create_func(objs)
    viewWindow.show()
