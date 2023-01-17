from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from ._reference import mainWindowUI as UI

class TreeWindowBase(UI.MainWindowBase):
    def __init__(self,*args,**kwargs):
        super(TreeWindowBase,self).__init__(*args,**kwargs)
        self.setWindowFlags(Qt.Window)
        #self.__sample()
    
    #Public Function
    def __sample(self):
        self.equipment_CTreeWidget=CTreeWidget()
        self.custom_QGridLayout.addWidget(self.equipment_CTreeWidget)
        self.equipment_CTreeWidget.setHeaderLabelList(["Name","Value"])

        self.equipment_CTreeWidget.setTreeParamDicts([
            {"parent":None,"nameParams":["sample0",None]},
            {"parent":"sample0","nameParams":["matrix",str([1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1])]},
            {"parent":"sample0","nameParams":["time",str(1)]},
            {"parent":"sample0","nameParams":["shapeType","transform"]},
            {"parent":"sample0","nameParams":["sampleShape0",None]},
            {"parent":"sampleShape0","nameParams":["sampleAttr0",str(10)]}
        ])
        #self.equipment_CTreeWidget.createBase()
        self.equipment_CTreeWidget.createTree()

class CTreeWidget(QTreeWidget):
    def __init__(self,*args,**kwargs):
        super(CTreeWidget,self).__init__(*args,**kwargs)
        self._topItems=[]
        self._headerLabel_list=[]
        self._treeParam_dicts=[]#{"parent":None,"nameParams":["sample0",None]},
    
    #Single Function
    def headerCount_check_func(self,header,nameParams):
        if not len(header) == len(nameParams):
            cmds.error("count Error")

    #Private Function
    def _header_create_list(self):
        self.setColumnCount(len(self._headerLabel_list))
        self.setHeaderLabels(self._headerLabel_list)
        return self._headerLabel_list

    def _treeWidgetItem_create_func(self,parent,nameParams):
        if parent == None:
            topItem_QTreeWidgetItem=QTreeWidgetItem(nameParams)
            self.addTopLevelItem(topItem_QTreeWidgetItem)
        else:
            parentItem_QTreeWidgetItems=self.findItems(parent,Qt.MatchRecursive)
            childItem_QTreeWidgetItem=QTreeWidgetItem(parentItem_QTreeWidgetItems[-1],nameParams)

    def _getTopLevelItems_query_list(self):
        self._topItems=[]
        itemCount_int=self.topLevelItemCount()
        for num in range(itemCount_int):
            topItem_QTreeWidgetItem=self.topLevelItem(num)
            topItem_CTreeWidgetItem=CTreeWidgetItem(topItem_QTreeWidgetItem)
            self._topItems.append(topItem_CTreeWidgetItem)
        return self._topItems

    #Public Function
    def setHeaderLabelList(self,validate):
        self._headerLabel_list=validate
        return self._headerLabel_list
    def getHeaderLabelList(self):
        return self._headerLabel_list

    def setTreeParamDicts(self,validate):
        self._treeParam_dicts=validate
        return self._treeParam_dicts
    def getTreeParamDicts(self):
        return self._treeParam_dicts

    def getTopItems(self):
        self._getTopLevelItems_query_list()
        return self._topItems

    def createBase(self):
        self._header_create_list()

    def createTree(self):
        header_list=self._header_create_list()
        for _treeParam_dict in self._treeParam_dicts:
            self.headerCount_check_func(header_list,_treeParam_dict["nameParams"])
            self._treeWidgetItem_create_func(_treeParam_dict["parent"],_treeParam_dict["nameParams"])


class CTreeWidgetItem(QTreeWidgetItem):
    def __init__(self,*args,**kwargs):
        super(CTreeWidgetItem,self).__init__(*args,**kwargs)
        self._childItems=[]

    #Private Function
    def _getChildItems_query_list(self):
        self._childItems=[]
        itemCount_int=self.childCount()
        for num in range(itemCount_int):
            childItem_QTreeWidgetItem=self.child(num)
            self._childItems.append(childItem_QTreeWidgetItem)
        return self._childItems

    #Public Function
    def getChildItems(self):
        return self._getChildItems_query_list()


#viewWindow=TreeWindowBase()
#viewWindow.show()