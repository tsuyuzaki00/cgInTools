# -*- coding: iso-8859-15 -*-

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import os
from maya import cmds
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance
import cgInTools as sf
from ...ui import scriptsRunUI as UI
class LookNodeTypeWindow(UI.ScriptsRunWindowBase):
    def __init__(self, parent):
        super(LookNodeTypeWindow, self).__init__(parent)
        self.setObjectName("select_list_view")
        self.setWindowTitle("select_list_view")
        self.left_button.setText("print")
        self.center_button.setText("Select Replace")
        self.right_button.setText("Select Add")

    def view_scripts(self,sels):
        for sel in sels:
            matrixs = sel_matrix(sel)
            for matrix in matrixs:
                self.scripts_plain.insertPlainText(sel+'\t:\t'+matrix["name"]+'\t:\t'+matrix["value"]+'\n')
        
    def left_button_onClicked(self):
        main()

    def center_button_onClicked(self):
        objs = cmds.ls(sl=True)
        self.scripts_plain.clear()
        self.view_scripts(objs)

    def right_button_onClicked(self):
        objs = cmds.ls(sl=True)
        self.view_scripts(objs)

def sel_matrix(sel):
    normalMatrix = cmds.getAttr(sel + ".matrix")
    worldMatrix = cmds.getAttr(sel + ".worldMatrix")
    parentMatrix = cmds.getAttr(sel + ".parentMatrix")
    xformMatrix = cmds.getAttr(sel + ".xformMatrix")
    inverseMatrix = cmds.getAttr(sel + ".inverseMatrix")
    worldInverseMatrix = cmds.getAttr(sel + ".worldInverseMatrix")
    parentInverseMatrix = cmds.getAttr(sel + ".parentInverseMatrix")
    offsetParentMatrix = cmds.getAttr(sel + ".offsetParentMatrix")
    matrixs = [
        {"name":"normalMatrixX", "value":str(normalMatrix[0])},
        {"name":"normalMatrixY", "value":str(normalMatrix[1])},
        {"name":"normalMatrixZ", "value":str(normalMatrix[2])},
        {"name":"normalMatrixT", "value":str(normalMatrix[3])},
        {"name":"worldMatrixX", "value":str(worldMatrix[0])},
        {"name":"worldMatrixY", "value":str(worldMatrix[1])},
        {"name":"worldMatrixZ", "value":str(worldMatrix[2])},
        {"name":"worldMatrixT", "value":str(worldMatrix[3])},
        {"name":"parentMatrixX", "value":str(parentMatrix[0])},
        {"name":"parentMatrixY", "value":str(parentMatrix[1])},
        {"name":"parentMatrixZ", "value":str(parentMatrix[2])},
        {"name":"parentMatrixT", "value":str(parentMatrix[3])},
        {"name":"xformMatrixX", "value":str(xformMatrix[0])},
        {"name":"xformMatrixY", "value":str(xformMatrix[1])},
        {"name":"xformMatrixZ", "value":str(xformMatrix[2])},
        {"name":"xformMatrixT", "value":str(xformMatrix[3])},
        {"name":"inverseMatrixX", "value":str(inverseMatrix[0])},
        {"name":"inverseMatrixY", "value":str(inverseMatrix[1])},
        {"name":"inverseMatrixZ", "value":str(inverseMatrix[2])},
        {"name":"inverseMatrixT", "value":str(inverseMatrix[3])},
        {"name":"inverseWorldMatrixX", "value":str(worldInverseMatrix[0])},
        {"name":"inverseWorldMatrixY", "value":str(worldInverseMatrix[1])},
        {"name":"inverseWorldMatrixZ", "value":str(worldInverseMatrix[2])},
        {"name":"inverseWorldMatrixT", "value":str(worldInverseMatrix[3])},
        {"name":"inverseParentMatrixX", "value":str(parentInverseMatrix[0])},
        {"name":"inverseParentMatrixY", "value":str(parentInverseMatrix[1])},
        {"name":"inverseParentMatrixZ", "value":str(parentInverseMatrix[2])},
        {"name":"inverseParentMatrixT", "value":str(parentInverseMatrix[3])},
        {"name":"offsetParentMatrixX", "value":str(offsetParentMatrix[0])},
        {"name":"offsetParentMatrixY", "value":str(offsetParentMatrix[1])},
        {"name":"offsetParentMatrixZ", "value":str(offsetParentMatrix[2])},
        {"name":"offsetParentMatrixT", "value":str(offsetParentMatrix[3])},
        ]
    return matrixs

# mayaのメインウインドウを取得する
def get_maya_main_window():
    omui.MQtUtil.mainWindow()
    ptr = omui.MQtUtil.mainWindow()
    widget = wrapInstance(long(ptr), QWidget)
    return widget

def main():
    # 依存関係のないウインドウを継承して作ったMaya用のボタンUI
    maya_window_instance = LookNodeTypeWindow(parent=get_maya_main_window())
    sels = cmds.ls(sl = True)
    maya_window_instance.view_scripts(sels)
    maya_window_instance.show()