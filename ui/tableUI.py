from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from maya import cmds

import cgInTools as cit
from . import baseUI as UI
from . import selfUI as sUI
cit.reloads([UI,sUI])

class TableWindowBase(UI.MainWindowBase):
    def __init__(self,*args,**kwargs):
        super(TableWindowBase,self).__init__(*args,**kwargs)
        self.setWindowFlags(Qt.Window)
        
        self.table_SelfTableWidget=sUI.SelfTableWidget(self)
        self.custom_QScrollArea.setWidget(self.table_SelfTableWidget)

#viewWindow=TableWindowBase()
#viewWindow.show()