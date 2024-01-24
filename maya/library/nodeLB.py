# -*- coding: iso-8859-15 -*-
import math
import maya.cmds as cmds
import maya.api.OpenMaya as om2

import cgInTools as cit
from . import appLB as aLB
from . import dataLB as dLB
from . import matrixLB as mLB
cit.reloads([aLB,dLB,mLB])

class AppNode(aLB.AppOpenMayaBase):
    def __init__(self):
        super(AppNode,self).__init__()
        self._node_DataNode=None
        self._parent_DataNode=None
        self._child_DataNodes=[]

    #Inheritance Function
    def _parent_edit_func(self,node_str,parent_str):
        node_MObject=self.node_query_MObject(node_str)
        
        parent_MObject=self.node_query_MObject(parent_str)

        parent_MDagModifier=om2.MDagModifier()
        parent_MDagModifier.reparentNode(node_MObject,parent_MObject)
        parent_MDagModifier.doIt()

    #Setting Function
    def setDataNode(self,variable):
        self._node_DataNode=variable
        return self._node_DataNode
    def getDataNode(self):
        return self._node_DataNode
    
    def setParentDataNode(self,variable):
        self._parent_DataNode=variable
        return self._parent_DataNode
    def currentParentDataNode(self):
        node_MObject=self.node_query_MObject(self._node_DataNode.getName())
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        parent_MObject=self.parent_query_MObject(node_MDagPath)
        self._parent_DataNode=dLB.DataNode(parent_MObject)
        return self._parent_DataNode
    def getParentDataNode(self):
        return self._parent_DataNode
    
    def setChildDataNodes(self,variables):
        self._child_DataNodes=variables
        return self._child_DataNodes
    def currentChildDataNodes(self):
        node_MObject=self.node_query_MObject(self._node_DataNode.getName())
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        child_MObjects=self.child_query_MObjects(node_MDagPath)
        self._child_DataNodes=[]
        for child_MObject in child_MObjects:
            child_DataNode=dLB.DataNode(child_MObject)
            self._child_DataNodes.append(child_DataNode)
        return self._child_DataNodes
    def getChildDataNodes(self):
        return self._child_DataNodes
    
    #Public Function
    def create(self):
        node_MObject=self.node_create_MObject(self._node_DataNode.getType(),self._node_DataNode.getName())
        node_DataNode=dLB.DataNode(node_MObject)
        return node_DataNode

    def moveParent(self):
        self._parent_edit_func(self._node_DataNode.getName(),self._parent_DataNode.getName())

    def worldParent(self):
        cmds.parent(self._node_DataNode.getName(),w=True)

    def addChilds(self):
        for _child_DataNode in self._child_DataNodes:
            self._parent_edit_func(_child_DataNode.getName(),self._node_DataNode.getName())

    def removeChilds(self):
        for _child_DataNode in self._child_DataNodes:
            cmds.parent(_child_DataNode.getName(),w=True)

    def queryName(self):
        nodeName_str=self._node_DataNode.getName()
        return nodeName_str

    def queryFullPathName(self):
        node_MObject=self.node_query_MObject(self._node_DataNode.getName())
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        node_MFnDagNode=om2.MFnDagNode(node_MDagPath)
        fullPathName_str=node_MFnDagNode.fullPathName()
        return fullPathName_str

    def queryParentName(self):
        node_MObject=self.node_query_MObject(self._node_DataNode.getName())
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        parent_MObject=self.parent_query_MObject(node_MDagPath)
        parent_MFnDependencyNode=om2.MFnDependencyNode(parent_MObject)
        parentName_str=parent_MFnDependencyNode.name()
        return parentName_str

    def queryFullPathParentName(self):
        node_MObject=self.node_query_MObject(self._node_DataNode.getName())
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        parent_MObject=self.parent_query_MObject(node_MDagPath)
        parent_MDagPath=self.convertMObject_query_MDagPath(parent_MObject)
        node_MFnDagNode=om2.MFnDagNode(parent_MDagPath)
        fullPathName_str=node_MFnDagNode.fullPathName()
        if fullPathName_str is "" or fullPathName_str is None:
            return None
        return fullPathName_str

    def queryChildNames(self):
        node_MObject=self.node_query_MObject(self._node_DataNode.getName())
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        child_MObjects=self.child_query_MObjects(node_MDagPath)
        if child_MObjects is None:
            return None
        childName_strs=[]
        for child_MObject in child_MObjects:
            child_MFnDependencyNode=om2.MFnDependencyNode(child_MObject)
            childName_str=child_MFnDependencyNode.name()
            childName_strs.append(childName_str)
        return childName_strs

    def queryFullPathChildNames(self):
        node_MObject=self.node_query_MObject(self._node_DataNode.getName())
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        child_MObjects=self.child_query_MObjects(node_MDagPath)
        if child_MObjects is None:
            return None
        fullPathName_strs=[]
        for child_MObject in child_MObjects:
            child_MDagPath=self.convertMObject_query_MDagPath(child_MObject)
            child_MFnDagNode=om2.MFnDagNode(child_MDagPath)
            fullPathName_str=child_MFnDagNode.fullPathName()
            fullPathName_strs.append(fullPathName_str)
        return fullPathName_strs

    def queryShapeNames(self):
        node_MObject=self.node_query_MObject(self._node_DataNode.getName())
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        shape_MObjects=self.child_query_MObjects(node_MDagPath,shapeOnly=True)
        shapeName_strs=[]
        for shape_MObject in shape_MObjects:
            shape_MFnDependencyNode=om2.MFnDependencyNode(shape_MObject)
            shapeName_str=shape_MFnDependencyNode.name()
            shapeName_strs.append(shapeName_str)
        return shapeName_strs