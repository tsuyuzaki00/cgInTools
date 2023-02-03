# -*- coding: iso-8859-15 -*-

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import os
from maya import cmds

import cgInTools as cit
from ...ui import plainTextUI as UI
from ..library import windowLB as wLB
from ..library import jsonLB as jLB
cit.reloads([UI,wLB,jLB])

PATHSET=cit.mayaData_dir
PATHRESET=cit.mayaSettings_dir
FILE="querySelections"

class SelectionTextWindow(UI.PlainTextWindowBase):
    def __init__(self,parent):
        super(SelectionTextWindow, self).__init__(parent)
        self.setObjectName("selectView_list")
        self.setWindowTitle("selectView_list")
        self.buttonLeft_QPushButton.setText("Selection")
        self.buttonCenter_QPushButton.setText("Select Replace")
        self.buttonRight_QPushButton.setText("Select Add")

        self._pathSet=PATHSET
        self._pathReset=PATHRESET
        self._file=FILE

    #Single Function
    def exportJson_edit_func(self,path,file,planeText_str):
        write_dict={
            "selections":planeText_str,
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

    #Private Function
    def __selectPlainText_create_func(self,objs,add=False):
        if add is True:
            getText_str=self.textPlain_QPlainTextEdit.toPlainText()
            texts=eval(getText_str)
            texts.extend(objs)
            texts=list(set(texts))
        else:
            texts=objs
        for num,text in enumerate(texts):
            if num == 0:
                text_str="[\n"
            text_str += '    "'+text+'",\n'
            if num == len(texts) - 1:
                text_str=text_str.rstrip(",\n")
                text_str += "\n]"
        self.textPlain_QPlainTextEdit.setPlainText(text_str)

    def __setPlaneText_edit_func(self,select_dict):
        text_str=select_dict["selections"]
        self.textPlain_QPlainTextEdit.setPlainText(text_str)

    def __getPlaneText_query_str(self):
        return self.textPlain_QPlainTextEdit.toPlainText()

    #Summary Function
    def __importJson(self,path,file):
        settings_dict=self.importJson_query_dict(path,file)
        self.__setPlaneText_edit_func(settings_dict)

    def __exportJson(self,path,file):
        planeText_str=self.__getPlaneText_query_str()
        self.exportJson_edit_func(path,file,planeText_str)

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
            self.__selectPlainText_create_func(objs)

    def buttonRightOnClicked(self):
        objs=cmds.ls(sl=True)
        if not objs == []:
            self.__selectPlainText_create_func(objs,add=True)

def main():
    viewWindow=SelectionTextWindow(parent=wLB.mayaMainWindow_query_widget())
    objs=cmds.ls(sl=True)
    if not objs == []:
        viewWindow.__selectPlainText_create_func(objs)
    viewWindow.show()
