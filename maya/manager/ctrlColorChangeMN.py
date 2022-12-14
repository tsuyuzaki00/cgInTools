# -*- coding: iso-8859-15 -*-
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import maya.cmds as cmds

import cgInTools as cit
from ...ui import ctrlColorChengeUI as UI
from ..library import sourceToTargetLB as sttLB
from ..library import windowLB as wLB
cit.reloads([UI,wLB,sttLB])

class ColorChangeWindow(UI.ColorChengeWindouBase):
    def __init__(self, parent):
        super(ColorChangeWindow, self).__init__(parent)
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle("ctrlColorChenge")

    def getSelectDrawingOverrides_query_list(self,objs):
        drawingOverride_objs=[]
        for obj in objs:
            if cmds.nodeType(obj)=="transform":
                shapes=cmds.listRelatives(objs[0:],type="nurbsCurve")
                for shape in shapes:
                    drawingOverride_objs.append(shape)
            elif cmds.nodeType(obj)=="joint":
                drawingOverride_objs.append(obj)
            else :
                cmds.error("Attribute Drowing Overrides is missing")
        return drawingOverride_objs

    def changeCtrlShapes_edit_func(self,objs,indexColor):
        for obj in objs:
            cmds.setAttr(obj+".overrideEnabled",1)
            cmds.setAttr(obj+".overrideColor",indexColor)

    def buttonRedOnClicked(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,13)#Red
    def buttonPinkOnClicked(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,20)#Pink
    def buttonCrimsonOnClicked(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,31)#Crimson
    def buttonDarkRedOnClicked(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,4)#DarkRed
    def buttonYellowOnClicked(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,17)#Yellow
    def buttonLimeOnClicked(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,14)#lime
    def buttonGreenOnClicked(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,27)#MediumSeaGreen
    def buttonDarkGreenOnClicked(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,7)#DarkGreen
    def buttonBlueOnClicked(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,6)#Blue
    def buttonCyanOnClicked(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,18)#Cyan
    def buttonTealOnClicked(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,28)#SteelBlue
    def buttonDarkBlueOnClicked(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,15)#DarkBlue
    def buttonMagentaOnClicked(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,9)#Magenta
    def buttonPurpleOnClicked(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,30)#Purple
    def buttonWhiteOnClicked(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,16)#White
    def buttonBlackOnClicked(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,1)#Black
    def buttonNeutralOnClicked(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        for drowing in drowings:
            cmds.setAttr(drowing+".overrideEnabled",0)

# mayaのメインウインドウを取得する
def get_maya_main_window():
    omui.MQtUtil.mainWindow()
    ptr = omui.MQtUtil.mainWindow()
    widget = wrapInstance(int(ptr),QWidget)
    return widget

def main():
    mayaWindow=ColorChangeWindow(parent=wLB.mayaMainWindow_query_widget())
    mayaWindow.show()