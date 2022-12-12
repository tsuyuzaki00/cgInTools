from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class MainWindowBase(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(MainWindowBase,self).__init__(*args,**kwargs)
        self.setWindowFlags(Qt.Window)
        
        #menu UI
        mainWindow_QMenuBar=self.menuBar()
        fileMenu_QAction=mainWindow_QMenuBar.addMenu("File")

        self.refresh_QAction=QAction("Refresh Settings",self)
        fileMenu_QAction.addAction(self.refresh_QAction)
        self.refresh_QAction.triggered.connect(self.refreshOnClicked)

        self.restore_QAction=QAction("Restore Settings",self)
        fileMenu_QAction.addAction(self.restore_QAction)
        self.restore_QAction.triggered.connect(self.restoreOnClicked)
        
        self.save_QAction=QAction("Save Settings",self)
        fileMenu_QAction.addAction(self.save_QAction)
        self.save_QAction.triggered.connect(self.saveOnClicked)
        
        fileMenu_QAction.addSeparator()
        
        self.import_QAction=QAction("Import Settings",self)
        fileMenu_QAction.addAction(self.import_QAction)
        self.import_QAction.triggered.connect(self.importOnClicked)
        
        self.export_QAction=QAction("Export Settings",self)
        fileMenu_QAction.addAction(self.export_QAction)
        self.export_QAction.triggered.connect(self.exportOnClicked)

        #main UI
        main_QBoxLayout=QBoxLayout(QBoxLayout.TopToBottom,self)

        self.custom_QGridLayout=QGridLayout(self)
        main_QBoxLayout.addLayout(self.custom_QGridLayout)
        
        button_QHBoxLayout=QHBoxLayout(self)
        main_QBoxLayout.addLayout(button_QHBoxLayout)

        central_QWidget=QWidget()
        central_QWidget.setLayout(main_QBoxLayout)
        self.setCentralWidget(central_QWidget)

        self.buttonLeft_QPushButton=QPushButton("left",self)
        button_QHBoxLayout.addWidget(self.buttonLeft_QPushButton)
        self.buttonLeft_QPushButton.clicked.connect(self.buttonLeftOnClicked)

        self.buttonCenter_QPushButton=QPushButton("center",self)
        button_QHBoxLayout.addWidget(self.buttonCenter_QPushButton)
        self.buttonCenter_QPushButton.clicked.connect(self.buttonCenterOnClicked)
        
        self.buttonRight_QPushButton=QPushButton("right",self)
        button_QHBoxLayout.addWidget(self.buttonRight_QPushButton)
        self.buttonRight_QPushButton.clicked.connect(self.buttonRightOnClicked)
        
    def refreshOnClicked(self):
        print("refresh")
    def restoreOnClicked(self):
        print("restore")
    def saveOnClicked(self):
        print("save")
    def importOnClicked(self):
        print("import")
    def exportOnClicked(self):
        print("export")

    def buttonLeftOnClicked(self):
        print("left")
    def buttonCenterOnClicked(self):
        print("center")
    def buttonRightOnClicked(self):
        print("right")
    
    def buttonOnClicked(self):
        print("base")

#viewWindow=MainWindowBase()
#viewWindow.show()

