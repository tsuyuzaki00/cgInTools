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

class LookNodeTypeWindow(UI.ScriptsRunWindowBase):
    def __init__(self, parent):
        super(LookNodeTypeWindow, self).__init__(parent)
        self.setObjectName("select_list_view")
        self.setWindowTitle("select_list_view")
        self.left_button.setText("print")
        self.center_button.setText("Select Replace")
        self.right_button.setText("Select Add")

    def view_scripts(self,sels):
        for sel in sels:
            shapes = cmds.listRelatives(sel, type='nurbsCurve')
            for shape in shapes:
                color_index = cmds.getAttr(shape+"."+"overrideColor")
                color_values = cmds.getAttr(shape+"."+"overrideColorRGB")
                self.scripts_plain.insertPlainText('name:\t'+shape+'\n'+'index:\t'+str(color_index)+'\n'+'values:\t'+str(color_values[0][0])+","+str(color_values[0][1])+","+str(color_values[0][2])+'\n\n')

    def left_button_onClicked(self):
        main()

    def center_button_onClicked(self):
        objs = cmds.ls(sl=True)
        self.scripts_plain.clear()
        self.view_scripts(objs)

    def right_button_onClicked(self):
        objs = cmds.ls(sl=True)
        self.view_scripts(objs)


# mayaのメインウインドウを取得する
def get_maya_main_window():
    omui.MQtUtil.mainWindow()
    ptr = omui.MQtUtil.mainWindow()
    widget = wrapInstance(int(ptr), QWidget)
    return widget

def main():
    # 依存関係のないウインドウを継承して作ったMaya用のボタンUI
    maya_window_instance = LookNodeTypeWindow(parent=get_maya_main_window())
    sels = cmds.ls(sl = True)
    maya_window_instance.view_scripts(sels)
    maya_window_instance.show()