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

OPTIONSET_DICT=jLB.getJson(PATHSET,FILE)
OPTIONRESET_DICT=jLB.getJson(PATHRESET,FILE)

class AutoRenameOP(UI.AutoRenameOPBase):
    def __init__(self,*args,**kwargs):
        super(AutoRenameOP,self).__init__(*args,**kwargs)
        self._path=PATHSET
        self._file=FILE
        self._setOption_dict=OPTIONSET_DICT
        self._resetOption_dict=OPTIONRESET_DICT
        self.__importJson()

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

    #Private Function
    def _replaceListWithUI_edit_func(self,settings_dict):
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

    def _modeSwitch_query_str(self):
        modeSwitch=self.radioGrp_QButtonGroup.checkedButton().text()
        return modeSwitch
    
    def _lineText_query_dict(self):
        custom=self.custom_QLineEdit.text()
        title=self.title_QLineEdit.text()
        node=self.node_QLineEdit.text()
        side=self.side_QLineEdit.text()
        lineText_dict={"custom":custom,"title":title,"node":node,"side":side}
        return lineText_dict

    def _replaceComboBox_query_list(self):
        name01=self.name01_QComboBox.currentText()
        name02=self.name02_QComboBox.currentText()
        name03=self.name03_QComboBox.currentText()
        name04=self.name04_QComboBox.currentText()
        name05=self.name05_QComboBox.currentText()
        order_list=[name01,name02,name03,name04,name05]
        return order_list

    #Public Function
    def __importJson(self):
        self._replaceListWithUI_edit_func(self._setOption_dict)

    def __exportJson(self):
        switch=self._modeSwitch_query_str()
        lineText_dict=self._lineText_query_dict()
        order_list=self._replaceComboBox_query_list()
        self.exportJson_edit_func(self._path,self._file,switch,lineText_dict["custom"],lineText_dict["title"],lineText_dict["node"],lineText_dict["side"],order_list)
    
    def refreshOnClicked(self):
        self.__importJson()

    def restoreOnClicked(self):
        self.__importJson()

    def saveOnClicked(self):
        self.__exportJson()

    def importOnClicked(self):
        self._path,self._file=wLB.mayaFileDialog_query_path_file("import setting",1)
        self.__importJson()

    def exportOnClicked(self):
        self._path,self._file=wLB.mayaFileDialog_query_path_file("export setting",0)
        self.__exportJson()

    def buttonLeftOnClicked(self):
        self.__exportJson()
        EX.main()
        self.close()

    def buttonCenterOnClicked(self):
        self.__exportJson()
        EX.main()

    def buttonRightOnClicked(self):
        self.close()

def main():
    viewWindow=AutoRenameOP(parent=wLB.mayaMainWindow_query_widget())
    viewWindow.show()
