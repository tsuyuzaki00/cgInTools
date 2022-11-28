from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class MainWindowBase(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(MainWindowBase,self).__init__(*args,**kwargs)
        self.setWindowFlags(Qt.Window)
        
        mainWindow_QMenuBar=self.menuBar()
        self.refresh_QAction=QAction("Refresh Settings",self)
        self.restore_QAction=QAction("Restore Settings",self)
        self.save_QAction=QAction("Save Settings",self)
        self.import_QAction=QAction("Import Settings",self)
        self.export_QAction=QAction("Export Settings",self)

        fileMenu_QAction=mainWindow_QMenuBar.addMenu("File")
        fileMenu_QAction.addAction(self.refresh_QAction)
        fileMenu_QAction.addAction(self.restore_QAction)
        fileMenu_QAction.addAction(self.save_QAction)
        fileMenu_QAction.addSeparator()
        fileMenu_QAction.addAction(self.import_QAction)
        fileMenu_QAction.addAction(self.export_QAction)

        self.refresh_QAction.triggered.connect(self.refresh_onClicked_func)
        self.restore_QAction.triggered.connect(self.restore_onClicked_func)
        self.save_QAction.triggered.connect(self.save_onClicked_func)
        self.import_QAction.triggered.connect(self.import_onClicked_func)
        self.export_QAction.triggered.connect(self.export_onClicked_func)

        main_QHBoxLayout=QVBoxLayout(self)
        button_QHBoxLayout=QHBoxLayout(self)
        self.edit_QFormLayout=QFormLayout(self)
        main_QHBoxLayout.addLayout(self.edit_QFormLayout)
        main_QHBoxLayout.addLayout(button_QHBoxLayout)

        self.center_QWidget=QWidget()
        self.center_QWidget.setLayout(main_QHBoxLayout)
        self.setCentralWidget(self.center_QWidget)

        self.buttonLeft_QPushButton=QPushButton("left",self)
        self.buttonCenter_QPushButton=QPushButton("center",self)
        self.buttonRight_QPushButton=QPushButton("right",self)

        button_QHBoxLayout.addWidget(self.buttonLeft_QPushButton)
        button_QHBoxLayout.addWidget(self.buttonCenter_QPushButton)
        button_QHBoxLayout.addWidget(self.buttonRight_QPushButton)

        self.buttonLeft_QPushButton.clicked.connect(self.buttonLeft_onClicked_func)
        self.buttonCenter_QPushButton.clicked.connect(self.buttonCenter_onClicked_func)
        self.buttonRight_QPushButton.clicked.connect(self.buttonRight_onClicked_func)
        
    def buttonLeft_onClicked_func(self):
        print("base")
    def buttonCenter_onClicked_func(self):
        print("base")
    def buttonRight_onClicked_func(self):
        print("base")
    def refresh_onClicked_func(self):
        print("base")
    def restore_onClicked_func(self):
        print("base")
    def save_onClicked_func(self):
        print("base")
    def import_onClicked_func(self):
        print("base")
    def export_onClicked_func(self):
        print("base")

#window_instance=MainWindowBase()
#window_instance.show()

