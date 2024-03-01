# -*- coding: iso-8859-15 -*-
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import random
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

import cgInTools as cit
from ...ui import paintWeightValueUI as UI
from ..library import windowLB as wLB
from ..library import paintWeightLB as pwLB
cit.reloads([UI,wLB,pwLB])

class PaintWeightWindow(MayaQWidgetDockableMixin,UI.PaintWeightWindowBase):
    def __init__(self,parent):
        super(PaintWeightWindow,self).__init__(parent)
        windowTitle_str="paintWeightValue"
        random_int=random.randint(0,9999)
        self.setObjectName(windowTitle_str+str(random_int))
        self.setWindowTitle(windowTitle_str)

        self.buttonLeft_QPushButton.setText("flood")
        self.buttonCenter_QPushButton.setText("reverse")
        self.buttonRight_QPushButton.setText("smooth")
        self.paintEdit=pwLB.AppPaintWeight()

    #Public Function
    def button0Clicked(self):
        attrAttr_str="artAttr"+self.radioGrp_QButtonGroup.checkedButton().text()
        self.paintEdit.setValue(0)
        self.paintEdit.setSelectedattroper("scale")
        self.paintEdit.setArtAttr(attrAttr_str)
        self.paintEdit.paintValue()
    
    def button0001Clicked(self):
        attrAttr_str="artAttr"+self.radioGrp_QButtonGroup.checkedButton().text()
        self.paintEdit.setValue(0.001)
        self.paintEdit.setSelectedattroper("additive")
        self.paintEdit.setArtAttr(attrAttr_str)
        self.paintEdit.paintValue()
    
    def button001Clicked(self):
        attrAttr_str="artAttr"+self.radioGrp_QButtonGroup.checkedButton().text()
        self.paintEdit.setValue(0.01)
        self.paintEdit.setSelectedattroper("additive")
        self.paintEdit.setArtAttr(attrAttr_str)
        self.paintEdit.paintValue()
    
    def button005Clicked(self):
        attrAttr_str="artAttr"+self.radioGrp_QButtonGroup.checkedButton().text()
        self.paintEdit.setValue(0.05)
        self.paintEdit.setSelectedattroper("additive")
        self.paintEdit.setArtAttr(attrAttr_str)
        self.paintEdit.paintValue()
    
    def button01Clicked(self):
        attrAttr_str="artAttr"+self.radioGrp_QButtonGroup.checkedButton().text()
        self.paintEdit.setValue(0.1)
        self.paintEdit.setSelectedattroper("additive")
        self.paintEdit.setArtAttr(attrAttr_str)
        self.paintEdit.paintValue()
    
    def button05Clicked(self):
        attrAttr_str="artAttr"+self.radioGrp_QButtonGroup.checkedButton().text()
        self.paintEdit.setValue(0.5)
        self.paintEdit.setSelectedattroper("absolute")
        self.paintEdit.setArtAttr(attrAttr_str)
        self.paintEdit.paintValue()
    
    def button1Clicked(self):
        attrAttr_str="artAttr"+self.radioGrp_QButtonGroup.checkedButton().text()
        self.paintEdit.setValue(1)
        self.paintEdit.setSelectedattroper("absolute")
        self.paintEdit.setArtAttr(attrAttr_str)
        self.paintEdit.paintValue()

    def buttonLeftClicked(self):
        attrAttr_str="artAttr"+self.radioGrp_QButtonGroup.checkedButton().text()
        self.paintEdit.setArtAttr(attrAttr_str)
        self.paintEdit.flood()

    def buttonCenterClicked(self):
        attrAttr_str="artAttr"+self.radioGrp_QButtonGroup.checkedButton().text()
        self.paintEdit.setArtAttr(attrAttr_str)
        self.paintEdit.reverse()

    def buttonRightClicked(self):
        attrAttr_str="artAttr"+self.radioGrp_QButtonGroup.checkedButton().text()
        self.paintEdit.setArtAttr(attrAttr_str)
        self.paintEdit.soomth()

def main():
    viewWindow=PaintWeightWindow(parent=wLB.mayaMainWindow_query_QWidget())
    viewWindow.show(dockable=True,floating=True)