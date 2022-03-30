from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import pymel.core as pm

class OptionWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(OptionWidget, self).__init__(*args, **kwargs)
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle('ctrlColorChenge')

        main_layout = QFormLayout(self)
        center_layout = QHBoxLayout(self)
        left_layout = QHBoxLayout(self)
        right_layout = QHBoxLayout(self)
        other_layout = QHBoxLayout(self)
        button_layout = QHBoxLayout(self)

        main_layout.addRow('Center Color', center_layout)
        main_layout.addRow('Left Color', left_layout)
        main_layout.addRow('Right Color', right_layout)
        main_layout.addRow('Other Color', other_layout)
        main_layout.addRow(button_layout)

        yellow = QRadioButton('Yellow', self)
        mainGreen = QRadioButton('Green', self)
        subGreen = QRadioButton('DarkGreen', self)
        mainRed = QRadioButton('Red', self)
        pink = QRadioButton('Pink', self)
        subRed = QRadioButton('DarkRed', self)
        mainBlue = QRadioButton('Blue', self)
        cyan = QRadioButton('Cyan', self)
        subBlue = QRadioButton('DarkBlue', self)
        purple = QRadioButton('Purple', self)
        magenta = QRadioButton('Magenta', self)
        crimson = QRadioButton('Crimson', self)
        change_button = QPushButton('chengeColor')
        yellow.setChecked(True)

        center_layout.addWidget(yellow, True)
        center_layout.addWidget(mainGreen, True)
        center_layout.addWidget(subGreen, True)
        left_layout.addWidget(mainBlue, True)
        left_layout.addWidget(cyan, True)
        left_layout.addWidget(subBlue, True)
        right_layout.addWidget(mainRed, True)
        right_layout.addWidget(pink, True)
        right_layout.addWidget(subRed, True)
        other_layout.addWidget(magenta, True)
        other_layout.addWidget(purple, True)
        other_layout.addWidget(crimson, True)

        self.__across = QButtonGroup(self)
        self.__across.addButton(yellow, 0)
        self.__across.addButton(mainGreen, 1)
        self.__across.addButton(subGreen, 2)
        self.__across.addButton(mainBlue, 3)
        self.__across.addButton(cyan, 4)
        self.__across.addButton(subBlue, 5)
        self.__across.addButton(mainRed, 6)
        self.__across.addButton(pink, 7)
        self.__across.addButton(subRed, 8)
        self.__across.addButton(magenta, 9)
        self.__across.addButton(purple, 10)
        self.__across.addButton(crimson, 11)

        button_layout.addWidget(change_button, True)
        change_button.clicked.connect(self.chenge)

        yellow.setStyleSheet('color: yellow;')
        mainGreen.setStyleSheet('color: lime;')
        subGreen.setStyleSheet('color: green;')
        mainRed.setStyleSheet('color: red;')
        pink.setStyleSheet('color: pink;')
        subRed.setStyleSheet('color: darkRed;')
        mainBlue.setStyleSheet('color: blue;')
        cyan.setStyleSheet('color: cyan;')
        subBlue.setStyleSheet('color: darkBlue;')
        purple.setStyleSheet('color: purple;')
        magenta.setStyleSheet('color: magenta;')
        crimson.setStyleSheet('color: crimson;')

    def chenge(self):
        self.num = self.__across.checkedId()
        colorChange(self.num)

from maya import cmds
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance

def colorChange(radio):
    sel = cmds.ls(sl=True)
    shapes = cmds.listRelatives(sel[0:], type='nurbsCurve')
    for shape in shapes:
        cmds.setAttr(shape + '.overrideEnabled', 1)
        if radio == 0:
            cmds.setAttr(shape + '.overrideColor', 17)#Yellow
        elif radio == 1:
            cmds.setAttr(shape + '.overrideColor', 14)#Green
        elif radio == 2:
            cmds.setAttr(shape + '.overrideColor', 7)#DarkGreen
        elif radio == 3:
            cmds.setAttr(shape + '.overrideColor', 6)#Blue
        elif radio == 4:
            cmds.setAttr(shape + '.overrideColor', 18)#Cyan
        elif radio == 5:
            cmds.setAttr(shape + '.overrideColor', 5)#DarkBlue
        elif radio == 6:
            cmds.setAttr(shape + '.overrideColor', 13)#Red
        elif radio == 7:
            cmds.setAttr(shape + '.overrideColor', 20)#Pink
        elif radio == 8:
            cmds.setAttr(shape + '.overrideColor', 4)#DarkRed
        elif radio == 9:
            cmds.setAttr(shape + '.overrideColor', 9)#Magenta
        elif radio == 10:
            cmds.setAttr(shape + '.overrideColor', 30)#Purple
        elif radio == 11:
            cmds.setAttr(shape + '.overrideColor', 31)#Crimson
            

def get_maya_main_window():
    omui.MQtUtil.mainWindow()
    ptr = omui.MQtUtil.mainWindow()
    widget = wrapInstance(long(ptr), QWidget)
    return widget

def main():
    maya_window_instance = OptionWidget(parent=get_maya_main_window())
    maya_window_instance.show()