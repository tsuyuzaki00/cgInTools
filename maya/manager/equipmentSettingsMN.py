from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import os
import maya.cmds as cmds

import cgInTools as cit
from ...ui import treeUI as UI
from ..library import windowLB as wLB
from ..library import renderLB as rLB
from ..library import jsonLB as jLB
from ..library import objectLB as oLB
cit.reloads([UI,wLB,rLB,jLB,oLB])

class EquipmentWindow(UI.TreeWindowBase):
    def __init__(self,*args,**kwargs):
        super(EquipmentWindow,self).__init__(*args,**kwargs)
        self.setWindowFlags(Qt.Window)
        self.buttonLeft_QPushButton.setText("Create")
        self.buttonCenter_QPushButton.setText("SetTree")
        self.buttonRight_QPushButton.setText("DeleteTree")

        self.equipment_CTreeWidget=UI.CTreeWidget()
        self.custom_QGridLayout.addWidget(self.equipment_CTreeWidget)
        self.equipment_CTreeWidget.setHeaderLabelList(["Name","Value"])
        self.equipment_CTreeWidget.createBase()
        """
        self.equipment_QTreeWidget.clear()
        self.equipment_dicts=[]
        for equipment_dict in self.equipment_dicts:
            self.treeWidgetItem_create_func(equipment_dict["name"],equipment_dict["value"],equipment_dict["parent"])
        """
    
    #Single Function
    def getModifiedAttr_query_dicts(self,obj):
        edit_dicts=[]
        shapes=cmds.listRelatives(obj,s=True)
        if shapes == None:
            return None
        for shape in shapes:
            nodeType=cmds.nodeType(shape)
            defShape=cmds.createNode(nodeType,n="getAttrDefShape")
            defTrs=cmds.listRelatives(defShape,p=True)
            attrs=cmds.listAttr(defShape,hd=True,m=True,se=True,s=True)
            for attr in attrs:
                defValue=cmds.getAttr(defShape+"."+attr)
                value=cmds.getAttr(shape+"."+attr)
                if not defValue == value:
                    edit_dict={"shape":shape,"attr":attr,"value":value}
                    edit_dicts.append(edit_dict)
            cmds.delete(defTrs)
        return edit_dicts
    
    def getWidgetAttr_query_dicts(self,obj):
        edit_dicts=[]
        shapes=cmds.listRelatives(obj,s=True)
        if shapes == None:
            return None
        for shape in shapes:
            shape_dict={"name":shape,"value":None,"parent":obj}
            edit_dicts.append(shape_dict)
            nodeType=cmds.nodeType(shape)
            defShape=cmds.createNode(nodeType,n="getAttrDefShape")
            defTrs=cmds.listRelatives(defShape,p=True)
            attrs=cmds.listAttr(defShape,hd=True,m=True,se=True,s=True)
            for attr in attrs:
                defValue=cmds.getAttr(defShape+"."+attr)
                value=cmds.getAttr(shape+"."+attr)
                if not defValue == value:
                    edit_dict={"name":attr,"value":str(value),"parent":shape}
                    edit_dicts.append(edit_dict)
            cmds.delete(defTrs)
        return edit_dicts

    #Private Function
    def _getTopLevelItems_query_list(self):
        self._topItems=[]
        itemCount_int=self.topLevelItemCount()
        for num in range(itemCount_int):
            topItem_QTreeWidgetItem=self.topLevelItem(num)
            topItem_CTreeWidgetItem=CTreeWidgetItem(topItem_QTreeWidgetItem)
            self._topItems.append(topItem_CTreeWidgetItem)
        return self._topItems

        obj=topItem_QTreeWidgetItem.text(0)

    #Public Function
    def buttonLeftOnClicked(self):
        itemCount_int=self.equipment_QTreeWidget.topLevelItemCount()
        for num in range(itemCount_int):
            topItem_QTreeWidgetItem=self.equipment_QTreeWidget.topLevelItem(num)
            obj=topItem_QTreeWidgetItem.text(0)
        
        itemCount_int=topItem_QTreeWidgetItem.childCount()
        objectItem_list=topItem_QTreeWidgetItem.child()
        matrix=objectItem_list[0].text(1)
        time=objectItem_list[1].text(1)
        nodeType=objectItem_list[2].text(1)
        shape=objectItem_list[-1].text(0)
        
        otherValueDicts=[]
        shapeItem_list=objectItem_list[-1].takeChildren()
        for num in range(len(shapeItem_list)):
            attr=shapeItem_list[num].text(0)
            value=shapeItem_list[num].text(1)
            value_dict={"node":shape,"attr":attr,"value":value}
            otherValueDicts.append(value_dict)

        newNode=cmds.createNode(nodeType,n=shape)

        matrixNode=oLB.MatrixObject(newNode.replace("Shape",""))
        print(matrixNode.getObject())
        matrixNode.setWorldMatrix(eval(matrix))
        print(matrixNode.getWorldMatrix())
        matrixNode.setTime(float(time))
        #matrixNode.setOtherValueDicts(otherValueDicts)
        matrixNode.worldMovement()

    def buttonCenterOnClicked(self):
        objs=cmds.ls(sl=True)
        if not objs == []:
            for obj in objs:
                matrixNode=oLB.MatrixObject(obj)
                matrixNode.loading()
                matrixNode.setCurrentTime()
                if not matrixNode.getShapes() == None:
                    nodeType=matrixNode.getShapeTypes()[0]
                else:
                    nodeType=matrixNode.getObjectType()
                select_dicts=[
                    {"name":obj,"value":None,"parent":None},
                    {"name":"matrix","value":str(list(matrixNode.getWorldMatrix())),"parent":obj},
                    {"name":"time","value":str(matrixNode.getTime()),"parent":obj},
                    {"name":"nodeType","value":str(nodeType),"parent":obj}
                ]
                attr_dicts=self.getWidgetAttr_query_dicts(obj)
                for attr_dict in attr_dicts:
                    select_dicts.append(attr_dict)
            for select_dict in select_dicts:
                self.treeWidgetItem_create_func(select_dict["name"],select_dict["value"],select_dict["parent"])

    def buttonRightOnClicked(self):
        self.equipment_QTreeWidget.clear()

def main():
    viewWindow=EquipmentWindow(parent=wLB.mayaMainWindow_query_widget())
    viewWindow.show()