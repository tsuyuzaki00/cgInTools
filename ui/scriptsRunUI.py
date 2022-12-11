from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class ScriptsRunWindowBase(QWidget):
    def __init__(self,*args,**kwargs):
        super(ScriptsRunWindowBase,self).__init__(*args,**kwargs)
        self.setWindowFlags(Qt.Window)

        self.setObjectName("object_name")
        self.setWindowTitle("window_title")

        main_QFormLayout=QFormLayout(self)
        
        plain_QVBoxLayout=QVBoxLayout(self)
        main_QFormLayout.addRow(plain_QVBoxLayout)
        
        button_QHBoxLayout=QHBoxLayout(self)
        main_QFormLayout.addRow(button_QHBoxLayout)
        
        self.textPlane_QPlainTextEdit=QPlainTextEdit(self)
        plain_QVBoxLayout.addWidget(self.textPlane_QPlainTextEdit)

        self.left_QPushButton=QPushButton("left",self)
        button_QHBoxLayout.addWidget(self.left_QPushButton)
        self.left_QPushButton.clicked.connect(self.left_button_onClicked)
        
        self.center_QPushButton=QPushButton("center",self)
        button_QHBoxLayout.addWidget(self.center_QPushButton)
        self.center_QPushButton.clicked.connect(self.center_button_onClicked)
        
        self.right_QPushButton=QPushButton("right",self)
        button_QHBoxLayout.addWidget(self.right_QPushButton)
        self.right_QPushButton.clicked.connect(self.right_button_onClicked)

    def left_button_onClicked(self):
        print("base")
    def center_button_onClicked(self):
        print("base")
    def right_button_onClicked(self):
        print("base")

#window_instance=ScriptsRunWindowBase()
#window_instance.show()