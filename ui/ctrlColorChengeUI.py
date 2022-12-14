from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class ColorChengeWindouBase(QWidget):
    def __init__(self, *args, **kwargs):
        super(ColorChengeWindouBase, self).__init__(*args, **kwargs)
        self.setWindowFlags(Qt.Window)

        main_QBoxLayout=QBoxLayout(QBoxLayout.TopToBottom,self)

        self.custom_QGridLayout=QGridLayout(self)
        main_QBoxLayout.addLayout(self.custom_QGridLayout)

        right_QLabel=QLabel("Right Color",self)
        self.custom_QGridLayout.addWidget(right_QLabel,0,0)

        right_QVBoxLayout=QVBoxLayout(self)
        self.custom_QGridLayout.addLayout(right_QVBoxLayout,1,0)

        red=QPushButton("Red",self)
        red.setStyleSheet("color: red;")
        red.clicked.connect(self.buttonRedOnClicked)
        right_QVBoxLayout.addWidget(red,True)

        pink=QPushButton("Pink",self)
        pink.setStyleSheet("color: pink;")
        pink.clicked.connect(self.buttonPinkOnClicked)
        right_QVBoxLayout.addWidget(pink,True)
        
        crimson=QPushButton("Crimson",self)
        crimson.setStyleSheet("color: crimson;")
        crimson.clicked.connect(self.buttonCrimsonOnClicked)
        right_QVBoxLayout.addWidget(crimson,True)
        
        darkRed=QPushButton("DarkRed",self)
        darkRed.setStyleSheet("color: darkRed;")
        darkRed.clicked.connect(self.buttonDarkRedOnClicked)
        right_QVBoxLayout.addWidget(darkRed,True)

        center_QLabel=QLabel("Center Color",self)
        self.custom_QGridLayout.addWidget(center_QLabel,0,1)

        center_QVBoxLayout=QVBoxLayout(self)
        self.custom_QGridLayout.addLayout(center_QVBoxLayout,1,1)

        yellow=QPushButton("Yellow",self)
        yellow.setStyleSheet("color: yellow;")
        yellow.clicked.connect(self.buttonYellowOnClicked)
        center_QVBoxLayout.addWidget(yellow,True)

        lime=QPushButton("Lime",self)
        lime.setStyleSheet("color: lime;")
        lime.clicked.connect(self.buttonLimeOnClicked)
        center_QVBoxLayout.addWidget(lime,True)

        green=QPushButton("Green",self)
        green.setStyleSheet("color: mediumseagreen;")
        green.clicked.connect(self.buttonGreenOnClicked)
        center_QVBoxLayout.addWidget(green,True)

        darkGreen=QPushButton("DarkGreen",self)
        darkGreen.clicked.connect(self.buttonDarkGreenOnClicked)
        darkGreen.setStyleSheet("color: darkGreen;")
        center_QVBoxLayout.addWidget(darkGreen,True)

        left_QLabel=QLabel("Left Color",self)
        self.custom_QGridLayout.addWidget(left_QLabel,0,2)
        
        left_QVBoxLayout=QVBoxLayout(self)
        self.custom_QGridLayout.addLayout(left_QVBoxLayout,1,2)

        blue=QPushButton("Blue",self)
        blue.setStyleSheet("color: blue;")
        blue.clicked.connect(self.buttonBlueOnClicked)
        left_QVBoxLayout.addWidget(blue,True)

        cyan=QPushButton("Cyan",self)
        cyan.setStyleSheet("color: cyan;")
        cyan.clicked.connect(self.buttonCyanOnClicked)
        left_QVBoxLayout.addWidget(cyan,True)
        
        teal=QPushButton("Teal",self)
        teal.setStyleSheet("color: steelBlue;")
        teal.clicked.connect(self.buttonTealOnClicked)
        left_QVBoxLayout.addWidget(teal,True)
        
        darkBlue=QPushButton("DarkBlue",self)
        darkBlue.setStyleSheet("color: darkBlue;")
        darkBlue.clicked.connect(self.buttonDarkBlueOnClicked)
        left_QVBoxLayout.addWidget(darkBlue,True)

        other_QLabel=QLabel("Other Color",self)
        self.custom_QGridLayout.addWidget(other_QLabel,0,3)
        
        other_QVBoxLayout=QVBoxLayout(self)
        self.custom_QGridLayout.addLayout(other_QVBoxLayout,1,3)

        magenta=QPushButton("Magenta",self)
        magenta.setStyleSheet("color: magenta;")
        magenta.clicked.connect(self.buttonMagentaOnClicked)
        other_QVBoxLayout.addWidget(magenta,True)

        purple=QPushButton("Purple",self)
        purple.setStyleSheet("color: purple;")
        purple.clicked.connect(self.buttonPurpleOnClicked)
        other_QVBoxLayout.addWidget(purple,True)
        
        white=QPushButton("White",self)
        white.setStyleSheet("color: white;")
        white.clicked.connect(self.buttonWhiteOnClicked)
        other_QVBoxLayout.addWidget(white,True)
        
        black=QPushButton("Black", self)
        black.setStyleSheet("color: black;")
        black.clicked.connect(self.buttonBlackOnClicked)
        other_QVBoxLayout.addWidget(black,True)

        neutral=QPushButton("Neutral",self)
        neutral.setStyleSheet("color: gray;")
        neutral.clicked.connect(self.buttonNeutralOnClicked)
        self.custom_QGridLayout.addWidget(neutral,2,0,2,4)

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
    def buttonNeutralOnClicked(self):
        print("Neutral")

#viewWindow=ColorChengeWindouBase()
#viewWindow.show()
