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
    def index01ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(1,colorSwicth_int)
    def index02ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(2,colorSwicth_int)
    def index03ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(3,colorSwicth_int)
    def index04ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(4,colorSwicth_int)
    def index05ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(5,colorSwicth_int)
    def index06ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(6,colorSwicth_int)
    def index07ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(7,colorSwicth_int)
    def index08ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(8,colorSwicth_int)
    def index09ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(9,colorSwicth_int)
    def index10ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(10,colorSwicth_int)
    def index11ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(11,colorSwicth_int)
    def index12ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(12,colorSwicth_int)
    def index13ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(13,colorSwicth_int)
    def index14ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(14,colorSwicth_int)
    def index15ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(15,colorSwicth_int)
    def index16ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(16,colorSwicth_int)
    def index17ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(17,colorSwicth_int)
    def index18ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(18,colorSwicth_int)
    def index19ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(19,colorSwicth_int)
    def index20ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(20,colorSwicth_int)
    def index21ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(21,colorSwicth_int)
    def index22ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(22,colorSwicth_int)
    def index23ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(23,colorSwicth_int)
    def index24ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(24,colorSwicth_int)
    def index25ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(25,colorSwicth_int)
    def index26ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(26,colorSwicth_int)
    def index27ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(27,colorSwicth_int)
    def index28ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(28,colorSwicth_int)
    def index29ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(29,colorSwicth_int)
    def index30ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(30,colorSwicth_int)
    def index31ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(31,colorSwicth_int)
    
    def index32ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(32,colorSwicth_int)
    def index33ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(33,colorSwicth_int)
    def index34ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(34,colorSwicth_int)
    def index35ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(35,colorSwicth_int)
    def index36ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(36,colorSwicth_int)
    def index37ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(37,colorSwicth_int)
    def index38ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(38,colorSwicth_int)
    def index39ButtonOnClicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(39,colorSwicth_int)

    def buttonOverrideNeutralOnClicked(self):
        self.changeColor_edit_func(None,0)#OverrideNeutral
    def buttonWireNeutralOnClicked(self):
        self.changeColor_edit_func(None,1)#WireFrameNeutral

def main():
    mayaWindow=ColorChangeWindow(parent=wLB.mayaMainWindow_query_QWidget())
    mayaWindow.show()