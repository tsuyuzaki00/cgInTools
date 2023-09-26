# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import maya.api.OpenMayaAnim as oma2
import sys,math

import cgInTools as cit
from ...library import baseLB as bLB
from ...library import jsonLB as jLB
from . import dataLB as dLB
cit.reloads([bLB,jLB,dLB])

RULES_DICT=jLB.readJson(cit.mayaSettings_dir,"openLibrary")

class SelfDGNode(bLB.SelfOrigin):
    def __init__(self,selfDGNode=None):
        super(SelfDGNode,self).__init__()
        if type(selfDGNode) is SelfDGNode:
            self._node_DataNode=selfDGNode.getDataNode()
            self._name_DataName=selfDGNode.getDataName()
            self._attrName_strs=selfDGNode.getAttributeNames()
        else:
            self._node_DataNode=None
            self._name_DataName=None
            self._attrName_str=None
        self._dataChoice_strs+=[
            "DataNode",
            "DataName",
            "AttributeName"
        ]
        self._doIt_strs+=[
            "createNode",
            "duplicateNode",
            "rename",
            "searchDataAttribute",
            "searchDataPlug"
        ]
    
    #Single Function
    def node_query_MObject(self,node):
        if node == None:
            return None
        elif not isinstance(node,str):
            om2.MGlobal.displayError("Please insert one string in value")
            sys.exit()
        node_MSelectionList=om2.MGlobal.getSelectionListByName(node)
        node_MObject=node_MSelectionList.getDependNode(0)
        return node_MObject
    
    def node_create_func(self,nodeName_str,nodeType_str):
        node_MFnDependencyNode=om2.MFnDependencyNode()
        node_MFnDependencyNode.create(nodeType_str)
        node_MFnDependencyNode.setName(nodeName_str)

    def findAttr_create_DataAttribute(self,node_MObject,attrName_str):
        node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)
        attr_MObject=node_MFnDependencyNode.findAlias(attrName_str)
        attr_MFnAttribute=om2.MFnAttribute(attr_MObject)
        attrName_str=attr_MFnAttribute.name
        plug_DataAttribute=dLB.DataAttribute()
        return plug_DataAttribute
    
    def findPlug_create_DataPlug(self,node_MObject,attrName_str):
        node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)
        plug_MPlug=node_MFnDependencyNode.findPlug(attrName_str,False)
        plug_DataPlug=dLB.DataPlug(plug_MPlug)
        return plug_DataPlug

    #Setting Function
    def setDataNode(self,variable):
        self._node_DataNode=variable
        return self._node_DataNode
    def getDataNode(self):
        return self._node_DataNode

    def setDataName(self,variable):
        self._name_DataName=variable
        return self._name_DataName
    def getDataName(self):
        return self._name_DataName
    
    def setAttributeName(self,variable):
        self._attrName_str=variable
        return self._attrName_str
    def getAttributeName(self):
        return self._attrName_str
    
    #Public Function
    def createNode(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode

        self.node_create_func(_node_DataNode.getNodeName(),_node_DataNode.getNodeType())

    def duplicateNode(self,dataNode):
        _node_DataNode=dataNode or self._node_DataNode

    def rename(self):
        pass

    def searchDataAttribute(self,node_DataNode=None,attrName=None):
        _node_DataNode=node_DataNode or self._node_DataNode
        _attrName_str=attrName or self._attrName_str

        node_MObject=self.node_query_MObject(_node_DataNode.getNodeName())
        attr_DataAttribute=self.findAttr_create_DataAttribute(node_MObject,_attrName_str)
        return attr_DataAttribute

    def searchDataPlug(self,node_DataNode=None,attrName=None):
        _node_DataNode=node_DataNode or self._node_DataNode
        _attrName_str=attrName or self._attrName_str

        node_MObject=self.node_query_MObject(_node_DataNode.getNodeName())
        plug_DataPlug=self.findPlug_create_DataPlug(node_MObject,_attrName_str)
        return plug_DataPlug

class SelfDAGNode(SelfDGNode):
    def __init__(self):
        super(SelfDAGNode,self).__init__()
        #self._node_DataNode=None
        #self._name_DataName=None
        #self._attrName_strs=[]
        self._matrix_DataMatrix=None
        self._fullPath_bool=False

        self._dataChoice_strs+=[
            "DataMatrix",
            "FullPath"
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
    def setDataMatrix(self,variable):
        self._matrix_DataMatrix=variable
        return self._matrix_DataMatrix
    def getDataMatrix(self):
        return self._matrix_DataMatrix
    
    def setFullPath(self,variable):
        self._fullPath_bool=variable
        return self._fullPath_bool
    def getFullPath(self):
        return self._fullPath_bool
    
    #Public Function
    def queryParentSelfDAGNode(self,node=None,fullPath=None):
        _node_MObject=self.selectNode_create_MObject(node) or self._node_MObject
        _fullPath_bool=fullPath or self._fullPath_bool

        node_MDagPath=self.convertMObject_create_MDagPath(_node_MObject)

        self._node_MObject=self.parent_query_MObject(node_MDagPath)
        node_str=self._fullPathSwitch_query_str(self._node_MObject,_fullPath_bool)
        return node_str
    
    def queryChildSelfDAGNodes(self,node=None,fullPath=False):
        _node_MObject=self.selectNode_create_MObject(node) or self._node_MObject
        _fullPath_bool=fullPath or self._fullPath_bool
        _firstAddress_int=firstAddress or self._firstAddress_int

        node_MDagPath=self.convertMObject_create_MDagPath(_node_MObject)

        child_MObjects=self.child_query_MObjects(node_MDagPath,shapeOnly=False)
        self._node_MObject=child_MObjects[_firstAddress_int]
        node_str=self._fullPathSwitch_query_str(self._node_MObject,_fullPath_bool)
        return node_str
        
    def queryParentDataNode(self,node=None,fullPath=None):
        _node_MObject=self.selectNode_create_MObject(node) or self._node_MObject
        _fullPath_bool=fullPath or self._fullPath_bool

        node_MDagPath=self.convertMObject_create_MDagPath(_node_MObject)
        parent_MObject=self.parent_query_MObject(node_MDagPath)
        parent_str=self._fullPathSwitch_query_str(parent_MObject,_fullPath_bool)
        if parent_str == "world" or parent_str == "":
            return None
        else:
            return parent_str

    def queryChildDataNodes(self,node=None,fullPath=False):
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

    def editTransform(self):
        pass

    def editTranslate(self):
        pass

    def editRotation(self):
        pass

    def editQuaternion(self):
        pass

    def editScale(self):
        pass

    def editShear(self):
        pass

    def matchTransform(self):
        pass
    
    def matchTranslate(self):
        pass

    def matchRotation(self):
        pass
    
    def matchQuaternion(self):
        pass
    
    def matchAimVector(self):
        pass
    
    def matchScale(self):
        pass
    
    def matchShear(self):
        pass

    def mirrorTransform(self):
        pass

    def mirrorTranslate(self):
        pass
    
    def mirrorRotation(self):
        pass

    def mirrorQuaternion(self):
        pass
    
    def mirrorShear(self):
        pass

class SelfPlug(bLB.SelfOrigin):
    def __init__(self):
        super(SelfPlug,self).__init__()
        self._plug_DataPlug=None
        self._anim_DataKey=None
        self._driven_DataKey=None
        self._keyLock_bool=False
        self._valueLock_bool=False
        self._hide_bool=False
        self._value_value=None
        self._dataChoice_strs+=[
            "DataPlug",
            "AnimDataKey",
            "DrivenDataKey",
            "KeyLock",
            "ValueLock",
            "Hide",
            "Value"
        ]
        self._doIt_strs+=[
            "animKey",
            "drivenKey",
            "keyLock",
            "valueLock",
            "hide",
            "editValue",
            "queryValue"
        ]
    
    #Setting Function
    def setDataPlug(self,variable):
        self._plug_DataPlug=variable
        return self._plug_DataPlug
    def getDataPlug(self):
        return self._plug_DataPlug
    
    def setAnimDataKey(self,variable):
        self._anim_DataKey=variable
        return self._anim_DataKey
    def getAnimDataKey(self):
        return self._anim_DataKey
    
    def setDrivenDataKey(self,variable):
        self._driven_DataKey=variable
        return self._driven_DataKey
    def getDrivenDataKey(self):
        return self._driven_DataKey
    
    def setKeyLock(self,variable):
        self._keyLock_bool=variable
        return self._keyLock_bool
    def getKeyLock(self):
        return self._keyLock_bool
    
    def setValueLock(self,variable):
        self._valueLock_bool=variable
        return self._valueLock_bool
    def getValueLock(self):
        return self._valueLock_bool
    
    def setHide(self,variable):
        self._hide_bool=variable
        return self._hide_bool
    def getHide(self):
        return self._hide_bool

    def setValue(self,variable):
        self._value_value=variable
        return self._value_value
    def getValue(self):
        return self._value_value
    
    #Public Function
    def animKey(self):
        pass

    def drivenKey(self):
        pass

    def keyLock(self):
        pass

    def valueLock(self):
        pass

    def hide(self):
        pass

    def editValue(self):
        pass

    def queryValue(self):
        pass

class SelfJoint(SelfDAGNode):
    def __init__(self):
        super(SelfJoint,self).__init__()
        #self._node_DataNode=None
        #self._name_DataName=None
        #self._attrName_strs=[]
        #self._matrix_DataMatrix=None
        #self._fullPath_bool=False
        self._joint_DataJoint=None

        self._dataChoice_strs+=[
        ]
        self._doIt_strs+=[
        ]

    def setDataJoint(self,variable):
        self._joint_DataJoint=variable
        return self._joint_DataJoint
    def getDataJoint(self):
        return self._joint_DataJoint
    
    #Public Function

class SelfLight(SelfDAGNode):
    def __init__(self):
        super(SelfLight,self).__init__()
        #self._node_DataNode=None
        #self._name_DataName=None
        #self._attrName_strs=[]
        #self._matrix_DataMatrix=None
        #self._fullPath_bool=False

class SelfCamera(SelfDAGNode):
    def __init__(self):
        super(SelfCamera,self).__init__()
        #self._node_DataNode=None
        #self._name_DataName=None
        #self._attrName_strs=[]
        #self._matrix_DataMatrix=None
        #self._fullPath_bool=False

class SelfGeometry(SelfDAGNode):
    def __init__(self):
        super(SelfGeometry,self).__init__()
        #self._node_DataNode=None
        #self._name_DataName=None
        #self._attrName_strs=[]
        #self._matrix_DataMatrix=None
        #self._fullPath_bool=False
        self._geo_DataGeometry=None
        self._skin_DataSkinWeight=None

    #Setting Function
    def setDataGeometry(self,variable):
        self._geo_DataGeometry=variable
        return self._geo_DataGeometry
    def currentDataGeometry(self):
        pass
    def getDataGeometry(self):
        return self._geo_DataGeometry
    
    def setDataSkinWeight(self,variable):
        self._skin_DataSkinWeight=variable
        return self._skin_DataSkinWeight
    def currentDataSkinWeight(self):
        pass
    def getDataSkinWeight(self):
        return self._skin_DataSkinWeight
    
    #Public Function
    def createGeometry(self):
        pass

    def updateGeometry(self):
        pass

    def createSkinWeight(self):
        pass

    def updateSkinWeight(self):
        pass

class SelfCurve(SelfDAGNode):
    def __init__(self):
        super(SelfCurve,self).__init__()
        #self._node_DataNode=None
        #self._name_DataName=None
        #self._attrName_strs=[]
        #self._matrix_DataMatrix=None
        #self._fullPath_bool=False
        self._curve_DataCurve=None

    #Setting Function
    def setDataCurve(self,variable):
        self._curve_DataCurve=variable
        return self._curve_DataCurve
    def getDataCurve(self):
        return self._curve_DataCurve
    
    #Public Function
    def createCurve(self):
        pass

    def updateCurve(self):
        pass

class SelfSurface(SelfDAGNode):
    def __init__(self):
        super(SelfSurface,self).__init__()
        #self._node_DataNode=None
        #self._name_DataName=None
        #self._attrName_strs=[]
        #self._matrix_DataMatrix=None
        #self._fullPath_bool=False
        self._surface_DataSurface=None

    #Setting Function
    def setDataCurve(self,variable):
        self._surface_DataSurface=variable
        return self._surface_DataSurface
    def getDataCurve(self):
        return self._surface_DataSurface
    
    #Public Function
    def createSurface(self):
        pass

    def updateSurface(self):
        pass

class SelfTime(bLB.SelfOrigin):
    def __init__(self):
        self._time_DataTimes=None