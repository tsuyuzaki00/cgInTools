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

class AutoRenameOP(UI.AutoRenameOPBase):
    def __init__(self,*args,**kwargs):
        super(AutoRenameOP,self).__init__(*args, **kwargs)
        self.setPath=cit.mayaData_path
        self.resetPath=cit.mayaSettings_path
        self.fileName="autoRename"

        self.__importJson(self.setPath,self.fileName)

    #Single Function
    def exportJson_edit_func(self,path,file,orders,switch,custom,node,side):
        write_dict={
            "modeSwitch":switch,
            "customText":custom,
            "nodeText":node,
            "sideText":side,
            "nameOrders":orders
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
    def _replaceListWithUI_edit_func(self,settings_dict):
        naming_list=settings_dict["nameOrders"]
        switch_str=settings_dict["modeSwitch"]
        custom_str=settings_dict["customText"]
        node_str=settings_dict["nodeText"]
        side_str=settings_dict["sideText"]
        self.name01_QComboBox.setCurrentText(naming_list[0])
        self.name02_QComboBox.setCurrentText(naming_list[1])
        self.name03_QComboBox.setCurrentText(naming_list[2])
        self.name04_QComboBox.setCurrentText(naming_list[3])
        self.name05_QComboBox.setCurrentText(naming_list[4])
        self.custom_QLineEdit.setText(custom_str)
        self.node_QLineEdit.setText(node_str)
        self.side_QLineEdit.setText(side_str)
        if switch_str == "fullAuto":
            self.fullAuto_QRadioButton.setChecked(True)
        elif switch_str == "setAuto":
            self.setAuto_QRadioButton.setChecked(True)
        elif switch_str == "markAuto":
            self.mark_QRadioButton.setChecked(True)
        else:
            self.fullAuto_QRadioButton.setChecked(True)
    
    def __importJson(self,path,file):
        settings_dict=self.importJson_query_dict(path,file)
        self._replaceListWithUI_edit_func(settings_dict)

    def _replaceUIWithList_query_list(self):
        name01=self.name01_QComboBox.currentText()
        name02=self.name02_QComboBox.currentText()
        name03=self.name03_QComboBox.currentText()
        name04=self.name04_QComboBox.currentText()
        name05=self.name05_QComboBox.currentText()
        orders=[name01,name02,name03,name04,name05]
        return orders
    
    def _modeSwitch_query_str(self):
        modeSwitch=self.radioGrp_QButtonGroup.checkedButton().text()
        return modeSwitch
    
    def _plainText_query_list(self):
        custom=self.custom_QLineEdit.text()
        node=self.node_QLineEdit.text()
        side=self.side_QLineEdit.text()
        plainText_dict={"custom":custom,"node":node,"side":side}
        return plainText_dict

    def __exportJson(self,path,file):
        orders=self._replaceUIWithList_query_list()
        switch=self._modeSwitch_query_str()
        plainText_dict=self._plainText_query_list()
        self.exportJson_edit_func(path,file,orders,switch,plainText_dict["custom"],plainText_dict["node"],plainText_dict["side"])

    #Public Function
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

def main():
    viewWindow=AutoRenameOP(parent=wLB.mayaMainWindow_query_widget())
    viewWindow.show()
