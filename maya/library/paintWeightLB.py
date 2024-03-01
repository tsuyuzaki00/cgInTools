# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

class AppPaintWeight(object):
    def __init__(self):
        self._artAttr_str="artAttrSkinContext" # "artAttrContext" or "artAttrSkinContext" or "artAttrBlendShapeContext"
        self._selectedattroper_str="absolute" # "absolute" or "additive" or "scale" or "smooth"
        self._value_float=0.0 # 0.0~1.0

    #Single Function
    @staticmethod
    def paintValue_edit_func(artAttr_str,value_float=0.0,sao=None):
        if sao is None:
            selectedattroper_str=cmds.artAttrCtx(artAttr_str,q=True,sao=True)
            cmds.artAttrCtx(artAttr_str,e=True,val=value_float,sao=selectedattroper_str)
        elif sao is "absolute" or sao is "additive" or sao is "scale" or sao is "smooth":
            cmds.artAttrCtx(artAttr_str,e=True,val=value_float,sao=sao)
        else:
            cmds.error("The selector trooper name is incorrect.")

    @staticmethod
    def flood_edit_func(artAttr_str):
        cmds.artAttrCtx(artAttr_str,e=True,clear=True)

    @staticmethod
    def soomth_edit_func(artAttr_str):
        selectedattroper_str=cmds.artAttrCtx(artAttr_str,q=True,sao=True)
        cmds.artAttrCtx(artAttr_str,e=True,sao="smooth")
        cmds.artAttrCtx(artAttr_str,e=True,clear=True)
        cmds.artAttrCtx(artAttr_str,e=True,sao=selectedattroper_str)

    #Multi Function
    def _reverse_edit_func(self,artAttr_str):
        selectedattroper_str=cmds.artAttrCtx(artAttr_str,q=True,sao=True)
        getValue_float=cmds.artAttrCtx(artAttr_str,q=True,val=0)
        reverseValue_float=1-getValue_float
        if selectedattroper_str == "additive":
            self.paintValue_edit_func(artAttr_str,reverseValue_float,"scale")
        elif selectedattroper_str == "scale":
            self.paintValue_edit_func(artAttr_str,reverseValue_float,"additive")
        else:
            self.paintValue_edit_func(artAttr_str,reverseValue_float)
    
    #Setting Function
    def setArtAttr(self,variable):
        self._artAttr_str=variable
        return self._artAttr_str
    def getArtAttr(self):
        return self._artAttr_str

    def setValue(self,variable):
        self._value_float=variable
        return self._value_float
    def getValue(self):
        return self._value_float

    def setSelectedattroper(self,variable):
        self._selectedattroper_str=variable
        return self._selectedattroper_str
    def getSelectedattroper(self):
        return self._selectedattroper_str

    #Public Function
    def paintValue(self):
        self.paintValue_edit_func(self._artAttr_str,self._value_float,self._selectedattroper_str)

    def flood(self):
        self.flood_edit_func(self._artAttr_str)
    
    def reverse(self):
        self._reverse_edit_func(self._artAttr_str)
    
    def soomth(self):
        self.soomth_edit_func(self._artAttr_str)
