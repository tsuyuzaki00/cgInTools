from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class DockWindowBase(QDockWidget):
    def __init__(self,*args,**kwargs):
        super(DockWindowBase,self).__init__(*args,**kwargs)
        self.setWindowFlags(Qt.Window)

        #main UI
        main_QWidget=QWidget()
        self.setWidget(main_QWidget)
        
        main_QBoxLayout=QBoxLayout(QBoxLayout.TopToBottom,self)
        main_QWidget.setLayout(main_QBoxLayout)

        self.custom_QGridLayout=QGridLayout(self)
        main_QBoxLayout.addLayout(self.custom_QGridLayout)
        
        button_QHBoxLayout=QHBoxLayout(self)
        main_QBoxLayout.addLayout(button_QHBoxLayout)

        self.buttonLeft_QPushButton=QPushButton("left",self)
        button_QHBoxLayout.addWidget(self.buttonLeft_QPushButton)
        self.buttonLeft_QPushButton.clicked.connect(self.buttonLeftOnClicked)

        self.buttonCenter_QPushButton=QPushButton("center",self)
        button_QHBoxLayout.addWidget(self.buttonCenter_QPushButton)
        self.buttonCenter_QPushButton.clicked.connect(self.buttonCenterOnClicked)
        
        self.buttonRight_QPushButton=QPushButton("right",self)
        button_QHBoxLayout.addWidget(self.buttonRight_QPushButton)
        self.buttonRight_QPushButton.clicked.connect(self.buttonRightOnClicked)

    def buttonLeftOnClicked(self):
        print("left")
    def buttonCenterOnClicked(self):
        print("center")
    def buttonRightOnClicked(self):
        print("right")
    
    def buttonOnClicked(self):
        print("base")

#viewWindow=DockWindowBase()
#viewWindow.show()

