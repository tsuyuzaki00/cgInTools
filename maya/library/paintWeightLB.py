# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from . import setBaseLB as sbLB
cit.reloads([sbLB])

class PaintWeight():
    def __init__(self):
        #artAttr_strs = ["artAttrContext","artAttrSkinContext","artAttrBlendShapeContext"]
        self._artAttr="artAttrSkinContext"
        self._selectedattroper="absolute"
        self._value=0

    def setArtAttr(self,variable):
        self._artAttr=variable
        return self._artAttr
    def getArtAttr(self):
        return self._artAttr

    def setValue(self,variable):
        self._value=variable
        return self._value
    def getValue(self):
        return self._value

    def setSelectedattroper(self,variable):
        self._selectedattroper=variable
        return self._selectedattroper
    def getSelectedattroper(self):
        return self._selectedattroper

    #Single Function
    def paintValue_edit_func(self,artAttr_str,value=0,sao=None):
        if sao is None:
            self._selectedattroper=cmds.artAttrCtx(artAttr_str,q=True,sao=True)
            cmds.artAttrCtx(artAttr_str,e=True,val=value,sao=self._selectedattroper)
        elif sao is "absolute" or sao is "additive" or sao is "scale" or sao is "smooth":
            cmds.artAttrCtx(artAttr_str,e=True,val=value,sao=sao)
        else:
            cmds.error("The selector trooper name is incorrect.")

    def flood_edit_func(self,artAttr_str):
        cmds.artAttrCtx(artAttr_str,e=True,clear=True)

    def soomth_edit_func(self,artAttr_str):
        selectedattroper_str=cmds.artAttrCtx(artAttr_str,q=True,sao=True)
        cmds.artAttrCtx(artAttr_str,e=True,sao="smooth")
        cmds.artAttrCtx(artAttr_str,e=True,clear=True)
        cmds.artAttrCtx(artAttr_str,e=True,sao=selectedattroper_str)

    #Multi Function
    def _reverse_edit_func(self,artAttr_str):
        selectedattroper_str=cmds.artAttrCtx(artAttr_str,q=True,sao=True)
        getValue=cmds.artAttrCtx(artAttr_str,q=True,val=0)
        value=1-getValue
        if selectedattroper_str == "additive":
            self.paintValue_edit_func(artAttr_str,value,"scale")
        elif selectedattroper_str == "scale":
            self.paintValue_edit_func(artAttr_str,value,"additive")
        else:
            self.paintValue_edit_func(artAttr_str,value)
    
    #Public Function
    def paintValue(self):
        self.paintValue_edit_func(self._artAttr,self._value,self._selectedattroper)
    def flood(self):
        self.flood_edit_func(self._artAttr)
    def reverse(self):
        self._reverse_edit_func(self._artAttr)
    def soomth(self):
        self.soomth_edit_func(self._artAttr)
        
