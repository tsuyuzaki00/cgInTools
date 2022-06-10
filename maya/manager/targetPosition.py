# -*- coding: iso-8859-15 -*-

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import os
import maya.cmds as cmds
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance
import cgInTools as sf
from ...ui import targetPositionUI as UI
from ..library import targetMove as TM

class TargetPosWindow(UI.TargetPosWindowBase):
    def __init__(self, parent):
        super(TargetPosWindow, self).__init__(parent)
        self.setObjectName("target_move_position")
        self.setWindowTitle("target_move_position")
        self.left_button.setText("Run")
        self.center_button.setText("Reverse")
        self.right_button.setText("Clear")
        
    def left_button_onClicked(self):
        source_line = self.source_line.text()
        target_line = self.target_line.text()
        position_id = self.position_group.checkedId()
        source_name = eval(source_line)
        target_name = eval(target_line)
        _CTgmv = TM.CTargetMove(target_name,source_name,position_id)
        _CTgmv.run()

    def center_button_onClicked(self):
        source_line = self.source_line.text()
        target_line = self.target_line.text()
        self.source_line.setText(str(target_line))
        self.target_line.setText(str(source_line))

    def right_button_onClicked(self):
        self.source_line.clear()
        self.target_line.clear()

    def source_button_onClicked(self):
        objs = cmds.ls(sl=True)
        self.source_line.setText(str(objs))

    def target_button_onClicked(self):
        objs = cmds.ls(sl=True)
        self.target_line.setText(str(objs))

# mayaのメインウインドウを取得する
def get_maya_main_window():
    omui.MQtUtil.mainWindow()
    ptr = omui.MQtUtil.mainWindow()
    widget = wrapInstance(long(ptr), QWidget)
    return widget

def main():
    # 依存関係のないウインドウを継承して作ったMaya用のボタンUI
    maya_window_instance = TargetPosWindow(parent=get_maya_main_window())
    maya_window_instance.show()