# -*- coding: iso-8859-15 -*-
from PySide2.QtWidgets import *

from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance

# mayaのメインウインドウを取得する
def mayaMainWindow_query_widget():
    ptr=omui.MQtUtil.mainWindow()
    widget=wrapInstance(int(ptr),QWidget)
    return widget