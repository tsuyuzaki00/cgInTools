from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import os
import maya.cmds as cmds

import cgInTools as cit
from ...ui import equipmentSettingsUI as UI
from ..library import windowLB as wLB
from ..library import renderLB as rLB
from ..library import jsonLB as jLB
from ..library import objectLB as oLB
cit.reloads([UI,wLB,rLB,jLB,oLB])

class EquipmentWindow(UI.EquipmentWindowBase):
    def __init__(self,*args,**kwargs):
        super(EquipmentWindow,self).__init__(*args,**kwargs)
        self.setWindowFlags(Qt.Window)
        self.equipment_QTreeWidget.clear()
        self.equipment_dicts=[]
        for equipment_dict in self.equipment_dicts:
            self.treeWidgetItem_create_func(equipment_dict["name"],equipment_dict["value"],equipment_dict["parent"])
    
    #Single Function

    #Public Function
    def buttonLeftOnClicked(self):
        objs=cmds.ls(sl=True)
        for obj in objs:
            matrixNode=oLB.MatrixObject(obj)
            matrixNode.setWorldMatrix([1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1])
            matrixNode.setTime(1)
            matrixNode.worldMovement()

    def buttonCenterOnClicked(self):
        objs=cmds.ls(sl=True)
        if not objs == []:
            for obj in objs:
                select_dicts=[
                    {"name":obj,"value":None,"parent":None},
                    {"name":"matrix","value":str(cmds.getAttr(obj+".worldMatrix")),"parent":obj},
                    {"name":"time","value":str(cmds.currentTime(q=True)),"parent":obj}
                ]
            for select_dict in select_dicts:
                self.treeWidgetItem_create_func(select_dict["name"],select_dict["value"],select_dict["parent"])

    def buttonRightOnClicked(self):
        self.equipment_QTreeWidget.clear()

def main():
    viewWindow=EquipmentWindow(parent=wLB.mayaMainWindow_query_widget())
    viewWindow.show()