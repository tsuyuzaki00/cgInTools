# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import maya.api.OpenMayaAnim as oma2
import sys,math

import cgInTools as cit
from ...library import jsonLB as jLB
cit.reloads([jLB])

def childTypes_query_strs(obj,nodeType):
    childs=cmds.ls(obj,sl=True,dag=True,type=nodeType)
    if nodeType == "nurbsCurve" or nodeType == "mesh" or nodeType == "nurbsSurface":
        transforms=[cmds.listRelatives(child,p=True,type="transform")[0] for child in childs]
        childs=transforms
    return childs
    
def removeIncludedNames_query_strs(names,removes=[]):
    newNames=[item for item in names if not any(substring in item for substring in removes)]
    return newNames

def _childSelections_query_strs(nodeType="transform",removes=[]):
    objs=cmds.ls(sl=True)
    selects=[]
    for obj in objs:
        childs=childTypes_query_strs(obj,nodeType)
        newChilds=removeIncludedNames_query_strs(childs,removes)
        cmds.select(newChilds,add=True)
        for newChild in newChilds:
            selects.append(newChild)
    return selects