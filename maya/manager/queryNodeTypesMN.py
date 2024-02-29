# -*- coding: iso-8859-15 -*-
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import random

import cgInTools as cit
from ...ui import tableUI as UI
from ..library import windowLB as wLB
from ...library import functionLB as fLB
from ..library import checkLB as chLB
cit.reloads([UI,wLB,fLB,chLB])

DATAFOLDER="queryNodeTypes"
RESETDIR,DATADIR=cit.checkScriptsData(DATAFOLDER,cit.mayaSettings_dir,cit.mayaData_dir)

class QueryNodeTypeWindow(UI.TableWindowBase):
    def __init__(self, parent):
        super(QueryNodeTypeWindow, self).__init__(parent)
        self._dataFolder_str=DATAFOLDER
        self._reset_dir=RESETDIR
        self._data_dir=DATADIR
        
        windowTitle="queryNodeTypes"
        random_int=random.randint(0,9999)
        self.setObjectName(windowTitle+str(random_int))
        self.setWindowTitle(windowTitle)
        self.buttonLeft_QPushButton.setText("Print")
        self.buttonCenter_QPushButton.setText("Select Replace")
        self.buttonRight_QPushButton.setText("Select Add")

        self.table_SelfTableWidget.setHeaderLabelStrs(["ObjectName","NodeType","MFnType","MFnTypeID"])
        self.table_SelfTableWidget.createBase()
        geometry=self.table_SelfTableWidget.geometry()
        self.setGeometry(geometry)

    #Single Function
    @staticmethod
    def sameObjName_check_func(objs):
        check=chLB.CheckBoolean()
        for obj in objs:
            check.setNode(obj)
            judge_dict=check.sameObjName()
            if judge_dict["bool"]:
                #print("OK:"+" node:"+str(judge_dict["node"]))
                pass
            else:
                cmds.error("NG:"+"sameObjName node:"+str(judge_dict["node"]))

    @staticmethod
    def addChilds_query_list(objs):
        nodes=[]
        for obj in objs:
            nodes.append(obj)
            shapes=cmds.listRelatives(obj,s=True)
            if not shapes == None:
                for shape in shapes:
                    nodes.append(shape)
        return nodes

    @staticmethod
    def MFuType_query_str_int(node):
        if node == None:
            return None
        node_MSelectionList=om2.MSelectionList()
        node_MSelectionList.add(node)
        node_MObject=node_MSelectionList.getDependNode(0)
        return node_MObject.apiTypeStr,node_MObject.apiType()

    #Private Function
    def __setTableWidget_create_func(self,objs,add=False):
        table_lists=[]
        if add:
            table_lists=self.table_SelfTableWidget.queryTableLists()
        nodes=self.addChilds_query_list(objs)
        for node in nodes:
            nodeType_str=cmds.nodeType(node)
            MFnType_str,MFnTypeID_int=self.MFuType_query_str_int(node)
            table_lists.append([node,nodeType_str,MFnType_str,str(MFnTypeID_int)])
        self.table_SelfTableWidget.setDataTableWidgetLists(table_lists)
        self.table_SelfTableWidget.createTable()

    def __getTableWidget_query_dict(self):
        tableWidgetItem_lists=self.table_SelfTableWidget.queryTableLists()
        return tableWidgetItem_lists
    
    #Public Function
    def refreshClicked(self):
        settings_dict=fLB.readJson(cit.mayaData_dir,self._dataFolder_str)
        self.__setTableWidget_create_func(settings_dict.get("tableLists"))

    def restoreClicked(self):
        data_dict=fLB.readJson(cit.mayaData_dir,self._dataFolder_str)
        self.__setTableWidget_create_func(data_dict.get("tableLists"))

    def saveClicked(self):
        write_dict=self.__getTableWidget_query_dict()
        fLB.writeJson(absolute=cit.mayaData_dir,relative=self._dataFolder_str,write=write_dict)

    def importClicked(self):
        import_dict=wLB.mayaPathDialog_query_dict(text="import setting",fileMode=1,directory=self._data_dir)
        if import_dict is None:
            return
        data_dict=fLB.readJson(absolute=import_dict["directory"],file=import_dict["file"])
        self.__setTableWidget_create_func(data_dict.get("tableLists"))

    def exportClicked(self):
        export_dict=wLB.mayaPathDialog_query_dict(text="export setting",fileMode=0,directory=self._data_dir)
        if export_dict is None:
            return
        write_dict=self.__getTableWidget_query_dict()
        fLB.writeJson(absolute=export_dict["directory"],file=export_dict["file"],write=write_dict)

    def buttonLeftClicked(self):
        main()

    def buttonCenterClicked(self):
        objs=cmds.ls(sl=True)
        self.sameObjName_check_func(objs)
        self.__setTableWidget_create_func(objs)

    def buttonRightClicked(self):
        objs=cmds.ls(sl=True)
        self.sameObjName_check_func(objs)
        self.__setTableWidget_create_func(objs,add=True)

def main():
    viewWindow=QueryNodeTypeWindow(parent=wLB.mayaMainWindow_query_QWidget())
    viewWindow.buttonCenterClicked()
    viewWindow.show()