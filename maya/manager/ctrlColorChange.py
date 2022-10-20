# -*- coding: iso-8859-15 -*-
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import maya.cmds as cmds
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance
from ...ui import ctrlColorChengeUI as UI

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

    def yellowButton_onClicked_func(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,17)#Yellow
    def limeButton_onClicked_func(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,14)#lime
    def greenButton_onClicked_func(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,27)#MediumSeaGreen
    def darkGreenButton_onClicked_func(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,7)#DarkGreen
    def blueButton_onClicked_func(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,6)#Blue
    def cyanButton_onClicked_func(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,18)#Cyan
    def tealButton_onClicked_func(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,28)#SteelBlue
    def darkBlueButton_onClicked_func(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,15)#DarkBlue
    def redButton_onClicked_func(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,13)#Red
    def pinkButton_onClicked_func(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,20)#Pink
    def crimsonButton_onClicked_func(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,31)#Crimson
    def darkRedButton_onClicked_func(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,4)#DarkRed
    def magentaButton_onClicked_func(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,9)#Magenta
    def purpleButton_onClicked_func(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,30)#Purple
    def whiteButton_onClicked_func(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,16)#White
    def blackButton_onClicked_func(self):
        objs=cmds.ls(sl=True)
        drowings=self.getSelectDrawingOverrides_query_list(objs)
        self.changeCtrlShapes_edit_func(drowings,1)#Black
    def neutralButton_onClicked_func(self):
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
    # 依存関係のないウインドウを継承して作ったMaya用のボタンUI
    maya_window_instance = ColorChangeWindow(parent=get_maya_main_window())
    maya_window_instance.show()