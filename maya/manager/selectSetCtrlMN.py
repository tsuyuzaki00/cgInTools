# -*- coding: iso-8859-15 -*-

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import os
from maya import cmds

import cgInTools as cit
from ...ui import selectSetCtrlUI as UI
from ..library import windowLB as wLB
from ..library import jsonLB as jLB
from ..library import curveLB as cLB
cit.reloads([UI,wLB,jLB,cLB])

class SelectSetCtrlWindow(UI.SelectSetCtrlWindowBase):
    def __init__(self,parent):
        super(SelectSetCtrlWindow,self).__init__(parent)
    
    def buttonLeftOnClicked(self):
        ctrl_QListWidget=self.ctrl_QTabWidget.currentWidget()
        planeCtrl_QListWidgetItem=ctrl_QListWidget.currentItem()
        ctrlType_str=planeCtrl_QListWidgetItem.text()
        
        ctrl=cLB.SetCurve()
        ctrl.setCurveType(ctrlType_str)
        ctrl.create()

    def buttonCenterOnClicked(self):
        objs=cmds.ls(sl=True)
        ctrl_QListWidget=self.ctrl_QTabWidget.currentWidget()
        planeCtrl_QListWidgetItem=ctrl_QListWidget.currentItem()
        ctrlType_str=planeCtrl_QListWidgetItem.text()
        
        ctrl=cLB.SetCurve()
        ctrl.setCurveType(ctrlType_str)
        curve=ctrl.create()

        replace=cLB.EditCurve()
        replace.setSourceNode(curve)
        for obj in objs:
            replace.setTargetNode(obj)
            replace.replaceShape()
        cmds.delete(curve)

    def buttonRightOnClicked(self):
        objs=cmds.ls(sl=True)
        for obj in objs:
            parent_list=cmds.listRelatives(obj,p=True,pa=True)
            childs=cmds.listRelatives(obj,c=True,pa=True,typ="transform")
            if not childs == None:
                if not parent_list == None:
                    parent=parent_list[0]
                    cmds.parent(childs,parent)
                else:
                    cmds.parent(childs,w=True)
            cmds.delete(obj)

def main():
    viewWindow=SelectSetCtrlWindow(parent=wLB.mayaMainWindow_query_widget())
    viewWindow.show()