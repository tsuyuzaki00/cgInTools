from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class TargetPosWindowBase(QWidget):
    def __init__(self, *args, **kwargs):
        super(TargetPosWindowBase, self).__init__(*args, **kwargs)
        self.setWindowFlags(Qt.Window)

        self.setObjectName("object_name")
        self.setWindowTitle("window_title")

        main_layout = QFormLayout(self)
        button_layout = QHBoxLayout(self)
        position_layout = QGridLayout(self)
        self.obj_text_layout = QGridLayout(self)

        main_layout.addRow(self.obj_text_layout)
        main_layout.addRow(position_layout)
        main_layout.addRow(button_layout)

        self.left_button = QPushButton("left",self)
        self.center_button = QPushButton("center",self)
        self.right_button = QPushButton("right",self)
        
        self.position_label = QLabel("Position:",self)
        self.up_radio = QRadioButton("up",self)
        self.back_radio = QRadioButton("back",self)
        self.left_radio = QRadioButton("left",self)
        self.center_radio = QRadioButton("center",self)
        self.right_radio = QRadioButton("right",self)
        self.front_radio = QRadioButton("front",self)
        self.down_radio = QRadioButton("down",self)

        self.target_label = QLabel("Obj Source:",self)
        self.source_label = QLabel(">Pos Target:",self)
        self.target_line = QLineEdit(self)
        self.source_line = QLineEdit(self)
        self.target_button = QPushButton("<<",self)
        self.source_button = QPushButton("<<",self)
        
        button_layout.addWidget(self.left_button)
        button_layout.addWidget(self.center_button)
        button_layout.addWidget(self.right_button)

        self.position_group = QButtonGroup()
        self.position_group.addButton(self.up_radio,1)
        self.position_group.addButton(self.back_radio,2)
        self.position_group.addButton(self.left_radio,3)
        self.position_group.addButton(self.center_radio,4)
        self.position_group.addButton(self.right_radio,5)
        self.position_group.addButton(self.front_radio,6)
        self.position_group.addButton(self.down_radio,7)
        self.center_radio.toggle()

        position_layout.addWidget(self.position_label,0,0)
        position_layout.addWidget(self.up_radio,0,2)
        position_layout.addWidget(self.back_radio,0,3)
        position_layout.addWidget(self.left_radio,1,1)
        position_layout.addWidget(self.center_radio,1,2)
        position_layout.addWidget(self.right_radio,1,3)
        position_layout.addWidget(self.front_radio,2,1)
        position_layout.addWidget(self.down_radio,2,2)

        self.obj_text_layout.addWidget(self.target_label,0,0)
        self.obj_text_layout.addWidget(self.target_line,0,1)
        self.obj_text_layout.addWidget(self.target_button,0,2)
        self.obj_text_layout.addWidget(self.source_label,0,3)
        self.obj_text_layout.addWidget(self.source_line,0,4)
        self.obj_text_layout.addWidget(self.source_button,0,5)

        self.left_button.clicked.connect(self.left_button_onClicked)
        self.center_button.clicked.connect(self.center_button_onClicked)
        self.right_button.clicked.connect(self.right_button_onClicked)
        self.source_button.clicked.connect(self.source_button_onClicked)
        self.target_button.clicked.connect(self.target_button_onClicked)

    def left_button_onClicked(self):
        print("base")
    def center_button_onClicked(self):
        print("base")
    def right_button_onClicked(self):
        print("base")
    def source_button_onClicked(self):
        print("base")
    def target_button_onClicked(self):
        print("base")

#window_instance = TargetPosWindowBase()
#window_instance.show()