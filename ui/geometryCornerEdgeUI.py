from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import cgInTools as cit
from cgInTools.ui._reference import mayaWindowUI as UI
cit.reloads([UI])

class ObjCornerEdgeOPBase(UI.MainWindowBase):
    def __init__(self,*args,**kwargs):
        super(ObjCornerEdgeOPBase,self).__init__(*args, **kwargs)
        self.setObjectName("objectCornerEdge")
        self.setWindowTitle("objectCornerEdgeOption")

        self.lowAngle_QSpinBox=QSpinBox(self)
        self.highAngle_QSpinBox=QSpinBox(self)

        self.lowAngle_QSpinBox.setMaximum(180)
        self.lowAngle_QSpinBox.setSingleStep(15)
        self.lowAngle_QSpinBox.setBaseSize(300,50)
        
        self.highAngle_QSpinBox.setMaximum(180)
        self.highAngle_QSpinBox.setSingleStep(15)
        self.highAngle_QSpinBox.setBaseSize(300,50)

        self.edit_QFormLayout.addRow("lowAngle:",self.lowAngle_QSpinBox)
        self.edit_QFormLayout.addRow("highAngle:",self.highAngle_QSpinBox)

        self.buttonLeft_QPushButton.setText("run")
        self.buttonCenter_QPushButton.setText("apply")
        self.buttonRight_QPushButton.setText("close")
                
#window_instance=ObjCornerEdgeOPBase()
#window_instance.show()