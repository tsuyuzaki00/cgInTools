# -*- coding: iso-8859-15 -*-
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import os
from maya import cmds
import maya.api.OpenMaya as om2

import cgInTools as cit
from ...ui import tableUI as UI
from ..library import windowLB as wLB
from ..library import checkLB as chLB
cit.reloads([UI,wLB,chLB])

class LookNodeTypeWindow(UI.TableWindowBase):
    def __init__(self, parent):
        super(LookNodeTypeWindow, self).__init__(parent)
        self.setObjectName("selectView_list")
        self.setWindowTitle("selectView_list")
        self.buttonLeft_QPushButton.setText("print")
        self.buttonCenter_QPushButton.setText("Select Replace")
        self.buttonRight_QPushButton.setText("Select Add")
        self.headerTitle_list=["ObjectName","NodeType","MFnType","MFnTypeID"]
        self.createHeaderTitle()

    #Single Function
    def sameObjName_check_func(self,objs):
        check=chLB.CheckBoolean()
        for obj in objs:
            check.setNode(obj)
            judge_dict=check.sameObjName()
            if judge_dict["bool"]:
                #print("OK:"+" node:"+str(judge_dict["node"]))
                pass
            else:
                cmds.error("NG:"+"sameObjName node:"+str(judge_dict["node"]))

    def addChilds_query_list(self,objs):
        nodes=[]
        for obj in objs:
            nodes.append(obj)
            shapes=cmds.listRelatives(obj,s=True)
            if not shapes == None:
                for shape in shapes:
                    nodes.append(shape)
        return nodes

    def MFuType_query_str_int(self,node):
        if node == None:
            return None
        node_MSelectionList=om2.MSelectionList()
        node_MSelectionList.add(node)
        node_MObject=node_MSelectionList.getDependNode(0)
        return node_MObject.apiTypeStr,node_MObject.apiType()

    #Private Function
    def _tableList_create_func(self,nodes,add=False):
        if not add:
            self.data_lists=[]
        nodes=self.addChilds_query_list(nodes)
        for node in nodes:
            nodeType=cmds.nodeType(node)
            MFnType,MFnTypeID=self.MFuType_query_str_int(node)
            self.data_lists.append([node,nodeType,MFnType,str(MFnTypeID)])
            self.createTableItem()

    #Public Function
    def buttonLeftOnClicked(self):
        main()

    def buttonCenterOnClicked(self):
        objs=cmds.ls(sl=True)
        self.sameObjName_check_func(objs)
        self._tableList_create_func(objs)

    def buttonRightOnClicked(self):
        objs=cmds.ls(sl=True)
        self.sameObjName_check_func(objs)
        self._tableList_create_func(objs,add=True)

def main():
    viewWindow=LookNodeTypeWindow(parent=wLB.mayaMainWindow_query_widget())
    objs=cmds.ls(sl=True)
    viewWindow.sameObjName_check_func(objs)
    viewWindow._tableList_create_func(objs)
    viewWindow.show()