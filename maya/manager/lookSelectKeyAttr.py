# -*- coding: iso-8859-15 -*-

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import os
from maya import cmds
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance
import cgInTools as sf
from ...ui import scriptsRunUI as UI
from ..library import simpleJson as SJ

class LookNodeTypeWindow(UI.ScriptsRunWindowBase):
    def __init__(self, parent):
        super(LookNodeTypeWindow, self).__init__(parent)
        self.setObjectName("select_list_view")
        self.setWindowTitle("select_list_view")
        self.left_button.setText("print")
        self.center_button.setText("Select Replace")
        self.right_button.setText("Select Add")
        self.simple_json = SJ.SimpleJson()

    def view_scripts(self,nodes):
        for node in nodes:
            cmds.select(node)
            selLists = cmds.listAttr(k=True)
            for selList in selLists:
                selAttr = cmds.getAttr(node + "." + selList)
                self.scripts_plain.insertPlainText('"' + node + '", "' + selList + '", ' + str(round(selAttr, 3)) + "\n")
            self.scripts_plain.insertPlainText("\n")
        
    def left_button_onClicked(self):
        main()

    def center_button_onClicked(self):
        objs = cmds.ls(sl=True)
        self.scripts_plain.clear()
        self.view_scripts(objs)

    def right_button_onClicked(self):
        objs = cmds.ls(sl=True)
        self.view_scripts(objs)

def node_list(sels):
    nodes = []
    for sel in sels:
        childs = cmds.listRelatives(sel)
        if childs == None:
            nodes.append(sel)
        else :
            for child in childs:
                nodes.append(sel)
                nodes.append(child)
    return nodes


# mayaのメインウインドウを取得する
def get_maya_main_window():
    omui.MQtUtil.mainWindow()
    ptr = omui.MQtUtil.mainWindow()
    widget = wrapInstance(long(ptr), QWidget)
    return widget

def main():
    # 依存関係のないウインドウを継承して作ったMaya用のボタンUI
    maya_window_instance = LookNodeTypeWindow(parent=get_maya_main_window())
    sels = cmds.ls(sl = True)
    maya_window_instance.view_scripts(sels)
    maya_window_instance.show()