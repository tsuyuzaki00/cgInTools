# -*- coding: iso-8859-15 -*-
from PySide2.QtWidgets import *

import os
import maya.cmds as cmds
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

# mayaのメインウインドウを取得する
def mayaMainWindow_query_QWidget():
    mainWindow_SwigPyObject=omui.MQtUtil.mainWindow()
    mayaWindow_QWidget=wrapInstance(int(mainWindow_SwigPyObject),QWidget)
    return mayaWindow_QWidget

# fileMode 0=Export 1=Import
def mayaPathDialog_query_dict(text,fileMode,extension="json",directory=None):
    default_dir=directory or cmds.workspace(q=True,rd=True)
    path_strs=cmds.fileDialog2(
        fileFilter=text+" ."+extension+"(*."+extension+")",
        ds=2,
        fm=fileMode,
        dir=default_dir,
        spe=False
    )
    if path_strs is None or path_strs is []:
        return None
    directory_dir=os.path.dirname(path_strs[0])
    file_str=os.path.splitext(os.path.basename(path_strs[0]))[0]
    return {"directory":directory_dir,"file":file_str}

# fileMode 0=Export 1=Import
def mayaDirDialog_query_dict(text,directory=None,upRoot=False):
    if upRoot:
        wrkspace_dir=cmds.workspace(q=True,rd=True)
        root_dir=os.path.abspath(os.path.join(wrkspace_dir,os.pardir))
        default_dir=root_dir.replace(os.sep,'/')
    else:
        default_dir=directory or cmds.workspace(q=True,rd=True)
    path_strs=cmds.fileDialog2(
        cap=text+" Directory",
        okc=text,
        fileFilter="Folder Name",
        ds=2,
        fm=3,
        dir=default_dir,
        spe=False
    )
    if path_strs is None or path_strs is []:
        return None
    directory_dir=os.path.dirname(path_strs[0])
    folder_str=os.path.splitext(os.path.basename(path_strs[0]))[0]
    return {"directory":directory_dir,"folder":folder_str}