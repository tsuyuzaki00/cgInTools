#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from ._reference import mainWindowUI as UI

planeCtrls=[
    "circlePlane",
    "circleSmooth",
    "circlePlaneHalf",
    "trianglePlane",
    "featherPlane",
    "featherSmooth",
    "squarePlane",
    "squareSmooth",
    "crossPlane",
    "crossSmooth",
    "pentagonPlane",
    "hexagonPlane",
    "starPlane",
    "starSmooth",
    "pinPlane",
    "antennaPlane"
    ]
solidCtrls=[
    "cubeSolid",
    "ballSolid",
    "ballSmooth",
    "ballSolidHalf",
    "hexagonSolid",
    "octagonSolid",
    "diamondSolid",
    "pyramidSolid",
    "coneSolid",
    "pinSolid",
    "antennaSolid",
    "circleCurve"
    ]
arrowCtrls=[
    "singleArrow",
    "doubleArrow",
    "fourArrow",
    "smoothFour",
    "rightAngleArrow",
    "rotArrow",
    "archArrow",
    "ballArrow",
    "solidArrow",
    "solidFour"
    ]
otherCtrls=[
    "cog",
    "thorns",
    "sun",
    "gear",
    "lens"
    ]

class SelectSetCtrlWindowBase(UI.MainWindowBase):
    def __init__(self,*args,**kwargs):
        super(SelectSetCtrlWindowBase,self).__init__(*args,**kwargs)
        self.setWindowFlags(Qt.Window)
        self.setObjectName("ctrlCurves")
        self.setWindowTitle("ctrlCurvesOption")
        self.buttonLeft_QPushButton.setText("run")
        self.buttonCenter_QPushButton.setText("replace")
        self.buttonRight_QPushButton.setText("delete")

        main_QVBoxLayout=QVBoxLayout(self)
        self.custom_QGridLayout.addLayout(main_QVBoxLayout,0,0)

        unitSet_QLabel=QLabel("unit Setting",self)
        main_QVBoxLayout.addWidget(unitSet_QLabel)

        meters_QHBoxLayout=QHBoxLayout(self)
        main_QVBoxLayout.addLayout(meters_QHBoxLayout)

        self.meters_QButtonGroup=QButtonGroup(self)

        meter_QRadioButton=QRadioButton("m")
        meter_QRadioButton.setChecked(True)
        meters_QHBoxLayout.addWidget(meter_QRadioButton)
        self.meters_QButtonGroup.addButton(meter_QRadioButton,2)

        centimeter_QRadioButton=QRadioButton("cm")
        meters_QHBoxLayout.addWidget(centimeter_QRadioButton)
        self.meters_QButtonGroup.addButton(centimeter_QRadioButton,1)
        
        millimeter_QRadioButton=QRadioButton("mm")
        meters_QHBoxLayout.addWidget(millimeter_QRadioButton)
        self.meters_QButtonGroup.addButton(millimeter_QRadioButton,0)

        meters_QFrame=QFrame(self)
        meters_QFrame.setFrameShape(QFrame.HLine)
        meters_QFrame.setFrameShadow(QFrame.Sunken)
        main_QVBoxLayout.addWidget(meters_QFrame)

        direction_QGridLayout=QGridLayout(self)
        main_QVBoxLayout.addLayout(direction_QGridLayout)

        direction_QLabel=QLabel("Direction:",self)
        direction_QGridLayout.addWidget(direction_QLabel,0,0)

        self.direction_QButtonGroup=QButtonGroup()

        plusX_QRadioButton=QRadioButton("+X",self)
        plusX_QRadioButton.setChecked(True)
        self.direction_QButtonGroup.addButton(plusX_QRadioButton,0)
        direction_QGridLayout.addWidget(plusX_QRadioButton,0,1)

        plusY_QRadioButton=QRadioButton("+Y",self)
        self.direction_QButtonGroup.addButton(plusY_QRadioButton,1)
        direction_QGridLayout.addWidget(plusY_QRadioButton,0,2)

        plusZ_QRadioButton=QRadioButton("+Z",self)
        self.direction_QButtonGroup.addButton(plusZ_QRadioButton,2)
        direction_QGridLayout.addWidget(plusZ_QRadioButton,0,3)
        
        minusX_QRadioButton=QRadioButton("-X",self)
        self.direction_QButtonGroup.addButton(minusX_QRadioButton,3)
        direction_QGridLayout.addWidget(minusX_QRadioButton,1,1)
        
        minusY_QRadioButton=QRadioButton("-Y",self)
        self.direction_QButtonGroup.addButton(minusY_QRadioButton,4)
        direction_QGridLayout.addWidget(minusY_QRadioButton,1,2)
        
        minusZ_QRadioButton=QRadioButton("-Z",self)
        self.direction_QButtonGroup.addButton(minusZ_QRadioButton,5)
        direction_QGridLayout.addWidget(minusZ_QRadioButton,1,3)

        direction_QFrame=QFrame(self)
        direction_QFrame.setFrameShape(QFrame.HLine)
        direction_QFrame.setFrameShadow(QFrame.Raised)
        main_QVBoxLayout.addWidget(direction_QFrame)

        snap_QLabel=QLabel("snap",self)
        main_QVBoxLayout.addWidget(snap_QLabel)

        snap_QVBoxLayout=QVBoxLayout(self)
        main_QVBoxLayout.addLayout(snap_QVBoxLayout)
        
        self.snapTranslate_QCheckBox=QCheckBox("snapTranslate",self)
        snap_QVBoxLayout.addWidget(self.snapTranslate_QCheckBox)

        self.snapRotate_QCheckBox=QCheckBox("snapRotate",self)
        snap_QVBoxLayout.addWidget(self.snapRotate_QCheckBox)
        
        self.snapParent_QCheckBox=QCheckBox("snapParent",self)
        snap_QVBoxLayout.addWidget(self.snapParent_QCheckBox)

        snap_QFrame=QFrame(self)
        snap_QFrame.setFrameShape(QFrame.HLine)
        snap_QFrame.setFrameShadow(QFrame.Plain)
        main_QVBoxLayout.addWidget(snap_QFrame)

        setTransform_QVBoxLayout=QVBoxLayout(self)
        main_QVBoxLayout.addLayout(setTransform_QVBoxLayout)

        self.setTranslate_QCheckBox=QCheckBox("setTranslate",self)
        setTransform_QVBoxLayout.addWidget(self.setTranslate_QCheckBox)

        setTranslate_QHBoxLayout=QHBoxLayout(self)
        setTransform_QVBoxLayout.addLayout(setTranslate_QHBoxLayout)
        
        self.translateX_QDoubleSpinBox=QDoubleSpinBox(self)
        self.translateX_QDoubleSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.translateX_QDoubleSpinBox.setValue(0)
        self.translateX_QDoubleSpinBox.setRange(-100,100)
        self.translateX_QDoubleSpinBox.setEnabled(False)
        self.setTranslate_QCheckBox.stateChanged.connect(self.translateX_QDoubleSpinBox.setEnabled)
        setTranslate_QHBoxLayout.addWidget(self.translateX_QDoubleSpinBox)
        
        self.translateY_QDoubleSpinBox=QDoubleSpinBox(self)
        self.translateY_QDoubleSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.translateY_QDoubleSpinBox.setValue(0)
        self.translateY_QDoubleSpinBox.setRange(-100,100)
        self.translateY_QDoubleSpinBox.setEnabled(False)
        self.setTranslate_QCheckBox.stateChanged.connect(self.translateY_QDoubleSpinBox.setEnabled)
        setTranslate_QHBoxLayout.addWidget(self.translateY_QDoubleSpinBox)
        
        self.translateZ_QDoubleSpinBox=QDoubleSpinBox(self)
        self.translateZ_QDoubleSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.translateZ_QDoubleSpinBox.setValue(0)
        self.translateZ_QDoubleSpinBox.setRange(-100,100)
        self.translateZ_QDoubleSpinBox.setEnabled(False)
        self.setTranslate_QCheckBox.stateChanged.connect(self.translateZ_QDoubleSpinBox.setEnabled)
        setTranslate_QHBoxLayout.addWidget(self.translateZ_QDoubleSpinBox)

        self.setRotate_QCheckBox=QCheckBox("setRotate",self)
        setTransform_QVBoxLayout.addWidget(self.setRotate_QCheckBox)

        setRotate_QHBoxLayout=QHBoxLayout(self)
        setTransform_QVBoxLayout.addLayout(setRotate_QHBoxLayout)
        
        self.rotateX_QDoubleSpinBox=QDoubleSpinBox(self)
        self.rotateX_QDoubleSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.rotateX_QDoubleSpinBox.setValue(0)
        self.rotateX_QDoubleSpinBox.setRange(-360,360)
        self.rotateX_QDoubleSpinBox.setEnabled(False)
        self.setRotate_QCheckBox.stateChanged.connect(self.rotateX_QDoubleSpinBox.setEnabled)
        setRotate_QHBoxLayout.addWidget(self.rotateX_QDoubleSpinBox)
        
        self.rotateY_QDoubleSpinBox=QDoubleSpinBox(self)
        self.rotateY_QDoubleSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.rotateY_QDoubleSpinBox.setValue(0)
        self.rotateY_QDoubleSpinBox.setRange(-360,360)
        self.rotateY_QDoubleSpinBox.setEnabled(False)
        self.setRotate_QCheckBox.stateChanged.connect(self.rotateY_QDoubleSpinBox.setEnabled)
        setRotate_QHBoxLayout.addWidget(self.rotateY_QDoubleSpinBox)
        
        self.rotateZ_QDoubleSpinBox=QDoubleSpinBox(self)
        self.rotateZ_QDoubleSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.rotateZ_QDoubleSpinBox.setValue(0)
        self.rotateZ_QDoubleSpinBox.setRange(-360,360)
        self.rotateZ_QDoubleSpinBox.setEnabled(False)
        self.setRotate_QCheckBox.stateChanged.connect(self.rotateZ_QDoubleSpinBox.setEnabled)
        setRotate_QHBoxLayout.addWidget(self.rotateZ_QDoubleSpinBox)

        self.setScale_QCheckBox=QCheckBox("setScale",self)
        setTransform_QVBoxLayout.addWidget(self.setScale_QCheckBox)

        setScale_QHBoxLayout=QHBoxLayout(self)
        setTransform_QVBoxLayout.addLayout(setScale_QHBoxLayout)
        
        self.scaleX_QDoubleSpinBox=QDoubleSpinBox(self)
        self.scaleX_QDoubleSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.scaleX_QDoubleSpinBox.setValue(1)
        self.scaleX_QDoubleSpinBox.setRange(0,100)
        self.scaleX_QDoubleSpinBox.setEnabled(False)
        self.setScale_QCheckBox.stateChanged.connect(self.scaleX_QDoubleSpinBox.setEnabled)
        setScale_QHBoxLayout.addWidget(self.scaleX_QDoubleSpinBox)
        
        self.scaleY_QDoubleSpinBox=QDoubleSpinBox(self)
        self.scaleY_QDoubleSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.scaleY_QDoubleSpinBox.setValue(1)
        self.scaleY_QDoubleSpinBox.setRange(0,100)
        self.scaleY_QDoubleSpinBox.setEnabled(False)
        self.setScale_QCheckBox.stateChanged.connect(self.scaleY_QDoubleSpinBox.setEnabled)
        setScale_QHBoxLayout.addWidget(self.scaleY_QDoubleSpinBox)
        
        self.scaleZ_QDoubleSpinBox=QDoubleSpinBox(self)
        self.scaleZ_QDoubleSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.scaleZ_QDoubleSpinBox.setValue(1)
        self.scaleZ_QDoubleSpinBox.setRange(0,100)
        self.scaleZ_QDoubleSpinBox.setEnabled(False)
        self.setScale_QCheckBox.stateChanged.connect(self.scaleZ_QDoubleSpinBox.setEnabled)
        setScale_QHBoxLayout.addWidget(self.scaleZ_QDoubleSpinBox)

        setTransform_QFrame=QFrame(self)
        setTransform_QFrame.setFrameShape(QFrame.HLine)
        setTransform_QFrame.setFrameShadow(QFrame.Plain)
        main_QVBoxLayout.addWidget(setTransform_QFrame)
        
        self.ctrl_QTabWidget=QTabWidget(self)
        main_QVBoxLayout.addWidget(self.ctrl_QTabWidget)

        planeCtrl_QListWidget=QListWidget(self)
        planeCtrl_QListWidget.addItems(planeCtrls)
        self.ctrl_QTabWidget.addTab(planeCtrl_QListWidget,"Plane")

        solidCtrl_QListWidget=QListWidget(self)
        solidCtrl_QListWidget.addItems(solidCtrls)
        self.ctrl_QTabWidget.addTab(solidCtrl_QListWidget,"Solid")

        arrowCtrl_QListWidget=QListWidget(self)
        arrowCtrl_QListWidget.addItems(arrowCtrls)
        self.ctrl_QTabWidget.addTab(arrowCtrl_QListWidget,"Arrow")
        
        otherCtrl_QListWidget=QListWidget(self)
        otherCtrl_QListWidget.addItems(otherCtrls)
        self.ctrl_QTabWidget.addTab(otherCtrl_QListWidget,"Other")

#viewWindow=SelectSetCtrlWindowBase()
#viewWindow.show()