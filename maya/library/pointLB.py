# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

def getPoints_query_list():
    pass

def setTargetPos_edit_obj(source,target):
    cmds.parent(source,target)
    cmds.move(0,0,0,ls=True)
    cmds.rotate(0,0,0,os=True)
    cmds.parent(source,w=True)