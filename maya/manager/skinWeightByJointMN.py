# -*- coding: iso-8859-15 -*-
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import os
import maya.cmds as cmds

import cgInTools as cit
from ...ui import skinWeightByJointUI as UI
from ..library import windowLB as wLB
from ..library import skinLB as sLB
from ..library import objectLB as oLB
from ..library import jsonLB as jLB
cit.reloads([UI,wLB,sLB,oLB,jLB])

PATHSET=cit.mayaData_dir
PATHRESET=cit.mayaSettings_dir

class SkinWeightByJointWindow(UI.SkinWeightByJointWindowBase):
    def __init__(self,parent):
        super(SkinWeightByJointWindow,self).__init__(parent)
        self.setObjectName("selectView_list")
        self.setWindowTitle("selectView_list")
        self.setFixedSize(650,750)
        self.headerTitle_list=["UseJoint","Value","Vertexs","Joint"]
        self.createHeaderTitle()
        self.data_lists=[["1","1.0","[]",""]]
        self.createTableItem()
        print(self.table_QTableWidget.mimeTypes())

        self.setPath=PATHSET
        self.resetPath=PATHRESET
        self.fileName="skinWeightByJoint"
        self.extension="byJointWeight"
        self.__importJson(self.setPath,self.fileName)

    #Single Function
    def importJson_query_dict(self,path,file,extension):
        setting=jLB.Json()
        setting.setPath(path)
        setting.setFile(file)
        setting.setExtension(extension)
        setting_dict=setting.read()
        return setting_dict

    def exportJson_edit_func(self,path,file,extension,weights):
        write_dict={
            "geometry":self.geometry_QLineEdit.text(),
            "weights":weights
        }
        setting=jLB.Json()
        setting.setPath(path)
        setting.setFile(file)
        setting.setExtension(extension)
        setting.setWriteDict(write_dict)
        setting.write()

    #Private Function
    def __getTable_query_lists(self):
        table_list=[]
        for colNum in range(len(self.data_lists)):
            table_list.append([])
        for rowNum in range(len(self.headerTitle_list)):
            for colNum in range(len(self.data_lists)):
                item_QTableWidgetItem=self.table_QTableWidget.item(colNum,rowNum)
                text_str=item_QTableWidgetItem.text()
                table_list[colNum].append(text_str)
        return table_list

    def __getColumnIntItem_query_str(self,column_int):
        self.data_lists=self.__getTable_query_lists()
        selectItem_QTableWidgetItem=self.table_QTableWidget.currentItem()
        if not selectItem_QTableWidgetItem == None:
            row_int=selectItem_QTableWidgetItem.row()
            joint_str=self.data_lists[row_int][column_int]
            return joint_str
        else:
            cmds.error("Please select item.")

    def __replaceListWithUI_edit_lists(self,setting_dict):
        weight_dicts=setting_dict["weights"]
        weights=[]
        for weight_dict in weight_dicts:
            weight_list=[str(weight_dict["use"]),str(weight_dict["value"]),str(weight_dict["vertexs"]),str(weight_dict["joint"])]
            weights.append(weight_list)
        return weights

    def __replaceUIWithList_query_list(self):
        self.data_lists=self.__getTable_query_lists()
        weights=[]
        for data_list in self.data_lists:
            weight_dict={"use":int(data_list[0]),"value":float(data_list[1]),"vertexs":eval(data_list[2]),"joint":data_list[3],"geometry":self.geometry_QLineEdit.text()}
            weights.append(weight_dict)
        return weights

    #Public Function
    def __importJson(self,path,file,extension="json"):
        setting_dict=self.importJson_query_dict(path,file,extension)
        self.geometry_QLineEdit.setText(setting_dict["geometry"])
        self.data_lists=self.__replaceListWithUI_edit_lists(setting_dict)
        self.createTableItem()

    def __exportJson(self,path,file,extension="json"):
        weights=self.__replaceUIWithList_query_list()
        self.exportJson_edit_func(path,file,extension,weights)

    def refreshOnClicked(self):
        self.__importJson(self.resetPath,self.fileName)
    
    def restoreOnClicked(self):
        self.__importJson(self.setPath,self.fileName)
    
    def saveOnClicked(self):
        self.__exportJson(self.setPath,self.fileName)
    
    def importOnClicked(self):
        path,file=wLB.mayaFileDialog_query_path_file("import setting",1,extension=self.extension)
        self.__importJson(path,file,self.extension)

    def exportOnClicked(self):
        path,file=wLB.mayaFileDialog_query_path_file("export setting",0,extension=self.extension)
        self.__exportJson(path,file,self.extension)

    def geometryOnClicked(self):
        geometry=cmds.ls(sl=True,type="transform")
        mesh=cmds.listRelatives(geometry,type="mesh")
        if not mesh == None:
            self.geometry_QLineEdit.setText(geometry[0])

    def weightsOnClicked(self):
        joint_str=self.__getColumnIntItem_query_str(3)
        geometry_str=self.geometry_QLineEdit.text()

        paint_SkinWeightByJoint=sLB.SkinWeightByJoint()
        paint_JointWeights=paint_SkinWeightByJoint.addWeights_create_JointWeights(joint_str,geometry_str)

        selectItem_QTableWidgetItem=self.table_QTableWidget.currentItem()
        if not selectItem_QTableWidgetItem == None:
            row_int=selectItem_QTableWidgetItem.row()
            for num,paint_JointWeight in enumerate(paint_JointWeights,1):
                newColumn_list=[str(int(paint_JointWeight.getUseJoint())),str(paint_JointWeight.getValue()),str(paint_JointWeight.getVertexs()),str(paint_JointWeight.getObject())]
                self.data_lists.insert(row_int+num,newColumn_list)
        self.createTableItem()
    
    def markOnClicked(self):
        print("mark")

    def useSwitchOnClicked(self):
        self.data_lists=self.__getTable_query_lists()
        selectItem_QTableWidgetItem=self.table_QTableWidget.currentItem()
        if not selectItem_QTableWidgetItem == None:
            row_int=selectItem_QTableWidgetItem.row()
            self.data_lists[row_int][0]=str(int(not bool(int(self.data_lists[row_int][0]))))
            self.createTableItem()
    
    def vertexsOnClicked(self):
        self.data_lists=self.__getTable_query_lists()
        selectItem_QTableWidgetItem=self.table_QTableWidget.currentItem()
        if not selectItem_QTableWidgetItem == None:
            row_int=selectItem_QTableWidgetItem.row()
            vertexs=cmds.ls(sl=True)
            self.data_lists[row_int][2]=str(vertexs)
            self.createTableItem()

    def jointOnClicked(self):
        self.data_lists=self.__getTable_query_lists()
        selectItem_QTableWidgetItem=self.table_QTableWidget.currentItem()
        if not selectItem_QTableWidgetItem == None:
            row_int=selectItem_QTableWidgetItem.row()
            joint=cmds.ls(sl=True,type="joint")
            if not joint == []:
                self.data_lists[row_int][3]=joint[0]
                self.createTableItem()

    def buttonLeftOnClicked(self):
        self.data_lists=self.__getTable_query_lists()
        jointWeights=[]
        for data_list in self.data_lists:
            jointWeight=oLB.JointWeight(data_list[3])
            jointWeight.setUseJoint(bool(int(data_list[0])))
            jointWeight.setValue(float(data_list[1]))
            jointWeight.setVertexs(eval(data_list[2]))
            jointWeight.setSubject(self.geometry_QLineEdit.text())
            jointWeights.append(jointWeight)
        skinWeightByJoint=sLB.SkinWeightByJoint()
        skinWeightByJoint.setWeights(jointWeights)
        skinWeightByJoint.run()

    def buttonCenterOnClicked(self):
        self.data_lists=self.__getTable_query_lists()
        selectItem_QTableWidgetItem=self.table_QTableWidget.currentItem()
        if not selectItem_QTableWidgetItem == None:
            row_int=selectItem_QTableWidgetItem.row()
            newColumn_list=[self.data_lists[row_int][0],self.data_lists[row_int][1],self.data_lists[row_int][2],self.data_lists[row_int][3]]
            self.data_lists.insert(row_int+1,newColumn_list)
            self.createTableItem()
            self.table_QTableWidget.setCurrentCell(row_int+1,0)
        else:
            self.data_lists.append(["1","1.0","[]",""])
            self.createTableItem()

    def buttonRightOnClicked(self):
        self.data_lists=self.__getTable_query_lists()
        selectItem_QTableWidgetItems=self.table_QTableWidget.selectedItems()
        if not selectItem_QTableWidgetItems == None:
            row_ints=[]
            for selectItem_QTableWidgetItem in selectItem_QTableWidgetItems:
                row_int=selectItem_QTableWidgetItem.row()
                row_ints.append(row_int)
            row_ints=list(set(row_ints))# For removal when multiple columns are selected.
            for sortRow in sorted(row_ints,reverse=True):
                self.data_lists.pop(sortRow)
            self.createTableItem()

def main():
    viewWindow=SkinWeightByJointWindow(parent=wLB.mayaMainWindow_query_widget())
    viewWindow.show()