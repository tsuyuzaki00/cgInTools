from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from ._reference import mainWindowUI as UI

class ObjCornerEdgeOPBase(UI.MainWindowBase):
    def __init__(self,*args,**kwargs):
        super(ObjCornerEdgeOPBase,self).__init__(*args, **kwargs)
        self.setObjectName("objectCornerEdge")
        self.setWindowTitle("objectCornerEdgeOption")
        self.buttonLeft_QPushButton.setText("run")
        self.buttonCenter_QPushButton.setText("apply")
        self.buttonRight_QPushButton.setText("close")

        lowAngle_QLabel=QLabel("lowAngle:",self)
        self.custom_QGridLayout.addWidget(lowAngle_QLabel,0,0)

        self.lowAngle_QSpinBox=QSpinBox(self)
        self.lowAngle_QSpinBox.setMaximum(180)
        self.lowAngle_QSpinBox.setSingleStep(15)
        self.lowAngle_QSpinBox.setBaseSize(300,50)
        self.custom_QGridLayout.addWidget(self.lowAngle_QSpinBox,0,1)

        highAngle_QLabel=QLabel("highAngle:",self)
        self.custom_QGridLayout.addWidget(highAngle_QLabel,1,0)
        
        self.highAngle_QSpinBox=QSpinBox(self)
        self.highAngle_QSpinBox.setMaximum(180)
        self.highAngle_QSpinBox.setSingleStep(15)
        self.highAngle_QSpinBox.setBaseSize(300,50)
        self.custom_QGridLayout.addWidget(self.highAngle_QSpinBox,1,1)
                
#viewWindow=ObjCornerEdgeOPBase()
#viewWindow.show()