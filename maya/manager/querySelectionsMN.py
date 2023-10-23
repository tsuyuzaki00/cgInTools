# -*- coding: iso-8859-15 -*-

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import os
from maya import cmds

import cgInTools as cit
from ...ui import plainTextUI as UI
from ..library import windowLB as wLB
from ...library import jsonLB as jLB
from ...library import pathLB as pLB
cit.reloads([UI,wLB,jLB,pLB])

mayaData_dir=pLB.actionScriptsData(os.environ["MAYACGINTOOLSDATA_DIRECTORY"],"querySelections")
PATHSET=mayaData_dir
PATHRESET=cit.mayaSettings_dir
FILE="init"

class SelectionTextWindow(UI.PlainTextWindowBase):
    def __init__(self,parent):
        super(SelectionTextWindow, self).__init__(parent)
        self.setObjectName("SelectionsQuery")
        self.setWindowTitle("SelectionsQuery")
        self.buttonLeft_QPushButton.setText("Selection")
        self.buttonCenter_QPushButton.setText("Select Replace")
        self.buttonRight_QPushButton.setText("Select Add")

        self._pathSet=PATHSET
        self._pathReset=PATHRESET
        self._file=FILE

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

    #Private Function
    def __setPlainText_create_func(self,objs,add=False):
        organizeTexts=objs
        if add:
            getText_str=self.textPlain_QPlainTextEdit.toPlainText()
            addTexts=self.convertStringToList_edit_list(getText_str)
            organizeTexts=self.organizeList_edit_list([addTexts,objs])
        text_str=self.convertListToString_edit_str(organizeTexts)
        self.textPlain_QPlainTextEdit.setPlainText(text_str)

    def __getSelectText_query_list(self):
        getText_str=self.textPlain_QPlainTextEdit.toPlainText()
        texts=self.convertStringToList_edit_list(getText_str)
        return texts

    #Summary Function
    def __importJson(self,path,file):
        settings_dict=self.importJson_query_dict(path,file)
        self.__setPlainText_create_func(settings_dict["selections"])

    def __exportJson(self,path,file):
        selectText_list=self.__getSelectText_query_list()
        self.exportJson_edit_func(path,file,selectText_list)

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
