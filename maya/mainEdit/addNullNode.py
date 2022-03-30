import pymel.core as pm
from mainEdit import qt
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

class OptionWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(OptionWidget, self).__init__(*args, **kwargs)
        mainLayout = QFormLayout(self)
        self.setWindowTitle('addNullNode')

        self.text1 = QLineEdit('off', self)
        self.text2 = QLineEdit('mov', self)
        button = QPushButton('addNullNode')

        mainLayout.addRow(self.text1)
        mainLayout.addRow(self.text2)
        mainLayout.addRow(button)

        button.clicked.connect(self._setText)

    def _setText(self):
        addNullNode(self.text1.text(), self.text2.text())

def addNullNode(offName, movName):
    sel = pm.selected()[0]
    nullName = pm.listRelatives(sel, p = True)
    part = sel.split("_")
    offName = '_'.join([offName, part[1], part[2], part[3]])
    movName = '_'.join([movName, part[1], part[2], part[3]])
    
    off = pm.duplicate(nullName , po = True, n = offName)
    mov = pm.duplicate(sel , po = True, n = movName)
    
    pm.parent(mov[0], off[0])
    pm.parent(nullName,mov[0])

def main():
    window = OptionWidget(qt.getMayaWindow())
    window.setWindowFlags(Qt.Window)
    window.show()