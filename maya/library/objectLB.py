# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import maya.api.OpenMayaAnim as oma2
import sys,math

import cgInTools as cit
from ...library import baseLB as bLB
from ...library import jsonLB as jLB
cit.reloads([bLB,jLB])

RULES_DICT=jLB.readJson(cit.mayaSettings_dir,"openLibrary")

class DataNode(bLB.SelfOrigin):
    def __init__(self):
        super(DataNode,self).__init__()

class DataAttribute(bLB.SelfOrigin):
    def __init__(self):
        super(DataAttribute,self).__init__()

class DataVertex(bLB.SelfOrigin):
    def __init__(self):
        super(DataVertex,self).__init__()

class DataEdge(bLB.SelfOrigin):
    def __init__(self):
        super(DataVertex,self).__init__()

class DataFace(bLB.SelfOrigin):
    def __init__(self):
        super(DataFace,self).__init__()

class SelfDGNode(bLB.SelfOrigin):
    def __init__(self):
        super(SelfDGNode,self).__init__()
        self._node_Node=None
        self._attr_Attributes=[]
        self._plug_Plugs=[]
        self._dataChoice_strs+=[
            "Plugs"
        ]
        self._doIt_strs+=[
            "plugsDoIt",
        ]

    #Setting Function
    def setPlugs(self,variables):
        self._plug_Plugs=variables
        return self._plug_Plugs
    def addPlugs(self,variables):
        self._plug_Plugs+=variables
        return self._plug_Plugs
    def getPlugs(self):
        return self._plug_Plugs
    
    #Public Function
    def plugsDoIt(self):
        for _plug_Plug in self._plug_Plugs:
            _plug_Plug.doIt()

class SelfDAGNode(SelfDGNode):
    def __init__(self):
        super(SelfDAGNode,self).__init__()
        self._parent_MObject=None
        self._fullPath_bool=False
        self._firstOnly_bool=False
        self._firstAddress_int=0
        self._dataChoice_strs+=[
            "FullPath",
            "FirstOnly",
            "FirstAddress",
        ]
        self._doIt_strs+=[
            "parent",
            "replaceByParent",
            "replaceByChild",
            "replaceByShape"
        ]
    
    #Single Function
    def convertMObject_create_MDagPath(self,node_MObject):
        node_MDagPath=om2.MDagPath().getAPathTo(node_MObject)
        return node_MDagPath
    
    def fullPath_query_str(self,node_MDagPath):
        name_str=node_MDagPath.fullPathName()
        return name_str
    
    def shape_query_MObject(self,node_MDagPath):
        shape_MDagPath=node_MDagPath.extendToShape()
        shape_MObject=shape_MDagPath.node()
        return shape_MObject

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

    def nodeTypes_query_strs(self,node_MObjects):
        if node_MObjects == None:
            return None
        nodeType_strs=[om2.MFnDependencyNode(node_MObject).typeName for node_MObject in node_MObjects]
        if nodeType_strs == []:
            return None
        else:
            return nodeType_strs
    
    #Multi Function
    def _fullPathSwitch_query_str(self,node_MObject,fullPath=False):
        if fullPath:
            node_MDagPath=self.convertMObject_create_MDagPath(node_MObject)
            name_str=self.fullPath_query_str(node_MDagPath)
        else:
            node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)
            name_str=node_MFnDependencyNode.name()
        return name_str

    def _fullPathSwitch_query_strs(self,node_MObjects,fullPath=False):
        name_strs=[self._fullPathSwitch_query_str(node_MObject,fullPath) for node_MObject in node_MObjects]
        return name_strs

    #Setting Function
    def setFullPath(self,variable):
        self._fullPath_bool=variable
    def getFullPath(self):
        return self._fullPath_bool
    
    def setFirstOnly(self,variable):
        self._firstOnly_bool=variable
    def getFirstOnly(self):
        return self._firstOnly_bool
    
    def setFirstAddress(self,variable):
        self._firstAddress_int=variable
    def getFirstAddress(self):
        return self._firstAddress_int
    
    def getNode(self,fullPath=None):
        _fullPath_bool=fullPath or self._fullPath_bool
        node_str=self._fullPathSwitch_query_str(self._node_MObject,_fullPath_bool)
        return node_str

    def setParent(self,variable):
        self._parent_MObject=self.selectNode_create_MObject(variable)
    def getParent(self,fullPath=None):
        _fullPath_bool=fullPath or self._fullPath_bool
        node_str=self._fullPathSwitch_query_str(self._parent_MObject,_fullPath_bool)
        return node_str
    
    #Public Function
    def parent(self,node=None,parent=None):
        _node_MObject=self.selectNode_create_MObject(node) or self._node_MObject
        _parent_MObject=self.selectNode_create_MObject(parent) or self._parent_MObject
        
        node_MDagPath=self.convertMObject_create_MDagPath(_node_MObject)
        parent_MDagPath=self.convertMObject_create_MDagPath(_parent_MObject)
        
        parent_MDagModifier=om2.MDagModifier()
        parent_MDagModifier.reparentNode(node_MDagPath,parent_MDagPath)
        parent_MDagModifier.doIt()

    def replaceByParent(self,node=None,fullPath=None):
        _node_MObject=self.selectNode_create_MObject(node) or self._node_MObject
        _fullPath_bool=fullPath or self._fullPath_bool

        node_MDagPath=self.convertMObject_create_MDagPath(_node_MObject)

        self._node_MObject=self.parent_query_MObject(node_MDagPath)
        node_str=self._fullPathSwitch_query_str(self._node_MObject,_fullPath_bool)
        return node_str
    
    def replaceByChild(self,node=None,fullPath=False,firstAddress=None):
        _node_MObject=self.selectNode_create_MObject(node) or self._node_MObject
        _fullPath_bool=fullPath or self._fullPath_bool
        _firstAddress_int=firstAddress or self._firstAddress_int

        node_MDagPath=self.convertMObject_create_MDagPath(_node_MObject)

        child_MObjects=self.child_query_MObjects(node_MDagPath,shapeOnly=False)
        self._node_MObject=child_MObjects[_firstAddress_int]
        node_str=self._fullPathSwitch_query_str(self._node_MObject,_fullPath_bool)
        return node_str
        
    def replaceByShape(self,node=None,fullPath=False,firstAddress=None):
        _node_MObject=self.selectNode_create_MObject(node) or self._node_MObject
        _fullPath_bool=fullPath or self._fullPath_bool
        _firstAddress_int=firstAddress or self._firstAddress_int

        node_MDagPath=self.convertMObject_create_MDagPath(_node_MObject)

        shape_MObjects=self.child_query_MObjects(node_MDagPath,shapeOnly=True)
        self._node_MObject=shape_MObjects[_firstAddress_int]
        node_str=self._fullPathSwitch_query_str(self._node_MObject,_fullPath_bool)
        return node_str

    def queryShape(self,node=None,fullPath=None):
        _node_MObject=self.selectNode_create_MObject(node) or self._node_MObject
        _fullPath_bool=fullPath or self._fullPath_bool
        node_MDagPath=self.convertMObject_create_MDagPath(_node_MObject)
        shape_MObject=self.shape_query_MObject(node_MDagPath)
        shape_str=self._fullPathSwitch_query_str(shape_MObject,_fullPath_bool)
        return shape_str
    
    def queryShapes(self,node=None,fullPath=None,firstOnly=None,firstAddress=None):
        _node_MObject=self.selectNode_create_MObject(node) or self._node_MObject
        _fullPath_bool=fullPath or self._fullPath_bool
        _firstOnly_bool=firstOnly or self._firstOnly_bool
        _firstAddress_int=firstAddress or self._firstAddress_int

        node_MDagPath=self.convertMObject_create_MDagPath(_node_MObject)
        shape_MObjects=self.child_query_MObjects(node_MDagPath,shapeOnly=True)
        if shape_MObjects == None:
            return None
        if _firstOnly_bool:
            shape_str=self._fullPathSwitch_query_str(shape_MObjects[_firstAddress_int],_fullPath_bool)
            return shape_str
        else:
            shape_strs=self._fullPathSwitch_query_strs(shape_MObjects,_fullPath_bool)
            return shape_strs
    
    def queryShapeType(self,node=None):
        _node_MObject=self.selectNode_create_MObject(node) or self._node_MObject

        node_MDagPath=self.convertMObject_create_MDagPath(_node_MObject)
        shape_MObject=self.shape_query_MObject(node_MDagPath)
        shapeType_str=self.nodeType_query_str(shape_MObject)
        return shapeType_str
    
    def queryShapeTypes(self,node=None,firstOnly=None,firstAddress=None):
        _node_MObject=self.selectNode_create_MObject(node) or self._node_MObject
        _firstOnly_bool=firstOnly or self._firstOnly_bool
        _firstAddress_int=firstAddress or self._firstAddress_int

        node_MDagPath=self.convertMObject_create_MDagPath(_node_MObject)
        shape_MObjects=self.child_query_MObjects(node_MDagPath,shapeOnly=True)
        if shape_MObjects == None:
            return None
        if _firstOnly_bool:
            shapeType_str=self.nodeType_query_str(shape_MObjects[_firstAddress_int])
            return shapeType_str
        else:
            shapeType_strs=[]
            for shape_MObject in shape_MObjects:
                shapeType_str=self.nodeType_query_str(shape_MObject)
                shapeType_strs.append(shapeType_str)
            return shapeType_strs

    def queryParent(self,node=None,fullPath=None):
        _node_MObject=self.selectNode_create_MObject(node) or self._node_MObject
        _fullPath_bool=fullPath or self._fullPath_bool

        node_MDagPath=self.convertMObject_create_MDagPath(_node_MObject)
        parent_MObject=self.parent_query_MObject(node_MDagPath)
        parent_str=self._fullPathSwitch_query_str(parent_MObject,_fullPath_bool)
        if parent_str == "world" or parent_str == "":
            return None
        else:
            return parent_str

    def queryChilds(self,node=None,fullPath=False,firstOnly=None,firstAddress=None):
        _node_MObject=self.selectNode_create_MObject(node) or self._node_MObject
        _fullPath_bool=fullPath or self._fullPath_bool
        _firstOnly_bool=firstOnly or self._firstOnly_bool
        _firstAddress_int=firstAddress or self._firstAddress_int

        node_MDagPath=self.convertMObject_create_MDagPath(_node_MObject)
        child_MObjects=self.child_query_MObjects(node_MDagPath)
        if child_MObjects == None:
            return None
        if _firstOnly_bool:
            child_str=self._fullPathSwitch_query_str(child_MObjects[_firstAddress_int],_fullPath_bool)
            return child_str
        else:
            child_strs=self._fullPathSwitch_query_strs(child_MObjects,_fullPath_bool)
            return child_strs

class SelfTransNode(SelfDAGNode):
    def __init__(self):
        super(SelfTransNode,self).__init__()

class SelfJoint(SelfDAGNode):
    def __init__(self):
        super(SelfJoint,self).__init__()

class SelfLight(SelfDAGNode):
    def __init__(self):
        super(SelfLight,self).__init__()

class SelfCamera(SelfDAGNode):
    def __init__(self):
        super(SelfCamera,self).__init__()

class SelfGeometry(SelfDAGNode):
    def __init__(self):
        super(SelfGeometry,self).__init__()

class SelfCurve(SelfDAGNode):
    def __init__(self):
        super(SelfCurve,self).__init__()

class SelfSurface(SelfDAGNode):
    def __init__(self):
        super(SelfSurface,self).__init__()

