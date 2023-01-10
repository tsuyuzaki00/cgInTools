# -*- coding: iso-8859-15 -*-
from PySide2.QtWidgets import *

import os
import maya.cmds as cmds
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

# mayaのメインウインドウを取得する
def mayaMainWindow_query_widget():
    ptr=omui.MQtUtil.mainWindow()
    widget=wrapInstance(int(ptr),QWidget)
    return widget

def mayaMixinWindow_query_widget():
    restored_control=omui.MQtUtil.getCurrentParent()
    ptr=omui.MQtUtil.mainWindow()
    omui.MQtUtil.addWidgetToMayaLayout(int(ptr),int(restored_control))

# fileMode 0=Export 1=Import
def mayaFileDialog_query_path_file(text,fileMode,extension="json"):
    workPath=cmds.workspace(q=True,rd=True)
    pathFile_list=cmds.fileDialog2(fileFilter=text+" ."+extension+"(*."+extension+")",ds=2,fm=fileMode,dir=workPath)
    if pathFile_list == None:
        return False
    path=pathFile_list[0].split("/")[:-1]
    path=os.path.join(*path)
    file=pathFile_list[0].split("/")[-1]
    file=file.split(".")[0]
    return path,file