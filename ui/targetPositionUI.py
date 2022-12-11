from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class TargetPosWindowBase(QWidget):
    def __init__(self,*args,**kwargs):
        super(TargetPosWindowBase,self).__init__(*args, **kwargs)
        self.setWindowFlags(Qt.Window)

        self.setObjectName("object_name")
        self.setWindowTitle("window_title")

        main_QFormLayout=QFormLayout(self)

        position_QGridLayout=QGridLayout(self)
        main_QFormLayout.addRow(position_QGridLayout)

        self.objectText_QGridLayout=QGridLayout(self)
        main_QFormLayout.addRow(self.objectText_QGridLayout)

        button_QHBoxLayout=QHBoxLayout(self)
        main_QFormLayout.addRow(button_QHBoxLayout)
        
        self.position_QButtonGroup=QButtonGroup()

        self.position_QLabel=QLabel("Position:",self)
        position_QGridLayout.addWidget(self.position_QLabel,0,0)

        self.up_QRadioButton=QRadioButton("up",self)
        position_QGridLayout.addWidget(self.up_QRadioButton,0,2)
        self.position_QButtonGroup.addButton(self.up_QRadioButton,1)

        self.back_QRadioButton=QRadioButton("back",self)
        position_QGridLayout.addWidget(self.back_QRadioButton,0,3)
        self.position_QButtonGroup.addButton(self.back_QRadioButton,2)

        self.left_QRadioButton=QRadioButton("left",self)
        position_QGridLayout.addWidget(self.left_QRadioButton,1,1)
        self.position_QButtonGroup.addButton(self.left_QRadioButton,3)
        
        self.center_QRadioButton=QRadioButton("center",self)
        position_QGridLayout.addWidget(self.center_QRadioButton,1,2)
        self.position_QButtonGroup.addButton(self.center_QRadioButton,4)
        self.center_QRadioButton.toggle()
        
        self.right_QRadioButton=QRadioButton("right",self)
        position_QGridLayout.addWidget(self.right_QRadioButton,1,3)
        self.position_QButtonGroup.addButton(self.right_QRadioButton,5)
        
        self.front_QRadioButton=QRadioButton("front",self)
        position_QGridLayout.addWidget(self.front_QRadioButton,2,1)
        self.position_QButtonGroup.addButton(self.front_QRadioButton,6)
        
        self.down_QRadioButton=QRadioButton("down",self)
        position_QGridLayout.addWidget(self.down_QRadioButton,2,2)
        self.position_QButtonGroup.addButton(self.down_QRadioButton,7)

        self.source_QLabel=QLabel("Obj Source:",self)
        self.objectText_QGridLayout.addWidget(self.source_QLabel,0,0)

        self.source_QLineEdit=QLineEdit(self)
        self.objectText_QGridLayout.addWidget(self.source_QLineEdit,0,1)
        
        self.source_QPushButton=QPushButton("<<",self)
        self.objectText_QGridLayout.addWidget(self.source_QPushButton,0,2)
        self.source_QPushButton.clicked.connect(self.buttonSource_onClicked_func)
        
        self.target_QLabel=QLabel(">Pos Target:",self)
        self.objectText_QGridLayout.addWidget(self.target_QLabel,0,3)
        
        self.target_QLineEdit=QLineEdit(self)
        self.objectText_QGridLayout.addWidget(self.target_QLineEdit,0,4)
        
        self.target_QPushButton=QPushButton("<<",self)
        self.objectText_QGridLayout.addWidget(self.target_QPushButton,0,5)
        self.target_QPushButton.clicked.connect(self.buttonTarget_onClicked_func)

        self.left_QPushButton=QPushButton("left",self)
        button_QHBoxLayout.addWidget(self.left_QPushButton)
        self.left_QPushButton.clicked.connect(self.buttonLeft_onClicked_func)

        self.center_QPushButton=QPushButton("center",self)
        button_QHBoxLayout.addWidget(self.center_QPushButton)
        self.center_QPushButton.clicked.connect(self.buttonCenter_onClicked_func)

        self.right_QPushButton=QPushButton("right",self)
        button_QHBoxLayout.addWidget(self.right_QPushButton)
        self.right_QPushButton.clicked.connect(self.buttonRight_onClicked_func)

    def buttonSource_onClicked_func(self):
        print("base")
    def buttonTarget_onClicked_func(self):
        print("base")
    def buttonLeft_onClicked_func(self):
        print("base")
    def buttonCenter_onClicked_func(self):
        print("base")
    def buttonRight_onClicked_func(self):
        print("base")

#window_instance = TargetPosWindowBase()
#window_instance.show()