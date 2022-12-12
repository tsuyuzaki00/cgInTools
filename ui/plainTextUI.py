from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from ._reference import mainWindowUI as UI

class PlainTextWindowBase(UI.MainWindowBase):
    def __init__(self,*args,**kwargs):
        super(PlainTextWindowBase,self).__init__(*args,**kwargs)
        self.setWindowFlags(Qt.Window)

        self.textPlain_QPlainTextEdit=QPlainTextEdit(self)
        self.custom_QGridLayout.addWidget(self.textPlain_QPlainTextEdit,0,0)

viewWindow=PlainTextWindowBase()
viewWindow.show()