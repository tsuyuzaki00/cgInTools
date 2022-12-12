from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from ._reference import mainWindowUI as UI

class TableWindowBase(UI.MainWindowBase):
    def __init__(self,*args,**kwargs):
        super(TableWindowBase,self).__init__(*args,**kwargs)
        self.setWindowFlags(Qt.Window)

        self.table_QTableWidget=QTableWidget()
        self.custom_QGridLayout.addWidget(self.table_QTableWidget,0,0)
        self.headerAsix="Horizontal"
        self.headerTitle_list=["Select","Subject"]
        self.data_lists=[["",""],["",""]]
    
    #Single Function
    def headerTitle_create_func(self,headerTitle_list,QTableWidget,headerAsix="Horizontal"):
        if headerAsix is "Horizontal":
            QTableWidget.setColumnCount(len(headerTitle_list))
            QTableWidget.setHorizontalHeaderLabels(headerTitle_list)
        elif headerAsix is "Vertical":
            QTableWidget.setRowCount(len(headerTitle_list))
            QTableWidget.setVerticalHeaderLabels(headerTitle_list)
        
    def tableItem_create_func(self,data_lists,QTableWidget,headerAsix="Horizontal"):   
        if headerAsix is "Horizontal":
            QTableWidget.setRowCount(len(data_lists))
        elif headerAsix is "Vertical":
            QTableWidget.setColumnCount(len(data_lists))

        for row,colData in enumerate(data_lists):
            for col,value in enumerate(colData):
                item_QTableWidgetItem=QTableWidgetItem(value)
                if headerAsix is "Horizontal":
                    QTableWidget.setItem(row,col,item_QTableWidgetItem)
                elif headerAsix is "Vertical":
                    QTableWidget.setItem(col,row,item_QTableWidgetItem)

    #Public Function
    def createHeaderTitle(self):
        self.headerTitle_create_func(self.headerTitle_list,self.table_QTableWidget,self.headerAsix)

    def createTableItem(self):
        self.tableItem_create_func(self.data_lists,self.table_QTableWidget,self.headerAsix)

#viewWindow=TableWindowBase()
#viewWindow.show()