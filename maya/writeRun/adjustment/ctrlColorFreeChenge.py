import os, json
import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore, QtGui
from ..library import qt

class OptionWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(OptionWidget, self).__init__(*args, **kwargs)

        dialog = QtWidgets.QColorDialog(self)
        result = dialog.exec_()
        if result:
            colorChange(dialog.selectedColor())

def colorChange(radio):
    objs = cmds.ls(sl=True)
    shapes = cmds.listRelatives(objs[0:],type='nurbsCurve')
    for shape in shapes:
        cmds.setAttr(shape + '.overrideEnabled', 1)
        cmds.setAttr(shape + '.overrideRGBColors', 1)
        cmds.setAttr(shape + '.overrideColorRGB', radio.redF(), radio.greenF(), radio.blueF(), type = 'double3')


def main():
    window = OptionWidget(qt.getMayaWindow())
    window.show()
