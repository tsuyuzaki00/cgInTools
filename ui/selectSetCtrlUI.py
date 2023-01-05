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
        
        translateX_QDoubleSpinBox=QDoubleSpinBox(self)
        translateX_QDoubleSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        translateX_QDoubleSpinBox.setValue(0)
        translateX_QDoubleSpinBox.setRange(-100,100)
        translateX_QDoubleSpinBox.setEnabled(False)
        self.setTranslate_QCheckBox.stateChanged.connect(translateX_QDoubleSpinBox.setEnabled)
        setTranslate_QHBoxLayout.addWidget(translateX_QDoubleSpinBox)
        
        translateY_QDoubleSpinBox=QDoubleSpinBox(self)
        translateY_QDoubleSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        translateY_QDoubleSpinBox.setValue(0)
        translateY_QDoubleSpinBox.setRange(-100,100)
        translateY_QDoubleSpinBox.setEnabled(False)
        self.setTranslate_QCheckBox.stateChanged.connect(translateY_QDoubleSpinBox.setEnabled)
        setTranslate_QHBoxLayout.addWidget(translateY_QDoubleSpinBox)
        
        translateZ_QDoubleSpinBox=QDoubleSpinBox(self)
        translateZ_QDoubleSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        translateZ_QDoubleSpinBox.setValue(0)
        translateZ_QDoubleSpinBox.setRange(-100,100)
        translateZ_QDoubleSpinBox.setEnabled(False)
        self.setTranslate_QCheckBox.stateChanged.connect(translateZ_QDoubleSpinBox.setEnabled)
        setTranslate_QHBoxLayout.addWidget(translateZ_QDoubleSpinBox)

        self.setRotate_QCheckBox=QCheckBox("setRotate",self)
        setTransform_QVBoxLayout.addWidget(self.setRotate_QCheckBox)

        setRotate_QHBoxLayout=QHBoxLayout(self)
        setTransform_QVBoxLayout.addLayout(setRotate_QHBoxLayout)
        
        rotateX_QDoubleSpinBox=QDoubleSpinBox(self)
        rotateX_QDoubleSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        rotateX_QDoubleSpinBox.setValue(0)
        rotateX_QDoubleSpinBox.setRange(-360,360)
        rotateX_QDoubleSpinBox.setEnabled(False)
        self.setRotate_QCheckBox.stateChanged.connect(rotateX_QDoubleSpinBox.setEnabled)
        setRotate_QHBoxLayout.addWidget(rotateX_QDoubleSpinBox)
        
        rotateY_QDoubleSpinBox=QDoubleSpinBox(self)
        rotateY_QDoubleSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        rotateY_QDoubleSpinBox.setValue(0)
        rotateY_QDoubleSpinBox.setRange(-360,360)
        rotateY_QDoubleSpinBox.setEnabled(False)
        self.setRotate_QCheckBox.stateChanged.connect(rotateY_QDoubleSpinBox.setEnabled)
        setRotate_QHBoxLayout.addWidget(rotateY_QDoubleSpinBox)
        
        rotateZ_QDoubleSpinBox=QDoubleSpinBox(self)
        rotateZ_QDoubleSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        rotateZ_QDoubleSpinBox.setValue(0)
        rotateZ_QDoubleSpinBox.setRange(-360,360)
        rotateZ_QDoubleSpinBox.setEnabled(False)
        self.setRotate_QCheckBox.stateChanged.connect(rotateZ_QDoubleSpinBox.setEnabled)
        setRotate_QHBoxLayout.addWidget(rotateZ_QDoubleSpinBox)

        self.setScale_QCheckBox=QCheckBox("setScale",self)
        setTransform_QVBoxLayout.addWidget(self.setScale_QCheckBox)

        setScale_QHBoxLayout=QHBoxLayout(self)
        setTransform_QVBoxLayout.addLayout(setScale_QHBoxLayout)
        
        scaleX_QDoubleSpinBox=QDoubleSpinBox(self)
        scaleX_QDoubleSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        scaleX_QDoubleSpinBox.setValue(1)
        scaleX_QDoubleSpinBox.setRange(0,100)
        scaleX_QDoubleSpinBox.setEnabled(False)
        self.setScale_QCheckBox.stateChanged.connect(scaleX_QDoubleSpinBox.setEnabled)
        setScale_QHBoxLayout.addWidget(scaleX_QDoubleSpinBox)
        
        scaleY_QDoubleSpinBox=QDoubleSpinBox(self)
        scaleY_QDoubleSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        scaleY_QDoubleSpinBox.setValue(1)
        scaleY_QDoubleSpinBox.setRange(0,100)
        scaleY_QDoubleSpinBox.setEnabled(False)
        self.setScale_QCheckBox.stateChanged.connect(scaleY_QDoubleSpinBox.setEnabled)
        setScale_QHBoxLayout.addWidget(scaleY_QDoubleSpinBox)
        
        scaleZ_QDoubleSpinBox=QDoubleSpinBox(self)
        scaleZ_QDoubleSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        scaleZ_QDoubleSpinBox.setValue(1)
        scaleZ_QDoubleSpinBox.setRange(0,100)
        scaleZ_QDoubleSpinBox.setEnabled(False)
        self.setScale_QCheckBox.stateChanged.connect(scaleZ_QDoubleSpinBox.setEnabled)
        setScale_QHBoxLayout.addWidget(scaleZ_QDoubleSpinBox)

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