from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from . import baseUI as UI

class CreateNodesWindow(UI.MainWindowBase):
    def __init__(self,*args,**kwargs):
        super(CreateNodesWindow,self).__init__(*args,**kwargs)
        self.setWindowFlags(Qt.Window)

        self.custom_QGridLayout.addWidget(self.createNodesWidget(),0,0)

    def createNodesWidget(self):
        pass