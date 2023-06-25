from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import cgInTools as cit
from ..library import jsonLB as jLB
cit.reloads([jLB])

RULES_DICT=jLB.readJson(cit.settings_dir,"library")

class ColorChengeWindouBase(QWidget):
    def __init__(self, *args, **kwargs):
        super(ColorChengeWindouBase, self).__init__(*args, **kwargs)
        self._colorIndex_dicts=RULES_DICT["colorIndex_dicts"]
        self.setWindowFlags(Qt.Window)

        main_QVBoxLayout=QVBoxLayout(self)

        artAttr_QHBoxLayout=self.artAttrLayout_create_QHBoxLayout()
        neutralButton_QHBoxLayout=self.neutralButtonLayout_create_QHBoxLayout()
        templateColor_QWidget=self.templateColor_create_QWidget()
        indexColor_QWidget=self.indexColor_create_QWidget()
        mgearColor_QWidget=self.mgearColor_create_QWidget()
        grisColor_QWidget=self.grisColor_create_QWidget()

        ctrlColor_QTabWidget=QTabWidget(self)
        ctrlColor_QTabWidget.addTab(templateColor_QWidget,"Default")
        ctrlColor_QTabWidget.addTab(indexColor_QWidget,"Index")
        ctrlColor_QTabWidget.addTab(mgearColor_QWidget,"Mgear")
        ctrlColor_QTabWidget.addTab(grisColor_QWidget,"Gris")

        main_QVBoxLayout.addLayout(artAttr_QHBoxLayout)
        main_QVBoxLayout.addLayout(neutralButton_QHBoxLayout)
        main_QVBoxLayout.addWidget(ctrlColor_QTabWidget)

    #Single Function
    def artAttrLayout_create_QHBoxLayout(self):
        artAttr_QHBoxLayout=QHBoxLayout(self)
        self.radioGrp_QButtonGroup=QButtonGroup()

        override_QRadioButton=QRadioButton("Override",self)
        override_QRadioButton.setChecked(True)
        self.radioGrp_QButtonGroup.addButton(override_QRadioButton,0)
        artAttr_QHBoxLayout.addWidget(override_QRadioButton)

        wireframe_QRadioButton=QRadioButton("WireFrame",self)
        self.radioGrp_QButtonGroup.addButton(wireframe_QRadioButton,1)
        artAttr_QHBoxLayout.addWidget(wireframe_QRadioButton)
        
        return artAttr_QHBoxLayout
    
    def neutralButtonLayout_create_QHBoxLayout(self):
        neutralButton_QHBoxLayout=QHBoxLayout(self)

        overrideNeutral_QPushButton=QPushButton("OverrideNeutral",self)
        overrideNeutral_QPushButton.setStyleSheet("color: gray;")
        overrideNeutral_QPushButton.clicked.connect(self.buttonOverrideNeutralOnClicked)
        neutralButton_QHBoxLayout.addWidget(overrideNeutral_QPushButton)

        wireNeutral_QPushButton=QPushButton("WireNeutral",self)
        wireNeutral_QPushButton.setStyleSheet("color: gray;")
        wireNeutral_QPushButton.clicked.connect(self.buttonWireNeutralOnClicked)
        neutralButton_QHBoxLayout.addWidget(wireNeutral_QPushButton)
        
        return neutralButton_QHBoxLayout
    
    def templateColor_create_QWidget(self):
        color_QWidget=QWidget()
        custom_QGridLayout=QGridLayout(self)
        color_QWidget.setLayout(custom_QGridLayout)

        right_QVBoxLayout=QVBoxLayout(self)
        custom_QGridLayout.addLayout(right_QVBoxLayout,1,0)

        right_QLabel=QLabel("Right Color",self)
        right_QVBoxLayout.addWidget(right_QLabel,True)

        index13_QPushButton=QPushButton("main",self)
        index13_str=self._colorIndex_dicts[13]["RGBFF"]
        index13_QPushButton.setStyleSheet("color:#888888; background:"+index13_str+";")
        index13_QPushButton.clicked.connect(self.index13ButtonOnClicked)
        right_QVBoxLayout.addWidget(index13_QPushButton,True)

        index20_QPushButton=QPushButton("sub",self)
        index20_str=self._colorIndex_dicts[20]["RGBFF"]
        index20_QPushButton.setStyleSheet("color:#888888; background:"+index20_str+";")
        index20_QPushButton.clicked.connect(self.index20ButtonOnClicked)
        right_QVBoxLayout.addWidget(index20_QPushButton,True)
        
        index31_QPushButton=QPushButton("support",self)
        index31_str=self._colorIndex_dicts[31]["RGBFF"]
        index31_QPushButton.setStyleSheet("color:#BBBBBB; background:"+index31_str+";")
        index31_QPushButton.clicked.connect(self.index31ButtonOnClicked)
        right_QVBoxLayout.addWidget(index31_QPushButton,True)
        
        index04_QPushButton=QPushButton("inside",self)
        index04_str=self._colorIndex_dicts[4]["RGBFF"]
        index04_QPushButton.setStyleSheet("color:#BBBBBB; background:"+index04_str+";")
        index04_QPushButton.clicked.connect(self.index04ButtonOnClicked)
        right_QVBoxLayout.addWidget(index04_QPushButton,True)

        center_QVBoxLayout=QVBoxLayout(self)
        custom_QGridLayout.addLayout(center_QVBoxLayout,1,1)

        center_QLabel=QLabel("Center Color",self)
        center_QVBoxLayout.addWidget(center_QLabel,True)

        index17_QPushButton=QPushButton("main",self)
        index17_str=self._colorIndex_dicts[17]["RGBFF"]
        index17_QPushButton.setStyleSheet("color:#888888; background:"+index17_str+";")
        index17_QPushButton.clicked.connect(self.index17ButtonOnClicked)
        center_QVBoxLayout.addWidget(index17_QPushButton,True)

        index14_QPushButton=QPushButton("sub",self)
        index14_str=self._colorIndex_dicts[14]["RGBFF"]
        index14_QPushButton.setStyleSheet("color:#888888; background:"+index14_str+";")
        index14_QPushButton.clicked.connect(self.index14ButtonOnClicked)
        center_QVBoxLayout.addWidget(index14_QPushButton,True)

        index27_QPushButton=QPushButton("support",self)
        index27_str=self._colorIndex_dicts[27]["RGBFF"]
        index27_QPushButton.setStyleSheet("color:#BBBBBB; background:"+index27_str+";")
        index27_QPushButton.clicked.connect(self.index27ButtonOnClicked)
        center_QVBoxLayout.addWidget(index27_QPushButton,True)

        index07_QPushButton=QPushButton("inside",self)
        index07_str=self._colorIndex_dicts[7]["RGBFF"]
        index07_QPushButton.setStyleSheet("color:#BBBBBB; background:"+index07_str+";")
        index07_QPushButton.clicked.connect(self.index07ButtonOnClicked)
        center_QVBoxLayout.addWidget(index07_QPushButton,True)
        
        left_QVBoxLayout=QVBoxLayout(self)
        custom_QGridLayout.addLayout(left_QVBoxLayout,1,2)
        
        left_QLabel=QLabel("Left Color",self)
        left_QVBoxLayout.addWidget(left_QLabel,True)

        index06_QPushButton=QPushButton("main",self)
        index06_str=self._colorIndex_dicts[6]["RGBFF"]
        index06_QPushButton.setStyleSheet("color:#888888; background:"+index06_str+";")
        index06_QPushButton.clicked.connect(self.index06ButtonOnClicked)
        left_QVBoxLayout.addWidget(index06_QPushButton,True)

        index18_QPushButton=QPushButton("sub",self)
        index18_str=self._colorIndex_dicts[18]["RGBFF"]
        index18_QPushButton.setStyleSheet("color:#888888; background:"+index18_str+";")
        index18_QPushButton.clicked.connect(self.index18ButtonOnClicked)
        left_QVBoxLayout.addWidget(index18_QPushButton,True)
        
        index28_QPushButton=QPushButton("support",self)
        index28_str=self._colorIndex_dicts[28]["RGBFF"]
        index28_QPushButton.setStyleSheet("color:#BBBBBB; background:"+index28_str+";")
        index28_QPushButton.clicked.connect(self.index28ButtonOnClicked)
        left_QVBoxLayout.addWidget(index28_QPushButton,True)
        
        index15_QPushButton=QPushButton("inside",self)
        index15_str=self._colorIndex_dicts[15]["RGBFF"]
        index15_QPushButton.setStyleSheet("color:#BBBBBB; background:"+index15_str+";")
        index15_QPushButton.clicked.connect(self.index15ButtonOnClicked)
        left_QVBoxLayout.addWidget(index15_QPushButton,True)

        other_QVBoxLayout=QVBoxLayout(self)
        custom_QGridLayout.addLayout(other_QVBoxLayout,1,3)

        other_QLabel=QLabel("Other Color",self)
        other_QVBoxLayout.addWidget(other_QLabel,True)
        
        index16_QPushButton=QPushButton("main",self)
        index16_str=self._colorIndex_dicts[16]["RGBFF"]
        index16_QPushButton.setStyleSheet("color:#888888; background:"+index16_str+";")
        index16_QPushButton.clicked.connect(self.index16ButtonOnClicked)
        other_QVBoxLayout.addWidget(index16_QPushButton,True)

        index09_QPushButton=QPushButton("sub",self)
        index09_str=self._colorIndex_dicts[9]["RGBFF"]
        index09_QPushButton.setStyleSheet("color:#888888; background:"+index09_str+";")
        index09_QPushButton.clicked.connect(self.index09ButtonOnClicked)
        other_QVBoxLayout.addWidget(index09_QPushButton,True)

        index30_QPushButton=QPushButton("support",self)
        index30_str=self._colorIndex_dicts[30]["RGBFF"]
        index30_QPushButton.setStyleSheet("color:#BBBBBB; background:"+index30_str+";")
        index30_QPushButton.clicked.connect(self.index30ButtonOnClicked)
        other_QVBoxLayout.addWidget(index30_QPushButton,True)
        
        index01_QPushButton=QPushButton("inside",self)
        index01_str=self._colorIndex_dicts[1]["RGBFF"]
        index01_QPushButton.setStyleSheet("color:#BBBBBB; background:"+index01_str+";")
        index01_QPushButton.clicked.connect(self.index01ButtonOnClicked)
        other_QVBoxLayout.addWidget(index01_QPushButton,True)
        return color_QWidget

    def indexColor_create_QWidget(self):
        color_QWidget=QWidget()
        custom_QGridLayout=QGridLayout(self)
        color_QWidget.setLayout(custom_QGridLayout)

        index01_QPushButton=QPushButton("1",self)
        index01_str=self._colorIndex_dicts[1]["RGBFF"]
        index01_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index01_str+";")
        index01_QPushButton.clicked.connect(self.index01ButtonOnClicked)
        custom_QGridLayout.addWidget(index01_QPushButton,0,0)
        
        index02_QPushButton=QPushButton("2",self)
        index02_str=self._colorIndex_dicts[2]["RGBFF"]
        index02_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index02_str+";")
        index02_QPushButton.clicked.connect(self.index02ButtonOnClicked)
        custom_QGridLayout.addWidget(index02_QPushButton,0,1)
        
        index03_QPushButton=QPushButton("3",self)
        index03_str=self._colorIndex_dicts[3]["RGBFF"]
        index03_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index03_str+";")
        index03_QPushButton.clicked.connect(self.index03ButtonOnClicked)
        custom_QGridLayout.addWidget(index03_QPushButton,0,2)
        
        index04_QPushButton=QPushButton("4",self)
        index04_str=self._colorIndex_dicts[4]["RGBFF"]
        index04_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index04_str+";")
        index04_QPushButton.clicked.connect(self.index04ButtonOnClicked)
        custom_QGridLayout.addWidget(index04_QPushButton,0,3)
        
        index05_QPushButton=QPushButton("5",self)
        index05_str=self._colorIndex_dicts[5]["RGBFF"]
        index05_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index05_str+";")
        index05_QPushButton.clicked.connect(self.index05ButtonOnClicked)
        custom_QGridLayout.addWidget(index05_QPushButton,0,4)
        
        index06_QPushButton=QPushButton("6",self)
        index06_str=self._colorIndex_dicts[6]["RGBFF"]
        index06_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index06_str+";")
        index06_QPushButton.clicked.connect(self.index06ButtonOnClicked)
        custom_QGridLayout.addWidget(index06_QPushButton,0,5)
        
        index07_QPushButton=QPushButton("7",self)
        index07_str=self._colorIndex_dicts[7]["RGBFF"]
        index07_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index07_str+";")
        index07_QPushButton.clicked.connect(self.index07ButtonOnClicked)
        custom_QGridLayout.addWidget(index07_QPushButton,0,6)
        
        index08_QPushButton=QPushButton("8",self)
        index08_str=self._colorIndex_dicts[8]["RGBFF"]
        index08_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index08_str+";")
        index08_QPushButton.clicked.connect(self.index08ButtonOnClicked)
        custom_QGridLayout.addWidget(index08_QPushButton,0,7)
        
        index09_QPushButton=QPushButton("9",self)
        index09_str=self._colorIndex_dicts[9]["RGBFF"]
        index09_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index09_str+";")
        index09_QPushButton.clicked.connect(self.index09ButtonOnClicked)
        custom_QGridLayout.addWidget(index09_QPushButton,0,8)
        
        index10_QPushButton=QPushButton("10",self)
        index10_str=self._colorIndex_dicts[10]["RGBFF"]
        index10_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index10_str+";")
        index10_QPushButton.clicked.connect(self.index10ButtonOnClicked)
        custom_QGridLayout.addWidget(index10_QPushButton,0,9)
        
        index11_QPushButton=QPushButton("11",self)
        index11_str=self._colorIndex_dicts[11]["RGBFF"]
        index11_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index11_str+";")
        index11_QPushButton.clicked.connect(self.index11ButtonOnClicked)
        custom_QGridLayout.addWidget(index11_QPushButton,1,0)
        
        index12_QPushButton=QPushButton("12",self)
        index12_str=self._colorIndex_dicts[12]["RGBFF"]
        index12_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index12_str+";")
        index12_QPushButton.clicked.connect(self.index12ButtonOnClicked)
        custom_QGridLayout.addWidget(index12_QPushButton,1,1)
        
        index13_QPushButton=QPushButton("13",self)
        index13_str=self._colorIndex_dicts[13]["RGBFF"]
        index13_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index13_str+";")
        index13_QPushButton.clicked.connect(self.index13ButtonOnClicked)
        custom_QGridLayout.addWidget(index13_QPushButton,1,2)
        
        index14_QPushButton=QPushButton("14",self)
        index14_str=self._colorIndex_dicts[14]["RGBFF"]
        index14_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index14_str+";")
        index14_QPushButton.clicked.connect(self.index14ButtonOnClicked)
        custom_QGridLayout.addWidget(index14_QPushButton,1,3)
        
        index15_QPushButton=QPushButton("15",self)
        index15_str=self._colorIndex_dicts[15]["RGBFF"]
        index15_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index15_str+";")
        index15_QPushButton.clicked.connect(self.index15ButtonOnClicked)
        custom_QGridLayout.addWidget(index15_QPushButton,1,4)
        
        index16_QPushButton=QPushButton("16",self)
        index16_str=self._colorIndex_dicts[16]["RGBFF"]
        index16_QPushButton.setStyleSheet("color:#202020; background:"+index16_str+";")
        index16_QPushButton.clicked.connect(self.index16ButtonOnClicked)
        custom_QGridLayout.addWidget(index16_QPushButton,1,5)
        
        index17_QPushButton=QPushButton("17",self)
        index17_str=self._colorIndex_dicts[17]["RGBFF"]
        index17_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index17_str+";")
        index17_QPushButton.clicked.connect(self.index17ButtonOnClicked)
        custom_QGridLayout.addWidget(index17_QPushButton,1,6)
        
        index18_QPushButton=QPushButton("18",self)
        index18_str=self._colorIndex_dicts[18]["RGBFF"]
        index18_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index18_str+";")
        index18_QPushButton.clicked.connect(self.index18ButtonOnClicked)
        custom_QGridLayout.addWidget(index18_QPushButton,1,7)
        
        index19_QPushButton=QPushButton("19",self)
        index19_str=self._colorIndex_dicts[19]["RGBFF"]
        index19_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index19_str+";")
        index19_QPushButton.clicked.connect(self.index19ButtonOnClicked)
        custom_QGridLayout.addWidget(index19_QPushButton,1,8)
        
        index20_QPushButton=QPushButton("20",self)
        index20_str=self._colorIndex_dicts[20]["RGBFF"]
        index20_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index20_str+";")
        index20_QPushButton.clicked.connect(self.index20ButtonOnClicked)
        custom_QGridLayout.addWidget(index20_QPushButton,1,9)
        
        index21_QPushButton=QPushButton("21",self)
        index21_str=self._colorIndex_dicts[21]["RGBFF"]
        index21_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index21_str+";")
        index21_QPushButton.clicked.connect(self.index21ButtonOnClicked)
        custom_QGridLayout.addWidget(index21_QPushButton,2,0)
        
        index22_QPushButton=QPushButton("22",self)
        index22_str=self._colorIndex_dicts[22]["RGBFF"]
        index22_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index22_str+";")
        index22_QPushButton.clicked.connect(self.index22ButtonOnClicked)
        custom_QGridLayout.addWidget(index22_QPushButton,2,1)
        
        index23_QPushButton=QPushButton("23",self)
        index23_str=self._colorIndex_dicts[23]["RGBFF"]
        index23_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index23_str+";")
        index23_QPushButton.clicked.connect(self.index23ButtonOnClicked)
        custom_QGridLayout.addWidget(index23_QPushButton,2,2)
        
        index24_QPushButton=QPushButton("24",self)
        index24_str=self._colorIndex_dicts[24]["RGBFF"]
        index24_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index24_str+";")
        index24_QPushButton.clicked.connect(self.index24ButtonOnClicked)
        custom_QGridLayout.addWidget(index24_QPushButton,2,3)
        
        index25_QPushButton=QPushButton("25",self)
        index25_str=self._colorIndex_dicts[25]["RGBFF"]
        index25_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index25_str+";")
        index25_QPushButton.clicked.connect(self.index25ButtonOnClicked)
        custom_QGridLayout.addWidget(index25_QPushButton,2,4)
        
        index26_QPushButton=QPushButton("26",self)
        index26_str=self._colorIndex_dicts[26]["RGBFF"]
        index26_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index26_str+";")
        index26_QPushButton.clicked.connect(self.index26ButtonOnClicked)
        custom_QGridLayout.addWidget(index26_QPushButton,2,5)
        
        index27_QPushButton=QPushButton("27",self)
        index27_str=self._colorIndex_dicts[27]["RGBFF"]
        index27_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index27_str+";")
        index27_QPushButton.clicked.connect(self.index27ButtonOnClicked)
        custom_QGridLayout.addWidget(index27_QPushButton,2,6)
        
        index28_QPushButton=QPushButton("28",self)
        index28_str=self._colorIndex_dicts[28]["RGBFF"]
        index28_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index28_str+";")
        index28_QPushButton.clicked.connect(self.index28ButtonOnClicked)
        custom_QGridLayout.addWidget(index28_QPushButton,2,7)
        
        index29_QPushButton=QPushButton("29",self)
        index29_str=self._colorIndex_dicts[29]["RGBFF"]
        index29_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index29_str+";")
        index29_QPushButton.clicked.connect(self.index29ButtonOnClicked)
        custom_QGridLayout.addWidget(index29_QPushButton,2,8)
        
        index30_QPushButton=QPushButton("30",self)
        index30_str=self._colorIndex_dicts[30]["RGBFF"]
        index30_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index30_str+";")
        index30_QPushButton.clicked.connect(self.index30ButtonOnClicked)
        custom_QGridLayout.addWidget(index30_QPushButton,2,9)
        
        index31_QPushButton=QPushButton("31",self)
        index31_str=self._colorIndex_dicts[31]["RGBFF"]
        index31_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index31_str+";")
        index31_QPushButton.clicked.connect(self.index31ButtonOnClicked)
        custom_QGridLayout.addWidget(index31_QPushButton,3,0)
        
        

        return color_QWidget
    
    def mgearColor_create_QWidget(self):
        color_QWidget=QWidget()
        custom_QGridLayout=QGridLayout(self)
        color_QWidget.setLayout(custom_QGridLayout)

        right_QVBoxLayout=QVBoxLayout(self)
        right_QVBoxLayout.addStretch(1)
        custom_QGridLayout.addLayout(right_QVBoxLayout,1,0)

        right_QLabel=QLabel("Right Color",self)
        right_QVBoxLayout.addWidget(right_QLabel,True)

        index23_QPushButton=QPushButton("FK",self)
        index23_str=self._colorIndex_dicts[23]["RGBFF"]
        index23_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index23_str+";")
        index23_QPushButton.clicked.connect(self.index23ButtonOnClicked)
        right_QVBoxLayout.addWidget(index23_QPushButton,True)

        index14_QPushButton=QPushButton("IK",self)
        index14_str=self._colorIndex_dicts[14]["RGBFF"]
        index14_QPushButton.setStyleSheet("color:#202020; background:"+index14_str+";")
        index14_QPushButton.clicked.connect(self.index14ButtonOnClicked)
        right_QVBoxLayout.addWidget(index14_QPushButton,True)

        center_QVBoxLayout=QVBoxLayout(self)
        center_QVBoxLayout.addStretch(1)
        custom_QGridLayout.addLayout(center_QVBoxLayout,1,1)

        center_QLabel=QLabel("Center Color",self)
        center_QVBoxLayout.addWidget(center_QLabel,True)

        index13_QPushButton=QPushButton("FK",self)
        index13_str=self._colorIndex_dicts[13]["RGBFF"]
        index13_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index13_str+";")
        index13_QPushButton.clicked.connect(self.index13ButtonOnClicked)
        center_QVBoxLayout.addWidget(index13_QPushButton,True)

        index17_QPushButton=QPushButton("IK",self)
        index17_str=self._colorIndex_dicts[17]["RGBFF"]
        index17_QPushButton.setStyleSheet("color:#202020; background:"+index17_str+";")
        index17_QPushButton.clicked.connect(self.index17ButtonOnClicked)
        center_QVBoxLayout.addWidget(index17_QPushButton,True)
        
        left_QVBoxLayout=QVBoxLayout(self)
        left_QVBoxLayout.addStretch(1)
        custom_QGridLayout.addLayout(left_QVBoxLayout,1,2)
        
        left_QLabel=QLabel("Left Color",self)
        left_QVBoxLayout.addWidget(left_QLabel,True)

        index06_QPushButton=QPushButton("FK",self)
        index06_str=self._colorIndex_dicts[6]["RGBFF"]
        index06_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index06_str+";")
        index06_QPushButton.clicked.connect(self.index06ButtonOnClicked)
        left_QVBoxLayout.addWidget(index06_QPushButton,True)

        index18_QPushButton=QPushButton("IK",self)
        index18_str=self._colorIndex_dicts[18]["RGBFF"]
        index18_QPushButton.setStyleSheet("color:#202020; background:"+index18_str+";")
        index18_QPushButton.clicked.connect(self.index18ButtonOnClicked)
        left_QVBoxLayout.addWidget(index18_QPushButton,True)
        return color_QWidget
    
    def grisColor_create_QWidget(self):
        color_QWidget=QWidget()
        custom_QGridLayout=QGridLayout(self)
        color_QWidget.setLayout(custom_QGridLayout)

        right_QVBoxLayout=QVBoxLayout(self)
        custom_QGridLayout.addLayout(right_QVBoxLayout,1,0)

        right_QLabel=QLabel("Right Color",self)
        right_QVBoxLayout.addWidget(right_QLabel,True)

        index13_QPushButton=QPushButton("main",self)
        index13_str=self._colorIndex_dicts[13]["RGBFF"]
        index13_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index13_str+";")
        index13_QPushButton.clicked.connect(self.index13ButtonOnClicked)
        right_QVBoxLayout.addWidget(index13_QPushButton,True)

        index20_QPushButton=QPushButton("sub",self)
        index20_str=self._colorIndex_dicts[20]["RGBFF"]
        index20_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index20_str+";")
        index20_QPushButton.clicked.connect(self.index20ButtonOnClicked)
        right_QVBoxLayout.addWidget(index20_QPushButton,True)
        
        index31_QPushButton=QPushButton("support",self)
        index31_str=self._colorIndex_dicts[31]["RGBFF"]
        index31_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index31_str+";")
        index31_QPushButton.clicked.connect(self.index31ButtonOnClicked)
        right_QVBoxLayout.addWidget(index31_QPushButton,True)
        
        index04_QPushButton=QPushButton("inside",self)
        index04_str=self._colorIndex_dicts[4]["RGBFF"]
        index04_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index04_str+";")
        index04_QPushButton.clicked.connect(self.index04ButtonOnClicked)
        right_QVBoxLayout.addWidget(index04_QPushButton,True)

        center_QVBoxLayout=QVBoxLayout(self)
        custom_QGridLayout.addLayout(center_QVBoxLayout,1,1)

        center_QLabel=QLabel("Center Color",self)
        center_QVBoxLayout.addWidget(center_QLabel,True)

        index17_QPushButton=QPushButton("main",self)
        index17_str=self._colorIndex_dicts[17]["RGBFF"]
        index17_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index17_str+";")
        index17_QPushButton.clicked.connect(self.index17ButtonOnClicked)
        center_QVBoxLayout.addWidget(index17_QPushButton,True)

        index14_QPushButton=QPushButton("sub",self)
        index14_str=self._colorIndex_dicts[14]["RGBFF"]
        index14_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index14_str+";")
        index14_QPushButton.clicked.connect(self.index14ButtonOnClicked)
        center_QVBoxLayout.addWidget(index14_QPushButton,True)

        index27_QPushButton=QPushButton("support",self)
        index27_str=self._colorIndex_dicts[27]["RGBFF"]
        index27_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index27_str+";")
        index27_QPushButton.clicked.connect(self.index27ButtonOnClicked)
        center_QVBoxLayout.addWidget(index27_QPushButton,True)

        index07_QPushButton=QPushButton("inside",self)
        index07_str=self._colorIndex_dicts[7]["RGBFF"]
        index07_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index07_str+";")
        index07_QPushButton.clicked.connect(self.index07ButtonOnClicked)
        center_QVBoxLayout.addWidget(index07_QPushButton,True)
        
        left_QVBoxLayout=QVBoxLayout(self)
        custom_QGridLayout.addLayout(left_QVBoxLayout,1,2)
        
        left_QLabel=QLabel("Left Color",self)
        left_QVBoxLayout.addWidget(left_QLabel,True)

        index06_QPushButton=QPushButton("main",self)
        index06_str=self._colorIndex_dicts[6]["RGBFF"]
        index06_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index06_str+";")
        index06_QPushButton.clicked.connect(self.index06ButtonOnClicked)
        left_QVBoxLayout.addWidget(index06_QPushButton,True)

        index18_QPushButton=QPushButton("sub",self)
        index18_str=self._colorIndex_dicts[18]["RGBFF"]
        index18_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index18_str+";")
        index18_QPushButton.clicked.connect(self.index18ButtonOnClicked)
        left_QVBoxLayout.addWidget(index18_QPushButton,True)
        
        index28_QPushButton=QPushButton("support",self)
        index28_str=self._colorIndex_dicts[28]["RGBFF"]
        index28_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index28_str+";")
        index28_QPushButton.clicked.connect(self.index28ButtonOnClicked)
        left_QVBoxLayout.addWidget(index28_QPushButton,True)
        
        index15_QPushButton=QPushButton("inside",self)
        index15_str=self._colorIndex_dicts[15]["RGBFF"]
        index15_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index15_str+";")
        index15_QPushButton.clicked.connect(self.index15ButtonOnClicked)
        left_QVBoxLayout.addWidget(index15_QPushButton,True)
        return color_QWidget

    #Public Function
    def index01ButtonOnClicked(self):
        print(1)
    def index02ButtonOnClicked(self):
        print(2)
    def index03ButtonOnClicked(self):
        print(3)
    def index04ButtonOnClicked(self):
        print(4)
    def index05ButtonOnClicked(self):
        print(5)
    def index06ButtonOnClicked(self):
        print(6)
    def index07ButtonOnClicked(self):
        print(7)
    def index08ButtonOnClicked(self):
        print(8)
    def index09ButtonOnClicked(self):
        print(9)
    def index10ButtonOnClicked(self):
        print(10)
    def index11ButtonOnClicked(self):
        print(11)
    def index12ButtonOnClicked(self):
        print(12)
    def index13ButtonOnClicked(self):
        print(13)
    def index14ButtonOnClicked(self):
        print(14)
    def index15ButtonOnClicked(self):
        print(15)
    def index16ButtonOnClicked(self):
        print(16)
    def index17ButtonOnClicked(self):
        print(17)
    def index18ButtonOnClicked(self):
        print(18)
    def index19ButtonOnClicked(self):
        print(19)
    def index20ButtonOnClicked(self):
        print(20)
    def index21ButtonOnClicked(self):
        print(21)
    def index22ButtonOnClicked(self):
        print(22)
    def index23ButtonOnClicked(self):
        print(23)
    def index24ButtonOnClicked(self):
        print(24)
    def index25ButtonOnClicked(self):
        print(25)
    def index26ButtonOnClicked(self):
        print(26)
    def index27ButtonOnClicked(self):
        print(27)
    def index28ButtonOnClicked(self):
        print(28)
    def index29ButtonOnClicked(self):
        print(29)
    def index30ButtonOnClicked(self):
        print(30)
    def index31ButtonOnClicked(self):
        print(31)
    def buttonOverrideNeutralOnClicked(self):
        print("OverrideNeutral")
    def buttonWireNeutralOnClicked(self):
        print("WireNeutral")

#viewWindow=ColorChengeWindouBase()
#viewWindow.show()
