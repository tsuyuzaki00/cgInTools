import os
from mainEdit import qt
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
import maya.cmds as cmds
import maya.api.OpenMaya as om

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('testChecker')

        widget = ListTree()
        self.setCentralWidget(widget)

class ListTree(QWidget):
    def __init__(self, *args, **kwargs):
        super(ListTree, self).__init__(*args, **kwargs)
        self.listTreeLayout = QVBoxLayout(self)
        print args

    def OKItem(self, sel, contents):
        print sel
        print contents
        self.listTreeLayout = QVBoxLayout(self)
        self.listTreeLayout.addWidget(QLabel('OK'))
        OKWidget = QTreeWidget()

        OKobject = [contents]
        OKselect = sel
        OKItem = QTreeWidgetItem(OKobject)

        QTreeWidgetItem(OKItem, [OKselect])
        
        OKWidget.addTopLevelItem(OKItem)

        OKWidget.setSelectionMode(QAbstractItemView.ContiguousSelection)
        OKWidget.itemSelectionChanged.connect(cmds.select(OKselect))
        self.listTreeLayout.addWidget(OKWidget)

    def NGItem(self, sels, contents):
        self.listTreeLayout = QVBoxLayout(self)
        NGobject = ['NGtype']
        NGselect = ['NGobject']
        self.listTreeLayout.addWidget(QLabel('NG'))
        NGWidget = QTreeWidget()
        NGItem = QTreeWidgetItem(NGobject)
        QTreeWidgetItem(NGItem, NGselect)
        NGWidget.addTopLevelItem(NGItem)
        NGWidget.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.listTreeLayout.addWidget(NGWidget)

def frozenTransformCheck(sels):
    check = 'FrozenTransform'
    for sel in sels:
        translation = cmds.xform(sel, q=True, worldSpace = True, translation = True)
        rotation = cmds.xform(sel, q=True, worldSpace = True, rotation = True)
        scale = cmds.xform(sel, q=True, worldSpace = True, scale = True)
        if translation == [0.0,0.0,0.0] and rotation == [0.0,0.0,0.0] and scale == [1.0,1.0,1.0]:
            listTree = ListTree()
            listTree.OKItem(sel, check)
        elif not translation == [0.0,0.0,0.0] or not rotation == [0.0,0.0,0.0] or not scale == [1.0,1.0,1.0]:
            listTree = ListTree()
            listTree.NGItem(sel, check)

def unCenterPivotCheck(sels):
    check = 'UnCenterPivot'
    for sel in sels:
        if cmds.xform(sel,q=1,ws=1,rp=1) == [0,0,0]:
            listTree = ListTree()
            listTree.OKItem(sel, check)
        else :
            listTree = ListTree()
            listTree.NGItem(sel, check)
            
def main():
    sels = cmds.ls(sl = True)
    frozenTransformCheck(sels)
    unCenterPivotCheck(sels)
    window = MainWindow(qt.getMayaWindow())
    window.show()

main()