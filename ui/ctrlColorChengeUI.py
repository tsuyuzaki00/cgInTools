from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class ColorChengeWindouBase(QWidget):
    def __init__(self, *args, **kwargs):
        super(ColorChengeWindouBase, self).__init__(*args, **kwargs)
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

        red_QPushButton=QPushButton("Red",self)
        red_QPushButton.setStyleSheet("color: red;")
        red_QPushButton.clicked.connect(self.buttonRedOnClicked)
        right_QVBoxLayout.addWidget(red_QPushButton,True)

        pink_QPushButton=QPushButton("Pink",self)
        pink_QPushButton.setStyleSheet("color: pink;")
        pink_QPushButton.clicked.connect(self.buttonPinkOnClicked)
        right_QVBoxLayout.addWidget(pink_QPushButton,True)
        
        crimson_QPushButton=QPushButton("Crimson",self)
        crimson_QPushButton.setStyleSheet("color: crimson;")
        crimson_QPushButton.clicked.connect(self.buttonCrimsonOnClicked)
        right_QVBoxLayout.addWidget(crimson_QPushButton,True)
        
        darkRed_QPushButton=QPushButton("DarkRed",self)
        darkRed_QPushButton.setStyleSheet("color: darkRed;")
        darkRed_QPushButton.clicked.connect(self.buttonDarkRedOnClicked)
        right_QVBoxLayout.addWidget(darkRed_QPushButton,True)

        center_QVBoxLayout=QVBoxLayout(self)
        custom_QGridLayout.addLayout(center_QVBoxLayout,1,1)

        center_QLabel=QLabel("Center Color",self)
        center_QVBoxLayout.addWidget(center_QLabel,True)

        yellow_QPushButton=QPushButton("Yellow",self)
        yellow_QPushButton.setStyleSheet("color: yellow;")
        yellow_QPushButton.clicked.connect(self.buttonYellowOnClicked)
        center_QVBoxLayout.addWidget(yellow_QPushButton,True)

        lime_QPushButton=QPushButton("Lime",self)
        lime_QPushButton.setStyleSheet("color: lime;")
        lime_QPushButton.clicked.connect(self.buttonLimeOnClicked)
        center_QVBoxLayout.addWidget(lime_QPushButton,True)

        green_QPushButton=QPushButton("Green",self)
        green_QPushButton.setStyleSheet("color: mediumseagreen;")
        green_QPushButton.clicked.connect(self.buttonGreenOnClicked)
        center_QVBoxLayout.addWidget(green_QPushButton,True)

        darkGreen_QPushButton=QPushButton("DarkGreen",self)
        darkGreen_QPushButton.clicked.connect(self.buttonDarkGreenOnClicked)
        darkGreen_QPushButton.setStyleSheet("color: darkGreen;")
        center_QVBoxLayout.addWidget(darkGreen_QPushButton,True)
        
        left_QVBoxLayout=QVBoxLayout(self)
        custom_QGridLayout.addLayout(left_QVBoxLayout,1,2)
        
        left_QLabel=QLabel("Left Color",self)
        left_QVBoxLayout.addWidget(left_QLabel,True)

        blue_QPushButton=QPushButton("Blue",self)
        blue_QPushButton.setStyleSheet("color: blue;")
        blue_QPushButton.clicked.connect(self.buttonBlueOnClicked)
        left_QVBoxLayout.addWidget(blue_QPushButton,True)

        cyan_QPushButton=QPushButton("Cyan",self)
        cyan_QPushButton.setStyleSheet("color: cyan;")
        cyan_QPushButton.clicked.connect(self.buttonCyanOnClicked)
        left_QVBoxLayout.addWidget(cyan_QPushButton,True)
        
        teal_QPushButton=QPushButton("Teal",self)
        teal_QPushButton.setStyleSheet("color: steelBlue;")
        teal_QPushButton.clicked.connect(self.buttonTealOnClicked)
        left_QVBoxLayout.addWidget(teal_QPushButton,True)
        
        darkBlue_QPushButton=QPushButton("DarkBlue",self)
        darkBlue_QPushButton.setStyleSheet("color: darkBlue;")
        darkBlue_QPushButton.clicked.connect(self.buttonDarkBlueOnClicked)
        left_QVBoxLayout.addWidget(darkBlue_QPushButton,True)

        other_QVBoxLayout=QVBoxLayout(self)
        custom_QGridLayout.addLayout(other_QVBoxLayout,1,3)

        other_QLabel=QLabel("Other Color",self)
        other_QVBoxLayout.addWidget(other_QLabel,True)
        
        white_QPushButton=QPushButton("White",self)
        white_QPushButton.setStyleSheet("color: white;")
        white_QPushButton.clicked.connect(self.buttonWhiteOnClicked)
        other_QVBoxLayout.addWidget(white_QPushButton,True)

        magenta_QPushButton=QPushButton("Magenta",self)
        magenta_QPushButton.setStyleSheet("color: magenta;")
        magenta_QPushButton.clicked.connect(self.buttonMagentaOnClicked)
        other_QVBoxLayout.addWidget(magenta_QPushButton,True)

        purple_QPushButton=QPushButton("Purple",self)
        purple_QPushButton.setStyleSheet("color: purple;")
        purple_QPushButton.clicked.connect(self.buttonPurpleOnClicked)
        other_QVBoxLayout.addWidget(purple_QPushButton,True)
        
        black_QPushButton=QPushButton("Black", self)
        black_QPushButton.setStyleSheet("color: black;")
        black_QPushButton.clicked.connect(self.buttonBlackOnClicked)
        other_QVBoxLayout.addWidget(black_QPushButton,True)
        return color_QWidget

    def indexColor_create_QWidget(self):
        color_QWidget=QWidget()
        custom_QGridLayout=QGridLayout(self)
        color_QWidget.setLayout(custom_QGridLayout)

        right_QVBoxLayout=QVBoxLayout(self)
        custom_QGridLayout.addLayout(right_QVBoxLayout,1,0)

        right_QLabel=QLabel("Right Color",self)
        right_QVBoxLayout.addWidget(right_QLabel,True)
        return color_QWidget
    
    def mgearColor_create_QWidget(self):
        color_QWidget=QWidget()
        custom_QGridLayout=QGridLayout(self)
        color_QWidget.setLayout(custom_QGridLayout)

        right_QVBoxLayout=QVBoxLayout(self)
        custom_QGridLayout.addLayout(right_QVBoxLayout,1,0)

        right_QLabel=QLabel("Right Color",self)
        right_QVBoxLayout.addWidget(right_QLabel,True)
        return color_QWidget
    
    def grisColor_create_QWidget(self):
        color_QWidget=QWidget()
        custom_QGridLayout=QGridLayout(self)
        color_QWidget.setLayout(custom_QGridLayout)

        right_QVBoxLayout=QVBoxLayout(self)
        custom_QGridLayout.addLayout(right_QVBoxLayout,1,0)

        right_QLabel=QLabel("Right Color",self)
        right_QVBoxLayout.addWidget(right_QLabel,True)
        return color_QWidget

    #Public Function
    def buttonRedOnClicked(self):
        print("Red")
    def buttonPinkOnClicked(self):
        print("Pink")
    def buttonCrimsonOnClicked(self):
        print("Crimson")
    def buttonDarkRedOnClicked(self):
        print("DarkRed")
    def buttonYellowOnClicked(self):
        print("Yellow")
    def buttonLimeOnClicked(self):
        print("Lime")
    def buttonGreenOnClicked(self):
        print("Green")
    def buttonDarkGreenOnClicked(self):
        print("DarkGreen")
    def buttonBlueOnClicked(self):
        print("Blue")
    def buttonCyanOnClicked(self):
        print("Cyan")
    def buttonTealOnClicked(self):
        print("Teal")
    def buttonDarkBlueOnClicked(self):
        print("DarkBlue")
    def buttonMagentaOnClicked(self):
        print("Magenta")
    def buttonPurpleOnClicked(self):
        print("Purple")
    def buttonWhiteOnClicked(self):
        print("White")
    def buttonBlackOnClicked(self):
        print("Black")
    def buttonOverrideNeutralOnClicked(self):
        print("OverrideNeutral")
    def buttonWireNeutralOnClicked(self):
        print("WireNeutral")

#viewWindow=ColorChengeWindouBase()
#viewWindow.show()
