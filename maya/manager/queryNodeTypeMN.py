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
from ..library import jsonLB as jLB
cit.reloads([UI,wLB,chLB,jLB])

PATHSET=cit.mayaData_dir
PATHRESET=cit.mayaSettings_dir
FILE="queryNodeType"

class LookNodeTypeWindow(UI.TableWindowBase):
    def __init__(self, parent):
        super(LookNodeTypeWindow, self).__init__(parent)
        self.setObjectName("selectView_list")
        self.setWindowTitle("selectView_list")
        self.buttonLeft_QPushButton.setText("print")
        self.buttonCenter_QPushButton.setText("Select Replace")
        self.buttonRight_QPushButton.setText("Select Add")

        self.queryNodeType_CTableWidget=UI.CTableWidget()
        self.custom_QGridLayout.addWidget(self.queryNodeType_CTableWidget)
        self.queryNodeType_CTableWidget.setHeaderLabelList(["ObjectName","NodeType","MFnType","MFnTypeID"])
        self.queryNodeType_CTableWidget.createBase()

        self._pathSet=PATHSET
        self._pathReset=PATHRESET
        self._file=FILE

    #Single Function
    def exportJson_edit_func(self,path,file,table_lists):
        write_dict={
            "tableLists":table_lists,
        }
        setting=jLB.Json()
        setting.setPath(path)
        setting.setFile(file)
        setting.setWriteDict(write_dict)
        setting.write()

    def importJson_query_dict(self,path,file):
        setting=jLB.Json()
        setting.setPath(path)
        setting.setFile(file)
        settings_dict=setting.read()
        return settings_dict

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
    def __replaceListWithUI_create_func(self,settings_dict):
        table_lists=settings_dict["tableLists"]
        self.queryNodeType_CTableWidget.setTableParamLists(table_lists)
        self.queryNodeType_CTableWidget.createTable()

    def __tableList_create_func(self,nodes,add=False):
        if not add:
            self._table_lists=[]
        nodes=self.addChilds_query_list(nodes)
        for node in nodes:
            nodeType=cmds.nodeType(node)
            MFnType,MFnTypeID=self.MFuType_query_str_int(node)
            self._table_lists.append([node,nodeType,MFnType,str(MFnTypeID)])
            self.queryNodeType_CTableWidget.setTableParamLists(self._table_lists)
            self.queryNodeType_CTableWidget.createTable()

    #Summary Function
    def __importJson(self,path,file):
        settings_dict=self.importJson_query_dict(path,file)
        self.__replaceListWithUI_create_func(settings_dict)

    def __exportJson(self,path,file):
        table_lists=self.queryNodeType_CTableWidget.getTableParamLists()
        self.exportJson_edit_func(path,file,table_lists)
    
    #Public Function
    def refreshOnClicked(self):
        self.__importJson(self._pathReset,self._file)

    def restoreOnClicked(self):
        self.__importJson(self._pathSet,self._file)

    def saveOnClicked(self):
        self.__exportJson(self._pathSet,self._file)

    def importOnClicked(self):
        path,file=wLB.mayaFileDialog_query_path_file("import setting",1)
        self.__importJson(path,file)

    def exportOnClicked(self):
        path,file=wLB.mayaFileDialog_query_path_file("export setting",0)
        self.__exportJson(path,file)

    def buttonLeftOnClicked(self):
        main()

    def buttonCenterOnClicked(self):
        objs=cmds.ls(sl=True)
        self.sameObjName_check_func(objs)
        self.__tableList_create_func(objs)

    def buttonRightOnClicked(self):
        objs=cmds.ls(sl=True)
        self.sameObjName_check_func(objs)
        self.__tableList_create_func(objs,add=True)

def main():
    viewWindow=LookNodeTypeWindow(parent=wLB.mayaMainWindow_query_widget())
    objs=cmds.ls(sl=True)
    viewWindow.sameObjName_check_func(objs)
    viewWindow.__tableList_create_func(objs)
    viewWindow.show()