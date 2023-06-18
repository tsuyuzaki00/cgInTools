# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from . import setBaseLB as sbLB
from . import jsonLB as jLB
cit.reloads([sbLB,jLB])

RULES_DICT=jLB.getJson(cit.mayaSettings_dir,"library")

class Color(object):
    def __init__(self):
        super(Color,self).__init__()
        self._colorIndex_lists=RULES_DICT["rgbToColorIndex_lists"]
        self._node=None
        self._value=None

    #Single Function
    def drawingOverrideShape_query_list(self,node):
        if cmds.nodeType(node)=="transform":
            shapes=cmds.listRelatives(node,type="nurbsCurve")
            if not shapes == None:
                return shapes
        elif cmds.nodeType(node)=="joint":
            return [node]
        else :
            cmds.error("Attribute Drowing Overrides is missing")

    def overrideColor_edit_func(self,shapes,color=None):
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
        for shape in shapes:
            cmds.setAttr(shape+".overrideEnabled",use)
            cmds.setAttr(shape+".overrideRGBColors",mode)
            cmds.setAttr(shape+".overrideColor",indexColor)
            cmds.setAttr(shape+".overrideColorRGB",*rgbColor,type="double3")

    def wireColorShape_query_list(self,node):
        shapes=cmds.listRelatives(node,shapes=True,ni=True,pa=True)
        nodeShapes=[node]+shapes
        return nodeShapes

    def wireframeColor_edit_func(self,nodeShapes,color=None,ruleData=[]):
        if isinstance(color,int):
            use=2
            color=ruleData[color]
        elif isinstance(color,list) or isinstance(color,tuple):
            use=2
        else:
            use=0
            color=(0,0,0)
        for nodeShape in nodeShapes:
            cmds.setAttr(nodeShape+'.useObjectColor',use)
            cmds.setAttr(nodeShape+'.wireColorRGB',*color)

    #Setting Function
    def setNode(self,variable):
        self._node=variable
    def getNode(self):
        return self._node
    
    def setValue(self,variable):
        self._value=variable
    def getValue(self):
        return self._value

    #Public Function
    def overrideColor(self,node=None,value=None):
        _node=node or self._node 
        _value=value or self._value 

        shapes=self.drawingOverrideShape_query_list(_node)
        self.overrideColor_edit_func(shapes,_value)
    
    def wireframeColor(self,node=None,value=None):
        _node=node or self._node
        _value=value or self._value
        
        nodeShapes=self.wireColorShape_query_list(_node)
        self.wireframeColor_edit_func(nodeShapes,_value,ruleData=self._colorIndex_lists)
