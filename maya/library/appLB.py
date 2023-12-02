# -*- coding: iso-8859-15 -*-
import maya.api.OpenMaya as om2
import maya.api.OpenMayaAnim as oma2
import sys,math

class AppOpenMayaBase(object):
    def __init__(self):
        pass
    
    #Single Function
    def node_query_MObject(self,node):
        if node == None:
            return None
        elif not type(node) is str and not type(node) is unicode:
            om2.MGlobal.displayError("TypeError: Please insert one string in value. This is a "+str(type(node))+" type")
            sys.exit()
        node_MSelectionList=om2.MGlobal.getSelectionListByName(node)
        node_MObject=node_MSelectionList.getDependNode(0)
        return node_MObject
    
    def convertMObject_query_MDagPath(self,node_MObject):
        node_MDagPath=om2.MDagPath().getAPathTo(node_MObject)
        return node_MDagPath
    
    def nodeAttr_query_MPlug(self,node_MObject,attr_str):
        node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)
        node_MPlug=node_MFnDependencyNode.findPlug(attr_str,False)
        return node_MPlug

    def findAttr_query_MObject(self,node_MObject,attrName_str):
        node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)
        attr_MObject=node_MFnDependencyNode.findAlias(attrName_str)
        return attr_MObject
    
    def node_create_MObject(self,nodeType_str,nodeName_str):
        node_MFnDependencyNode=om2.MFnDependencyNode()
        node_MObject=node_MFnDependencyNode.create(nodeType_str,nodeName_str)
        return node_MObject
    
    def parent_query_MObject(self,node_MDagPath):
        node_MFnDagNode=om2.MFnDagNode(node_MDagPath)
        parent_MObject=node_MFnDagNode.parent(0)
        return parent_MObject

    def child_query_MObjects(self,node_MDagPath,shapeOnly=False):
        childs=[]
        for num in range(node_MDagPath.childCount()):
            child_MObject=node_MDagPath.child(num)
            if shapeOnly:
                if child_MObject.hasFn(om2.MFn.kShape):
                    childs.append(child_MObject)
            else:
                if not child_MObject.hasFn(om2.MFn.kShape):
                    childs.append(child_MObject)
        if childs == []:
            return None
        else:
            return childs