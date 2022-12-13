# -*- coding: iso-8859-15 -*-
from PySide2.QtWidgets import *

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