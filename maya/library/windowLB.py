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
def mayaPathDialog_query_dict(word,fileMode,extension="json",directory=None):
    default_dir=directory or cmds.workspace(q=True,rd=True)
    path_list=cmds.fileDialog2(
        fileFilter=word+" ."+extension+"(*."+extension+")",
        ds=2,
        fm=fileMode,
        dir=default_dir,
        spe=False
    )
    if path_list is None:
        return None
    directory_dir=os.path.dirname(path_list[0])
    file_str=os.path.splitext(os.path.basename(path_list[0]))[0]
    return {"directory":directory_dir,"file":file_str}

# fileMode 0=Export 1=Import
def mayaDirDialog_query_dict(word,directory=None,upRoot=False):
    if upRoot:
        wrkspace_dir=cmds.workspace(q=True,rd=True)
        root_dir=os.path.abspath(os.path.join(wrkspace_dir,os.pardir))
        default_dir=root_dir.replace(os.sep,'/')
    else:
        default_dir=directory or cmds.workspace(q=True,rd=True)
    path_list=cmds.fileDialog2(
        cap=word+" Directory",
        okc=word,
        fileFilter="Folder Name",
        ds=2,
        fm=3,
        dir=default_dir,
        spe=False
    )
    if path_list is None:
        return None
    directory_dir=os.path.dirname(path_list[0])
    folder_str=os.path.splitext(os.path.basename(path_list[0]))[0]
    return {"directory":directory_dir,"folder":folder_str}