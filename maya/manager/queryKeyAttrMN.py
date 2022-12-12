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

class LookKeyWindow(UI.TableWindowBase):
    def __init__(self,parent):
        super(LookKeyWindow, self).__init__(parent)
        self.setObjectName("selectView_list")
        self.setWindowTitle("selectView_list")
        self.buttonLeft_QPushButton.setText("print")
        self.buttonCenter_QPushButton.setText("Select Replace")
        self.buttonRight_QPushButton.setText("Select Add")
        self.headerAsix="Vertical"

    #Private Function
    def _getKeyAttrs_query_list(self,obj):
        attrValues=[]
        attrValues.append(obj)
        keyAttrs=cmds.listAttr(obj,k=True)
        self.headerTitle_list=["ObjectName"]
        for keyAttr in keyAttrs:
            self.headerTitle_list.append(str(keyAttr))
            self.createHeaderTitle()
            attrValue=cmds.getAttr(obj+"."+keyAttr)
            attrValues.append(str(attrValue))
        return attrValues

    def _tableList_create_func(self,objs,add=False):
        if not add:
            self.data_lists=[]
        for obj in objs:
            keyAttr_list=self._getKeyAttrs_query_list(obj)
            self.data_lists.append(keyAttr_list)
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
    viewWindow=LookKeyWindow(parent=wLB.mayaMainWindow_query_widget())
    objs=cmds.ls(sl=True)
    viewWindow._tableList_create_func(objs)
    viewWindow.show()