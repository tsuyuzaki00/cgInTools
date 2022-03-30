from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from maya import cmds
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance

def uiOnly_check_ui(uiClass):
    window_instance = uiClass
    window_instance.show()

def mayaRun_check_ui(uiClass):
    # 依存関係のないウインドウを継承して作ったMaya用のボタンUI
    maya_window_instance = uiClass(parent=get_maya_main_window())
    maya_window_instance.show()

# mayaのメインウインドウを取得する
def get_maya_main_window():
    omui.MQtUtil.mainWindow()
    ptr = omui.MQtUtil.mainWindow()
    widget = wrapInstance(long(ptr), QWidget)
    return widget

