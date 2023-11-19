# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import maya.api.OpenMayaAnim as oma2

import cgInTools as cit
from ...library import baseLB as bLB
cit.reloads([bLB])

#Definition Data
class DataAttribute(bLB.SelfOrigin):
    def __init__(self,dataAttribute=None):
        super(DataAttribute,self).__init__()
        if dataAttribute is None:
            self._longName_str=None
            self._shortName_str=None
        elif type(dataAttribute) is DataAttribute:
            self._longName_str=dataAttribute.getName()
            self._shortName_str=dataAttribute.getShortName()
        elif type(dataAttribute) is om2.MObject:
            attr_MFnNumericAttribute=om2.MFnNumericAttribute(dataAttribute)

            self._longName_str=attr_MFnNumericAttribute.name
            self._shortName_str=attr_MFnNumericAttribute.shortName

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
    
class DataAttributeBoolean(DataAttribute):
    def __init__(self,dataValueBoolean=None):
        super(DataAttributeBoolean,self).__init__()
        if type(dataValueBoolean) is DataAttributeBoolean:
            pass
        else:
            self._valueType_str=None
class DataValueInt(DataAttribute):
    def __init__(self,dataValueInt=None):
        super(DataValueInt,self).__init__()
        if type(dataValueInt) is DataValueInt:
            pass
        else:
            self._valueType_str=None

class DataValueFloat(DataAttribute):
    def __init__(self,dataValueFloat=None):
        super(DataValueFloat,self).__init__()
        if type(dataValueFloat) is DataValueFloat:
            pass
        else:
            self._valueType_str=None

class DataValueString(DataAttribute):
    def __init__(self,dataValueString=None):
        super(DataValueString,self).__init__()
        if type(dataValueString) is DataValueString:
            pass
        else:
            self._valueType_str=None

class DataValueWeight(DataAttribute):
    def __init__(self):
        super(DataValueWeight,self).__init__()
        self._valueWeight_float=None
        self._indexWeight_int=None

    #Setting Function
    def setValueWeight(self,variable):
        self._valueWeight_float=variable
        return self._valueWeight_float
    def getValueWeight(self):
        return self._valueWeight_float
    
    def setIndexWeight(self,variable):
        self._indexWeight_int=variable
        return self._indexWeight_int
    def getIndexWeight(self):
        return self._indexWeight_int
    
class DataValueVector(DataAttribute):
    def __init__(self,dataValueVector=None):
        super(DataValueVector,self).__init__()
        if type(dataValueVector) is DataValueVector:
            pass
        else:
            self._valueType_str=None

class DataValueEnum(DataAttribute):
    def __init__(self,dataValueEnum=None):
        super(DataValueEnum,self).__init__()
        if type(dataValueEnum) is DataValueEnum:
            pass
        else:
            self._valueType_str=None

class DataName(bLB.SelfOrigin):
    def __init__(self):
        self._titleName_str=None
        self._nodeTypeName_str=None
        self._sideName_str=None
        self._numberName_ints=[0]
        self._hierarchyName_strs=["A"]
        self._customName_strs=[]
        #["Title","NodeType","Side","Number_0","Hierarchy_1","Custom_10","Title_Number_0","Title_Hierarchy_2","Side_Number_0","Side_Hierarchy_2"]
        self._orderName_enums=["Title","NodeType"]
        #"Number_0","Hierarchy_10"
        self._increaseName_enum="Number_0"

    #Setting Function
    def setTitle(self,variable):
        self._titleName_str=variable
        return self._titleName_str
    def getTitle(self):
        return self._titleName_str
    
    def setNodeType(self,variable):
        self._nodeTypeName_str=variable
        return self._nodeTypeName_str
    def getNodeType(self):
        return self._nodeTypeName_str
    
    def setSide(self,variable):
        self._sideName_str=variable
        return self._sideName_str
    def getSide(self):
        return self._sideName_str
    
    def setNumbers(self,variables):
        self._numberName_ints=variables
        return self._numberName_ints
    def addNumbers(self,variables):
        self._numberName_ints+=variables
        return self._numberName_ints
    def getNumbers(self):
        return self._numberName_ints
    
    def setHierarchys(self,variables):
        self._hierarchyName_strs=variables
        return self._hierarchyName_strs
    def addHierarchys(self,variables):
        self._hierarchyName_strs+=variables
        return self._hierarchyName_strs
    def getHierarchys(self):
        return self._hierarchyName_strs
    
    def setCustoms(self,variables):
        self._customName_strs=variables
        return self._customName_strs
    def addCustoms(self,variables):
        self._customName_strs+=variables
        return self._customName_strs
    def getCustoms(self):
        return self._customName_strs
    
    def setOrders(self,variables):
        self._orderName_enums=variables
        return self._orderName_enums
    def addOrders(self,variables):
        self._orderName_enums+=variables
        return self._orderName_enums
    def getOrders(self):
        return self._orderName_enums

    def setIncrease(self,variable):
        self._increaseName_enum=variable
        return self._increaseName_enum
    def getIncrease(self):
        return self._increaseName_enum

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

class DataTime(om2.MTime):
    def __init__(self,*time):
        super(DataTime,self).__init__(*time)
        # self.unit=int(Unit Type constant)
        # self.value=float
        
    def setUnitType(self,variable):
        self.unit=variable
        return self.unit
    def currentUnitType(self):
        self.unit=self.uiUnit
        return self.unit
    def getUnitType(self):
        return self.unit
    
    def setTime(self,variable):
        self.value=variable
        return self.value
    def currentTime(self):
        current_MTime=oma2.MAnimControl.currentTime()
        self.value=current_MTime.value
        return self.value
    def getTime(self):
        return self.value

class DataVertex(bLB.SelfOrigin):
    def __init__(self):
        super(DataVertex,self).__init__()

class DataEdge(bLB.SelfOrigin):
    def __init__(self):
        super(DataVertex,self).__init__()

class DataFace(bLB.SelfOrigin):
    def __init__(self):
        super(DataFace,self).__init__()

class DataKey(bLB.SelfOrigin):
    def __init__(self):
        super(DataKey,self).__init__()
        self._inputValue_value=None
        self._outputValue_value=None
        self._inTanType_str=None
        self._outTanType_str=None

    #Setting Function
    def setInputValue(self,variable):
        self._inputValue_value=variable
        return self._inputValue_value
    def getInputValue(self):
        return self._inputValue_value
    
    def setOutputValue(self,variable):
        self._outputValue_value=variable
        return self._outputValue_value
    def getOutputValue(self):
        return self._outputValue_value
    
    def setInputTanType(self,variable):
        self._inputTanType_str=variable
        return self._inputTanType_str
    def getInputTanType(self):
        return self._inputTanType_str
    
    def setOutputTanType(self,variable):
        self._outputTanType_str=variable
        return self._outputTanType_str
    def getOutputTanType(self):
        return self._outputTanType_str

#Array Data
class DataValueWeightArray(bLB.SelfOrigin):
    def __init__(self):
        super(DataValueWeightArray,self).__init__()
        self._indexContainer_int=None
        self._valueWeight_DataValueWeights=[]

class DataKeyArray(bLB.SelfOrigin):
    def __init__(self):
        super(DataKeyArray,self).__init__()
        self._key_DataKeys=[]

#Object Data
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

class DataPlugArray(bLB.SelfOrigin):
    def __init__(self):
        super(DataPlugArray,self).__init__()
        self._source_DataPlug=None
        self._target_DataPlugs=[]

#Action Data
class DataEditPlug(bLB.SelfOrigin):
    def __init__(self):
        super(DataEditPlug,self).__init__()
        self._edit_DataPlugs=[]

class DataConnectPlug(bLB.SelfOrigin):
    def __init__(self):
        super(DataConnectPlug,self).__init__()
        self._connect_DataPlugArrays=[]

class DataBind(bLB.SelfOrigin):
    def __init__(self):
        super(DataBind,self).__init__()
        self._joint_DataNodes=[]
        self._skicWeight_DataValueWeightArrays=[]

class DataKeyable(bLB.SelfOrigin):
    def __init__(self):
        super(DataKeyable,self).__init__()
        self._keyable_DataKeyArrays=[]

class DataDrivenKey(bLB.SelfOrigin):
    def __init__(self):
        super(DataDrivenKey,self).__init__()
        self._source_DataPlug=None
        self._drivenKey_DataKeyArrays=[]
