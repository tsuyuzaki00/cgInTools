# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import maya.api.OpenMayaAnim as oma2
import sys,math

import cgInTools as cit
from ...library import baseLB as bLB
cit.reloads([bLB])

class DataNode(bLB.SelfOrigin):
    def __init__(self,dataNode=None):
        super(DataNode,self).__init__()
        if dataNode is None:
            self._nodeName_str=None
            self._nodeType_str=None
        elif type(dataNode) is DataNode:
            self._nodeName_str=dataNode.getName()
            self._nodeType_str=dataNode.getType()
        elif type(dataNode) is om2.MObject:
            node_MFnDependencyNode=om2.MFnDependencyNode(dataNode)
            self._nodeName_str=node_MFnDependencyNode.name()
            self._nodeType_str=node_MFnDependencyNode.typeName
    
    def __repr__(self):
        return self._nodeName_str

    def __str__(self):
        return str(self._nodeName_str)

    #Setting Function
    def setName(self,variable):
        self._nodeName_str=variable
        return self._nodeName_str
    def getName(self):
        return self._nodeName_str
    
    def setType(self,variable):
        self._nodeType_str=variable
        return self._nodeType_str
    def getType(self):
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
        if dataAttribute is None:
            self._longName_str=None
            self._shortName_str=None
            self._value_DataValueType=None
            self._keyLock_bool=False
            self._valueLock_bool=False
            self._channelHide_bool=False
            self._proxyAttr_bool=False
        elif type(dataAttribute) is DataAttribute:
            self._longName_str=dataAttribute.getName()
            self._shortName_str=dataAttribute.getShortName()
            self._value_DataValueType=dataAttribute.getDataValueType()
            self._keyLock_bool=dataAttribute.getKeyLockState()
            self._valueLock_bool=dataAttribute.getValueLockState()
            self._channelHide_bool=dataAttribute.getChannelHideState()
            self._proxyAttr_bool=dataAttribute.getProxyAttrState()
        elif type(dataAttribute) is om2.MObject:
            attr_MFnNumericAttribute=om2.MFnNumericAttribute(dataAttribute)

            self._longName_str=attr_MFnNumericAttribute.name
            self._shortName_str=attr_MFnNumericAttribute.shortName
            self._value_DataValueType=None
            self._keyLock_bool=not attr_MFnNumericAttribute.keyable
            self._valueLock_bool=False
            self._channelHide_bool=not attr_MFnNumericAttribute.channelBox
            self._proxyAttr_bool=attr_MFnNumericAttribute.isProxyAttribute

    #Setting Function
    def setName(self,variable):
        self._longName_str=variable
        return self._longName_str
    def getName(self):
        return self._longName_str
    
    def setShortName(self,variable):
        self._shortName_str=variable
        return self._shortName_str
    def getShortName(self):
        return self._shortName_str
    
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
        if dataPlug is None:
            self._node_DataNode=None
            self._attr_DataAttribute=None
        elif type(dataPlug) is DataPlug:
            self._node_DataNode=dataPlug.getDataNode()
            self._attr_DataAttribute=dataPlug.getDataAttribute()
        elif type(dataPlug) is om2.MPlug:
            self._node_DataNode=DataNode(dataPlug.node())
            self._attr_DataAttribute=DataAttribute(dataPlug.attribute())

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

class DataMatrix(om2.MMatrix):
    def __init__(self,*matrix):
        super(DataMatrix,self).__init__(*matrix)
        #self.kIdentity=om2.MMatrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
        self._MSpace=om2.MSpace.kTransform #1
        self._rotateOrder=om2.MEulerRotation.kXYZ #0

    def setMatrix(self,variable):
        self.kIdentity=om2.MMatrix(variable)
        return self.kIdentity
    def getMatrix(self):
        matrix=list(self.kIdentity)
        return matrix
    def getMMatrix(self):
        return self.self.kIdentity
    
    def setMSpace(self,variable):
        self._MSpace=variable
    def getMSpace(self):
        return self._MSpace

    def setRotateOrder(self,variable):
        self._rotateOrder=variable
    def getRotateOrder(self):
        return self._rotateOrder

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
    
