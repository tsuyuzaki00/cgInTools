from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from . import baseUI as UI

class CreateNodesWindow(UI.MainWindowBase):
    def __init__(self,*args,**kwargs):
        super(CreateNodesWindow,self).__init__(*args,**kwargs)
        self.setWindowFlags(Qt.Window)
        self.setObjectName("CreateNodes")
        self.setWindowTitle("Create Nodes")
        self.buttonLeft_QPushButton.setText("Create")
        self.buttonCenter_QPushButton.setText("Menu Add")
        self.buttonRight_QPushButton.setText("Select Add")
        self._rowCount_int=self.custom_QGridLayout.rowCount()
        
        widget_CreateNodeWidget=CreateNodeWidget(self)
        self.custom_QGridLayout.addWidget(widget_CreateNodeWidget,0,0)

    def buttonCenterClicked(self):
        widget_CreateNodeWidget=CreateNodeWidget(self)
        self.custom_QGridLayout.addWidget(widget_CreateNodeWidget,self._rowCount_int,0)

class CreateNodeWidget(QWidget):
    def __init__(self,*args,**kwargs):
        super(CreateNodeWidget,self).__init__(*args,**kwargs)
        widget_QHBoxLayout=QHBoxLayout(self)

        name_QLabel=QLabel("Name",self)
        widget_QHBoxLayout.addWidget(name_QLabel)

        self.name_QLineEdit=QLineEdit(self)
        widget_QHBoxLayout.addWidget(self.name_QLineEdit)
        
        type_QLabel=QLabel("NodeType",self)
        widget_QHBoxLayout.addWidget(type_QLabel)
        
        self.type_QLineEdit=QLineEdit(self)
        widget_QHBoxLayout.addWidget(self.type_QLineEdit)

        delete_QPuthButton=QPushButton("Delete",self)
        widget_QHBoxLayout.addWidget(delete_QPuthButton)
        delete_QPuthButton.clicked.connect(self.buttonDeleteClicked)

    #Public Function
    def buttonDeleteClicked(self):
        #parentWidget.removeWidget(self)
        self.setParent(None)
        self.deleteLater()

#viewWindow=CreateNodesWindow()
#viewWindow.show()