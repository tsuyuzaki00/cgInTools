# -*- coding: iso-8859-15 -*-

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance

import cgInTools as cit
from cgInTools.ui import geometryCornerEdgeUI as UI
from cgInTools.maya.library import jsonLB as jLB
from cgInTools.maya.execute import geometryCornerEdgeEX as ex
cit.verReload(UI)

class ObjCornerEdgeOP(UI.ObjCornerEdgeOPBase):
    def __init__(self,*args,**kwargs):
        super(ObjCornerEdgeOP,self).__init__(*args, **kwargs)
        self.setPath=cit.mayaData_path
        self.resetPath=cit.mayaSettings_path
        self.fileName="geometryCornerEdge"

        self.__importJson(self.setPath,self.fileName)

    def buttonLeft_onClicked_func(self):
        self.__exportJson(self.setPath,self.fileName)
        ex.main()
        self.close()

    def buttonCenter_onClicked_func(self):
        self.__exportJson(self.setPath,self.fileName)
        ex.main()

    def buttonRight_onClicked_func(self):
        self.close()

    def refresh_onClicked_func(self):
        self.__importJson(self.resetPath,self.fileName)

    def restore_onClicked_func(self):
        self.__importJson(self.setPath,self.fileName)

    def save_onClicked_func(self):
        self.__exportJson(self.setPath,self.fileName)

    def import_onClicked_func(self):
        print("base")

    def export_onClicked_func(self):
        print("base")

    def __exportJson(self,path,file):
        lowAngle_int=self.lowAngle_QSpinBox.value()
        highAngle_int=self.highAngle_QSpinBox.value()
        self.exportJson_edit_func(path,file,lowAngle_int,highAngle_int)

    def __importJson(self,path,file):
        settings_dict=self.importJson_query_dict(path,file)
        self.lowAngle_QSpinBox.setValue(settings_dict["lowAngle"])
        self.highAngle_QSpinBox.setValue(settings_dict["highAngle"])

    def exportJson_edit_func(self,path,file,lowAngle,highAngle):
        write_dict={
        "lowAngle":lowAngle,
        "highAngle":highAngle
        }
        setting=jLB.Json()
        setting.setPath(path)
        setting.setFile(file)
        setting.setWriteDict(write_dict)
        setting.write()

    def importJson_query_dict(self,path,file):
        setting=jLB.Json()
        setting.setPath(path)
        setting.setFile(file)
        settings_dict=setting.read()
        return settings_dict

def get_maya_main_window():
    omui.MQtUtil.mainWindow()
    ptr=omui.MQtUtil.mainWindow()
    widget=wrapInstance(int(ptr), QWidget)
    return widget

def main():
    maya_window_instance=ObjCornerEdgeOP(parent=get_maya_main_window())
    maya_window_instance.show()
