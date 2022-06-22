# -*- coding: iso-8859-15 -*-

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import os
import maya.cmds as cmds
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance

from ...ui import mainWindowUI as mainUI
from ...ui import clickSelectUI as UI
from ..library import simpleJson as SJ

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
        self.itemContainer = ""

    def listClick_onClicked(self):
        for obj in self.itemContainer:
            cmds.select(obj,add=True)

    def doubleClick_onClicked(self):
        item=self.select_lisWig.currentItem()
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.select_lisWig.editItem(item)

    def create_button_onClicked(self):
        item=self.select_lisWig.addItem("item")
        self.select_lisWig.editItem(item)

    def delete_button_onClicked(self):
        test=self.select_lisWig.currentRow()
        self.select_lisWig.takeItem(test)

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
        self.itemContainer = selObjs
        print(self.itemContainer)

    def add_button_onClicked(self):
        selObjs=self.comboType_query_str()
        for selObj in selObjs:
            self.itemContainer.append(selObj)
        print(self.itemContainer)

    def edit_button_onClicked(self):
        print("base")

    def clean_button_onClicked(self):
        self.itemContainer = ""
        print(self.itemContainer)

# mayaのメインウインドウを取得する
def get_maya_main_window():
    omui.MQtUtil.mainWindow()
    ptr = omui.MQtUtil.mainWindow()
    widget = wrapInstance(long(ptr), QWidget)
    return widget

def main():
    # 依存関係のないウインドウを継承して作ったMaya用のボタンUI
    maya_window_instance = MainMenu(parent=get_maya_main_window())
    maya_window_instance.show()