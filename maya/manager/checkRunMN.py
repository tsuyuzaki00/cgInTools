# -*- coding: iso-8859-15 -*-

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import cgInTools as cit
from ...ui._reference import mainWindowUI as UI
from ...ui import checkRunUI as wUI
from ..library import windowLB as wLB
from ...library import jsonLB as jLB
cit.reloads([UI,wLB,jLB])

PATHSET=cit.mayaData_dir
PATHRESET=cit.mayaSettings_dir
FILE="checkRun"

class CheckRunWindow(UI.MainWindowBase):
    def __init__(self,*args,**kwargs):
        super(CheckRunWindow,self).__init__(*args,**kwargs)
        self._pathSet=PATHSET
        self._pathReset=PATHRESET
        self._file=FILE
        self._widgets=[]
        self.__importUI()

        self.setObjectName("checkRun")
        self.setWindowTitle("checkRun")
        self.buttonLeft_QPushButton.setText("check run")
        self.buttonCenter_QPushButton.setText("all run")
        self.buttonRight_QPushButton.setText("check off")

        main_QVBoxLayout=QVBoxLayout(self)
        self.custom_QGridLayout.addLayout(main_QVBoxLayout,0,0)

        settings_dict=self.importJson_query_dict(self._pathSet,self._file)
        for checkRun_dict in settings_dict["checkRun_dicts"]:
            check_QWidget=wUI.CheckRunWidget()
            check_QWidget.setLabel(checkRun_dict["label"])
            check_QWidget.setFromFolder(checkRun_dict["fromFolder"])
            check_QWidget.setImportFile(checkRun_dict["importFile"])
            check_QWidget.setFunction(checkRun_dict["function"])
            check_QWidget.setup()
            main_QVBoxLayout.addWidget(check_QWidget)
            self._widgets.append(check_QWidget)

    #Single Function
    def importJson_query_dict(self,path,file):
        setting=jLB.Json()
        setting.setDirectory(path)
        setting.setFile(file)
        settings_dict=setting.read()
        return settings_dict

    #Private Function

    #Summary Function
    def __importUI(self):
        pass

    #Public Function
    def refreshOnClicked(self):
        pass
        #self.__importJson(self._pathReset,self._file)

    def restoreOnClicked(self):
        pass
        #self.__importJson(self._pathSet,self._file)

    def saveOnClicked(self):
        pass
        #self.__exportJson(self._pathSet,self._file)

    def importOnClicked(self):
        pass
        #path,file=wLB.mayaFileDialog_query_path_file("import setting",1)
        #self.__importJson(path,file)

    def exportOnClicked(self):
        pass
        #path,file=wLB.mayaFileDialog_query_path_file("export setting",0)
        #elf.__exportJson(path,file)

    def buttonLeftOnClicked(self):
        for _widget in self._widgets:
            if _widget.runCheck_QCheckBox.isChecked():
                _widget.execution()

    def buttonCenterOnClicked(self):
        for _widget in self._widgets:
            _widget.execution()

    def buttonRightOnClicked(self):
        for _widget in self._widgets:
            _widget.runCheck_QCheckBox.setChecked(False)

def main():
    viewWindow=CheckRunWindow(parent=wLB.mayaMainWindow_query_QWidget())
    viewWindow.show()
