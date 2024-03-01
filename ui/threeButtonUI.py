from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class ThreeButtonWindowBase(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(ThreeButtonWindowBase,self).__init__(*args,**kwargs)
        self.setWindowFlags(Qt.Window)
        self._mainUI_create_func() # self.custom_QScrollArea.setWidget()

    #Multi Function
    def _mainUI_create_func(self):
        main_QBoxLayout=QBoxLayout(QBoxLayout.TopToBottom,self)

        self.custom_QScrollArea=QScrollArea(self)
        self.custom_QScrollArea.setWidgetResizable(True)
        main_QBoxLayout.addWidget(self.custom_QScrollArea)
        
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

    def buttonLeftClicked(self):
        print("left")
    def buttonCenterClicked(self):
        print("center")
    def buttonRightClicked(self):
        print("right")
    
    def buttonClicked(self):
        print("base")

#viewWindow=ThreeButtonWindowBase()
#viewWindow.show()