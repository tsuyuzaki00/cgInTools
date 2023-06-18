# -*- coding: iso-8859-15 -*-
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import maya.cmds as cmds

import cgInTools as cit
from ...ui import ctrlColorChengeUI as UI
from ..library import windowLB as wLB
from ..library import colorLB as cLB
cit.reloads([UI,wLB,cLB])

class ColorChangeWindow(UI.ColorChengeWindouBase):
    def __init__(self,parent):
        super(ColorChangeWindow,self).__init__(parent)
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle("ctrlColorChenge")

    #Single Function
    def changeColor_edit_func(self,value,swicth=0):
        change=cLB.Color()
        change.setValue(value)
        sels=cmds.ls(sl=True)
        for sel in sels:
            change.setNode(sel)
            if swicth is 0:
                change.overrideColor()
            elif swicth is 1:
                change.wireframeColor()

    #Public Function
    def buttonRedOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(13,id_int)#Red
    def buttonPinkOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(20,id_int)#Pink
    def buttonCrimsonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(31,id_int)#Crimson
    def buttonDarkRedOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(4,id_int)#DarkRed
    def buttonYellowOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(17,id_int)#Yellow
    def buttonLimeOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(14,id_int)#lime
    def buttonGreenOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(27,id_int)#MediumSeaGreen
    def buttonDarkGreenOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(7,id_int)#DarkGreen
    def buttonBlueOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(6,id_int)#Blue
    def buttonCyanOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(18,id_int)#Cyan
    def buttonTealOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(28,id_int)#SteelBlue
    def buttonDarkBlueOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(15,id_int)#DarkBlue
    def buttonMagentaOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(9,id_int)#Magenta
    def buttonPurpleOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(30,id_int)#Purple
    def buttonWhiteOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(16,id_int)#White
    def buttonBlackOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(1,id_int)#Black
    def buttonOverrideNeutralOnClicked(self):
        self.changeColor_edit_func(None,0)#OverrideNeutral
    def buttonWireNeutralOnClicked(self):
        self.changeColor_edit_func(None,1)#WireFrameNeutral

def main():
    mayaWindow=ColorChangeWindow(parent=wLB.mayaMainWindow_query_widget())
    mayaWindow.show()