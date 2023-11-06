# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import maya.api.OpenMayaAnim as oma2
import sys,math

def node_query_MObject(nodeName_str):
    if nodeName_str == None:
        return None
    elif not isinstance(nodeName_str,str):
        om2.MGlobal.displayError("Please insert one string in value")
        sys.exit()
    node_MSelectionList=om2.MGlobal.getSelectionListByName(nodeName_str)
    node_MObject=node_MSelectionList.getDependNode(0)
    return node_MObject

def main():
    node_MObject=node_query_MObject("pCube1")
    node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)
    
    attr_MFnAttribute=om2.MFnGenericAttribute()

    #attr_MFnAttribute.addDataType(1)
    #attr_MTypeId=om2.MTypeId(0x07EFE)
    #attr_MFnAttribute.addTypeId(attr_MTypeId)
    attr_MObject=attr_MFnAttribute.create("Zest","zt")
    attr_MFnAttribute.addNumericType(11)

    node_MFnDependencyNode.addAttribute(attr_MObject)
    node_MPlug=node_MFnDependencyNode.findPlug(attr_MObject,False)
    node_MPlug.isChannelBox=False
    #node_MPlug.isKeyable=True
    #node_MPlug.isLocked=False
    #translate_MPlug=node_MFnDependencyNode.findPlug("translate",False)
    #print(translate_MPlug.isChild)

main()