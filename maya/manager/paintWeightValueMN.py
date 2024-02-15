# -*- coding: iso-8859-15 -*-
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import os
import maya.cmds as cmds

import cgInTools as cit
from ...ui import paintWeightValueUI as UI
from ..library import windowLB as wLB
from ..library import paintWeightLB as pwLB
from ..library import jsonLB as jLB
cit.reloads([UI,wLB,pwLB,jLB])

class PaintWeightWindow(UI.PaintWeightWindowBase):
    def __init__(self,parent):
        super(PaintWeightWindow,self).__init__(parent)
        self.setObjectName("selectView_list")
        self.setWindowTitle("selectView_list")
        self.buttonLeft_QPushButton.setText("flood")
        self.buttonCenter_QPushButton.setText("reverse")
        self.buttonRight_QPushButton.setText("smooth")
        self.paintEdit=pwLB.PaintWeight()

    #Public Function           
    def button0OnClicked(self):
        self._attrAttr="artAttr"+self.radioGrp_QButtonGroup.checkedButton().text()
        self.paintEdit.setValue(0)
        self.paintEdit.setSelectedattroper("scale")
        self.paintEdit.setArtAttr(self._attrAttr)
        self.paintEdit.paintValue()
    
    def button0001OnClicked(self):
        self._attrAttr="artAttr"+self.radioGrp_QButtonGroup.checkedButton().text()
        self.paintEdit.setValue(0.001)
        self.paintEdit.setSelectedattroper("additive")
        self.paintEdit.setArtAttr(self._attrAttr)
        self.paintEdit.paintValue()
    
    def button001OnClicked(self):
        self._attrAttr="artAttr"+self.radioGrp_QButtonGroup.checkedButton().text()
        self.paintEdit.setValue(0.01)
        self.paintEdit.setSelectedattroper("additive")
        self.paintEdit.setArtAttr(self._attrAttr)
        self.paintEdit.paintValue()
    
    def button005OnClicked(self):
        self._attrAttr="artAttr"+self.radioGrp_QButtonGroup.checkedButton().text()
        self.paintEdit.setValue(0.05)
        self.paintEdit.setSelectedattroper("additive")
        self.paintEdit.setArtAttr(self._attrAttr)
        self.paintEdit.paintValue()
    
    def button01OnClicked(self):
        self._attrAttr="artAttr"+self.radioGrp_QButtonGroup.checkedButton().text()
        self.paintEdit.setValue(0.1)
        self.paintEdit.setSelectedattroper("additive")
        self.paintEdit.setArtAttr(self._attrAttr)
        self.paintEdit.paintValue()
    
    def button05OnClicked(self):
        self._attrAttr="artAttr"+self.radioGrp_QButtonGroup.checkedButton().text()
        self.paintEdit.setValue(0.5)
        self.paintEdit.setSelectedattroper("absolute")
        self.paintEdit.setArtAttr(self._attrAttr)
        self.paintEdit.paintValue()
    
    def button1OnClicked(self):
        self._attrAttr="artAttr"+self.radioGrp_QButtonGroup.checkedButton().text()
        self.paintEdit.setValue(1)
        self.paintEdit.setSelectedattroper("absolute")
        self.paintEdit.setArtAttr(self._attrAttr)
        self.paintEdit.paintValue()

    def buttonLeftOnClicked(self):
        self._attrAttr="artAttr"+self.radioGrp_QButtonGroup.checkedButton().text()
        self.paintEdit.setArtAttr(self._attrAttr)
        self.paintEdit.flood()

    def buttonCenterOnClicked(self):
        self._attrAttr="artAttr"+self.radioGrp_QButtonGroup.checkedButton().text()
        self.paintEdit.setArtAttr(self._attrAttr)
        self.paintEdit.reverse()

    def buttonRightOnClicked(self):
        self._attrAttr="artAttr"+self.radioGrp_QButtonGroup.checkedButton().text()
        self.paintEdit.setArtAttr(self._attrAttr)
        self.paintEdit.soomth()

def main():
    viewWindow=PaintWeightWindow(parent=wLB.mayaMainWindow_query_QWidget())
    viewWindow.show()