from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import json
class MainWindowBase(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(MainWindowBase,self).__init__(*args,**kwargs)
        self.setWindowFlags(Qt.Window)
        self.menuUI_create_func()
        self.mainUI_create_QGridLayout()
    
    #Single Function
    def convertString_query_dict(self,dictText_str):
        text_dict={}
        if not dictText_str is "" and not dictText_str is None:
            text_dict=eval(dictText_str)
        return text_dict

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

        UIText_QTabWidget=QTabWidget(self)
        main_QBoxLayout.addWidget(UIText_QTabWidget)

        custom_QWidget=QWidget()
        self.custom_QGridLayout=QGridLayout(self)
        custom_QWidget.setLayout(self.custom_QGridLayout)
        UIText_QTabWidget.addTab(custom_QWidget,"UI")

        self.textPlain_QPlainTextEdit=QPlainTextEdit(self)
        UIText_QTabWidget.addTab(self.textPlain_QPlainTextEdit,"Text")
        
        central_QWidget=QWidget()
        central_QWidget.setLayout(main_QBoxLayout)
        self.setCentralWidget(central_QWidget)
        
        button_QHBoxLayout=QHBoxLayout(self)
        main_QBoxLayout.addLayout(button_QHBoxLayout)

        self.buttonLeft_QPushButton=QPushButton("left",self)
        button_QHBoxLayout.addWidget(self.buttonLeft_QPushButton)
        self.buttonLeft_QPushButton.clicked.connect(self.buttonLeftClicked)

        self.buttonCenter_QPushButton=QPushButton("center",self)
        button_QHBoxLayout.addWidget(self.buttonCenter_QPushButton)
        self.buttonCenter_QPushButton.clicked.connect(self.buttonCenterClicked)
        
        self.buttonRight_QPushButton=QPushButton("right",self)
        button_QHBoxLayout.addWidget(self.buttonRight_QPushButton)
        self.buttonRight_QPushButton.clicked.connect(self.buttonRightClicked)
    
    #Multi Function
    def _setText_query_dict(self,text_dict):
        text_str=json.dumps(text_dict,indent=4).replace(": null",": None")
        self.textPlain_QPlainTextEdit.setPlainText(text_str)

    def _getText_query_dict(self):
        getText_str=self.textPlain_QPlainTextEdit.toPlainText()
        write_dict=self.convertString_query_dict(getText_str)
        return write_dict
    
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

