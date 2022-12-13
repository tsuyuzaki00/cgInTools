from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import cgInTools as cit
from ui._reference import mainWindowUI as UI
cit.reloads([UI])

class AutoRenameOPBase(UI.MainWindowBase):
    def __init__(self,*args,**kwargs):
        super(AutoRenameOPBase,self).__init__(*args, **kwargs)
        self.setObjectName("autoRename")
        self.setWindowTitle("autoRenameOption")
        self.buttonLeft_QPushButton.setText("run")
        self.buttonCenter_QPushButton.setText("apply")
        self.buttonRight_QPushButton.setText("close")

        self.name01_QComboBox=QComboBox()
        self.name01_QComboBox.addItems(["title","node","side","titleNum","nodeNum","sideNum","titleHie","scene"])
        self.custom_QGridLayout.addWidget(self.name01_QComboBox,0,0)

        self.name02_QComboBox=QComboBox()
        self.name02_QComboBox.addItems(["none","title","node","side","num","titleNum","nodeNum","sideNum","titleHie","scene"])
        self.custom_QGridLayout.addWidget(self.name02_QComboBox,0,1)

        self.name03_QComboBox=QComboBox()
        self.name03_QComboBox.addItems(["none","title","node","side","num","titleNum","nodeNum","sideNum","titleHie","scene"])
        self.custom_QGridLayout.addWidget(self.name03_QComboBox,0,2)

        self.name04_QComboBox=QComboBox()
        self.name04_QComboBox.addItems(["none","title","node","side","num","titleNum","nodeNum","sideNum","titleHie","scene"])
        self.custom_QGridLayout.addWidget(self.name04_QComboBox,0,3)

        self.name05_QComboBox=QComboBox()
        self.name05_QComboBox.addItems(["none","title","node","side","num","titleNum","nodeNum","sideNum","titleHie","scene"])
        self.custom_QGridLayout.addWidget(self.name05_QComboBox,0,4)

#viewWindow=AutoRenameOPBase()
#viewWindow.show()