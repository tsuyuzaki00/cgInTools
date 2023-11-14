# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import maya.api.OpenMayaAnim as oma2
import sys,math

def node_query_MObject(node):
    if node == None:
        return None
    elif not type(node) is str and not type(node) is unicode:
        om2.MGlobal.displayError("Please insert one string in value")
        sys.exit()
    node_MSelectionList=om2.MGlobal.getSelectionListByName(node)
    node_MObject=node_MSelectionList.getDependNode(0)
    return node_MObject

def convertMObject_query_MDagPath(node_MObject):
    node_MDagPath=om2.MDagPath().getAPathTo(node_MObject)
    return node_MDagPath