# -*- coding: iso-8859-15 -*-
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import maya.cmds as cmds

import cgInTools as cit
from ...ui import createNodesUI as UI
from ...library import jsonLB as jLB
from ..library import windowLB as wLB
from ..library import dataLB as dLB
from ..library import selfLB as sLB
cit.reloads([UI,jLB,wLB,dLB,sLB])

DATAFOLDER="createNodes"
RESETDIR,DATADIR=cit.checkScriptsData(DATAFOLDER,cit.mayaSettings_dir,cit.mayaData_dir)

class SelectionTextWindow(UI.CreateNodesWindow):
    def __init__(self,parent):
        super(SelectionTextWindow, self).__init__(parent)
        self._dataFolder_str=DATAFOLDER
        self._reset_dir=RESETDIR
        self._data_dir=DATADIR

    #Single Function
    def convertListToString_edit_str(self,texts):
        text_str=""
        if not texts is []:
            for num,text in enumerate(texts):
                if num == 0:
                    text_str="[\n"
                text_str+='    "'+text+'",\n'
                if num == len(texts)-1:
                    text_str=text_str.rstrip(",\n")
                    text_str+="\n]"
        return text_str

    def convertStringToList_edit_list(self,listText_str):
        #text_list=[]
        if not listText_str is "":
            text_list=eval(listText_str)
        return text_list

    def organizeList_edit_list(self,text_lists=[[],[]]):
        texts=[]
        for text_list in text_lists:
            texts.extend(text_list)
            texts=list(set(texts))
            texts.sort()
        return texts

    def importJson_query_dict(self,path,file):
        setting=jLB.Json()
        setting.setPath(path)
        setting.setFile(file)
        settings_dict=setting.read()
        return settings_dict

    def exportJson_edit_func(self,path,file,selectText_list):
        write_dict={
            "selections":selectText_list,
        }
        setting=jLB.Json()
        setting.setPath(path)
        setting.setFile(file)
        setting.setWriteDict(write_dict)
        setting.write()

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

    #Public Function
    def refreshClicked(self):
        settings_dict=jLB.readJson(cit.mayaSettings_dir,self._dataFolder_str)

    def restoreClicked(self):
        data_dict=jLB.readJson(cit.mayaData_dir,self._dataFolder_str)

    def saveClicked(self):
        write_dict=None
        jLB.writeJson(absolute=cit.mayaData_dir,relative=self._dataFolder_str,write=write_dict)

    def importClicked(self):
        import_dict=wLB.mayaPathDialog_query_dict(text="import setting",fileMode=1,directory=self._data_str)
        if import_dict is None:
            return
        data_dict=jLB.readJson(absolute=import_dict["directory"],file=import_dict["file"])

    def exportClicked(self):
        export_dict=wLB.mayaPathDialog_query_dict(text="export setting",fileMode=0,directory=self._data_str)
        if export_dict is None:
            return
        write_dict=None
        jLB.writeJson(absolute=export_dict["directory"],file=export_dict["file"],write=write_dict)
    
    def buttonLeftClicked(self):
        widget_CreateNodeWidgets=self._widget_query_CreateNodeWidgets()
        for widget_CreateNodeWidget in widget_CreateNodeWidgets:
            if not widget_CreateNodeWidget == []:
                name_str=widget_CreateNodeWidget.name_QLineEdit.text()  
                nodeType_str=widget_CreateNodeWidget.type_QLineEdit.text()
        
                node_DataNode=dLB.DataNode()
                node_DataNode.setName(name_str)
                node_DataNode.setType(nodeType_str)
        
                node_SelfDGNode=sLB.SelfDGNode()
                node_SelfDGNode.setDataNodeForCreate(node_DataNode)
                node_SelfDGNode.createNode()

    def buttonRightClicked(self):
        objs=cmds.ls(sl=True)
        if not objs == []:
            self.__setPlainText_create_func(objs,add=True)

def main():
    viewWindow=SelectionTextWindow(parent=wLB.mayaMainWindow_query_widget())
    viewWindow.show()