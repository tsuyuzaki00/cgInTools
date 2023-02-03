from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from ._reference import mainWindowUI as UI

class TreeWindowBase(UI.MainWindowBase):
    def __init__(self,*args,**kwargs):
        super(TreeWindowBase,self).__init__(*args,**kwargs)
        self.setWindowFlags(Qt.Window)
        #self.__sample()
    
    #Summary Function
    def __sample(self):
        self.sample_CTreeWidget=CTreeWidget()
        self.custom_QGridLayout.addWidget(self.sample_CTreeWidget,0,0)
        self.sample_CTreeWidget.setHeaderLabelList(["Name","Value"])

        self.sample_CTreeWidget.setTreeParamDicts([
            {"parent":None,"nameParams":["sample0",None]},
            {"parent":"sample0","nameParams":["matrix",str([1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1])]},
            {"parent":"sample0","nameParams":["time",str(1)]},
            {"parent":"sample0","nameParams":["shapeType","transform"]},
            {"parent":"sample0","nameParams":["sampleShape0",None]},
            {"parent":"sampleShape0","nameParams":["sampleAttr0",str(10)]}
        ])
        #self.sample_CTreeWidget.createBase()
        self.sample_CTreeWidget.createTree()

class CTreeWidget(QTreeWidget):
    def __init__(self,*args,**kwargs):
        super(CTreeWidget,self).__init__(*args,**kwargs)
        self._headerLabel_list=[]
        self._treeParam_dicts=[]#{"parent":None,"nameParams":["sample0",None]},
    
    #Single Function
    def headerCount_check_func(self,header,relationList):
        if not len(header) == len(relationList):
            cmds.error("count Error")

    #Private Function
    def __header_create_list(self,headerLabel_list):
        self.setColumnCount(len(headerLabel_list))
        self.setHeaderLabels(headerLabel_list)
        return headerLabel_list

    def __treeWidgetItem_create_func(self,parent,nameParams):
        if parent == None:
            topItem_QTreeWidgetItem=QTreeWidgetItem(nameParams)
            self.addTopLevelItem(topItem_QTreeWidgetItem)
        else:
            parentItem_QTreeWidgetItems=self.findItems(parent,Qt.MatchRecursive)
            childItem_QTreeWidgetItem=QTreeWidgetItem(parentItem_QTreeWidgetItems[-1],nameParams)

    def __getTopLevelItems_query_QTreeWidgetItems(self):
        itemCount_int=self.topLevelItemCount()
        for num in range(itemCount_int):
            topItem_QTreeWidgetItem=self.topLevelItem(num)
            #topItem_CTreeWidgetItem=CTreeWidgetItem(topItem_QTreeWidgetItem)
            topItems.append(topItem_QTreeWidgetItem)
        return topItems

    #Public Function
    def setHeaderLabelList(self,validate):
        self._headerLabel_list=validate
        return self._headerLabel_list
    def getHeaderLabelList(self):
        return self._headerLabel_list

    def setTreeParamDicts(self,validates):
        self._treeParam_dicts=validates
        return self._treeParam_dicts
    def addTreeParamDicts(self,validates):
        for validate in validates:
            self._treeParam_dicts.append(validate)
        return self._treeParam_dicts
    def getTreeParamDicts(self):
        return self._treeParam_dicts

    def getTopItems(self):
        topItems=self.__getTopLevelItems_query_QTreeWidgetItems()
        return topItems

    def createBase(self):
        self.__header_create_list(self._headerLabel_list)

    def createTree(self):
        header_list=self.__header_create_list(self._headerLabel_list)
        for _treeParam_dict in self._treeParam_dicts:
            self.headerCount_check_func(header_list,_treeParam_dict["nameParams"])
            self.__treeWidgetItem_create_func(_treeParam_dict["parent"],_treeParam_dict["nameParams"])

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