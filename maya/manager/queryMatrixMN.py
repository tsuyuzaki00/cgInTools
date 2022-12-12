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
class LookMatrixWindow(UI.TableWindowBase):
    def __init__(self,parent):
        super(LookMatrixWindow,self).__init__(parent)
        self.setObjectName("selectView_list")
        self.setWindowTitle("selectView_list")
        self.buttonLeft_QPushButton.setText("print")
        self.buttonCenter_QPushButton.setText("Select Replace")
        self.buttonRight_QPushButton.setText("Select Add")
        self.headerAsix="Vertical"
        self.headerTitle_list=[
            "ObjectName",
            "NormalMatrixX",
            "NormalMatrixY",
            "NormalMatrixZ",
            "NormalMatrixT",
            "worldMatrixX",
            "worldMatrixY",
            "worldMatrixZ",
            "worldMatrixT",
            "ParentMatrixX",
            "ParentMatrixY",
            "ParentMatrixZ",
            "ParentMatrixT",
            "XformMatrixX",
            "XformMatrixY",
            "XformMatrixZ",
            "XformMatrixT",
            "InverseMatrixX",
            "InverseMatrixY",
            "InverseMatrixZ",
            "InverseMatrixT",
            "InverseWorldMatrixX",
            "InverseWorldMatrixY",
            "InverseWorldMatrixZ",
            "InverseWorldMatrixT",
            "InverseParentMatrixX",
            "InverseParentMatrixY",
            "InverseParentMatrixZ",
            "InverseParentMatrixT",
            "OffsetParentMatrixX",
            "OffsetParentMatrixY",
            "OffsetParentMatrixZ",
            "OffsetParentMatrixT",
        ]
        self.createHeaderTitle()

    #Single Function
    def getMatrix_query_list(self,obj):
        getAttrs=[
            "matrix",
            "worldMatrix",
            "parentMatrix",
            "xformMatrix",
            "inverseMatrix",
            "worldInverseMatrix",
            "parentInverseMatrix",
            "offsetParentMatrix"
        ]
        matrix_list=[]
        matrix_list.append(obj)
        for getAttr in getAttrs:
            getMatrix=cmds.getAttr(obj+"."+getAttr)
            for num in range(0,13,4):
                matrix_list.append(str(getMatrix[num])+", "+str(getMatrix[num+1])+", "+str(getMatrix[num+2])+", "+str(getMatrix[num+3]))
        return matrix_list

    #Private Function
    def _tableList_create_func(self,objs,add=False):
        if not add:
            self.data_lists=[]
        for obj in objs:
            matrix_list=self.getMatrix_query_list(obj)
            self.data_lists.append(matrix_list)
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
    viewWindow=LookMatrixWindow(parent=wLB.mayaMainWindow_query_widget())
    objs=cmds.ls(sl=True)
    viewWindow._tableList_create_func(objs)
    viewWindow.show()