from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class QueryObjectWindowBase(QWidget):
    def __init__(self, *args, **kwargs):
        super(QueryObjectWindowBase,self).__init__(*args,**kwargs)
        self.setWindowFlags(Qt.Window)

        self.setObjectName("object_name")
        self.setWindowTitle("window_title")

        main_QFormLayout=QFormLayout(self)
        
        plain_QVBoxLayout=QVBoxLayout(self)
        main_QFormLayout.addRow(plain_QVBoxLayout)
        
        button_QHBoxLayout=QHBoxLayout(self)
        main_QFormLayout.addRow(button_QHBoxLayout)
        
        self.object_QTableWidget=QTableWidget(self)
        plain_QVBoxLayout.addWidget(self.object_QTableWidget)

        self.left_QPushButton=QPushButton("left",self)
        button_QHBoxLayout.addWidget(self.left_QPushButton)
        self.left_button.clicked.connect(self.left_button_onClicked)
        
        self.center_QPushButton=QPushButton("center",self)
        button_QHBoxLayout.addWidget(self.center_QPushButton)
        self.center_button.clicked.connect(self.center_button_onClicked)
        
        self.right_QPushButton=QPushButton("right",self)
        button_QHBoxLayout.addWidget(self.right_QPushButton)
        self.right_button.clicked.connect(self.right_button_onClicked)

    def left_button_onClicked(self):
        print("click!")
    def center_button_onClicked(self):
        print("click!")
    def right_button_onClicked(self):
        print("click!")

#window_instance=ScriptsRunWindowBase()
#window_instance.show()