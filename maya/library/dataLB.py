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
    def __init__(self,dataNode=None):
        super(DataNode,self).__init__()
        if type(dataNode) is DataNode:
            self._nodeName_str=dataNode.getNodeName()
            self._nodeType_str=dataNode.getNodeType()
        elif type(dataNode) is om2.MObject:
            node_MFnDependencyNode=om2.MFnDependencyNode(dataNode)
            self._nodeName_str=node_MFnDependencyNode.name()
            self._nodeType_str=node_MFnDependencyNode.typeName
        else:
            self._nodeName_str=None
            self._nodeType_str=None

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

    #Setting Function
    def setNodeName(self,variable):
        self._nodeName_str=variable
        return self._nodeName_str
    def getNodeName(self):
        return self._nodeName_str
    
    def setNodeType(self,variable):
        self._nodeType_str=variable
        return self._nodeType_str
    def getNodeType(self):
        return self._nodeType_str
    
    #Public Function
    def searchNode(self,nodeName=None):
        _nodeName_str=nodeName or self._nodeName_str

        node_MObject=self.node_query_MObject(_nodeName_str)
        node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)
        self._nodeType_str=node_MFnDependencyNode.typeName

class DataAttribute(bLB.SelfOrigin):
    def __init__(self,dataAttribute=None):
        super(DataAttribute,self).__init__()
        if type(dataAttribute) is DataAttribute:
            self._longName_str=dataAttribute.getLongName()
            self._shortName_str=dataAttribute.getShortName()
            self._valueType_str=dataAttribute.getValueType()
            self._value_DataValueType=dataAttribute.getDataValueType()
            self._keyLock_bool=dataAttribute.getKeyLockState()
            self._valueLock_bool=dataAttribute.getValueLockState()
            self._hide_bool=dataAttribute.getHideState()
        elif type(dataAttribute) is om2.MObject:
            attr_MFnAttribute=om2.MFnAttribute(dataAttribute)

            self._longName_str=attr_MFnAttribute.name
            self._shortName_str=attr_MFnAttribute.shortName
            self._valueType_str=None
            self._value_DataValueType=None
            self._keyLock_bool=attr_MFnAttribute.keyable
            self._valueLock_bool=False
            self._hide_bool=attr_MFnAttribute.hidden
        else:
            self._longName_str=None
            self._shortName_str=None
            self._valueType_str=None
            self._value_DataValueType=None
            self._keyLock_bool=False
            self._valueLock_bool=False
            self._hide_bool=False

    #Setting Function
    def setLongName(self,variable):
        self._longName_str=variable
        return self._longName_str
    def getLongName(self):
        return self._longName_str
    
    def setShortName(self,variable):
        self._shortName_str=variable
        return self._shortName_str
    def getShortName(self):
        return self._shortName_str
    
    def setValueType(self,variable):
        self._valueType_str=variable
        return self._valueType_str
    def getValueType(self):
        return self._valueType_str
    
    def setDataValueType(self,variable):
        self._value_DataValueType=variable
        return self._value_DataValueType
    def getDataValueType(self):
        return self._value_DataValueType
    
    def setKeyLockState(self,variable):
        self._keyLock_bool=variable
        return self._keyLock_bool
    def getKeyLockState(self):
        return self._keyLock_bool
    
    def setValueLockState(self,variable):
        self._valueLock_bool=variable
        return self._valueLock_bool
    def getValueLockState(self):
        return self._valueLock_bool
    
    def setHideState(self,variable):
        self._hide_bool=variable
        return self._hide_bool
    def getHideState(self):
        return self._hide_bool
        
class DataValueInt(bLB.SelfOrigin):
    def __init__(self,dataValueInt=None):
        super(DataValueInt,self).__init__()
        if type(dataValueInt) is DataValueInt:
            pass
        else:
            self._valueType_str=None

class DataValueFloat(bLB.SelfOrigin):
    def __init__(self,dataValueFloat=None):
        super(DataValueFloat,self).__init__()
        if type(dataValueFloat) is DataValueFloat:
            pass
        else:
            self._valueType_str=None

class DataValueString(bLB.SelfOrigin):
    def __init__(self,dataValueString=None):
        super(DataValueString,self).__init__()
        if type(dataValueString) is DataValueString:
            pass
        else:
            self._valueType_str=None
class DataValueBoolean(bLB.SelfOrigin):
    def __init__(self,dataValueBoolean=None):
        super(DataValueBoolean,self).__init__()
        if type(dataValueBoolean) is DataValueBoolean:
            pass
        else:
            self._valueType_str=None
class DataValueVector(bLB.SelfOrigin):
    def __init__(self,dataValueVector=None):
        super(DataValueVector,self).__init__()
        if type(dataValueVector) is DataValueVector:
            pass
        else:
            self._valueType_str=None

class DataValueEnum(bLB.SelfOrigin):
    def __init__(self,dataValueEnum=None):
        super(DataValueEnum,self).__init__()
        if type(dataValueEnum) is DataValueEnum:
            pass
        else:
            self._valueType_str=None

class DataPlug(bLB.SelfOrigin):
    def __init__(self,dataPlug=None):
        super(DataPlug,self).__init__()
        if type(dataPlug) is DataPlug:
            self._node_DataNode=dataPlug.getDataNode()
            self._attr_DataAttribute=dataPlug.getDataAttribute()
        elif type(dataPlug) is om2.MPlug:
            self._node_DataNode=DataNode(dataPlug.node())
            self._attr_DataAttribute=DataAttribute(dataPlug.attribute())
        else:
            self._node_DataNode=None
            self._attr_DataAttribute=None

    #Setting Function
    def setDataNode(self,variable):
        self._node_DataNode=variable
        return self._node_DataNode
    def getDataNode(self):
        return self._node_DataNode
    
    def setDataAttribute(self,variable):
        self._attr_DataAttribute=variable
        return self._attr_DataAttribute
    def getDataAttribute(self):
        return self._attr_DataAttribute

    #Public Function
    def searchAttribute(self,dataNode=None,attrName=None):
        pass

class DataMatrix(bLB.SelfOrigin):
    def __init__(self):
        super(DataMatrix,self).__init__()
        self._matrix_MMatrix=None
        self._pivot_MMatrix=None
        self._match_MMatrix=None
        self._MSpace=om2.MSpace.kTransform #1
        self._rotateOrder=om2.MEulerRotation.kXYZ #0
        self._mirrorAxis_str=None
        self._mirrorOrientation_str=None

    def setMatrix(self):
        pass

class DataJoint(bLB.SelfOrigin):
    def __init__(self):
        super(DataJoint,self).__init__()


class DataLight(bLB.SelfOrigin):
    def __init__(self):
        super(DataLight,self).__init__()

class DataCamera(bLB.SelfOrigin):
    def __init__(self):
        super(DataCamera,self).__init__()

class DataGeometry(bLB.SelfOrigin):
    def __init__(self):
        super(DataGeometry,self).__init__()

class DataCurve(bLB.SelfOrigin):
    def __init__(self):
        super(DataCurve,self).__init__()

class DataSurface(bLB.SelfOrigin):
    def __init__(self):
        super(DataSurface,self).__init__()

class DataKey(bLB.SelfOrigin):
    def __init__(self):
        super(DataKey,self).__init__()

class DataVertex(bLB.SelfOrigin):
    def __init__(self):
        super(DataVertex,self).__init__()

class DataEdge(bLB.SelfOrigin):
    def __init__(self):
        super(DataVertex,self).__init__()

class DataFace(bLB.SelfOrigin):
    def __init__(self):
        super(DataFace,self).__init__()

class DataTime(bLB.SelfOrigin):
    def __init__(self):
        super(DataTime,self).__init__()
        self._time_MTime=None
        self._plug_DataPlug=None
        self._anim_DataKey=None
        
    def setMTime(self,variable):
        self._time_MTime=variable
        return self._time_MTime
    def findMTime(self,variable):
        pass
    def currentMTime(self):
        pass
    def getMTime(self):
        return self._time_MTime

    def setDataNode(self,variable):
        self._node_DataNode=variable
        return self._node_DataNode
    def getDataNode(self):
        return self._node_DataNode
    
    def setDataAttribute(self,variable):
        self._attr_DataAttribute=variable
        return self._attr_DataAttribute
    def getDataAttribute(self):
        return self._attr_DataAttribute
    
    def setDataPlug(self,variable):
        self._plug_DataPlug=variable
        return self._plug_DataPlug
    def getDataPlug(self):
        return self._plug_DataPlug
    
    def setDataKey(self,variable):
        self._anim_DataKey=variable
        return self._anim_DataKey
    def getDataKey(self):
        return self._anim_DataKey
    
