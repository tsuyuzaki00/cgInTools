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
        self._nodeName_str=None
        self._nodeType_str=None

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
        pass

class DataAttribute(bLB.SelfOrigin):
    def __init__(self):
        super(DataAttribute,self).__init__()
        self._longName_str=None
        self._shortName_str=None
        self._niceName_str=None
        self._value_value=None
        self._createType_str=None
        self._keyLock_bool=False
        self._valueLock_bool=False
        self._hide_bool=False
        self._min_bool=False
        self._max_bool=False
        self._min_float=None
        self._max_float=None

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

    def setNiceName(self,variable):
        self._niceName_str=variable
        return self._niceName_str
    def getNiceName(self):
        return self._niceName_str
    
    def setDefaultValue(self,variable):
        self._defValue_value=variable
        return self._defValue_value
    def getDefaultValue(self):
        return self._defValue_value

    def setCreateType(self,variable):
        self._createType_str=variable
        return self._createType_str
    def getCreateType(self):
        return self._createType_str

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
    
    def setMinState(self,variable):
        self._min_bool=variable
        return self._min_bool
    def getMinState(self):
        return self._min_bool
    
    def setMaxState(self,variable):
        self._max_bool=variable
        return self._max_bool
    def getMaxState(self):
        return self._max_bool
    
    def setMinValue(self,variable):
        self._min_float=variable
        return self._min_float
    def getMinValue(self):
        return self._min_float
    
    def setMaxValue(self,variable):
        self._max_float=variable
        return self._max_float
    def getMaxValue(self):
        return self._max_float
        
class DataPlug(bLB.SelfOrigin):
    def __init__(self):
        super(DataPlug,self).__init__()
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
        self._node_DataNode=None
        self._attr_DataAttribute=None
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
    
