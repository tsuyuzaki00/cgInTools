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
        self._tableList_create_func(objs)

    def buttonRightOnClicked(self):
        pass

def main():
    viewWindow=SelectSetCtrlWindow(parent=wLB.mayaMainWindow_query_widget())
    viewWindow.show()