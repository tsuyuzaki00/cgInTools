from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class SkinValueWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(SkinValueWindow, self).__init__(*args, **kwargs)
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle("skinValueWindow")

        main_Layout = QFormLayout(self)
        across_layout = QHBoxLayout(self)
        width_layout = QHBoxLayout(self)

        main_Layout.addRow("ValueNum", across_layout)
        main_Layout.addRow(width_layout)

        value_0 = QRadioButton("0", self)
        value_0001 = QRadioButton("0.001", self)
        value_001 = QRadioButton("0.01", self)
        value_005 = QRadioButton("0.05", self)
        value_01 = QRadioButton("0.1", self)
        value_05 = QRadioButton("0.5", self)
        value_1 = QRadioButton("1", self)
        value_1.setChecked(True)

        button1 = QPushButton("replace")
        button2 = QPushButton("add")
        button3 = QPushButton("sub")
        #button4 = QPushButton("reverse")
        button5 = QPushButton("flood")

        across_layout.addWidget(value_0, True)
        across_layout.addWidget(value_0001, True)
        across_layout.addWidget(value_001, True)
        across_layout.addWidget(value_005, True)
        across_layout.addWidget(value_01, True)
        across_layout.addWidget(value_05, True)
        across_layout.addWidget(value_1, True)

        self.__across = QButtonGroup(self)
        self.__across.addButton(value_0, 0)
        self.__across.addButton(value_0001, 1)
        self.__across.addButton(value_001, 2)
        self.__across.addButton(value_005, 3)
        self.__across.addButton(value_01, 4)
        self.__across.addButton(value_05, 5)
        self.__across.addButton(value_1, 6)

        width_layout.addWidget(button1, True)
        width_layout.addWidget(button2, True)
        width_layout.addWidget(button3, True)
        #width_layout.addWidget(button4, True)
        width_layout.addWidget(button5, True)
        
        button1.clicked.connect(self._setRep)
        button2.clicked.connect(self._setAdd)
        button3.clicked.connect(self._setSub)
        #button4.clicked.connect(self._setReverse)
        button5.clicked.connect(self._setFlood)

        value_0.setStyleSheet('color: cyan;')
        value_0001.setStyleSheet('color: pink;')
        value_001.setStyleSheet('color: pink;')
        value_005.setStyleSheet('color: pink;')
        value_01.setStyleSheet('color: pink;')
        value_05.setStyleSheet('color: yellow;')
        value_1.setStyleSheet('color: yellow;')

    def _setRep(self):
        self.num = self.__across.checkedId()
        rep(self.num)

    def _setAdd(self):
        self.num = self.__across.checkedId()
        add(self.num)

    def _setSub(self):
        self.num = self.__across.checkedId()
        sub(self.num)

    def _setReverse(self):
        self.reverse = True
        reverse(self.reverse)

    def _setFlood(self):
        self.flood = True
        flood(self.flood)

from maya import cmds
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance

def rep(across):
        if across == 0:
            value = 0
            paintValuesScale(value)
        elif across == 1:
            value = 0.001
            paintValuesAdditive(value)
        elif across == 2:
            value = 0.01
            paintValuesAdditive(value)
        elif across == 3:
            value = 0.05
            paintValuesAdditive(value)
        elif across == 4:            
            value = 0.1
            paintValuesAdditive(value)
        elif across == 5:            
            value = 0.5
            paintValuesAbsolute(value)
        elif across == 6:            
            value = 1
            paintValuesAbsolute(value)
      
def add(across):
    getValue = cmds.artAttrCtx("artAttrSkinContext", query = True, val = 0)
    if across == 1:
        value = getValue + 0.001
        paintValues(value)
    elif across == 2:
        value = getValue + 0.01
        paintValues(value)
    elif across == 3:
        value = getValue + 0.05
        paintValues(value)
    elif across == 4:
        value = getValue + 0.1
        paintValues(value)
    elif across == 5:
        value = getValue + 0.5
        paintValues(value)
    elif across == 6:
        value = getValue + 1
        paintValues(value)

def sub(across):
    getValue = cmds.artAttrCtx("artAttrSkinContext", query = True, val = 0)
    if across == 1:
        value = getValue - 0.001
        paintValues(value)
    elif across == 2:
        value = getValue - 0.01
        paintValues(value)
    elif across == 3:
        value = getValue - 0.05
        paintValues(value)
    elif across == 4:
        value = getValue - 0.1
        paintValues(value)
    elif across == 5:
        value = getValue - 0.5
        paintValues(value)
    elif across == 6:
        value = getValue - 1
        paintValues(value)

def reverse(reverse):
    if reverse == True :
        getValue = cmds.artAttrCtx("artAttrSkinContext", query = True, val = 0)
        value = 1 - getValue
        paintValues(value)

def flood(flood):
    if flood == True :
        cmds.artAttrCtx("artAttrSkinContext", edit = True, clear = True)
        cmds.artAttrCtx("artAttrContext", edit = True, clear = True)
        cmds.artAttrCtx("artAttrBlendShapeContext", edit = True, clear = True)

def paintValues(value):
    cmds.artAttrCtx("artAttrSkinContext", edit = True, val = value)
    cmds.artAttrCtx("artAttrContext", edit = True, val = value)
    cmds.artAttrCtx("artAttrBlendShapeContext", edit = True, val = value)

def paintValuesAbsolute(value):
    cmds.artAttrCtx("artAttrSkinContext", edit = True, val = value, sao = "absolute")
    cmds.artAttrCtx("artAttrContext", edit = True, val = value, sao = "absolute")
    cmds.artAttrCtx("artAttrBlendShapeContext", edit = True, val = value, sao = "absolute")

def paintValuesAdditive(value):
    cmds.artAttrCtx("artAttrSkinContext", edit = True, val = value, sao = "additive")
    cmds.artAttrCtx("artAttrContext", edit = True, val = value, sao = "additive")
    cmds.artAttrCtx("artAttrBlendShapeContext", edit = True, val = value, sao = "additive")

def paintValuesScale(value):
    cmds.artAttrCtx("artAttrSkinContext", edit = True, val = value, sao = "scale")
    cmds.artAttrCtx("artAttrContext", edit = True, val = value, sao = "scale")
    cmds.artAttrCtx("artAttrBlendShapeContext", edit = True, val = value, sao = "scale")

def get_maya_main_window():
    omui.MQtUtil.mainWindow()
    ptr = omui.MQtUtil.mainWindow()
    widget = wrapInstance(long(ptr), QWidget)
    return widget

def main():
    maya_window_instance = SkinValueWindow(parent=get_maya_main_window())
    maya_window_instance.show()

