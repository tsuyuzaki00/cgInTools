from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class MgearDictWindowBase(QWidget):
    def __init__(self, *args, **kwargs):
        super(MgearDictWindowBase, self).__init__(*args, **kwargs)
        self.setWindowFlags(Qt.Window)

        self.setObjectName("object_name")
        self.setWindowTitle("window_title")

        main_layout = QFormLayout(self)
        load_layout = QFormLayout(self)
        list_layout = QVBoxLayout(self)
        box_layout = QGridLayout(self)

        main_layout.addRow(load_layout)
        main_layout.addRow(list_layout)
        main_layout.addRow(box_layout)

        self.path_text = QLineEdit(self)
        self.name_text = QLineEdit(self)
        self.mode_text = QLineEdit("03_main",self)
        self.load_button = QPushButton("text",self)
        self.set_button = QPushButton("set",self)
        self.add_button = QPushButton("add",self)
        self.edit_button = QPushButton("edit",self)
        self.import_button = QPushButton("import",self)
        self.export_button = QPushButton("export",self)
        self.file_button = QPushButton("file",self) 

        self.guide = QRadioButton("guide",self)
        self.jskin = QRadioButton("jskin",self)
        self.gimmick_joints = QRadioButton("gimmick_joints",self)

        #self.list_table = QTableView(self)
        #self.docment_view = QListView(self)
        
        load_layout.addRow("path",self.path_text)
        load_layout.addRow("name",self.name_text)
        load_layout.addRow("mode",self.mode_text)
        load_layout.addRow(self.load_button)

        list_layout.addWidget(self.guide)
        list_layout.addWidget(self.jskin)
        list_layout.addWidget(self.gimmick_joints)
        #list_layout.addWidget(self.list_table)
        #list_layout.addWidget(self.docment_view)

        box_layout.addWidget(self.set_button,0,0)
        box_layout.addWidget(self.add_button,0,1)
        box_layout.addWidget(self.edit_button,0,2)
        box_layout.addWidget(self.import_button,1,0)
        box_layout.addWidget(self.export_button,1,1)
        box_layout.addWidget(self.file_button,1,2)

        self.load_button.clicked.connect(self.load_button_onClicked)
        self.set_button.clicked.connect(self.set_button_onClicked)
        self.add_button.clicked.connect(self.add_button_onClicked)
        self.edit_button.clicked.connect(self.edit_button_onClicked)
        self.import_button.clicked.connect(self.import_button_onClicked)
        self.export_button.clicked.connect(self.export_button_onClicked)
        self.file_button.clicked.connect(self.file_button_onClicked)

    def load_button_onClicked(self):
        print("base")
    def set_button_onClicked(self):
        print("base")
    def add_button_onClicked(self):
        print("base")
    def edit_button_onClicked(self):
        print("base")
    def import_button_onClicked(self):
        print("base")
    def export_button_onClicked(self):
        print("base")
    def file_button_onClicked(self):
        print("base")

#window_instance = MgearDictWindow()
#window_instance.show()

##########################################################
# ここからMaya依存にしたGUIを作っていきます。
##########################################################
from maya import cmds
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance

# MgearDictWindowBase継承したMaya用のクラス
class MayaMgearDictWindow(MgearDictWindowBase):
    def __init__(self, parent):
        super(MayaMgearDictWindow, self).__init__(parent)
        self.setObjectName("mgear_dict")
        self.setWindowTitle("mgear_dicts")
        self.load_button.setText("load")
        self.guide.setChecked(True)
        
    def load_button_onClicked(self):
        load_paths()
    def set_button_onClicked(self):
        set_json()
    def add_button_onClicked(self):
        add_json()
    def edit_button_onClicked(self):
        edit_json()
    def import_button_onClicked(self):
        import_json()
    def export_button_onClicked(self):
        export_json()
    def file_button_onClicked(self):
        file_json()

# mayaのメインウインドウを取得する
def get_maya_main_window():
    omui.MQtUtil.mainWindow()
    ptr = omui.MQtUtil.mainWindow()
    widget = wrapInstance(long(ptr), QWidget)
    return widget

# 依存関係のないウインドウを継承して作ったMaya用のボタンUI
maya_window_instance = MayaMgearDictWindow(parent=get_maya_main_window())
maya_window_instance.show()

# 実行関数
def load_paths():
    print("Maya load Clicked")

def set_json():
    print("Maya set Clicked")

def add_json():
    print("Maya add Clicked")

def edit_json():
    print("Maya edit Clicked")

def import_json():
    print("Maya import Clicked")

def export_json():
    print("Maya export Clicked")

def file_json():
    print("Maya file Clicked")