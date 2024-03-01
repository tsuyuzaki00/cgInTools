from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import cgInTools as cit
from . import baseUI as UI
cit.reloads([UI])

class PlainTextWindowBase(UI.MainWindowBase):
    def __init__(self,*args,**kwargs):
        super(PlainTextWindowBase,self).__init__(*args,**kwargs)
        self.setWindowFlags(Qt.Window)
        
        self.textPlain_QPlainTextEdit=QPlainTextEdit(self)
        self.custom_QScrollArea.setWidget(self.textPlain_QPlainTextEdit)

#viewWindow=PlainTextWindowBase()
#viewWindow.show()