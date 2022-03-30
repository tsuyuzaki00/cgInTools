from mainEdit import qt
from PySide2 import QtWidgets, QtCore, QtGui

class MainWindow(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        mainLayout = QtWidgets.QHBoxLayout(self)

        widgetA = QtWidgets.QRadioButton('TypeA', self)
        widgetB = QtWidgets.QRadioButton('TypeB', self)
        widgetB.setChecked(True)

        mainLayout.addWidget(widgetA)
        mainLayout.addWidget(widgetB)

        self.__across = QtWidgets.QButtonGroup(self)
        self.__across.addButton(widgetA, 0)
        self.__across.addButton(widgetB, 1)

        self.num = 1505135
        #self.num = self.__across.checkedId()

        widget = QtWidgets.QPushButton('Button', self)
        mainLayout.addWidget(widget)

        widget.clicked.connect(self.test)

    def test(self):
        self.num = self.__across.checkedId()
        print self.num

def option():
    window = MainWindow(qt.getMayaWindow())
    window.setWindowFlags(QtCore.Qt.Window)
    window.show()