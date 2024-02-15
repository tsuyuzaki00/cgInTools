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
        windowTitle="queryKeyAttr_lists"
        self.setObjectName(windowTitle)
        self.setWindowTitle(windowTitle)
        self.buttonLeft_QPushButton.setText("print")
        self.buttonCenter_QPushButton.setText("Select Replace")
        self.buttonRight_QPushButton.setText("Select Add")

        self.queryKeyAttr_CTableWidget=UI.CTableWidget()
        self.custom_QGridLayout.addWidget(self.queryKeyAttr_CTableWidget)
        self.queryKeyAttr_CTableWidget.setHeaderAsixStr("Vertical")# Horizontal or Vertical

    #Single Function
    def getKeyAttrs_query_list_list(self,obj):
        attrValue_list=[]
        attrValue_list.append(obj)
        keyAttrs=cmds.listAttr(obj,k=True)
        headerLabel_list=["ObjectName"]
        for keyAttr in keyAttrs:
            headerLabel_list.append(str(keyAttr))
            attrValue=cmds.getAttr(obj+"."+keyAttr)
            attrValue_list.append(str(attrValue))
        return headerLabel_list,attrValue_list
    
    #Private Function
    def __tableList_create_func(self,objs,add=False):
        if not add:
            self._table_lists=[]
        for obj in objs:
            self._headerLabel_list,attrValue_list=self.getKeyAttrs_query_list_list(obj)
            self._table_lists.append(attrValue_list)
            self.queryKeyAttr_CTableWidget.setHeaderLabelList(self._headerLabel_list)
            self.queryKeyAttr_CTableWidget.setTableParamLists(self._table_lists)
            self.queryKeyAttr_CTableWidget.createTable()

    #Public Function
    def buttonLeftOnClicked(self):
        main()

    def buttonCenterOnClicked(self):
        objs=cmds.ls(sl=True)
        self.__tableList_create_func(objs)

    def buttonRightOnClicked(self):
        objs=cmds.ls(sl=True)
        self.__tableList_create_func(objs,add=True)

def main():
    viewWindow=LookKeyWindow(parent=wLB.mayaMainWindow_query_QWidget())
    viewWindow.buttonCenterOnClicked()
    viewWindow.show()