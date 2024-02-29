# -*- coding: iso-8859-15 -*-
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import maya.cmds as cmds

import cgInTools as cit
from ...ui import createNodesUI as UI
from ...library import jsonLB as jLB
from ...library import functionLB as fLB
from ..library import windowLB as wLB
from ..library import dataLB as dLB
from ..library import selfLB as sLB
cit.reloads([UI,fLB,jLB,wLB,dLB,sLB])

DATAFOLDER="createNodes"
RESETDIR,DATADIR=cit.checkScriptsData(DATAFOLDER,cit.mayaSettings_dir,cit.mayaData_dir)

class CreateNodesWindow(UI.CreateNodesWindow):
    def __init__(self,parent):
        super(CreateNodesWindow, self).__init__(parent)
        self._dataFolder_str=DATAFOLDER
        self._reset_dir=RESETDIR
        self._data_dir=DATADIR

    #Inheritance Function
    def _widget_query_CreateNodeWidgets(self):
        widget_CreateNodeWidgets=[]
        rowCount_int=self.custom_QGridLayout.rowCount()
        for row_int in range(rowCount_int):
            widget_widgetItem=self.custom_QGridLayout.itemAtPosition(row_int,0)
            if widget_widgetItem is None:
                continue
            widget_CreateNodeWidget=widget_widgetItem.widget()
            widget_CreateNodeWidgets.append(widget_CreateNodeWidget)
        return widget_CreateNodeWidgets
    
    def __selectText_create_func(self,selections):
        getText_str=self.textPlain_QPlainTextEdit.toPlainText()
        text_dict=self.convertString_query_dict(getText_str)
        for selection in selections:
            type_str=cmds.nodeType(selection)
            selection_dict={"Name":str(selection),"Type":str(type_str)}
            text_dict.get("createNodes").append(selection_dict)
        text_str=jLB.textParaGraph(text_dict)
        self.textPlain_QPlainTextEdit.setPlainText(text_str)

    #Public Function
    def refreshClicked(self):
        settings_dict=fLB.readJson(cit.mayaSettings_dir,self._dataFolder_str)
        #self._setText_query_dict(settings_dict)

    def restoreClicked(self):
        data_dict=fLB.readJson(cit.mayaData_dir,self._dataFolder_str)
        #self._setText_query_dict(data_dict)

    def saveClicked(self):
        write_dict=self._getText_query_dict()
        fLB.writeJson(absolute=cit.mayaData_dir,relative=self._dataFolder_str,write=write_dict)

    def importClicked(self):
        import_dict=wLB.mayaPathDialog_query_dict(text="import setting",fileMode=1,directory=self._data_dir)
        if import_dict is None:
            return
        data_dict=fLB.readJson(absolute=import_dict["directory"],file=import_dict["file"])
        self._setText_query_dict(data_dict)

    def exportClicked(self):
        export_dict=wLB.mayaPathDialog_query_dict(text="export setting",fileMode=0,directory=self._data_dir)
        if export_dict is None:
            return
        write_dict=self._getText_query_dict()
        fLB.writeJson(absolute=export_dict["directory"],file=export_dict["file"],write=write_dict)
    
    def buttonLeftClicked(self):
        write_dict=self._getText_query_dict()
        for createDataNode_dict in write_dict.get("createNodes"):
            node_DataNode=dLB.DataNode()
            node_DataNode.setDataDict(createDataNode_dict)
            node_DataNode.readDict()
            node_SelfDGNode=sLB.SelfDGNode()
            node_SelfDGNode.setDataNodeForCreate(node_DataNode)
            node_SelfDGNode.createNode()

    def buttonRightClicked(self):
        objs=cmds.ls(sl=True)
        if not objs == []:
            self.__selectText_create_func(objs)

def main():
    viewWindow=CreateNodesWindow(parent=wLB.mayaMainWindow_query_QWidget())
    viewWindow.restoreClicked()
    viewWindow.show()