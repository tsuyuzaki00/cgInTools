# -*- coding: iso-8859-15 -*-
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import maya.cmds as cmds

import cgInTools as cit
from ...ui import plainTextUI as UI
from ..library import windowLB as wLB
from ...library import jsonLB as jLB
cit.reloads([UI,wLB,jLB])

DATAFOLDER="querySelections"
RESETDIR,DATADIR=cit.checkScriptsData(DATAFOLDER,cit.mayaSettings_dir,cit.mayaData_dir)

class SelectionTextWindow(UI.PlainTextWindowBase):
    def __init__(self,parent):
        super(SelectionTextWindow, self).__init__(parent)
        self._dataFolder_str=DATAFOLDER
        self._reset_dir=RESETDIR
        self._data_dir=DATADIR

        self.setObjectName("SelectionsQuery")
        self.setWindowTitle("SelectionsQuery")
        self.buttonLeft_QPushButton.setText("Selection")
        self.buttonCenter_QPushButton.setText("Select Replace")
        self.buttonRight_QPushButton.setText("Select Add")

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
        text_list=[]
        if not listText_str is "":
            text_list=eval(listText_str)
        return text_list

    def organizeList_edit_list(self,text_lists=[[],[]]):
        texts=[]
        for text_list in text_lists:
            texts.extend(text_list)
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

    def __getSelectText_query_dict(self):
        getText_str=self.textPlain_QPlainTextEdit.toPlainText()
        texts=self.convertStringToList_edit_list(getText_str)
        write_dict={
            "selections":texts,
        }
        return write_dict

    #Public Function
    def refreshOnClicked(self):
        settings_dict=jLB.readJson(cit.mayaSettings_dir,self._dataFolder_str)
        self.__setPlainText_create_func(settings_dict.get("selections"))

    def restoreOnClicked(self):
        data_dict=jLB.readJson(cit.mayaData_dir,self._dataFolder_str)
        self.__setPlainText_create_func(data_dict.get("selections"))

    def saveOnClicked(self):
        write_dict=self.__getSelectText_query_dict()
        jLB.writeJson(absolute=cit.mayaData_dir,relative=self._dataFolder_str,write=write_dict)

    def importOnClicked(self):
        import_dict=wLB.mayaPathDialog_query_dict(text="import setting",fileMode=1,directory=self._data_dir)
        if import_dict is None:
            return
        data_dict=jLB.readJson(absolute=import_dict["directory"],file=import_dict["file"])
        self.__setPlainText_create_func(data_dict.get("selections"))

    def exportOnClicked(self):
        export_dict=wLB.mayaPathDialog_query_dict(text="export setting",fileMode=0,directory=self._data_dir)
        if export_dict is None:
            return
        write_dict=self.__getSelectText_query_dict()
        jLB.writeJson(absolute=export_dict["directory"],file=export_dict["file"],write=write_dict)

    def buttonLeftOnClicked(self):
        getText_str=self.textPlain_QPlainTextEdit.toPlainText()
        if not getText_str == "":
            text_strs=eval(getText_str)
            for text_str in text_strs:
                if cmds.objExists(text_str):
                    cmds.select(text_str,add=True)

    def buttonCenterOnClicked(self):
        objs=cmds.ls(sl=True)
        if not objs == []:
            self.__setPlainText_create_func(objs)

    def buttonRightOnClicked(self):
        objs=cmds.ls(sl=True)
        if not objs == []:
            self.__setPlainText_create_func(objs,add=True)

def main():
    viewWindow=SelectionTextWindow(parent=wLB.mayaMainWindow_query_widget())
    objs=cmds.ls(sl=True)
    if not objs == []:
        viewWindow.__setPlainText_create_func(objs)
    viewWindow.show()
