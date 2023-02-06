from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from maya import cmds

from ._reference import mainWindowUI as UI

class TableWindowBase(UI.MainWindowBase):
    def __init__(self,*args,**kwargs):
        super(TableWindowBase,self).__init__(*args,**kwargs)
        self.setWindowFlags(Qt.Window)
        #self.__sample()

    #Summary Function
    def __sample(self):
        self.sample_CTableWidget=CTableWidget()
        self.custom_QGridLayout.addWidget(self.sample_CTableWidget)
        self.sample_CTableWidget.setHeaderLabelList(["Name","Value"])
        self.sample_CTableWidget.setHeaderAsixStr("Vertical")# Horizontal or Vertical
        self.sample_CTableWidget.setTableParamLists([["A","B"]])
        #self.sample_CTableWidget.addTableParamLists([["A","B"],["C","D"]])
        #self.sample_CTableWidget.createBase()
        self.sample_CTableWidget.createTable()

class CTableWidget(QTableWidget):
    def __init__(self,*args,**kwargs):
        super(CTableWidget,self).__init__(*args,**kwargs)
        self._headerAsix_str="Horizontal"
        self._headerLabel_list=[]
        self._tableParam_lists=[]#[[str(0,0),str(0,1)],[str(1,0),str(1,1)]],
    
    #Single Function
    def headerCount_check_func(self,header,relationList):
        if not len(header) == len(relationList):
            cmds.error("count Error headerList:"+len(header)+" TableList:"+len(relationList))

    #Private Function
    def __header_create_list(self,headerLabel_list,headerAsix="Horizontal"):
        if headerAsix == "Horizontal":
            self.setColumnCount(len(headerLabel_list))
            self.setHorizontalHeaderLabels(headerLabel_list)
        elif headerAsix == "Vertical":
            self.setRowCount(len(headerLabel_list))
            self.setVerticalHeaderLabels(headerLabel_list)
            print("test")
        return headerLabel_list

    def __tableItem_create_func(self,tableParam_lists,headerAsix="Horizontal"):   
        if headerAsix == "Horizontal":
            self.setRowCount(len(tableParam_lists))
        elif headerAsix == "Vertical":
            self.setColumnCount(len(tableParam_lists))

        for row,colData in enumerate(tableParam_lists):
            for col,value in enumerate(colData):
                item_QTableWidgetItem=QTableWidgetItem(value)
                if headerAsix is "Horizontal":
                    self.setItem(row,col,item_QTableWidgetItem)
                elif headerAsix is "Vertical":
                    self.setItem(col,row,item_QTableWidgetItem)

    #Public Function
    def setHeaderLabelList(self,validate):
        self._headerLabel_list=validate
        return self._headerLabel_list
    def getHeaderLabelList(self):
        return self._headerLabel_list

    def setHeaderAsixStr(self,validate):
        self._headerAsix_str=validate
        return self._headerAsix_str
    def getHeaderAsixStr(self):
        return self._headerAsix_str

    def setTableParamLists(self,validates):
        self._tableParam_lists=validates
        return self._tableParam_lists
    def addTableParamLists(self,validates):
        for validate in validates:
            self._tableParam_lists.append(validate)
        return self._tableParam_lists
    def getTableParamLists(self):
        return self._tableParam_lists

    def createBase(self):
        self.__header_create_list(self._headerLabel_list,self._headerAsix_str)

    def createTable(self):
        header_list=self.__header_create_list(self._headerLabel_list,self._headerAsix_str)
        for _tableParam_list in self._tableParam_lists:
            self.headerCount_check_func(header_list,_tableParam_list)
        self.__tableItem_create_func(self._tableParam_lists,self._headerAsix_str)

#viewWindow=TableWindowBase()
#viewWindow.show()