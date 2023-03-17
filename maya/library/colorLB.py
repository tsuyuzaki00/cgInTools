# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from . import setBaseLB as sbLB
from . import jsonLB as jLB
cit.reloads([sbLB,jLB])

RULES_DICT=jLB.getJson(cit.mayaSettings_dir,"library")

class Color(sbLB.BaseObject):
    def __init__(self):
        super(Color,self).__init__()
        self._colorIndex_lists=RULES_DICT["rgbToColorIndex_lists"]

    #Single Function
    def getDrawingOverrides_query_list(self,obj):
        if cmds.nodeType(obj)=="transform":
            shapes=cmds.listRelatives(obj,type="nurbsCurve")
            if not shapes == None:
                return shapes
        elif cmds.nodeType(obj)=="joint":
            return [obj]
        else :
            cmds.error("Attribute Drowing Overrides is missing")

    def overrideColor_edit_func(self,objs,color=None):
        use=0
        mode=0
        indexColor=0
        rgbColor=(0,0,0)
        if isinstance(color,int):
            use=1
            indexColor=color
        elif isinstance(color,list) or isinstance(color,tuple):
            use=1
            mode=1
            rgbColor=color
            print(rgbColor)
        for obj in objs:
            cmds.setAttr(obj+".overrideEnabled",use)
            cmds.setAttr(obj+".overrideRGBColors",mode)
            cmds.setAttr(obj+".overrideColor",indexColor)
            cmds.setAttr(obj+".overrideColorRGB",*rgbColor,type="double3")

    def wireframeColor_edit_func(self,objs,color=None,ruleData=[]):
        if isinstance(color,int):
            use=2
            color=ruleData[color]
        elif isinstance(color,list) or isinstance(color,tuple):
            use=2
        else:
            use=0
            color=(0,0,0)
        for obj in objs:
            cmds.setAttr(obj+'.useObjectColor',use)
            cmds.setAttr(obj+'.wireColorRGB',*color)

    #Summary Function
    def __loading(self):
        self._shapes=cmds.listRelatives(self._object,shapes=True,ni=True,pa=True)
        self.wireObjs=[self._object]+self._shapes

    #Public Function
    def overrideColor(self):
        objs=self.getDrawingOverrides_query_list(self._object)
        self.overrideColor_edit_func(objs,self._value)
    
    def wireframeColor(self):
        self.__loading()
        self.wireframeColor_edit_func(self.wireObjs,self._value,ruleData=self._colorIndex_lists)
