# -*- coding: iso-8859-15 -*-

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class ClickSelectWindowBase(QWidget):
    def __init__(self, *args, **kwargs):
        super(ClickSelectWindowBase, self).__init__(*args, **kwargs)
        self.setWindowFlags(Qt.Window)

        self.setObjectName("object_name")
        self.setWindowTitle("window_title")

        
        main_layout = QFormLayout(self)
        select_layout = QVBoxLayout(self)
        button01_layout = QHBoxLayout(self)
        type_layout = QVBoxLayout(self)
        button02_layout = QGridLayout(self)

        main_layout.addRow(select_layout)
        main_layout.addRow(button01_layout)
        main_layout.addRow(type_layout)
        main_layout.addRow(button02_layout)

        self.select_lisWig = QListWidget(self)
        self.create_button = QPushButton("create",self)
        self.delete_button = QPushButton("delete",self)
        self.type_combo = QComboBox(self)
        self.type_combo.addItems(["selections","connections","parent<childs","parents>child","lists"])
        self.set_button = QPushButton("set",self)
        self.add_button = QPushButton("add",self)
        self.edit_button = QPushButton("edit",self)
        self.clean_button = QPushButton("clean",self)
        
        select_layout.addWidget(self.select_lisWig)
        button01_layout.addWidget(self.create_button)
        button01_layout.addWidget(self.delete_button)
        type_layout.addWidget(self.type_combo)
        button02_layout.addWidget(self.set_button,0,0)
        button02_layout.addWidget(self.add_button,0,1)
        button02_layout.addWidget(self.edit_button,1,0)
        button02_layout.addWidget(self.clean_button,1,1)

        self.create_button.clicked.connect(self.create_button_onClicked)
        self.delete_button.clicked.connect(self.delete_button_onClicked)
        self.set_button.clicked.connect(self.set_button_onClicked)
        self.add_button.clicked.connect(self.add_button_onClicked)
        self.edit_button.clicked.connect(self.edit_button_onClicked)
        self.clean_button.clicked.connect(self.clean_button_onClicked)

    def create_button_onClicked(self):
        print("base")
    def delete_button_onClicked(self):
        print("base")
    def set_button_onClicked(self):
        print("base")
    def add_button_onClicked(self):
        print("base")
    def edit_button_onClicked(self):
        print("base")
    def clean_button_onClicked(self):
        print("base")

#window_instance = ClickSelectWindowBase()
#window_instance.show()