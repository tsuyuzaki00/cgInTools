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
        self._replaceCorePositions=[
            "up",
            "back",
            "left",
            "center",
            "right",
            "front",
            "down"
        ]
        self.setObjectName("targetMovePosition")
        self.setWindowTitle("targetMovePosition")
        self.buttonLeft_QPushButton.setText("Run")
        self.buttonCenter_QPushButton.setText("Reverse")
        self.buttonRight_QPushButton.setText("Clear")
        
    def buttonLeftOnClicked(self):
        source_str=self.source_QLineEdit.text()
        target_str=self.target_QLineEdit.text()
        position_id=self.position_QButtonGroup.checkedId()
        sources=eval(source_str)
        targets=eval(target_str)
        targetSet=sttLB.SourceToTarget()
        corePosition_str=self._replaceCorePositions[position_id]
        targetSet.setCorePosition(corePosition_str)
        targetSet.setTargetNode(targets)
        for source in sources:
            targetSet.setSourceNode(source)
            targetSet.moveToTarget()

    def buttonCenterOnClicked(self):
        source_str=self.source_QLineEdit.text()
        target_str=self.target_QLineEdit.text()
        self.source_QLineEdit.setText(str(target_str))
        self.target_QLineEdit.setText(str(source_str))

    def buttonRightOnClicked(self):
        self.source_QLineEdit.clear()
        self.target_QLineEdit.clear()

    def buttonSourceOnClicked(self):
        objs=cmds.ls(sl=True)
        self.source_QLineEdit.setText(str(objs))

    def buttonTargetOnClicked(self):
        objs=cmds.ls(sl=True)
        self.target_QLineEdit.setText(str(objs))

def main():
    mayaWindow=TargetPosWindow(parent=wLB.mayaMainWindow_query_widget())
    mayaWindow.show()