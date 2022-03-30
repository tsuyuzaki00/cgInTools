import os, json
from PySide2 import QtWidgets, QtGui
from myTool.lib import qt

class OptionWidget(QtWidgets.QWidget):
	def __init__(self, *args, **kwargs):
		super(OptionWidget, self).__init__(*args, **kwargs)
		mainLayout = QtWidgets.QFormLayout(self)
		
		widget = QtWidgets.QCheckBox('guide',self)
		widget.setChecked(True)
		mainLayout.addWidget(widget)
		
		widget = QtWidgets.QCheckBox('geomety',self)
		widget.setChecked(True)
		mainLayout.addWidget(widget)
		
		widget = QtWidgets.QCheckBox('joint',self)
		widget.setChecked(True)
		mainLayout.addWidget(widget)
		
		widget = QtWidgets.QCheckBox('ctrl',self)
		widget.setChecked(True)
		mainLayout.addWidget(widget)
		
		widget = QtWidgets.QCheckBox('camera',self)
		widget.setChecked(True)
		mainLayout.addWidget(widget)
		
		widget = QtWidgets.QCheckBox('light',self)
		widget.setChecked(True)
		mainLayout.addWidget(widget)
		
class MainWindow(QtWidgets.QMainWindow):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setWindowTitle('Test window')
		self.resize(400, 200)
		
		toolWidget = qt.ToolWidget(self)
		self.setCentralWidget(toolWidget)
		
		optionWidget = OptionWidget(self)
		toolWidget.setOptionWidget(optionWidget)


def option():
    window = MainWindow(qt.getMayaWindow())
    window.show()
    
option()