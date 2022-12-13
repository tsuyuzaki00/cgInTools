# -*- coding: iso-8859-15 -*-

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import cgInTools as cit
from cgInTools.ui import geometryCornerEdgeUI as UI
from ..library import windowLB as wLB
from ..library import jsonLB as jLB
from cgInTools.maya.execute import geometryCornerEdgeEX as EX
cit.reloads([UI,wLB,jLB,EX])

class ObjCornerEdgeOP(UI.ObjCornerEdgeOPBase):
    def __init__(self,*args,**kwargs):
        super(ObjCornerEdgeOP,self).__init__(*args, **kwargs)
        self.setPath=cit.mayaData_path
        self.resetPath=cit.mayaSettings_path
        self.fileName="geometryCornerEdge"

        self.__importJson(self.setPath,self.fileName)

    def buttonLeftOnClicked(self):
        self.__exportJson(self.setPath,self.fileName)
        EX.main()
        self.close()

    def buttonCenterOnClicked(self):
        self.__exportJson(self.setPath,self.fileName)
        EX.main()

    def buttonRightOnClicked(self):
        self.close()

    def refreshOnClicked(self):
        self.__importJson(self.resetPath,self.fileName)

    def restoreOnClicked(self):
        self.__importJson(self.setPath,self.fileName)

    def saveOnClicked(self):
        self.__exportJson(self.setPath,self.fileName)

    def importOnClicked(self):
        print("nanimonashi")

    def exportOnClicked(self):
        print("nanimonashi")

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

def main():
    viewWindow=ObjCornerEdgeOP(parent=wLB.mayaMainWindow_query_widget())
    viewWindow.show()
