# -*- coding: iso-8859-15 -*-

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import os
from maya import cmds
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance
import cgInTools as SF
from ..library import cJson as SJ
from ...ui import scriptsRunUI as UI
from ...ui import mainWindowUI as mainUI

class MainMenu(mainUI.MainWindowBase):
    def __init__(self, parent):
        super(MainMenu, self).__init__(parent)
        self.setWindowTitle("select_list_view")
        
        layouts = QFormLayout(self)
        self.centerWidget.setLayout(layouts)
        widget = ScriptsRunWindow(self)
        layouts.addWidget(widget)

class ScriptsRunWindow(UI.ScriptsRunWindowBase):
    def __init__(self, parent):
        super(ScriptsRunWindow, self).__init__(parent)
        self.setObjectName("select_list_view")
        self.left_button.setText("Selection")
        self.center_button.setText("Select Replace")
        self.right_button.setText("Select Add")

    def view_scripts(self,sels):
        for sel in sels:
            self.scripts_plain.insertPlainText(str(sel)+'\n')

    def dict_setting(self,path,key_name="selections",json_name="selections",new_folder=None):
        get_scripts = self.scripts_plain.toPlainText()
        self.list_scripts = get_scripts.splitlines()
        self.dict_text = {key_name:self.list_scripts}
        self.json_file = self.simple_json.path_setting(path,json_name,new_folder)
        
    def left_button_onClicked(self):
        get_scripts = self.scripts_plain.toPlainText()
        self.list_scripts = get_scripts.splitlines()
        run_script = "selections="+str(self.list_scripts)+"\n"+"cmds.select(selections)"
        select_function(run_script)

    def center_button_onClicked(self):
        objs = cmds.ls(sl=True)
        self.scripts_plain.clear()
        self.view_scripts(objs)

    def right_button_onClicked(self):
        objs = cmds.ls(sl=True)
        self.view_scripts(objs)

# mayaのメインウインドウを取得する
def get_maya_main_window():
    omui.MQtUtil.mainWindow()
    ptr = omui.MQtUtil.mainWindow()
    widget = wrapInstance(int(ptr), QWidget)
    return widget

def main():
    # 依存関係のないウインドウを継承して作ったMaya用のボタンUI
    maya_window_instance = MainMenu(parent=get_maya_main_window())
    sels = cmds.ls(sl = True)
    #maya_window_instance.view_scripts(sels)
    maya_window_instance.show()

# 実行関数
def select_function(get_scripts):
    exec(get_scripts)
    cmds.ls(sl=True)

def save_function(json_file,dict_text):
    simple_json = SJ.SimpleJson()
    simple_json.write_run(json_file,dict_text)

"""
self.dict_setting(path=self.get_folder.maya_json_folder,new_folder="selection_export")
dict_text = self.dict_text
json_file = self.json_file
save_function(json_file=json_file,dict_text=dict_text)
"""