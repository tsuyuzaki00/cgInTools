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

PATHSET=cit.mayaData_dir
PATHRESET=cit.mayaSettings_dir
FILE="geometryCornerEdge"
class ObjCornerEdgeOP(UI.ObjCornerEdgeOPBase):
    def __init__(self,*args,**kwargs):
        super(ObjCornerEdgeOP,self).__init__(*args, **kwargs)
        self._pathSet=PATHSET
        self._pathReset=PATHRESET
        self._file=FILE
        self.__importJson(self._pathSet,self._file)

    #Single Function
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

    #Private Function
    def __replaceListWithUI_edit_func(self,settings_dict):
        self.lowAngle_QSpinBox.setValue(settings_dict["lowAngle"])
        self.highAngle_QSpinBox.setValue(settings_dict["highAngle"])

    def __replaceCheckBox_query_int_int(self):
        lowAngle_int=self.lowAngle_QSpinBox.value()
        highAngle_int=self.highAngle_QSpinBox.value()
        return lowAngle_int,highAngle_int

    #Summary Function
    def __importJson(self,path,file):
        settings_dict=self.importJson_query_dict(path,file)
        self.__replaceListWithUI_edit_func(settings_dict)

    def __exportJson(self,path,file):
        lowAngle,highAngle=self.__replaceCheckBox_query_int_int()
        self.exportJson_edit_func(path,file,lowAngle,highAngle)

    #Public Function
    def refreshOnClicked(self):
        self.__importJson(self._pathReset,self._file)

    def restoreOnClicked(self):
        self.__importJson(self._pathSet,self._file)

    def saveOnClicked(self):
        self.__exportJson(self._pathSet,self._file)

    def importOnClicked(self):
        path,file=wLB.mayaFileDialog_query_path_file("import setting",1)
        self.__importJson(path,file)

    def exportOnClicked(self):
        path,file=wLB.mayaFileDialog_query_path_file("export setting",0)
        self.__exportJson(path,file)

    def buttonLeftOnClicked(self):
        self.__exportJson(self._pathSet,self._file)
        EX.main()
        self.close()

    def buttonCenterOnClicked(self):
        self.__exportJson(self._pathSet,self._file)
        EX.main()

    def buttonRightOnClicked(self):
        self.close()

def main():
    viewWindow=ObjCornerEdgeOP(parent=wLB.mayaMainWindow_query_widget())
    viewWindow.show()
