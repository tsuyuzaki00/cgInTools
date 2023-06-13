from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from cgInTools.ui._reference import mainWindowUI as UI
import os

class CheckRunWindow(UI.MainWindowBase):
    def __init__(self,*args,**kwargs):
        super(CheckRunWindow,self).__init__(*args,**kwargs)

class CheckRunWidget(QWidget):
    def __init__(self,*args,**kwargs):
        super(CheckRunWidget,self).__init__(*args, **kwargs)
        self._label_str=None
        self._fromFolder_str=None
        self._importFile_str=None
        self._function_str=None
        
    def setLabel(self,variable):
        self._label_str=variable
    def getLabel(self):
        return self._label_str

    def setFromFolder(self,variable):
        self._fromFolder_str=variable
    def getFromFolder(self):
        return self._fromFolder_str

    def setImportFile(self,variable):
        self._importFile_str=variable
    def getImportFile(self):
        return self._importFile_str

    def setFunction(self,variable):
        self._function_str=variable
    def getFunction(self):
        return self._function_str

    def execution(self):
        exec("import cgInTools as cit; from "+self._fromFolder_str+" import "+self._importFile_str+" as ps; cit.reloads([ps]); ps."+self._function_str)

    def runButtonOnClicked(self):
        self.execution()

    def settingButtonOnClicked(self):
        pathFolder=self._fromFolder_str.replace(".","/")
        filePath="/".join([pathFolder,self._importFile_str])
        print(filePath)
        #os.startfile()

    def setup(self):
        layout_QHBoxLayout=QHBoxLayout()

        self.runCheck_QCheckBox=QCheckBox()
        layout_QHBoxLayout.addWidget(self.runCheck_QCheckBox,alignment=Qt.AlignLeft)
        
        name_QLabel=QLabel(self._label_str)
        layout_QHBoxLayout.addWidget(name_QLabel,alignment=Qt.AlignLeft)
        
        name_QPushButton=QPushButton("run")
        name_QPushButton.clicked.connect(self.runButtonOnClicked)
        layout_QHBoxLayout.addWidget(name_QPushButton,alignment=Qt.AlignLeft)
        
        setting_QPushButton=QPushButton("setting")
        setting_QPushButton.clicked.connect(self.settingButtonOnClicked)
        layout_QHBoxLayout.addWidget(setting_QPushButton,alignment=Qt.AlignLeft)

        self.setLayout(layout_QHBoxLayout)
