from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from ._reference import mainWindowUI as UI

class EquipmentWindowBase(UI.MainWindowBase):
    def __init__(self,*args,**kwargs):
        super(EquipmentWindowBase,self).__init__(*args,**kwargs)
        self.setWindowFlags(Qt.Window)

        self.equipment_QTreeWidget=QTreeWidget()
        self.custom_QGridLayout.addWidget(self.equipment_QTreeWidget)
        headerLabel_list=["Name","Value"]
        self.equipment_QTreeWidget.setColumnCount(len(headerLabel_list))
        self.equipment_QTreeWidget.setHeaderLabels(headerLabel_list)
        self.equipment_dicts=[
            {"name":"sample0","value":None,"parent":None},
            {"name":"matrix","value":str([1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1]),"parent":"sample0"},
            {"name":"time","value":str(1),"parent":"sample0"},
            {"name":"sampleShape0","value":None,"parent":"sample0"},
            {"name":"sampleAttr0","value":str(10),"parent":"sampleShape0"}
        ]
        for equipment_dict in self.equipment_dicts:
            self.treeWidgetItem_create_func(equipment_dict["name"],equipment_dict["value"],equipment_dict["parent"])
    
    #Single Function
    def treeWidgetItem_create_func(self,name,value,parent):
        if parent == None:
            topItem_QTreeWidgetItem=QTreeWidgetItem([name])
            self.equipment_QTreeWidget.addTopLevelItem(topItem_QTreeWidgetItem)
        else:
            parentItem_QTreeWidgetItems=self.equipment_QTreeWidget.findItems(parent,Qt.MatchRecursive)
            childItem_QTreeWidgetItem=QTreeWidgetItem(parentItem_QTreeWidgetItems[-1],[name,value])

#viewWindow=EquipmentWindowBase()
#viewWindow.show()