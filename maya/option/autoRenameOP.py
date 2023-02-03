# -*- coding: iso-8859-15 -*-

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import cgInTools as cit
from cgInTools.ui import autoRenameUI as UI
from ..library import windowLB as wLB
from ..library import jsonLB as jLB
from cgInTools.maya.execute import autoRenameEX as EX
cit.reloads([UI,wLB,jLB,EX])

PATHSET=cit.mayaData_dir
PATHRESET=cit.mayaSettings_dir
FILE="autoRename"

class AutoRenameOP(UI.AutoRenameOPBase):
    def __init__(self,*args,**kwargs):
        super(AutoRenameOP,self).__init__(*args,**kwargs)
        self._pathSet=PATHSET
        self._pathReset=PATHRESET
        self._file=FILE
        self.__importJson(self._pathSet,self._file)

    #Single Function
    def exportJson_edit_func(self,path,file,switch,custom,title,node,side,order_list):
        write_dict={
            "modeSwitch":switch,
            "customText":custom,
            "titleText":title,
            "nodeText":node,
            "sideText":side,
            "nameOrderList":order_list
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
        naming_list=settings_dict["nameOrderList"]
        self.name01_QComboBox.setCurrentText(naming_list[0])
        self.name02_QComboBox.setCurrentText(naming_list[1])
        self.name03_QComboBox.setCurrentText(naming_list[2])
        self.name04_QComboBox.setCurrentText(naming_list[3])
        self.name05_QComboBox.setCurrentText(naming_list[4])

        custom_str=settings_dict["customText"]
        self.custom_QLineEdit.setText(custom_str)

        title_str=settings_dict["titleText"]
        self.title_QLineEdit.setText(title_str)
        
        node_str=settings_dict["nodeText"]
        self.node_QLineEdit.setText(node_str)
        
        side_str=settings_dict["sideText"]
        self.side_QLineEdit.setText(side_str)
        
        switch_str=settings_dict["modeSwitch"]
        if switch_str == "fullAuto":
            self.fullAuto_QRadioButton.setChecked(True)
        elif switch_str == "setAuto":
            self.setAuto_QRadioButton.setChecked(True)
        elif switch_str == "markAuto":
            self.mark_QRadioButton.setChecked(True)
        else:
            self.fullAuto_QRadioButton.setChecked(True)

    def __modeSwitch_query_str(self):
        modeSwitch=self.radioGrp_QButtonGroup.checkedButton().text()
        return modeSwitch
    
    def __lineText_query_dict(self):
        custom=self.custom_QLineEdit.text()
        title=self.title_QLineEdit.text()
        node=self.node_QLineEdit.text()
        side=self.side_QLineEdit.text()
        lineText_dict={"custom":custom,"title":title,"node":node,"side":side}
        return lineText_dict

    def __replaceComboBox_query_list(self):
        name01=self.name01_QComboBox.currentText()
        name02=self.name02_QComboBox.currentText()
        name03=self.name03_QComboBox.currentText()
        name04=self.name04_QComboBox.currentText()
        name05=self.name05_QComboBox.currentText()
        order_list=[name01,name02,name03,name04,name05]
        return order_list

    #Summary Function
    def __importJson(self,path,file):
        settings_dict=self.importJson_query_dict(path,file)
        self.__replaceListWithUI_edit_func(settings_dict)

    def __exportJson(self,path,file):
        switch=self.__modeSwitch_query_str()
        lineText_dict=self.__lineText_query_dict()
        order_list=self.__replaceComboBox_query_list()
        self.exportJson_edit_func(path,file,switch,lineText_dict["custom"],lineText_dict["title"],lineText_dict["node"],lineText_dict["side"],order_list)

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
    viewWindow=AutoRenameOP(parent=wLB.mayaMainWindow_query_widget())
    viewWindow.show()
