import pymel.core as pm
from mainEdit import qt
from PySide2 import QtWidgets, QtCore, QtGui

class OptionWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(OptionWidget, self).__init__(*args, **kwargs)
        mainLayout = QtWidgets.QFormLayout(self)
        self.setWindowTitle('addNullNode')

        self.text1 = QtWidgets.QLineEdit('off', self)
        self.text2 = QtWidgets.QLineEdit('mov', self)
        button = QtWidgets.QPushButton('addNullNode')

        mainLayout.addRow(self.text1)
        mainLayout.addRow(self.text2)
        mainLayout.addRow(button)

        button.clicked.connect(self.text)

    def text(self):
        addNullNode(self.text1.text(), self.text2.text())

def addNullNode(offName, movName):
    

def main():
    window = OptionWidget(qt.getMayaWindow())
    window.setWindowFlags(QtCore.Qt.Window)
    window.show()

window = QtWidgets.QWidget(qt.getMayaWindow())
window.setWindowFlags(QtCore.Qt.Window)
layout = QtWidgets.QHBoxLayout(window)

path  = 'C:'
model = QtWidgets.QFileSystemModel()
model.setRootPath(path)

widget = QtWidgets.QTreeView(window)
widget.setModel(model)
widget.setRootIndex(model.index(path))
layout.addWidget(widget)

widget.setModel(model)

window.show()