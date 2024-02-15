from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import cgInTools as cit
from . import dataUI as dLB
cit.reloads([dLB])

class SelfLineEdit(QLineEdit):
    def __init__(self,*args,**kwargs):
        super(SelfLineEdit,self).__init__(*args,**kwargs)
        

    def setLine(self,variable):
        pass

class SelfTextEdit(QTextEdit):
    def __init__(self,*args,**kwargs):
        super(SelfTextEdit,self).__init__(*args,**kwargs)

class SelfComboBox(QComboBox):
    def __init__(self,*args,**kwargs):
        super(SelfComboBox,self).__init__(*args,**kwargs)

class SelfSpinBox(QSpinBox):
    def __init__(self,*args,**kwargs):
        super(SelfSpinBox,self).__init__(*args,**kwargs)

class SelfTableWidget(QTableWidget):
    def __init__(self,*args,**kwargs):
        super(SelfTableWidget,self).__init__(*args,**kwargs)
        self._headerReverse_bool=False
        self._headerLabel_strs=[]
        self._tableWidgetItem_lists=[]

    #Private Function
    def __header_create_strs(self,headerLabel_strs,headerReverse=False):
        if headerReverse:
            self.setRowCount(len(headerLabel_strs))
            self.setVerticalHeaderLabels(headerLabel_strs)
        else:
            self.setColumnCount(len(headerLabel_strs))
            self.setHorizontalHeaderLabels(headerLabel_strs)
        return headerLabel_strs

    def __tableItem_create_func(self,tableWidgetItem_lists,headerReverse=False):   
        if headerReverse:
            self.setColumnCount(len(tableWidgetItem_lists))
        else:
            self.setRowCount(len(tableWidgetItem_lists))

        for row,item_strs in enumerate(tableWidgetItem_lists):
            for col,item_str in enumerate(item_strs):
                item_DataTableWidget=dLB.DataTableWidget(item_str)
                if headerReverse:
                    self.setItem(col,row,item_DataTableWidget)
                else:
                    self.setItem(row,col,item_DataTableWidget)

    #Setting Function
    def getColumnCount(self):
        return self.columnCount
        
    def getRowCount(self):
        return self.rowCount
    
    def getDataTableWidget(self,column,row):
        return self.item(row,column)

    def setHeaderReverseBool(self,validate):
        self._headerReverse_bool=validate
        return self._headerReverse_bool
    def getHeaderReverseBool(self):
        return self._headerReverse_bool

    def setHeaderLabelStrs(self,validate):
        self._headerLabel_strs=validate
        return self._headerLabel_strs
    def getHeaderLabelStrs(self):
        return self._headerLabel_strs

    def setDataTableWidgetLists(self,variables):
        self._tableWidgetItem_lists=variables
        return self._tableWidgetItem_lists
    def getDataTableWidgetLists(self):
        return self._tableWidgetItem_lists
    
    #Public Function
    def createBase(self):
        self.__header_create_strs(self._headerLabel_strs,self._headerReverse_bool)

    def createTable(self):
        self.__header_create_strs(self._headerLabel_strs,self._headerReverse_bool)
        self.__tableItem_create_func(self._tableWidgetItem_lists,self._headerReverse_bool)

    def queryTableLists(self):
        row_ints=self.rowCount()
        column_ints=self.columnCount()
        table_lists=[]
        for row_int in range(row_ints):
            row_strs=[]
            for column_int in range(column_ints):
                item_QTableWidgetItem=self.item(row_int,column_int)
                if item_QTableWidgetItem is not None:
                    row_strs.append(item_QTableWidgetItem.text())
                else:
                    row_strs.append('')
            table_lists.append(row_strs)
        return table_lists