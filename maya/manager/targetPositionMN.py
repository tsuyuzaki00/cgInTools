# -*- coding: iso-8859-15 -*-

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import maya.cmds as cmds
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance
from ...ui import targetPositionUI as ui
from ..library import sourceToTargetLB as sttLB

class TargetPosWindow(ui.TargetPosWindowBase):
    def __init__(self, parent):
        super(TargetPosWindow, self).__init__(parent)
        self.setObjectName("target_move_position")
        self.setWindowTitle("target_move_position")
        self.left_button.setText("Run")
        self.center_button.setText("Reverse")
        self.right_button.setText("Clear")
        
    def left_button_onClicked(self):
        source_line=self.source_line.text()
        target_line=self.target_line.text()
        position_id=self.position_group.checkedId()
        source_name=eval(source_line)
        target_name=eval(target_line)
        targetSet=sttLB.SourceToTarget()
        targetSet.setSourceNode(source_name)
        targetSet.setTargetNode(target_name)
        targetSet.setPos(position_id)
        targetSet.moveToTarget()

    def center_button_onClicked(self):
        source_line=self.source_line.text()
        target_line=self.target_line.text()
        self.source_line.setText(str(target_line))
        self.target_line.setText(str(source_line))

    def right_button_onClicked(self):
        self.source_line.clear()
        self.target_line.clear()

    def source_button_onClicked(self):
        objs=cmds.ls(sl=True)
        self.source_line.setText(str(objs))

    def target_button_onClicked(self):
        objs=cmds.ls(sl=True)
        self.target_line.setText(str(objs))

# mayaのメインウインドウを取得する
def get_maya_main_window():
    omui.MQtUtil.mainWindow()
    ptr=omui.MQtUtil.mainWindow()
    widget=wrapInstance(int(ptr), QWidget)
    return widget

def main():
    # 依存関係のないウインドウを継承して作ったMaya用のボタンUI
    maya_window_instance=TargetPosWindow(parent=get_maya_main_window())
    maya_window_instance.show()