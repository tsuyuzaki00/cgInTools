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
    def __init__(self, sel, contents, *args, **kwargs):
        super(ListTree, self).__init__(*args, **kwargs)
        self.listTreeLayout = QVBoxLayout(self)
        self.sel = sel
        self.contents = contents

    def OKItem(self, sel, contents):
        self.listTreeLayout.addWidget(QLabel('OK'))
        OKWidget = QTreeWidget()
        OKobject = [contents]
        OKselect = [sel]
        OKItem = QTreeWidgetItem(OKobject)
        QTreeWidgetItem(OKItem, OKselect)
        OKWidget.addTopLevelItem(OKItem)
        OKWidget.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.listTreeLayout.addWidget(OKWidget)

    def NGItem(self, sel, contents):
        self.listTreeLayout.addWidget(QLabel('NG'))
        NGWidget = QTreeWidget()
        NGobject = [contents]
        NGselect = [sel]
        NGItem = QTreeWidgetItem(NGobject)
        QTreeWidgetItem(NGItem, NGselect)
        NGWidget.addTopLevelItem(NGItem)
        NGWidget.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.listTreeLayout.addWidget(NGWidget)

def historyCheck(sels):
    check = 'History'
    for sel in sels:
        shape = cmds.listRelatives(sel, shapes = True, typ = 'mesh')
        historySize = len(cmds.listHistory(shape))
        if historySize < 2:
            listTree = ListTree()
            listTree.OKItem(sel, check)
        else :
            listTree = ListTree()
            listTree.NGItem(sel, check)

def main():
    sels = cmds.ls(sl = True)
    historyCheck(sels)
    window = MainWindow(qt.getMayaWindow())
    window.show()

main()