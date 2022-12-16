from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from ._reference import mainWindowUI as UI

class SkinWeightByJointWindowBase(UI.MainWindowBase):
    def __init__(self,*args,**kwargs):
        super(SkinWeightByJointWindowBase,self).__init__(*args,**kwargs)
        self.setWindowFlags(Qt.Window)

        self.buttonLeft_QPushButton.setText("Run")
        self.buttonCenter_QPushButton.setText("SetTable")
        self.buttonRight_QPushButton.setText("DeleteTable")

        geometry_QHBoxLayout=QHBoxLayout(self)
        self.custom_QGridLayout.addLayout(geometry_QHBoxLayout,0,0)
        
        geometry_QPushButton=QPushButton("setGeometry",self)
        geometry_QPushButton.clicked.connect(self.geometryOnClicked)
        geometry_QHBoxLayout.addWidget(geometry_QPushButton)

        self.geometry_QLineEdit=QLineEdit()
        geometry_QHBoxLayout.addWidget(self.geometry_QLineEdit)

        getParam_QHBoxLayout=QHBoxLayout(self)
        self.custom_QGridLayout.addLayout(getParam_QHBoxLayout,1,0)
        
        weights_QPushButton=QPushButton("setWeights",self)
        weights_QPushButton.clicked.connect(self.weightsOnClicked)
        getParam_QHBoxLayout.addWidget(weights_QPushButton)
        
        mark_QPushButton=QPushButton("setMark",self)
        mark_QPushButton.clicked.connect(self.markOnClicked)
        getParam_QHBoxLayout.addWidget(mark_QPushButton)

        self.table_QTableWidget=QTableWidget()
        self.custom_QGridLayout.addWidget(self.table_QTableWidget,2,0)
        self.headerAsix="Horizontal"
        self.headerTitle_list=["UseJoint","Value","Vertexs","Joint"]
        self.createHeaderTitle()
        self.data_lists=[["1","1.0","[]",""]]
        self.createTableItem()

        value_QHBoxLayout=QHBoxLayout(self)
        self.custom_QGridLayout.addLayout(value_QHBoxLayout,3,0)

        value_QLabel=QLabel("weight Value:",self)
        value_QHBoxLayout.addWidget(value_QLabel)

        self.value_QSlider=QSlider(Qt.Horizontal,self)
        self.value_QSlider.setRange(0,1000)
        self.value_QSlider.setTickPosition(QSlider.TicksBothSides)
        self.value_QSlider.setSingleStep(5)
        self.value_QSlider.setPageStep(10)
        self.value_QSlider.setTickInterval(10)
        value_QHBoxLayout.addWidget(self.value_QSlider)

        button_QHBoxLayout=QHBoxLayout(self)
        self.custom_QGridLayout.addLayout(button_QHBoxLayout,4,0)

        useSwitch_QPushButton=QPushButton("setUseSwitch",self)
        useSwitch_QPushButton.clicked.connect(self.useSwitchOnClicked)
        button_QHBoxLayout.addWidget(useSwitch_QPushButton)
        
        vertexs_QPushButton=QPushButton("setVertexs",self)
        vertexs_QPushButton.clicked.connect(self.vertexsOnClicked)
        button_QHBoxLayout.addWidget(vertexs_QPushButton)
        
        joint_QPushButton=QPushButton("setJoint",self)
        joint_QPushButton.clicked.connect(self.jointOnClicked)
        button_QHBoxLayout.addWidget(joint_QPushButton)

    
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

    def geometryOnClicked(self):
        print("geometry")
    
    def weightsOnClicked(self):
        print("weights")
    
    def markOnClicked(self):
        print("mark")

    def useSwitchOnClicked(self):
        print("use")

    def vertexsOnClicked(self):
        print("vertexs")

    def jointOnClicked(self):
        print("joint")


#viewWindow=SkinWeightByJointWindowBase()
#viewWindow.show()