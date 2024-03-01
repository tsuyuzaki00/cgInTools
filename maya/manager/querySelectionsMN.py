# -*- coding: iso-8859-15 -*-
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import maya.cmds as cmds
import random
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

import cgInTools as cit
from ...ui import plainTextUI as UI
from ..library import windowLB as wLB
from ...library import functionLB as fLB
cit.reloads([UI,wLB,fLB])

DATAFOLDER="querySelections"
RESETDIR,DATADIR=cit.checkScriptsData(DATAFOLDER,cit.mayaSettings_dir,cit.mayaData_dir)

class QuerySelectionsWindow(MayaQWidgetDockableMixin,UI.PlainTextWindowBase):
    def __init__(self,parent):
        super(QuerySelectionsWindow, self).__init__(parent)
        self._dataFolder_str=DATAFOLDER
        self._reset_dir=RESETDIR
        self._data_dir=DATADIR

        windowTitle_str="querySelections"
        random_int=random.randint(0,9999)
        self.setObjectName(windowTitle_str+str(random_int))
        self.setWindowTitle(windowTitle_str)
        
        self.buttonLeft_QPushButton.setText("Selection")
        self.buttonCenter_QPushButton.setText("Select Replace")
        self.buttonRight_QPushButton.setText("Select Add")

    #Single Function
    @staticmethod
    def convertListToString_edit_str(text_strs=[]):
        text_str=""
        if not text_strs is []:
            for num,text in enumerate(text_strs):
                if num == 0:
                    text_str="[\n"
                text_str+='    "'+text+'",\n'
                if num == len(text_strs)-1:
                    text_str=text_str.rstrip(",\n")
                    text_str+="\n]"
        return text_str

    @staticmethod
    def convertStringToList_edit_list(listText_str=""):
        text_list=[]
        if not listText_str is "":
            text_list=eval(listText_str)
        return text_list
    
    @staticmethod
    def organizeList_edit_list(text_list2s=[[],[]]):
        texts=[]
        for text_list2 in text_list2s:
            texts.extend(text_list2)
            texts=list(set(texts))
        return texts

    #Private Function
    def __setPlainText_create_func(self,objs,add=False):
        organizeTexts=objs
        if add:
            getText_str=self.textPlain_QPlainTextEdit.toPlainText()
            addTexts=self.convertStringToList_edit_list(getText_str)
            organizeTexts=self.organizeList_edit_list([addTexts,objs])
        organizeTexts.sort()
        text_str=self.convertListToString_edit_str(organizeTexts)
        self.textPlain_QPlainTextEdit.setPlainText(text_str)

    def __getPlainText_query_dict(self):
        getText_str=self.textPlain_QPlainTextEdit.toPlainText()
        text_strs=self.convertStringToList_edit_list(getText_str)
        write_dict={"selections":text_strs}
        return write_dict

    #Public Function
    def refreshClicked(self):
        settings_dict=fLB.readJson(cit.mayaSettings_dir,self._dataFolder_str)
        self.__setPlainText_create_func(settings_dict.get("selections"))

    def restoreClicked(self):
        data_dict=fLB.readJson(cit.mayaData_dir,self._dataFolder_str)
        self.__setPlainText_create_func(data_dict.get("selections"))

    def saveClicked(self):
        write_dict=self.__getPlainText_query_dict()
        fLB.writeJson(absolute=cit.mayaData_dir,relative=self._dataFolder_str,write=write_dict)

    def importClicked(self):
        import_dict=wLB.mayaPathDialog_query_dict(text="import setting",fileMode=1,directory=self._data_dir)
        if import_dict is None:
            return
        data_dict=fLB.readJson(absolute=import_dict["directory"],file=import_dict["file"])
        self.__setPlainText_create_func(data_dict.get("selections"))

    def exportClicked(self):
        export_dict=wLB.mayaPathDialog_query_dict(text="export setting",fileMode=0,directory=self._data_dir)
        if export_dict is None:
            return
        write_dict=self.__getPlainText_query_dict()
        fLB.writeJson(absolute=export_dict["directory"],file=export_dict["file"],write=write_dict)

    def buttonLeftClicked(self):
        getText_str=self.textPlain_QPlainTextEdit.toPlainText()
        if not getText_str == "":
            text_strs=eval(getText_str)
            for text_str in text_strs:
                if cmds.objExists(text_str):
                    cmds.select(text_str,add=True)

    def buttonCenterClicked(self):
        objs=cmds.ls(sl=True)
        if not objs == []:
            self.__setPlainText_create_func(objs)

    def buttonRightClicked(self):
        objs=cmds.ls(sl=True)
        if not objs == []:
            self.__setPlainText_create_func(objs,add=True)

def main():
    viewWindow=QuerySelectionsWindow(parent=wLB.mayaMainWindow_query_QWidget())
    objs=cmds.ls(sl=True)
    if not objs == []:
        viewWindow.__setPlainText_create_func(objs)
    viewWindow.show(dockable=True,floating=True)
