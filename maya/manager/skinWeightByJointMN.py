# -*- coding: iso-8859-15 -*-
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import os
import maya.cmds as cmds

import cgInTools as cit
from ...ui import tableUI as UI
from ..library import windowLB as wLB
from ..library import skinLB as sLB
from ..library import objectLB as oLB
from ..library import jsonLB as jLB
cit.reloads([UI,wLB,sLB,oLB,jLB])

class SkinWeightByJointWindow(UI.TableWindowBase):
    def __init__(self,parent):
        super(SkinWeightByJointWindow,self).__init__(parent)
        self.setObjectName("selectView_list")
        self.setWindowTitle("selectView_list")
        self.buttonLeft_QPushButton.setText("Run")
        self.buttonCenter_QPushButton.setText("Set")
        self.buttonRight_QPushButton.setText("Delete")
        self.headerTitle_list=["UseJoint","Value","Vertexs","Joint","Geometry"]
        self.createHeaderTitle()
        self.data_lists=[["1","1","","",""]]
        self.createTableItem()

        main_QGridLayout=QGridLayout(self)
        self.custom_QGridLayout.addLayout(main_QGridLayout,1,0)

        self.useSwitch_QPushButton=QPushButton("useSwitch",self)
        main_QGridLayout.addWidget(self.useSwitch_QPushButton,0,0)
        self.useSwitch_QPushButton.clicked.connect(self.useSwitchOnClicked)

        self.value_QSlider=QSlider(Qt.Horizontal,self)
        self.value_QSlider.setRange(0,1000)
        self.value_QSlider.setTickPosition(QSlider.TicksBothSides)
        self.value_QSlider.setSingleStep(5)
        self.value_QSlider.setPageStep(10)
        self.value_QSlider.setTickInterval(0)
        main_QGridLayout.addWidget(self.value_QSlider,0,1,0,2)

        self.vertexs_QPushButton=QPushButton("setVertexs",self)
        main_QGridLayout.addWidget(self.vertexs_QPushButton,1,0)
        self.vertexs_QPushButton.clicked.connect(self.vertexsOnClicked)
        
        self.joint_QPushButton=QPushButton("setJoint",self)
        main_QGridLayout.addWidget(self.joint_QPushButton,1,1)
        self.joint_QPushButton.clicked.connect(self.jointOnClicked)

        self.geometry_QPushButton=QPushButton("setGeometry",self)
        main_QGridLayout.addWidget(self.geometry_QPushButton,1,2)
        self.geometry_QPushButton.clicked.connect(self.geometryOnClicked)

    #Private Function
    def _nullTable_create_func(self):
        self.data_lists.append(["1","1","","",""])
        self.createTableItem()

    def _getTable_query_lists(self):
        table_list=[]
        for colNum in range(len(self.data_lists)):
            table_list.append([])
        for rowNum in range(len(self.headerTitle_list)):
            for colNum in range(len(self.data_lists)):
                item_QTableWidgetItem=self.table_QTableWidget.item(colNum,rowNum)
                text_str=item_QTableWidgetItem.text()
                table_list[colNum].append(text_str)
        return table_list

    #Public Function
    def useSwitchOnClicked(self):
        self.data_lists=self._getTable_query_lists()
        selectItem_QTableWidgetItem=self.table_QTableWidget.currentItem()
        if not selectItem_QTableWidgetItem == None:
            row_int=selectItem_QTableWidgetItem.row()
            self.data_lists[row_int][0]=str(int(not bool(int(self.data_lists[row_int][0]))))
            self.createTableItem()
    
    def vertexsOnClicked(self):
        self.data_lists=self._getTable_query_lists()
        selectItem_QTableWidgetItem=self.table_QTableWidget.currentItem()
        if not selectItem_QTableWidgetItem == None:
            row_int=selectItem_QTableWidgetItem.row()
            vertexs=cmds.ls(sl=True)
            self.data_lists[row_int][2]=str(vertexs)
            self.createTableItem()

    def jointOnClicked(self):
        self.data_lists=self._getTable_query_lists()
        selectItem_QTableWidgetItem=self.table_QTableWidget.currentItem()
        if not selectItem_QTableWidgetItem == None:
            row_int=selectItem_QTableWidgetItem.row()
            joint=cmds.ls(sl=True,type="joint")
            if not joint == []:
                self.data_lists[row_int][3]=joint[0]
                self.createTableItem()

    def geometryOnClicked(self):
        self.data_lists=self._getTable_query_lists()
        selectItem_QTableWidgetItem=self.table_QTableWidget.currentItem()
        if not selectItem_QTableWidgetItem == None:
            row_int=selectItem_QTableWidgetItem.row()
            geometry=cmds.ls(sl=True,type="transform")
            mesh=cmds.listRelatives(geometry,type="mesh")
            if not mesh == None:
                self.data_lists[row_int][4]=geometry[0]
                self.createTableItem()
    

    def buttonLeftOnClicked(self):
        self.data_lists=self._getTable_query_lists()
        jointWeights=[]
        for data_list in self.data_lists:
            jointWeight=oLB.JointWeight(data_list[3])
            jointWeight.setUseJoint(bool(int(data_list[0])))
            jointWeight.setValue(float(data_list[1]))
            jointWeight.setVertexs(eval(data_list[2]))
            jointWeight.setSubject(data_list[4])
            jointWeights.append(jointWeight)
        skinWeightByJoint=sLB.skinWeightByJoint()
        skinWeightByJoint.setWeights(jointWeights)
        skinWeightByJoint.run()

    def buttonCenterOnClicked(self):
        self.data_lists=self._getTable_query_lists()
        selectItem_QTableWidgetItem=self.table_QTableWidget.currentItem()
        if not selectItem_QTableWidgetItem == None:
            row_int=selectItem_QTableWidgetItem.row()
            newRow_list=[self.data_lists[row_int][0],self.data_lists[row_int][1],self.data_lists[row_int][2],self.data_lists[row_int][3],self.data_lists[row_int][4]]
            self.data_lists.insert(row_int+1,newRow_list)
            self.createTableItem()
            self.table_QTableWidget.setCurrentCell(row_int+1,0)
        else:
            self.data_lists.append(["1","1","","",""])
            self.createTableItem()

    def buttonRightOnClicked(self):
        self.data_lists=self._getTable_query_lists()
        selectItem_QTableWidgetItem=self.table_QTableWidget.currentItem()
        if not selectItem_QTableWidgetItem == None:
            row_int=selectItem_QTableWidgetItem.row()
            self.data_lists.pop(row_int)
            self.createTableItem()

def main():
    viewWindow=SkinWeightByJointWindow(parent=wLB.mayaMainWindow_query_widget())
    viewWindow.show()