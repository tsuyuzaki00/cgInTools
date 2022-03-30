from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class SkinValueWindowBase(QWidget):
    def __init__(self, *args, **kwargs):
        super(SkinValueWindowBase, self).__init__(*args, **kwargs)
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle("skinValueWindow")

        main_layout = QFormLayout(self)
        value_layout = QHBoxLayout(self)
        option_layout = QHBoxLayout(self)

        main_layout.addRow("ValueNum", value_layout)
        main_layout.addRow(option_layout)

        button_0 = QPushButton("0")
        button_0001 = QPushButton("0.001")
        button_001 = QPushButton("0.01")
        button_005 = QPushButton("0.05")
        button_01 = QPushButton("0.1")
        button_05 = QPushButton("0.5")
        button_1 = QPushButton("1")

        value_layout.addWidget(button_0, True)
        value_layout.addWidget(button_0001, True)
        value_layout.addWidget(button_001, True)
        value_layout.addWidget(button_005, True)
        value_layout.addWidget(button_01, True)
        value_layout.addWidget(button_05, True)
        value_layout.addWidget(button_1, True)

        button_0.clicked.connect(self.button_0_onClicked)
        button_0001.clicked.connect(self.button_0001_onClicked)
        button_001.clicked.connect(self.button_001_onClicked)
        button_005.clicked.connect(self.button_005_onClicked)
        button_01.clicked.connect(self.button_01_onClicked)
        button_05.clicked.connect(self.button_05_onClicked)
        button_1.clicked.connect(self.button_1_onClicked)

        button_0.setStyleSheet('color: cyan;')
        button_0001.setStyleSheet('color: pink;')
        button_001.setStyleSheet('color: pink;')
        button_005.setStyleSheet('color: pink;')
        button_01.setStyleSheet('color: pink;')
        button_05.setStyleSheet('color: yellow;')
        button_1.setStyleSheet('color: yellow;')

        button_flood = QPushButton("flood")
        button_reverse = QPushButton("reverse")
        button_smooth = QPushButton("smooth")

        option_layout.addWidget(button_flood, True)
        option_layout.addWidget(button_reverse, True)
        option_layout.addWidget(button_smooth, True)
        
        button_flood.clicked.connect(self.button_flood_onClicked)
        button_reverse.clicked.connect(self.button_reverse_onClicked)
        button_smooth.clicked.connect(self.button_smooth_onClicked)

    def button_0_onClicked(self):
        print("base")
    def button_0001_onClicked(self):
        print("base")
    def button_001_onClicked(self):
        print("base")
    def button_005_onClicked(self):
        print("base")
    def button_01_onClicked(self):
        print("base")
    def button_05_onClicked(self):
        print("base")
    def button_1_onClicked(self):
        print("base")
    
    def button_flood_onClicked(self):
        print("base")
    def button_reverse_onClicked(self):
        print("base")
    def button_smooth_onClicked(self):
        print("base")

#window_instance = TargetPosWindowBase()
#window_instance.show()