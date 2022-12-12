# -*- coding: iso-8859-15 -*-
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import os
from maya import cmds

import cgInTools as cit
from ...ui import tableUI as UI
from ..library import windowLB as wLB
cit.reloads([UI,wLB])

class LookShapeColorWindow(UI.TableWindowBase):
    def __init__(self, parent):
        super(LookShapeColorWindow, self).__init__(parent)
        self.setObjectName("selectView_list")
        self.setWindowTitle("selectView_list")
        self.buttonLeft_QPushButton.setText("print")
        self.buttonCenter_QPushButton.setText("Select Replace")
        self.buttonRight_QPushButton.setText("Select Add")
        self.headerAsix="Vertical"
        self.headerTitle_list=["ObjectName","OverrideColor","OverrideColorR","OverrideColorG","OverrideColorB","WireFrameColor","WireFrameColorR","WireFrameColorG","WireFrameColorB"]
        self.createHeaderTitle()

    #Single Function
    def nurbsCurves_check_bool(self,obj):
        shapes=cmds.listRelatives(obj,type='nurbsCurve')
        if None is shapes:
            return False
        else:
            return True

    #Private Function
    def _tableList_create_func(self,objs,add=False):
        getAttrs=["overrideColor","overrideColorR","overrideColorG","overrideColorB","objectColor","objectColorR","objectColorG","objectColorB"]
        if not add:
            self.data_lists=[]
        for obj in objs:
            check=self.nurbsCurves_check_bool(obj)
            if not check:
                continue
            shapes=cmds.listRelatives(obj,type='nurbsCurve')
            for shape in shapes:
                shapeValue_list=[shape]
                for getAttr in getAttrs:
                    getColor=cmds.getAttr(shape+"."+getAttr)
                    shapeValue_list.append(str(getColor))
                self.data_lists.append(shapeValue_list)
                self.createTableItem()

    #Public Function
    def buttonLeftOnClicked(self):
        main()

    def buttonCenterOnClicked(self):
        objs=cmds.ls(sl=True)
        self._tableList_create_func(objs)

    def buttonRightOnClicked(self):
        objs=cmds.ls(sl=True)
        self._tableList_create_func(objs,add=True)

def main():
    viewWindow=LookShapeColorWindow(parent=wLB.mayaMainWindow_query_widget())
    objs=cmds.ls(sl=True)
    viewWindow._tableList_create_func(objs)
    viewWindow.show()