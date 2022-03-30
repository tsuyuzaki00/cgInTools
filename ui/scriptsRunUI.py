from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class ScriptsRunWindowBase(QWidget):
    def __init__(self, *args, **kwargs):
        super(ScriptsRunWindowBase, self).__init__(*args, **kwargs)
        self.setWindowFlags(Qt.Window)

        self.setObjectName("object_name")
        self.setWindowTitle("window_title")

        main_layout = QFormLayout(self)
        plain_layout = QVBoxLayout(self)
        button_layout = QHBoxLayout(self)

        main_layout.addRow(plain_layout)
        main_layout.addRow(button_layout)

        self.scripts_plain = QPlainTextEdit(self)
        self.left_button = QPushButton("left",self)
        self.center_button = QPushButton("center",self)
        self.right_button = QPushButton("right",self)
        
        button_layout.addWidget(self.left_button)
        button_layout.addWidget(self.center_button)
        button_layout.addWidget(self.right_button)
        plain_layout.addWidget(self.scripts_plain)

        self.left_button.clicked.connect(self.left_button_onClicked)
        self.center_button.clicked.connect(self.center_button_onClicked)
        self.right_button.clicked.connect(self.right_button_onClicked)

    def left_button_onClicked(self):
        print("base")
    def center_button_onClicked(self):
        print("base")
    def right_button_onClicked(self):
        print("base")

#window_instance = ScriptsRunWindowBase()
#window_instance.show()