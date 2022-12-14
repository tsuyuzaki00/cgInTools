from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from ._reference import dockWindowUI as UI

class PaintWeightWindowBase(UI.DockWindowBase):
    def __init__(self,*args,**kwargs):
        super(PaintWeightWindowBase,self).__init__(*args,**kwargs)
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle("skinValueWindow")

        main_QVBoxLayout=QVBoxLayout(self)
        self.custom_QGridLayout.addLayout(main_QVBoxLayout,0,0)

        artAttr_QHBoxLayout=QHBoxLayout(self)
        main_QVBoxLayout.addLayout(artAttr_QHBoxLayout)

        self.radioGrp_QButtonGroup=QButtonGroup()

        context_QRadioButton=QRadioButton("Context",self)
        self.radioGrp_QButtonGroup.addButton(context_QRadioButton,0)
        artAttr_QHBoxLayout.addWidget(context_QRadioButton)

        skinContext_QRadioButton=QRadioButton("SkinContext",self)
        skinContext_QRadioButton.setChecked(True)
        self.radioGrp_QButtonGroup.addButton(skinContext_QRadioButton,1)
        artAttr_QHBoxLayout.addWidget(skinContext_QRadioButton)

        blendShapeContext_QRadioButton=QRadioButton("BlendShapeContext",self)
        self.radioGrp_QButtonGroup.addButton(blendShapeContext_QRadioButton,2)
        artAttr_QHBoxLayout.addWidget(blendShapeContext_QRadioButton)

        value_QHBoxLayout=QHBoxLayout(self)
        main_QVBoxLayout.addLayout(value_QHBoxLayout)

        valueNum_QLabel=QLabel("ValueNum",self)
        value_QHBoxLayout.addWidget(valueNum_QLabel,True)

        button0_QPushButton=QPushButton("0")
        button0_QPushButton.setStyleSheet('color: cyan;')
        button0_QPushButton.clicked.connect(self.button0OnClicked)
        value_QHBoxLayout.addWidget(button0_QPushButton,True)

        button0001_QPushButton=QPushButton("0.001")
        button0001_QPushButton.setStyleSheet('color: pink;')
        button0001_QPushButton.clicked.connect(self.button0001OnClicked)
        value_QHBoxLayout.addWidget(button0001_QPushButton,True)

        button001_QPushButton=QPushButton("0.01")
        button001_QPushButton.setStyleSheet('color: pink;')
        button001_QPushButton.clicked.connect(self.button001OnClicked)
        value_QHBoxLayout.addWidget(button001_QPushButton,True)

        button005_QPushButton=QPushButton("0.05")
        button005_QPushButton.setStyleSheet('color: pink;')
        button005_QPushButton.clicked.connect(self.button005OnClicked)
        value_QHBoxLayout.addWidget(button005_QPushButton,True)
        
        button01_QPushButton=QPushButton("0.1")
        button01_QPushButton.setStyleSheet('color: pink;')
        button01_QPushButton.clicked.connect(self.button01OnClicked)
        value_QHBoxLayout.addWidget(button01_QPushButton,True)
        
        button05_QPushButton=QPushButton("0.5")
        button05_QPushButton.setStyleSheet('color: yellow;')
        button05_QPushButton.clicked.connect(self.button05OnClicked)
        value_QHBoxLayout.addWidget(button05_QPushButton,True)
        
        button1_QPushButton=QPushButton("1")
        button1_QPushButton.setStyleSheet('color: yellow;')
        button1_QPushButton.clicked.connect(self.button1OnClicked)
        value_QHBoxLayout.addWidget(button1_QPushButton,True)

    def button0OnClicked(self):
        print("button0")
    def button0001OnClicked(self):
        print("button0001")
    def button001OnClicked(self):
        print("button001")
    def button005OnClicked(self):
        print("button005")
    def button01OnClicked(self):
        print("button01")
    def button05OnClicked(self):
        print("button05")
    def button1OnClicked(self):
        print("button1")

#viewWindow=PaintWeightWindowBase()
#viewWindow.show()