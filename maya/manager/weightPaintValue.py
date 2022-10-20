# -*- coding: iso-8859-15 -*-

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import os
import maya.cmds as cmds
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance
from ...ui import skinWeightUI as UI

class SkinValueWindow(UI.SkinValueWindowBase):
    def __init__(self, parent):
        super(SkinValueWindow, self).__init__(parent)
        
    def button_0_onClicked(self):
        value = 0
        paintValues_edit(value,sao="scale")
    
    def button_0001_onClicked(self):
        value = 0.001
        paintValues_edit(value,sao="additive")
    
    def button_001_onClicked(self):
        value = 0.01
        paintValues_edit(value,sao="additive")
    
    def button_005_onClicked(self):
        value = 0.05
        paintValues_edit(value,sao="additive")
    
    def button_01_onClicked(self):
        value = 0.1
        paintValues_edit(value,sao="additive")
    
    def button_05_onClicked(self):
        value = 0.5
        paintValues_edit(value,sao="absolute")
    
    def button_1_onClicked(self):
        value = 1
        paintValues_edit(value,sao="absolute")

    def button_flood_onClicked(self):
        flood_edit()

    def button_reverse_onClicked(self):
        reverse_edit()

    def button_smooth_onClicked(self):
        soomth_edit()

# mayaのメインウインドウを取得する
def get_maya_main_window():
    omui.MQtUtil.mainWindow()
    ptr = omui.MQtUtil.mainWindow()
    widget = wrapInstance(int(ptr), QWidget)
    return widget

def main():
    # 依存関係のないウインドウを継承して作ったMaya用のボタンUI
    maya_window_instance = SkinValueWindow(parent=get_maya_main_window())
    maya_window_instance.show()
    context_check()

def paintValues_edit(value,sao=""):
    artAttrs_string = ["artAttrSkinContext","artAttrContext","artAttrBlendShapeContext"]
    for artAttr_string in artAttrs_string:
        if sao == "":
            getContext_uni = cmds.artAttrCtx(artAttr_string, query = True, sao = True)
            cmds.artAttrCtx(artAttr_string, edit = True, val = value, sao = getContext_uni)
        else:
            cmds.artAttrCtx(artAttr_string, edit = True, val = value, sao = sao)

def reverse_edit():
    artAttrs_string = ["artAttrSkinContext","artAttrContext","artAttrBlendShapeContext"]
    for artAttr_string in artAttrs_string:
        getContext_uni = cmds.artAttrCtx(artAttr_string, query = True, sao = True)
        if getContext_uni == "additive":
            getValue = cmds.artAttrCtx(artAttr_string, query = True, val = 0)
            value = 1 - getValue
            paintValues_edit(value,sao="scale")
        elif getContext_uni == "scale":
            getValue = cmds.artAttrCtx(artAttr_string, query = True, val = 0)
            value = 1 - getValue
            paintValues_edit(value,sao="additive")
        else:
            getValue = cmds.artAttrCtx(artAttr_string, query = True, val = 0)
            value = 1 - getValue
            paintValues_edit(value)

def flood_edit():
    artAttrs_string = ["artAttrSkinContext","artAttrContext","artAttrBlendShapeContext"]
    for artAttr_string in artAttrs_string:
        cmds.artAttrCtx(artAttr_string, edit = True, clear = True)

def soomth_edit():
    artAttrs_string = ["artAttrSkinContext","artAttrContext","artAttrBlendShapeContext"]
    for artAttr_string in artAttrs_string:
        getContext_uni = cmds.artAttrCtx(artAttr_string, query = True, sao = True)
        cmds.artAttrCtx(artAttr_string, edit = True, sao = "smooth")
        cmds.artAttrCtx(artAttr_string, edit = True, clear = True)
        cmds.artAttrCtx(artAttr_string, edit = True, sao = getContext_uni)

def context_check():
    artAttrs_string = ["artAttrSkinContext","artAttrContext","artAttrBlendShapeContext"]
    for artAttr_string in artAttrs_string:
        try:
            cmds.artAttrCtx(artAttr_string) # To load the tools
        except RuntimeError:
            pass