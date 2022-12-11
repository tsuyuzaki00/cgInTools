# -*- coding: iso-8859-15 -*-

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import maya.cmds as cmds

import cgInTools as cit
from ...ui import targetPositionUI as UI
from ..library import sourceToTargetLB as sttLB
from ..library import windowLB as wLB
cit.reloads([UI,wLB,sttLB])

class TargetPosWindow(UI.TargetPosWindowBase):
    def __init__(self, parent):
        super(TargetPosWindow, self).__init__(parent)
        self.setObjectName("target_move_position")
        self.setWindowTitle("target_move_position")
        self.left_QPushButton.setText("Run")
        self.center_QPushButton.setText("Reverse")
        self.right_QPushButton.setText("Clear")
        
    def buttonLeft_onClicked_func(self):
        source_str=self.source_QLineEdit.text()
        target_str=self.target_QLineEdit.text()
        position_id=self.position_QButtonGroup.checkedId()
        sources=eval(source_str)
        target_list=eval(target_str)
        targetSet=sttLB.SourceToTarget()
        targetSet.setPos(position_id)
        targetSet.setTargetNode(target_list[0])
        for source in sources:
            targetSet.setSourceNode(source)
            targetSet.moveToTarget()

    def buttonCenter_onClicked_func(self):
        source_str=self.source_QLineEdit.text()
        target_str=self.target_QLineEdit.text()
        self.source_QLineEdit.setText(str(target_str))
        self.target_QLineEdit.setText(str(source_str))

    def buttonRight_onClicked_func(self):
        self.source_QLineEdit.clear()
        self.target_QLineEdit.clear()

    def buttonSource_onClicked_func(self):
        objs=cmds.ls(sl=True)
        self.source_QLineEdit.setText(str(objs))

    def buttonTarget_onClicked_func(self):
        objs=cmds.ls(sl=True)
        self.target_QLineEdit.setText(str(objs))

def main():
    mayaWindow=TargetPosWindow(parent=wLB.mayaMainWindow_query_widget())
    mayaWindow.show()