# -*- coding: iso-8859-15 -*-

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import os
import maya.cmds as cmds
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance
import scriptsInTools as sf
from ...ui import targetPositionUI as UI
from ..library import simpleJson as SJ

class TargetPosWindow(UI.TargetPosWindowBase):
    def __init__(self, parent):
        super(TargetPosWindow, self).__init__(parent)
        self.setObjectName("target_move_position")
        self.setWindowTitle("target_move_position")
        self.left_button.setText("Run")
        self.center_button.setText("Reverse")
        self.right_button.setText("Clear")
        self.simple_json = SJ.SimpleJson()
        
    def left_button_onClicked(self):
        source_line = self.source_line.text()
        target_line = self.target_line.text()
        position_id = self.position_group.checkedId()
        moving_obj(source_line,target_line,position_id)

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

def moving_obj(source_name,target_name,position_id):
    source_name = eval(source_name)
    target_name = eval(target_name)
    source_pos = conpornent_pos(source_name,position_id)
    cmds.move(source_pos[0],source_pos[1],source_pos[2],target_name,a=True)
    
def conpornent_pos(source_name,position_id):
    #bbox = cmds.xform(source_name, query=True, boundingBox=True, ws=True)
    bbox = cmds.exactWorldBoundingBox(source_name,ignoreInvisible=False)
    if position_id == 1:
        up = [(bbox[0]+bbox[3])/2,bbox[4],(bbox[2]+bbox[5])/2]
        return up
    elif position_id == 2:
        back = [(bbox[0]+bbox[3])/2,(bbox[1]+bbox[4])/2,bbox[2]]
        return back
    elif position_id == 3:
        left = [bbox[0],(bbox[1]+bbox[4])/2,(bbox[2]+bbox[5])/2]
        return left
    elif position_id == 4:    
        center = [(bbox[0]+bbox[3])/2,(bbox[1]+bbox[4])/2,(bbox[2]+bbox[5])/2]
        return center
    elif position_id == 5:
        right = [bbox[3],(bbox[1]+bbox[4])/2,(bbox[2]+bbox[5])/2]
        return right
    elif position_id == 6:
        front = [(bbox[0]+bbox[3])/2,(bbox[1]+bbox[4])/2,bbox[5]]
        return front
    elif position_id == 7:
        down = [(bbox[0]+bbox[3])/2,bbox[1],(bbox[2]+bbox[5])/2]
        return down