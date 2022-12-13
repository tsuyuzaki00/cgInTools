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

class SelectionTextWindow(UI.PlainTextWindowBase):
    def __init__(self,parent):
        super(SelectionTextWindow, self).__init__(parent)
        self.setObjectName("selectView_list")
        self.setWindowTitle("selectView_list")
        self.buttonLeft_QPushButton.setText("print")
        self.buttonCenter_QPushButton.setText("Select Replace")
        self.buttonRight_QPushButton.setText("Select Add")

    def _plainText_create_func(self,objs,add=False):
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

    #Public Function
    def buttonLeftOnClicked(self):
        getText_str=self.textPlain_QPlainTextEdit.toPlainText()
        text_list=eval(getText_str)
        cmds.select(text_list)

    def buttonCenterOnClicked(self):
        objs=cmds.ls(sl=True)
        self._plainText_create_func(objs)

    def buttonRightOnClicked(self):
        objs=cmds.ls(sl=True)
        self._plainText_create_func(objs,add=True)

def main():
    viewWindow=SelectionTextWindow(parent=wLB.mayaMainWindow_query_widget())
    objs=cmds.ls(sl=True)
    viewWindow._plainText_create_func(objs)
    viewWindow.show()
