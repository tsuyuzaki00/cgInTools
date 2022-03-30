import maya.cmds as cmds
from ..MayaLibrary import qt
from PySide2 import QtWidgets, QtCore, QtGui

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('JointRadiusEdit')
        self.resize(250, 20)

        widget = OptionWidget()
        self.setCentralWidget(widget)

class OptionWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(OptionWidget, self).__init__(*args, **kwargs)

        layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(layout)
        
        self.spinBox = QtWidgets.QDoubleSpinBox()
        self.spinBox.setValue(0.25)
        self.spinBox.setRange(0, 100)
        layout.addWidget(self.spinBox)

        button = QtWidgets.QPushButton('Edit')
        button.clicked.connect(self.setRadius)
        self.spinBox.valueChanged.connect(self.setRadius)
        layout.addWidget(button)

    def setRadius(self):
        self.num = self.spinBox.value()
        jointRadiusEdit(self.num)

def jointRadiusEdit(num = 1):
    sels = cmds.ls(sl = True, dag = True, typ = 'joint')
    for sel in sels:
        cmds.setAttr(sel + '.radius', num)

def option():
    window = MainWindow(qt.getMayaWindow())
    window.show()
    
def main():
    jointRadiusEdit()