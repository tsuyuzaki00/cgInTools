from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import cgInTools as cit
from . import baseUI as UI
cit.reloads([UI])

class CreateNodesWindow(UI.MainWindowBase):
    def __init__(self,*args,**kwargs):
        super(CreateNodesWindow,self).__init__(*args,**kwargs)
        self.setWindowFlags(Qt.Window)
        self.setObjectName("CreateNodes")
        self.setWindowTitle("Create Nodes")
        self.buttonLeft_QPushButton.setText("Create")
        self.buttonCenter_QPushButton.setText("Menu Add")
        self.buttonRight_QPushButton.setText("Select Add")
        
        widget_CreateNodeWidget=CreateNodeWidget(self)
        widget_CreateNodeWidget.setParentWidget(self.custom_QScrollArea)

        self.custom_QScrollArea.setWidget(widget_CreateNodeWidget)

    def buttonCenterClicked(self):
        widget_CreateNodeWidget=CreateNodeWidget(self)
        widget_CreateNodeWidget.setParentWidget(self.custom_QScrollArea)
        self.custom_QScrollArea.setWidget(widget_CreateNodeWidget)

class CreateNodeWidget(QWidget):
    def __init__(self,*args,**kwargs):
        super(CreateNodeWidget,self).__init__(*args,**kwargs)
        self._parent_QWidget=None
        self.createNodeWidget_create_func()

    #Single Function
    def createNodeWidget_create_func(self):
        widget_QHBoxLayout=QHBoxLayout(self)

        name_QLabel=QLabel("Name",self)
        widget_QHBoxLayout.addWidget(name_QLabel)

        self.name_QLineEdit=QLineEdit(self)
        widget_QHBoxLayout.addWidget(self.name_QLineEdit)
        
        type_QLabel=QLabel("NodeType",self)
        widget_QHBoxLayout.addWidget(type_QLabel)
        
        #self.type_QLineEdit=QLineEdit(self)
        #widget_QHBoxLayout.addWidget(self.type_QLineEdit)
        self.type_QComboBox=QComboBox(self)
        self.type_QComboBox.addItems([
            "transform",
            "joint"
        ])
        widget_QHBoxLayout.addWidget(self.type_QComboBox)

        Add_QPuthButton=QPushButton("Add",self)
        widget_QHBoxLayout.addWidget(Add_QPuthButton)
        Add_QPuthButton.clicked.connect(self.buttonAddClicked)

        duplicate_QPuthButton=QPushButton("Duplicate",self)
        widget_QHBoxLayout.addWidget(duplicate_QPuthButton)
        duplicate_QPuthButton.clicked.connect(self.buttonDuplicateClicked)

        delete_QPuthButton=QPushButton("Delete",self)
        widget_QHBoxLayout.addWidget(delete_QPuthButton)
        delete_QPuthButton.clicked.connect(self.buttonDeleteClicked)

    #Setting Function
    def setParentWidget(self,variable):
        self._parent_QWidget=variable
        return self._parent_QWidget
    def getParentWidget(self):
        return self._parent_QWidget

    #Public Function
    def buttonAddClicked(self):
        add_CreateNodeWidget=CreateNodeWidget()
        add_CreateNodeWidget.setParentWidget(self._parent_QWidget)
        self._parent_QWidget.addWidget(add_CreateNodeWidget,self._parent_QWidget.rowCount(),0)

    def buttonDuplicateClicked(self):
        widget_CreateNodeWidget=self
        name_str=widget_CreateNodeWidget.name_QLineEdit.text()
        nodeType_str=widget_CreateNodeWidget.type_QLineEdit.text()

        duplicate_CreateNodeWidget=CreateNodeWidget()
        duplicate_CreateNodeWidget.name_QLineEdit.setText(name_str)
        duplicate_CreateNodeWidget.type_QLineEdit.setText(nodeType_str)
        duplicate_CreateNodeWidget.setParentWidget(self._parent_QWidget)
        self._parent_QWidget.addWidget(duplicate_CreateNodeWidget,self._parent_QWidget.rowCount(),0)

    def buttonDeleteClicked(self):
        if not self._parent_QWidget.rowCount() == 0:
            print(self._parent_QWidget.rowCount())
            self.setParent(None)
            self.deleteLater()

#viewWindow=CreateNodesWindow()
#viewWindow.show()