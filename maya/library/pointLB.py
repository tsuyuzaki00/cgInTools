# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

def getPoints_query_list():
    pass

def jointOrientReset_edit_func(node):
    value=cmds.getAttr(node+".jointOrient")
    cmds.setAttr(node+".rotate",value,type="double3")
    cmds.setAttr(node+".jointOrient",0,0,0,type="double3")