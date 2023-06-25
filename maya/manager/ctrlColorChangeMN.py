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
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(1,id_int)
    def index02ButtonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(2,id_int)
    def index03ButtonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(3,id_int)
    def index04ButtonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(4,id_int)
    def index05ButtonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(5,id_int)
    def index06ButtonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(6,id_int)
    def index07ButtonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(7,id_int)
    def index08ButtonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(8,id_int)
    def index09ButtonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(9,id_int)
    def index10ButtonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(10,id_int)
    def index11ButtonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(11,id_int)
    def index12ButtonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(12,id_int)
    def index13ButtonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(13,id_int)
    def index14ButtonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(14,id_int)
    def index15ButtonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(15,id_int)
    def index16ButtonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(16,id_int)
    def index17ButtonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(17,id_int)
    def index18ButtonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(18,id_int)
    def index19ButtonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(19,id_int)
    def index20ButtonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(20,id_int)
    def index21ButtonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(21,id_int)
    def index22ButtonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(22,id_int)
    def index23ButtonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(23,id_int)
    def index24ButtonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(24,id_int)
    def index25ButtonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(25,id_int)
    def index26ButtonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(26,id_int)
    def index27ButtonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(27,id_int)
    def index28ButtonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(28,id_int)
    def index29ButtonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(29,id_int)
    def index30ButtonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(30,id_int)
    def index31ButtonOnClicked(self):
        id_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(31,id_int)
    def buttonOverrideNeutralOnClicked(self):
        self.changeColor_edit_func(None,0)#OverrideNeutral
    def buttonWireNeutralOnClicked(self):
        self.changeColor_edit_func(None,1)#WireFrameNeutral

def main():
    mayaWindow=ColorChangeWindow(parent=wLB.mayaMainWindow_query_widget())
    mayaWindow.show()