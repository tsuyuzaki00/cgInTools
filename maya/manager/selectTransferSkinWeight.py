# -*- coding: iso-8859-15 -*-

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from maya import cmds
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance
from ...ui import scriptsRunUI as UI;
from ..library import selectBindJoints as SBJ

class ScriptsRunWindow(UI.ScriptsRunWindowBase):
    def __init__(self, parent):
        super(ScriptsRunWindow, self).__init__(parent)
        self.setObjectName("select_copy_bind")
        self.setWindowTitle("select_copy_binds")
        self.left_button.setText("run")
        self.center_button.setText("reload")
        self.right_button.setText("print")


    def view_scripts(self,sel):
        get_bind_joints = SBJ.ListBindJoints()
        lbj = get_bind_joints.list_bind_joints(sel)
        gbj = get_bind_joints.get_skin_cluster(sel)
        print(gbj)
        self.scripts_plain.insertPlainText('Binds = [\n')
        for jnt_list in lbj:
            self.scripts_plain.insertPlainText('\t"' + str(jnt_list) + '",\n')
        self.scripts_plain.insertPlainText('\t]\n')
        self.scripts_plain.insertPlainText('influence_skc="'+gbj[0]+'"\n')
        self.scripts_plain.insertPlainText('cmds.skinCluster("'+sel+'",Binds,n=influence_skc,tsb=True)\n')
        self.scripts_plain.insertPlainText('cmds.copySkinWeights(ss="'+ gbj[0] +'",ds=influence_skc,sa="closestPoint",noMirror=True)\n')
        
    def left_button_onClicked(self):
        get_scripts = self.scripts_plain.toPlainText()
        run_function(get_scripts)

    def center_button_onClicked(self):
        reload_button()

    def right_button_onClicked(self):
        main()

# mayaのメインウインドウを取得する
def get_maya_main_window():
    omui.MQtUtil.mainWindow()
    ptr = omui.MQtUtil.mainWindow()
    widget = wrapInstance(long(ptr), QWidget)
    return widget

def main():
    # 依存関係のないウインドウを継承して作ったMaya用のボタンUI
    maya_window_instance = ScriptsRunWindow(parent=get_maya_main_window())
    maya_window_instance.show()
    sels = cmds.ls(sl = True)
    for sel in sels:
        maya_window_instance.view_scripts(sel)

def reload_button():
    maya_window_instance = ScriptsRunWindow(parent=get_maya_main_window())
    sels = cmds.ls(sl = True)
    for sel in sels:
        maya_window_instance.view_scripts(sel)

# 実行関数
def run_function(get_scripts):
    exec(get_scripts)