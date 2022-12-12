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

class LookNodeTypeWindow(UI.TableWindowBase):
    def __init__(self, parent):
        super(LookNodeTypeWindow, self).__init__(parent)
        self.setObjectName("selectView_list")
        self.setWindowTitle("selectView_list")
        self.buttonLeft_QPushButton.setText("print")
        self.buttonCenter_QPushButton.setText("Select Replace")
        self.buttonRight_QPushButton.setText("Select Add")
        self.headerTitle_list=["ObjectName","NodeType"]
        self.createHeaderTitle()

    #Single Function
    def addChilds_query_list(self,objs):
        nodes=[]
        for obj in objs:
            nodes.append(obj)
            shapes=cmds.listRelatives(obj,s=True)
            if not shapes == None:
                for shape in shapes:
                    nodes.append(shape)
        return nodes

    #Private Function
    def _tableList_create_func(self,nodes,add=False):
        if not add:
            self.data_lists=[]
        nodes=self.addChilds_query_list(nodes)
        for node in nodes:
            nodeType=cmds.nodeType(node)
            self.data_lists.append([node,nodeType])
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
    viewWindow=LookNodeTypeWindow(parent=wLB.mayaMainWindow_query_widget())
    objs=cmds.ls(sl=True)
    viewWindow._tableList_create_func(objs)
    viewWindow.show()