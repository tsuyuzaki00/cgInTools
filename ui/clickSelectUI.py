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
        button00_layout = QHBoxLayout(self)
        select_layout = QVBoxLayout(self)
        button01_layout = QHBoxLayout(self)
        type_layout = QVBoxLayout(self)
        button02_layout = QGridLayout(self)

        itemLabel_layout = QVBoxLayout(self)
        selectLabel_layout = QVBoxLayout(self)
        containerLabel_layout = QVBoxLayout(self)

        main_layout.addRow(itemLabel_layout)
        main_layout.addRow(button00_layout)
        main_layout.addRow(select_layout)
        main_layout.addRow(containerLabel_layout)
        main_layout.addRow(type_layout)
        main_layout.addRow(button02_layout)
        main_layout.addRow(selectLabel_layout)
        main_layout.addRow(button01_layout)

        self.select_lisWig = QListWidget(self)
        self.item_label = QLabel("item",self)
        self.create_button = QPushButton("create",self)
        self.delete_button = QPushButton("delete",self)
        self.container_label = QLabel("container",self)
        self.type_combo = QComboBox(self)
        self.type_combo.addItems(["selections","connections","parent<childs","parents>child","lists"])
        self.set_button = QPushButton("set",self)
        self.add_button = QPushButton("add",self)
        self.edit_button = QPushButton("edit",self)
        self.clean_button = QPushButton("clean",self)
        self.select_label = QLabel("select",self)
        self.single_button = QPushButton("single",self)
        self.multi_button = QPushButton("multi",self)
        
        itemLabel_layout.addWidget(self.item_label)
        button00_layout.addWidget(self.create_button)
        button00_layout.addWidget(self.delete_button)
        select_layout.addWidget(self.select_lisWig)
        selectLabel_layout.addWidget(self.select_label)
        button01_layout.addWidget(self.single_button)
        button01_layout.addWidget(self.multi_button)
        containerLabel_layout.addWidget(self.container_label)
        type_layout.addWidget(self.type_combo)
        button02_layout.addWidget(self.set_button,0,0)
        button02_layout.addWidget(self.add_button,0,1)
        button02_layout.addWidget(self.edit_button,1,0)
        button02_layout.addWidget(self.clean_button,1,1)

        self.create_button.clicked.connect(self.create_button_onClicked)
        self.delete_button.clicked.connect(self.delete_button_onClicked)
        self.single_button.clicked.connect(self.single_button_onClicked)
        self.multi_button.clicked.connect(self.multi_button_onClicked)
        self.set_button.clicked.connect(self.set_button_onClicked)
        self.add_button.clicked.connect(self.add_button_onClicked)
        self.edit_button.clicked.connect(self.edit_button_onClicked)
        self.clean_button.clicked.connect(self.clean_button_onClicked)

    def create_button_onClicked(self):
        print("base")
    def delete_button_onClicked(self):
        print("base")
    def single_button_onClicked(self):
        print("base")
    def multi_button_onClicked(self):
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