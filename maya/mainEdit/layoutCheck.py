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
        self.setWindowTitle('layoutCheck')
        self.resize(200,400)

        widget = SelectionRadio()
        self.setCentralWidget(widget)

class SelectionRadio(QWidget):
    def __init__(self, *args, **kwargs):
        super(SelectionRadio,self).__init__(*args, **kwargs)
        self.checkedButton = "tet"
        self.selectRadio = QRadioButton('Select', self)
        self.hierarchyRadio = QRadioButton('Hierarchy', self)
        self.allRadio = QRadioButton('All', self)
        self.selectRadio.setChecked(True)

        '''acrossLayout = QHBoxLayout(self)
        acrossLayout.addWidget(self.selectRadio, False)
        acrossLayout.addWidget(self.hierarchyRadio, True)
        acrossLayout.addWidget(self.allRadio, True)'''
        self.selectRadio.clicked.connect(self._setChecked)
        self.hierarchyRadio.clicked.connect(self._setChecked)
        self.allRadio.clicked.connect(self._setChecked)

        testLayout = QVBoxLayout()
        testButton = QPushButton('test')
        testLayout.addWidget(self.selectRadio, False)
        testLayout.addWidget(self.hierarchyRadio, True)
        testLayout.addWidget(self.allRadio, True)
        testLayout.addWidget(testButton)
        #testLayout.addChildLayout(acrossLayout)
        testButton.clicked.connect(self.printChecked)

        #self.setLayout(testLayout)
        
    

    def _setChecked(self):
        if self.sender()==self.selectRadio:
            self.checkedButton = "select"
        elif self.sender()==self.hierarchyRadio:
            self.checkedButton = "hierarchy"
        elif self.sender()==self.allRadio:
            self.checkedButton = "all"

        #print self.checkedButton
    def printChecked(self):
        print self.checkedButton


class OptionWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(OptionWidget, self).__init__(*args, **kwargs)
        buttonWid = QPushButton('hogehoge')
        _selectionRadio = SelectionRadio()

        testsLayout = QHBoxLayout()
        self.setLayout(testsLayout)
        #testsLayout.addWidget(_selectionRadio)
        testsLayout.addWidget(buttonWid)
        

def main():
    window = MainWindow(qt.getMayaWindow())
    window.show()

main()