# -*- coding: iso-8859-15 -*-
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import os
import maya.cmds as cmds

import cgInTools as cit
from ...ui import mainWindowUI as mainUI
from ...ui import clickSelectUI as UI
from ..library import windowLB as wLB
cit.reloads([UI,wLB])

class MainMenu(mainUI.MainWindowBase):
    def __init__(self, parent):
        super(MainMenu, self).__init__(parent)
        self.setWindowTitle("clickSelections")
        
        layouts = QFormLayout(self)
        self.centerWidget.setLayout(layouts)
        widget = ClickSelectWindow(self)
        layouts.addWidget(widget)

class ClickSelectWindow(UI.ClickSelectWindowBase):
    def __init__(self, parent):
        super(ClickSelectWindow, self).__init__(parent)
        self.setObjectName("click_selections")
        self.select_lisWig.itemClicked.connect(self.listClick_onClicked)
        self.select_lisWig.itemDoubleClicked.connect(self.doubleClick_onClicked)
        self.container={}

    def listClick_onClicked(self):
        itemNum=self.select_lisWig.currentRow()
        itemObjs=self.container[str(itemNum)]
        print(itemObjs),

    def doubleClick_onClicked(self):
        item=self.select_lisWig.currentItem()
        item.setFlags(item.flags()|Qt.ItemIsEditable)
        self.select_lisWig.editItem(item)

    def create_button_onClicked(self):
        item=QListWidgetItem()
        item.setText("item_"+self.type_combo.currentText())
        self.select_lisWig.insertItem(10000,item)
        row_int=self.select_lisWig.row(item)
        self.container[str(row_int)]=[]
        item.setSelected(True)

    def delete_button_onClicked(self):
        itemNum=self.select_lisWig.currentRow()
        max=len(self.container)
        max=max-1
        self.select_lisWig.takeItem(itemNum)
        for j in range(itemNum,max):
            if j == max:
                del self.container[str(max)]
            else:
                self.container[str(j)]=self.container[str(j+1)]

    def single_button_onClicked(self):
        cmds.select(cl=True)
        self.containerSelect_quary_list()
    
    def multi_button_onClicked(self):
        self.containerSelect_quary_list()

    def containerSelect_quary_list(self):
        itemNum=self.select_lisWig.currentRow()
        itemObjs=self.container[str(itemNum)]
        for obj in itemObjs:
            cmds.select(obj,add=True)

    def comboType_query_str(self):
        objs=cmds.ls(sl=True)
        if self.type_combo.currentText() == "selections":
            selections=objs
            return selections
        elif self.type_combo.currentText() == "connections":
            connections=[]
            it = iter(objs)
            for i,j in zip(it,it):
                connections.append([i,j])
            return connections
        elif self.type_combo.currentText() == "parent<childs":
            parentChilds=[objs[0],objs[1:]]
            return parentChilds
        elif self.type_combo.currentText() == "parents>child":
            parentsChild=[objs[:-1],objs[-1]]
            return parentsChild
        elif self.type_combo.currentText() == "lists":
            nodeLists=[]
            nodeLists.append(objs)
            return nodeLists

    def set_button_onClicked(self):
        selObjs=self.comboType_query_str()
        itemNum=self.select_lisWig.currentRow()
        self.container[str(itemNum)]=selObjs

    def add_button_onClicked(self):
        selObjs=self.comboType_query_str()
        itemNum=self.select_lisWig.currentRow()
        for selObj in selObjs:
            self.container[str(itemNum)].append(selObj)

    def edit_button_onClicked(self):
        itemNum=self.select_lisWig.currentRow()
        print(itemNum)
        itemContainer=self.container[str(itemNum)]
        print(itemContainer)

    def clean_button_onClicked(self):
        itemNum=self.select_lisWig.currentRow()
        self.container[str(itemNum)]=[]

"""
class CListWidgetItem(QListWidgetItem):
    def __init__(self,*args, **kwargs):
        super(CListWidgetItem,self).__init__(**kwargs)
        self.container=

    # 番号を格納する
    def setRow(self,row):
        self.container[str(row)]=[]

    # コンテナにオブジェクトを格納する
    def setObjs(self,row,objs):
        self.container[str(row)]=objs

    # 番号を取得してコンテナを返す
    def getContainer(self,row):
        container=self.container[str(row)]
        return container

    
    def delContainer(self,row):
        max=len(self.container)
        for j in range(row,max):

            self.container[str(j)]=self.container[str(j+1)]
"""

def main():
    mayaWindow=MainMenu(parent=wLB.mayaMainWindow_query_widget())
    mayaWindow.show()