from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class MainWindowBase(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(MainWindowBase,self).__init__(*args,**kwargs)
        self.setWindowFlags(Qt.Window)

        menuBar_QMenuBar=self.menuBar()
        statusBar_QStatusBar=self.statusBar()
        menuBar_QMenu=menuBar_QMenuBar.addMenu("File")

        refresh_QAction=QAction("Refresh Settings",self)
        menuBar_QMenu.addAction(refresh_QAction)
        
        restore_QAction=QAction("Restore Settings",self)
        menuBar_QMenu.addAction(restore_QAction)
        
        save_QAction=QAction("Save Settings",self)
        menuBar_QMenu.addAction(save_QAction)
        
        menuBar_QMenu.addSeparator()
        
        import_QAction=QAction("Import Settings",self)
        menuBar_QMenu.addAction(import_QAction)
        
        export_QAction=QAction("Export Settings",self)
        menuBar_QMenu.addAction(export_QAction)

        self.center_QWidget=QWidget()
        self.setCentralWidget(self.center_QWidget)
        statusBar_QStatusBar.showMessage("")

        test_QWidget=WeightWidget(parent=self)
        self.setCentralWidget(test_QWidget)

        threeButton_QWidget=QWidget()
        threeButton_QToolBar=QToolBar(threeButton_QWidget)
        self.addToolBar(threeButton_QToolBar)
        self.addToolBar(threeButton_QToolBar)

        main_QFormLayout=QFormLayout(threeButton_QWidget)

        button_QHBoxLayout=QHBoxLayout(threeButton_QWidget)
        main_QFormLayout.addRow(button_QHBoxLayout)

        self.left_QPushButton=QPushButton("left",threeButton_QWidget)
        button_QHBoxLayout.addWidget(self.left_QPushButton)
        self.left_QPushButton.clicked.connect(self.left_button_onClicked)

        self.center_QPushButton=QPushButton("center",threeButton_QWidget)
        button_QHBoxLayout.addWidget(self.center_QPushButton)
        self.center_QPushButton.clicked.connect(self.center_button_onClicked)

        self.right_QPushButton=QPushButton("right",threeButton_QWidget)
        button_QHBoxLayout.addWidget(self.right_QPushButton)
        self.right_QPushButton.clicked.connect(self.right_button_onClicked)

    def left_button_onClicked(self):
        print("base")
    def center_button_onClicked(self):
        print("base")
    def right_button_onClicked(self):
        print("base")

class WeightWidget(QWidget):
    def __init__(self,*args,**kwargs):
        super(WeightWidget,self).__init__(*args,**kwargs)

        self.main_QGridLayout=QGridLayout(self)

        self.useJoint_QCheckBox=QCheckBox(self)
        self.main_QGridLayout.addWidget(self.useJoint_QCheckBox,0,0)

        self.value_QLineEdit=QLineEdit(self)
        self.value_QLineEdit.setValidator(QDoubleValidator(0,1,4))
        self.value_QLineEdit.setText("0")
        self.main_QGridLayout.addWidget(self.value_QLineEdit,0,1)
        
        self.joint_QLineEdit=QLineEdit(self)
        self.main_QGridLayout.addWidget(self.joint_QLineEdit,0,2)
        
        self.geo_QLineEdit=QLineEdit(self)
        self.main_QGridLayout.addWidget(self.geo_QLineEdit,0,3)
        
        self.vertexs_QLineEdit=QLineEdit(self)
        self.main_QGridLayout.addWidget(self.vertexs_QLineEdit,0,4)

        self.del_QPushButton=QPushButton("Del",self)
        self.main_QGridLayout.addWidget(self.del_QPushButton,1,0)
        self.del_QPushButton.clicked.connect(self.del_button_onClicked)
        
        self.value_QSlider=QSlider(Qt.Horizontal,self)
        #self.value_QSlider.setRange(0,1)
        #self.value_QSlider.setTickPosition(QSlider.TicksBothSides)
        #self.value_QSlider.setSingleStep(0.001)
        #self.value_QSlider.setPageStep(0.01)
        #self.value_QSlider.setTickInterval(10)
        self.main_QGridLayout.addWidget(self.value_QSlider,1,1)
        
        self.joint_QPushButton=QPushButton("setJoint",self)
        self.main_QGridLayout.addWidget(self.joint_QPushButton,1,2)
        self.joint_QPushButton.clicked.connect(self.joint_button_onClicked)
        
        self.geometry_QPushButton=QPushButton("setGeometry",self)
        self.main_QGridLayout.addWidget(self.geometry_QPushButton,1,3)
        self.geometry_QPushButton.clicked.connect(self.geometry_button_onClicked)
        
        self.vertexs_QPushButton=QPushButton("setVertexs",self)
        self.main_QGridLayout.addWidget(self.vertexs_QPushButton,1,4)
        self.vertexs_QPushButton.clicked.connect(self.vertexs_button_onClicked)

    def del_button_onClicked(self):
        print("base")
    def joint_button_onClicked(self):
        print("base")
    def geometry_button_onClicked(self):
        print("base")
    def vertexs_button_onClicked(self):
        print("base")

window_instance=MainWindowBase()
window_instance.show()