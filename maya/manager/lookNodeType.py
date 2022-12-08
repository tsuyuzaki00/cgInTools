# -*- coding: iso-8859-15 -*-
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import os
from maya import cmds

import cgInTools as cit
from ...ui import scriptsRunUI as UI
from ..library import windowLB as wLB
cit.reloads([UI,wLB])
class LookNodeTypeWindow(UI.ScriptsRunWindowBase):
    def __init__(self, parent):
        super(LookNodeTypeWindow, self).__init__(parent)
        self.setObjectName("select_list_view")
        self.setWindowTitle("select_list_view")
        self.left_button.setText("print")
        self.center_button.setText("Select Replace")
        self.right_button.setText("Select Add")

    def view_scripts(self,nodes):
        for node in nodes:
            type = cmds.nodeType(node)
            self.scripts_plain.insertPlainText(node+'\t:\t'+str(type)+'\n')
        
    def left_button_onClicked(self):
        main()

    def center_button_onClicked(self):
        objs = cmds.ls(sl=True)
        self.scripts_plain.clear()
        self.view_scripts(objs)

    def right_button_onClicked(self):
        objs = cmds.ls(sl=True)
        self.view_scripts(objs)

def node_list(sels):
    nodes = []
    for sel in sels:
        childs = cmds.listRelatives(sel)
        if childs == None:
            nodes.append(sel)
        else :
            for child in childs:
                nodes.append(sel)
                nodes.append(child)
    return nodes

def main():
    maya_window_instance=LookNodeTypeWindow(parent=wLB.mayaMainWindow_query_widget())
    objs=cmds.ls(sl=True)
    maya_window_instance.view_scripts(objs)
    maya_window_instance.show()