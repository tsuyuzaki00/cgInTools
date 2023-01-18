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

SETPATH=cit.mayaData_dir
RESETPATH=cit.mayaSettings_dir

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

        self.setPath=SETPATH
        self.resetPath=RESETPATH
        self.fileName="equipmentSettings"
        self.__importJson(self.setPath,self.fileName)
    
    #Single Function
    def importJson_query_dict(self,path,file,extension):
        setting=jLB.Json()
        setting.setPath(path)
        setting.setFile(file)
        setting_dict=setting.read()
        return setting_dict

    def exportJson_edit_func(self,path,file,extension):
        write_dict={
            "dicts":self.equipment_CTreeWidget.getTreeParamDicts()
        }
        setting=jLB.Json()
        setting.setPath(path)
        setting.setFile(file)
        setting.setExtension(extension)
        setting.setWriteDict(write_dict)
        setting.write()

    def getWidgetAttr_query_dicts(self,obj):
        edit_dicts=[]
        shapes=cmds.listRelatives(obj,s=True)
        if shapes == None:
            return None
        for shape in shapes:
            shape_dict={"parent":obj,"nameParams":[shape,None]}
            edit_dicts.append(shape_dict)
            nodeType=cmds.nodeType(shape)
            defShape=cmds.createNode(nodeType,n="getAttrDefShape")
            defTrs=cmds.listRelatives(defShape,p=True)
            attrs=cmds.listAttr(defShape,hd=True,m=True,se=True,s=True)
            for attr in attrs:
                defValue=cmds.getAttr(defShape+"."+attr)
                value=cmds.getAttr(shape+"."+attr)
                if not defValue == value:
                    edit_dict={"parent":shape,"nameParams":[attr,str(value)]}
                    edit_dicts.append(edit_dict)
            cmds.delete(defTrs)
        return edit_dicts

    #Multi Function
    def _selectParams_create_dicts(self,obj):
        matrixNode=oLB.MatrixObject(obj)
        matrixNode.loading()
        matrixNode.setCurrentTime()
        if not matrixNode.getShapes() == None:
            nodeType=matrixNode.getShapeTypes()[0]
        else:
            nodeType=matrixNode.getObjectType()
        select_dicts=[
            {"parent":None,"nameParams":[obj,None]},
            {"parent":obj,"nameParams":["matrix",str(list(matrixNode.getWorldMatrix()))]},
            {"parent":obj,"nameParams":["time",str(matrixNode.getTime())]},
            {"parent":obj,"nameParams":["nodeType",str(nodeType)]}
        ]
        attr_dicts=self.getWidgetAttr_query_dicts(obj)
        for attr_dict in attr_dicts:
            select_dicts.append(attr_dict)
        return select_dicts

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
    def __importJson(self,path,file,extension="json"):
        setting_dict=self.importJson_query_dict(path,file,extension)
        self.equipment_CTreeWidget.setTreeParamDicts(setting_dict["dicts"])
        self.equipment_CTreeWidget.createTree()

    def __exportJson(self,path,file,extension="json"):
        self.exportJson_edit_func(path,file,extension)

    def refreshOnClicked(self):
        self.__importJson(self.resetPath,self.fileName)
    
    def restoreOnClicked(self):
        self.__importJson(self.setPath,self.fileName)
    
    def saveOnClicked(self):
        self.__exportJson(self.setPath,self.fileName)
    
    def importOnClicked(self):
        path,file=wLB.mayaFileDialog_query_path_file("import setting",1)
        self.__importJson(path,file)

    def exportOnClicked(self):
        path,file=wLB.mayaFileDialog_query_path_file("export setting",0)
        self.__exportJson(path,file)

    def buttonLeftOnClicked(self):
        topItem_QTreeWidgetItems=self.equipment_CTreeWidget.getTopItems()
        for topItem_QTreeWidgetItem in topItem_QTreeWidgetItems:
            itemCount_int=topItem_QTreeWidgetItem.childCount()
            objectItem_list=[]
            for num in range(itemCount_int):
                childItem_QTreeWidgetItem=topItem_QTreeWidgetItem.child(num)
                objectItem_list.append(childItem_QTreeWidgetItem)
            matrix=objectItem_list[0].text(1)
            time=objectItem_list[1].text(1)
            nodeType=objectItem_list[2].text(1)
            shape=objectItem_list[-1].text(0)
        
            otherValueDicts=[]
            shapeCount_int=objectItem_list[-1].childCount()
            for num in range(shapeCount_int):
                shapeItem_QTreeWidgetItem=objectItem_list[-1].child(num)
                attr=shapeItem_QTreeWidgetItem.text(0)
                value=shapeItem_QTreeWidgetItem.text(1)
                value_dict={"node":shape,"attr":attr,"value":eval(value)}
                otherValueDicts.append(value_dict)

            newNode=cmds.createNode(nodeType,n=shape)
            parentNode=cmds.listRelatives(newNode,p=True)

            matrixNode=oLB.MatrixObject(parentNode[0])
            matrixNode.setWorldMatrix(eval(matrix))
            matrixNode.setTime(float(time))
            matrixNode.setOtherValueDicts(otherValueDicts)
            matrixNode.worldMovement()

    def buttonCenterOnClicked(self):
        objs=cmds.ls(sl=True)
        create_dicts=[]
        if not objs == []:
            for obj in objs:
                select_dicts=self._selectParams_create_dicts(obj)
                for select_dict in select_dicts:
                    create_dicts.append(select_dict)
            self.equipment_CTreeWidget.setTreeParamDicts(create_dicts)
            self.equipment_CTreeWidget.createTree()

    def buttonRightOnClicked(self):
        self.equipment_CTreeWidget.clear()

def main():
    viewWindow=EquipmentWindow(parent=wLB.mayaMainWindow_query_widget())
    viewWindow.show()