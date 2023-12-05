from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class MainWindowBase(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(MainWindowBase,self).__init__(*args,**kwargs)
        self.setWindowFlags(Qt.Window)
        self.menuUI_create_func()
        self.custom_QGridLayout=self.mainUI_create_QGridLayout()
    
    #Single Function
    def menuUI_create_func(self):
        mainWindow_QMenuBar=self.menuBar()
        fileMenu_QAction=mainWindow_QMenuBar.addMenu("File")

        self.refresh_QAction=QAction("Refresh Settings",self)
        fileMenu_QAction.addAction(self.refresh_QAction)
        self.refresh_QAction.triggered.connect(self.refreshClicked)

        self.restore_QAction=QAction("Restore Settings",self)
        fileMenu_QAction.addAction(self.restore_QAction)
        self.restore_QAction.triggered.connect(self.restoreClicked)
        
        self.save_QAction=QAction("Save Settings",self)
        fileMenu_QAction.addAction(self.save_QAction)
        self.save_QAction.triggered.connect(self.saveClicked)
        
        fileMenu_QAction.addSeparator()
        
        self.import_QAction=QAction("Import Settings",self)
        fileMenu_QAction.addAction(self.import_QAction)
        self.import_QAction.triggered.connect(self.importClicked)
        
        self.export_QAction=QAction("Export Settings",self)
        fileMenu_QAction.addAction(self.export_QAction)
        self.export_QAction.triggered.connect(self.exportClicked)

    def mainUI_create_QGridLayout(self):
        main_QBoxLayout=QBoxLayout(QBoxLayout.TopToBottom,self)

        custom_QGridLayout=QGridLayout(self)
        main_QBoxLayout.addLayout(custom_QGridLayout)
        
        button_QHBoxLayout=QHBoxLayout(self)
        main_QBoxLayout.addLayout(button_QHBoxLayout)

        central_QWidget=QWidget()
        central_QWidget.setLayout(main_QBoxLayout)
        self.setCentralWidget(central_QWidget)

        self.buttonLeft_QPushButton=QPushButton("left",self)
        button_QHBoxLayout.addWidget(self.buttonLeft_QPushButton)
        self.buttonLeft_QPushButton.clicked.connect(self.buttonLeftClicked)

        self.buttonCenter_QPushButton=QPushButton("center",self)
        button_QHBoxLayout.addWidget(self.buttonCenter_QPushButton)
        self.buttonCenter_QPushButton.clicked.connect(self.buttonCenterClicked)
        
        self.buttonRight_QPushButton=QPushButton("right",self)
        button_QHBoxLayout.addWidget(self.buttonRight_QPushButton)
        self.buttonRight_QPushButton.clicked.connect(self.buttonRightClicked)
        
        return custom_QGridLayout
    
    #Public Function
    def refreshClicked(self):
        print("refresh")
    def restoreClicked(self):
        print("restore")
    def saveClicked(self):
        print("save")
    def importClicked(self):
        print("import")
    def exportClicked(self):
        print("export")

    def buttonLeftClicked(self):
        print("left")
    def buttonCenterClicked(self):
        print("center")
    def buttonRightClicked(self):
        print("right")
    
    def buttonClicked(self):
        print("base")

#viewWindow=MainWindowBase()
#viewWindow.show()

