from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *


class DataTableWidget(QTableWidgetItem):
    def __init__(self,*args,**kwargs):
        super(DataTableWidget,self).__init__(*args,**kwargs)
        