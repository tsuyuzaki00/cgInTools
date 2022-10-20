from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class ColorChengeWindouBase(QWidget):
    def __init__(self, *args, **kwargs):
        super(ColorChengeWindouBase, self).__init__(*args, **kwargs)
        self.setWindowFlags(Qt.Window)

        main_layout=QFormLayout(self)
        center_layout=QHBoxLayout(self)
        left_layout=QHBoxLayout(self)
        right_layout=QHBoxLayout(self)
        other_layout=QHBoxLayout(self)
        neutral_layout=QHBoxLayout(self)

        main_layout.addRow("Center Color",center_layout)
        main_layout.addRow("Left Color",left_layout)
        main_layout.addRow("Right Color",right_layout)
        main_layout.addRow("Other Color",other_layout)
        main_layout.addRow(neutral_layout)

        yellow=QPushButton("Yellow",self)
        lime=QPushButton("Lime",self)
        green=QPushButton("Green",self)
        darkGreen=QPushButton("DarkGreen",self)
        blue=QPushButton("Blue",self)
        cyan=QPushButton("Cyan",self)
        teal=QPushButton("Teal",self)
        darkBlue=QPushButton("DarkBlue",self)
        red=QPushButton("Red",self)
        pink=QPushButton("Pink",self)
        crimson=QPushButton("Crimson",self)
        darkRed=QPushButton("DarkRed",self)
        magenta=QPushButton("Magenta",self)
        purple=QPushButton("Purple",self)
        white=QPushButton("White",self)
        black=QPushButton("Black", self)
        neutral=QPushButton("Neutral",self)

        center_layout.addWidget(yellow,True)
        center_layout.addWidget(lime,True)
        center_layout.addWidget(green,True)
        center_layout.addWidget(darkGreen,True)
        left_layout.addWidget(blue,True)
        left_layout.addWidget(cyan,True)
        left_layout.addWidget(teal,True)
        left_layout.addWidget(darkBlue,True)
        right_layout.addWidget(red,True)
        right_layout.addWidget(pink,True)
        right_layout.addWidget(crimson,True)
        right_layout.addWidget(darkRed,True)
        other_layout.addWidget(magenta,True)
        other_layout.addWidget(purple,True)
        other_layout.addWidget(white,True)
        other_layout.addWidget(black,True)
        neutral_layout.addWidget(neutral,True)

        yellow.clicked.connect(self.yellowButton_onClicked_func)
        lime.clicked.connect(self.limeButton_onClicked_func)
        green.clicked.connect(self.greenButton_onClicked_func)
        darkGreen.clicked.connect(self.darkGreenButton_onClicked_func)
        blue.clicked.connect(self.blueButton_onClicked_func)
        cyan.clicked.connect(self.cyanButton_onClicked_func)
        teal.clicked.connect(self.tealButton_onClicked_func)
        darkBlue.clicked.connect(self.darkBlueButton_onClicked_func)
        red.clicked.connect(self.redButton_onClicked_func)
        pink.clicked.connect(self.pinkButton_onClicked_func)
        crimson.clicked.connect(self.crimsonButton_onClicked_func)
        darkRed.clicked.connect(self.darkRedButton_onClicked_func)
        magenta.clicked.connect(self.magentaButton_onClicked_func)
        purple.clicked.connect(self.purpleButton_onClicked_func)
        white.clicked.connect(self.whiteButton_onClicked_func)
        black.clicked.connect(self.blackButton_onClicked_func)
        neutral.clicked.connect(self.neutralButton_onClicked_func)

        yellow.setStyleSheet("color: yellow;")
        lime.setStyleSheet("color: lime;")
        green.setStyleSheet("color: mediumseagreen;")
        darkGreen.setStyleSheet("color: darkGreen;")
        blue.setStyleSheet("color: blue;")
        cyan.setStyleSheet("color: cyan;")
        teal.setStyleSheet("color: steelBlue;")
        darkBlue.setStyleSheet("color: darkBlue;")
        red.setStyleSheet("color: red;")
        pink.setStyleSheet("color: pink;")
        crimson.setStyleSheet("color: crimson;")
        darkRed.setStyleSheet("color: darkRed;")
        magenta.setStyleSheet("color: magenta;")
        purple.setStyleSheet("color: purple;")
        white.setStyleSheet("color: white;")
        black.setStyleSheet("color: black;")
        neutral.setStyleSheet("color: gray;")

    def yellowButton_onClicked_func(self):
        print("base")
    def limeButton_onClicked_func(self):
        print("base")
    def greenButton_onClicked_func(self):
        print("base")
    def darkGreenButton_onClicked_func(self):
        print("base")
    def blueButton_onClicked_func(self):
        print("base")
    def cyanButton_onClicked_func(self):
        print("base")
    def tealButton_onClicked_func(self):
        print("base")
    def darkBlueButton_onClicked_func(self):
        print("base")
    def redButton_onClicked_func(self):
        print("base")
    def pinkButton_onClicked_func(self):
        print("base")
    def crimsonButton_onClicked_func(self):
        print("base")
    def darkRedButton_onClicked_func(self):
        print("base")
    def magentaButton_onClicked_func(self):
        print("base")
    def purpleButton_onClicked_func(self):
        print("base")
    def whiteButton_onClicked_func(self):
        print("base")
    def blackButton_onClicked_func(self):
        print("base")
    def neutralButton_onClicked_func(self):
        print("base")

#window_instance = ColorChengeWindouBase()
#window_instance.show()
