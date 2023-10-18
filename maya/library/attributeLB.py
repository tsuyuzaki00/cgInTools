# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

import cgInTools as cit
from ...library import baseLB as bLB
from ...library import jsonLB as jLB
cit.reloads([bLB,jLB])

"""
Attribute memo
アトリビュート自体を作成
アトリビュート自体の編集
"""
class Attribute():
    def __init__(self):
        self._longName_str=None
        self._shortName_str=None
        self._niceName_str=None
        self._value_value=None
        self._createType_str=None
        self._min_float=None
        self._max_float=None

    def __str__(self):
        return self._longName_str

    #Single Function
    def addAttr_check_bool(self,node,attr):
        attr_bool=cmds.attributeQuery(attr,node=node,exists=True)
        return attr_bool

    def addAttrVector_create_attrName(self,obj,name,niceName=None):
        XYZs=["","X","Y","Z"]
        for xyz in XYZs:
            if xyz=="":
                cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="double3")
            else:
                cmds.addAttr(obj,ln=name+xyz,nn=name.capitalize()+xyz or niceName+xyz,at="double",p=name)
        for xyz in XYZs:
            cmds.setAttr(obj+"."+name+xyz,keyable=True)
        return name

    def addAttrInt_create_attrName(self,obj,name,niceName=None,defaultValue=0):
        cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="long",dv=defaultValue)
        return name
    
    def addAttrFloat_create_attrName(self,obj,name,niceName=None,defaultValue=0):
        cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="double",dv=defaultValue)
        return name

    def addAttrIntLimit_create_attrName(self,obj,name,niceName=None,min=0,max=1,defaultValue=0):
        cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="long",min=min,max=max,dv=defaultValue)
        return name
    
    def addAttrFloatLimit_create_attrName(self,obj,name,niceName=None,min=0,max=1,defaultValue=0):
        cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="double",min=min,max=max,dv=defaultValue)
        return name
    
    def addAttrBool_create_attrName(self,obj,name,niceName=None):
        cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="bool")
        return name

    def addAttrString_create_attrName(self,obj,name,niceName=None):
        cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,dt="string")
        return name
    
    def addAttrEnum_create_attrName(self,obj,name,niceName=None,enums=["Green","Blue","Red"],defaultValue=0):
        cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="enum",en=":".join(enums),dv=defaultValue)
        return name

    def hide_edit_func(self,obj,names,value=True):
        for name in names:
            cmds.setAttr(obj+"."+name,k=not value,cb=not value)

    def lockAndHide_edit_func(self,obj,names,value=True):
        for name in names:
            cmds.setAttr(obj+"."+name,l=value,k=not value,cb=not value)

    def keyable_quary_list(self,obj,findName=None):
        if findName is None or findName is "":
            attr_list=cmds.listAttr(obj,k=True)
            return attr_list
        else :
            attr_list=cmds.listAttr(obj,k=True)
            newNode_list=[node for node in attr_list if findName in node]
            return newNode_list

    def lock_quary_list(self,obj,findName=None):
        if findName is None or findName is "":
            attr_list=cmds.listAttr(obj,l=True)
            return attr_list
        else :
            attr_list=cmds.listAttr(obj,l=True)
            newNode_list=[node for node in attr_list if findName in node]
            return newNode_list

    def isProxy_edit_nodeAttr(self,obj,attr,proxy=False):
        if cmds.addAttr(obj+"."+attr,q=True,usedAsProxy=True) == None:
            cmds.error("Cannot be set for standard attributes.")
        nodeAttr=obj+"."+attr
        nodeAttr_MSelectionList=om2.MSelectionList().add(nodeAttr)
        nodeAttr_MPlug=nodeAttr_MSelectionList.getPlug(0)
        nodeAttr_MFnAttribute=om2.MFnAttribute(nodeAttr_MPlug.attribute())
        nodeAttr_MFnAttribute.isProxyAttribute=proxy
        return nodeAttr
    
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
    
    def setValue(self,variable):
        self._value_value=variable
        return self._value_value
    def getValue(self):
        return self._value_value

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
    
    #Public Function
    def create(self):
        pass

    def edit(self):
        pass

    def getKeyableAttrs(self,find=""):
        keyable_list=self.keyable_quary_list(self._object,find)
        return keyable_list

    def getLockAttrs(self,find=""):
        lock_list=self.lock_quary_list(self._object,find)
        return lock_list

    def lockAndHide(self):
        cmds.setAttr(self._object+"."+self._attr,l=self._lockAndHide,k=not self._lockAndHide,cb=not self._lockAndHide)
        return self._attr
    
    def hide(self):
        cmds.setAttr(self._object+"."+self._attr,k=not self._lockAndHide,cb=not self._lockAndHide)
        return self._attr

    def createAttr(self):
        attr_bool=self.addAttr_check_bool(self._object,self._attr)
        if not attr_bool:
            if self._attrType == "bool":
                attrName=self.addAttrBool_create_attrName(self._object,self._attr,self._niceName)
            elif self._attrType == "int":
                if self._useMinMax:
                    attrName=self.addAttrIntLimit_create_attrName(self._object,self._attr,self._niceName,self._min,self._max,self._value)
                else:
                    attrName=self.addAttrInt_create_attrName(self._object,self._attr,self._niceName,self._value)
            elif self._attrType == "float":
                if self._useMinMax:
                    attrName=self.addAttrFloatLimit_create_attrName(self._object,self._attr,self._niceName,self._min,self._max,self._value)
                else:
                    attrName=self.addAttrFloat_create_attrName(self._object,self._attr,self._niceName,self._value)
            elif self._attrType == "string":
                attrName=self.addAttrString_create_attrName(self._object,self._attr,self._niceName,self._stringName)
            elif self._attrType == "enum":
                attrName=self.addAttrEnum_create_attrName(self._object,self._attr,self._niceName,self._enums,self._value)
            elif self._attrType == "vector":
                attrName=self.addAttrVector_create_attrName(self._object,self._attr,self._niceName)
            else:
                cmds.error('There is no attribute type "'+self._attrType+'".')
        cmds.setAttr(self._object+"."+self._attr,keyable=True)
        return attrName

    def isProxy(self):
        nodeAttr=self.isProxy_edit_nodeAttr(self._object,self._attr,self._proxy)
        return nodeAttr
    
"""
Plug memo
アトリビュートの変数の編集
アトリビュートの変数を取得
ノード同士のコネクト
アニメーションキーの設定
ドリブンキーの設定
"""
class Plug():
    def __init__(self):
        self._node_Node=None
        self._attr_Attribute=None
        self._animKey_Keys=[]
        self._target_Node=None
        self._source_Node=None

    #Setting Function
    def setNodeName(self,variable):
        self._nodeName_str=variable
        return self._nodeName_str
    def getNodeName(self):
        return self._nodeName_str
    
    def setAttribute(self,variable):
        self._attr_Attribute=variable
        return self._attr_Attribute
    def getAttribute(self):
        return self._attr_Attribute
    
    def setAnimKeys(self,variables):
        self._animKey_Keys=variables
        return self._animKey_Keys
    def addAnimKeys(self,variables):
        self._animKey_Keys+=variables
        return self._animKey_Keys
    def getAnimKeys(self):
        return self._animKey_Keys
    
    def setTargetNode(self,variable):
        self._target_Node=variable
        return self._target_Node
    def getTargetNode(self):
        return self._target_Node

    def setSourceNode(self,variable):
        self._source_Node=variable
        return self._source_Node
    def getSourceNode(self):
        return self._source_Node

    #Public Function
    def editAttr(self):
        pass
    
    def queryAttr(self):
        pass

    def connectTarget(self):
        pass
    
    def connectSource(self):
        pass

    def createAnimKey(self):
        pass

    def deleteAnimKey(self):
        pass

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

class DataAttribute(bLB.SelfOrigin):
    def __init__(self,dataAttribute=None):
        super(DataAttribute,self).__init__()
        if dataAttribute is None:
            self._longName_str=None
            self._shortName_str=None
            self._valueType_str=None
            self._value_DataValueType=None
            self._keyLock_bool=False
            self._valueLock_bool=False
            self._hide_bool=False
        elif type(dataAttribute) is DataAttribute:
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

class SelfPlug(bLB.SelfOrigin):
    pass

class SelfAttribute(bLB.SelfOrigin):
    pass