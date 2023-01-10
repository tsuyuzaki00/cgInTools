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

SETPATH=cit.mayaData_dir
RESETPATH=cit.mayaSettings_dir

class SelectSetCtrlWindow(UI.SelectSetCtrlWindowBase):
    def __init__(self,parent):
        super(SelectSetCtrlWindow,self).__init__(parent)

        self.setPath=SETPATH
        self.resetPath=RESETPATH
        self.fileName="selectSetCtrl"
        self.__importJson(self.setPath,self.fileName)

    #Single Function
    def importJson_query_dict(self,path,file,extension):
        setting=jLB.Json()
        setting.setPath(path)
        setting.setFile(file)
        setting.setExtension(extension)
        setting_dict=setting.read()
        return setting_dict

    def exportJson_edit_func(self,path,file,extension,write):
        setting=jLB.Json()
        setting.setPath(path)
        setting.setFile(file)
        setting.setExtension(extension)
        setting.setWriteDict(write)
        setting.write()

    #Private Function
    def _replaceListWithUI_edit_func(self,setting_dict):
        meters_QAbstractButton=self.meters_QButtonGroup.button(setting_dict["metersID"])
        meters_QAbstractButton.setChecked(True)
        
        direction_QAbstractButton=self.direction_QButtonGroup.button(setting_dict["directionID"])
        direction_QAbstractButton.setChecked(True)
        
        self.snapTranslate_QCheckBox.setChecked(setting_dict["snapTranslate"])
        self.snapRotate_QCheckBox.setChecked(setting_dict["snapRotate"])
        self.snapParent_QCheckBox.setChecked(setting_dict["snapParent"])
        
        self.setTranslate_QCheckBox.setChecked(setting_dict["setTranslate"])
        self.translateX_QDoubleSpinBox.setValue(setting_dict["translateX"])
        self.translateY_QDoubleSpinBox.setValue(setting_dict["translateY"])
        self.translateZ_QDoubleSpinBox.setValue(setting_dict["translateZ"])

        self.setRotate_QCheckBox.setChecked(setting_dict["setRotate"])
        self.rotateX_QDoubleSpinBox.setValue(setting_dict["rotateX"])
        self.rotateY_QDoubleSpinBox.setValue(setting_dict["rotateY"])
        self.rotateZ_QDoubleSpinBox.setValue(setting_dict["rotateZ"])

        self.setScale_QCheckBox.setChecked(setting_dict["setScale"])
        self.scaleX_QDoubleSpinBox.setValue(setting_dict["scaleX"])
        self.scaleY_QDoubleSpinBox.setValue(setting_dict["scaleY"])
        self.scaleZ_QDoubleSpinBox.setValue(setting_dict["scaleZ"])

    def _replaceUIWithList_query_list(self):
        meters_int=self.meters_QButtonGroup.checkedId()

        direction_int=self.direction_QButtonGroup.checkedId()
        
        snapTranslate_bool=self.snapTranslate_QCheckBox.isChecked()
        snapRotate_bool=self.snapRotate_QCheckBox.isChecked()
        snapParent_bool=self.snapParent_QCheckBox.isChecked()
        
        setTranslate_bool=self.setTranslate_QCheckBox.isChecked()
        translateX_double=self.translateX_QDoubleSpinBox.value()
        translateY_double=self.translateY_QDoubleSpinBox.value()
        translateZ_double=self.translateZ_QDoubleSpinBox.value()

        setRotate_bool=self.setRotate_QCheckBox.isChecked()
        rotateX_double=self.rotateX_QDoubleSpinBox.value()
        rotateY_double=self.rotateY_QDoubleSpinBox.value()
        rotateZ_double=self.rotateZ_QDoubleSpinBox.value()

        setScale_bool=self.setScale_QCheckBox.isChecked()
        scaleX_double=self.scaleX_QDoubleSpinBox.value()
        scaleY_double=self.scaleY_QDoubleSpinBox.value()
        scaleZ_double=self.scaleZ_QDoubleSpinBox.value()

        write_dict={
            "metersID":meters_int,
            "directionID":direction_int,
            "snapTranslate":snapTranslate_bool,
            "snapRotate":snapRotate_bool,
            "snapParent":snapParent_bool,
            "setTranslate":setTranslate_bool,
            "translateX":translateX_double,
            "translateY":translateY_double,
            "translateZ":translateZ_double,
            "setRotate":setRotate_bool,
            "rotateX":rotateX_double,
            "rotateY":rotateY_double,
            "rotateZ":rotateZ_double,
            "setScale":setScale_bool,
            "scaleX":scaleX_double,
            "scaleY":scaleY_double,
            "scaleZ":scaleZ_double,
            }
        return write_dict

    #Public Function
    def __importJson(self,path,file,extension="json"):
        setting_dict=self.importJson_query_dict(path,file,extension)
        self._replaceListWithUI_edit_func(setting_dict)

    def __exportJson(self,path,file,extension="json"):
        write_dict=self._replaceUIWithList_query_list()
        self.exportJson_edit_func(path,file,extension,write_dict)

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