# -*- coding: iso-8859-15 -*-
import maya.api.OpenMaya as om2

import cgInTools as cit
from . import appLB as aLB
from . import dataLB as dLB
cit.reloads([aLB,dLB])

class AppPlug(aLB.AppOpenMayaBase):
    def __init__(self):
        super(AppPlug,self).__init__()
        self._plug_DataPlugArray=None
        self._plug_DataPlugConnectArray=None

    #Single Function
    def booleanAttr_create_MObject(self,attr_DataAttributeBoolean):
        attr_MFnNumericAttribute=om2.MFnNumericAttribute()
        attr_MObject=attr_MFnNumericAttribute.create(
            attr_DataAttributeBoolean.getName(),
            attr_DataAttributeBoolean.getShortName(),
            attr_DataAttributeBoolean.getValueType(),
            attr_DataAttributeBoolean.getValue()
        )
        return attr_MObject
    
    def intAttr_create_MObject(self,attr_DataAttributeInt):
        attr_MFnNumericAttribute=om2.MFnNumericAttribute()
        attr_MObject=attr_MFnNumericAttribute.create(
            attr_DataAttributeInt.getName(),
            attr_DataAttributeInt.getShortName(),
            attr_DataAttributeInt.getValueType(),
            attr_DataAttributeInt.getValue()
        )
        if type(attr_DataAttributeInt.getMax()) is int:
            attr_MFnNumericAttribute.setMax(attr_DataAttributeInt.getMax())
        if type(attr_DataAttributeInt.getMin()) is int:
            attr_MFnNumericAttribute.setMin(attr_DataAttributeInt.getMin())
        return attr_MObject
    
    def floatAttr_create_MObject(self,attr_DataAttributeFloat):
        attr_MFnNumericAttribute=om2.MFnNumericAttribute()
        attr_MObject=attr_MFnNumericAttribute.create(
            attr_DataAttributeFloat.getName(),
            attr_DataAttributeFloat.getShortName(),
            attr_DataAttributeFloat.getValueType(),
            attr_DataAttributeFloat.getValue()
        )
        if type(attr_DataAttributeFloat.getMax()) is float:
            attr_MFnNumericAttribute.setMax(attr_DataAttributeFloat.getMax())
        if type(attr_DataAttributeFloat.getMin()) is float:
            attr_MFnNumericAttribute.setMin(attr_DataAttributeFloat.getMin())
        return attr_MObject
    
    def stringAttr_create_MObject(self,attr_DataAttributeString):
        attr_MFnStringData=om2.MFnStringData()
        defaultValue_MObject=attr_MFnStringData.create(attr_DataAttributeString.getValue())

        attr_MFnTypedAttribute=om2.MFnTypedAttribute()
        attr_MObject=attr_MFnTypedAttribute.create(
            attr_DataAttributeString.getName(),
            attr_DataAttributeString.getShortName(),
            attr_DataAttributeString.getValueType(),
            defaultValue_MObject
        )
        return attr_MObject
    
    def vectorAttr_create_MObject(self,attr_DataAttributeVector):
        attr_MFnNumericData=om2.MFnNumericData()
        defaultValue_MObject=attr_MFnNumericData.create(attr_DataAttributeVector.getValueType())
        attr_MFnNumericData.setData(attr_DataAttributeVector.getValue())

        attr_MFnNumericAttribute=om2.MFnNumericAttribute()
        attr_MObject=attr_MFnNumericAttribute.createPoint(
            attr_DataAttributeVector.getName(),
            attr_DataAttributeVector.getShortName()
        )
        return attr_MObject

    #Multi Function
    def _convertDataPlug_query_MPlug(self,plug_DataPlug):
        plug_MObject=self.node_query_MObject(str(plug_DataPlug.getDataNode()))
        plug_MPlug=self.nodeAttr_query_MPlug(plug_MObject,str(plug_DataPlug.getDataAttribute()))
        return plug_MPlug
    
    #Private Function
    def __connectDataPlug_edit_func(self,source_DataPlug,target_DataPlug):
        source_MPlug=self._convertDataPlug_query_MPlug(source_DataPlug)
        target_MPlug=self._convertDataPlug_query_MPlug(target_DataPlug)

        MDGModifier=om2.MDGModifier()
        MDGModifier.connect(source_MPlug,target_MPlug)
        MDGModifier.doIt()

    #Setting Function
    def setDataPlugArray(self,variable):
        self._plug_DataPlugArray=variable
        return self._plug_DataPlugArray
    def getDataPlugArray(self):
        return self._plug_DataPlugArray
    
    def setDataPlugConnectArray(self,variable):
        self._plug_DataPlugConnectArray=variable
        return self._plug_DataPlugConnectArray
    def getDataPlugConnectArray(self):
        return self._plug_DataPlugConnectArray
    
    #Public Function
    def create(self,dataPlugArray=None):
        _plug_DataPlugArray=dataPlugArray or self._plug_DataPlugArray

        for _plug_DataPlug in _plug_DataPlugArray:
            node_DataNode=_plug_DataPlug.getDataNode()
            attr_DataAttribute=_plug_DataPlug.getDataAttribute()

            node_MObject=self.node_query_MObject(node_DataNode.getName())
            node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)

            if type(attr_DataAttribute) is dLB.DataAttributeBoolean:
                attr_MObject=self.booleanAttr_create_MObject(attr_DataAttribute)
            elif type(attr_DataAttribute) is dLB.DataAttributeInt:
                attr_MObject=self.intAttr_create_MObject(attr_DataAttribute)
            elif type(attr_DataAttribute) is dLB.DataAttributeFloat:
                attr_MObject=self.floatAttr_create_MObject(attr_DataAttribute)
            elif type(attr_DataAttribute) is dLB.DataAttributeString:
                attr_MObject=self.stringAttr_create_MObject(attr_DataAttribute)
            elif type(attr_DataAttribute) is dLB.DataAttributeVector:
                attr_MObject=self.vectorAttr_create_MObject(attr_DataAttribute)
            else:
                continue

            node_MFnDependencyNode.addAttribute(attr_MObject)
            node_MPlug=node_MFnDependencyNode.findPlug(attr_MObject,False)
            node_MPlug.isChannelBox=not _plug_DataPlug.getHideState()
            node_MPlug.isKeyable=not _plug_DataPlug.getKeyLockState()
            node_MPlug.isLocked=_plug_DataPlug.getValueLockState()

    def edit(self,dataPlugArray=None):
        pass

    def connect(self,dataPlugConnectArray=None):
        _plug_DataPlugConnectArray=dataPlugConnectArray or self._plug_DataPlugConnectArray

        plug_DataPlug=_plug_DataPlugConnectArray.getDataPlug()
        source_DataPlug=_plug_DataPlugConnectArray.getSourceDataPlug()
        self.__connectDataPlug_edit_func(source_DataPlug,plug_DataPlug)
        
        target_DataPlugs=_plug_DataPlugConnectArray.getTargetDataPlugs()
        for target_DataPlug in target_DataPlugs:
            self.__connectDataPlug_edit_func(plug_DataPlug,target_DataPlug)
    
    def sourceConnect(self,dataPlugConnectArray=None):
        _plug_DataPlugConnectArray=dataPlugConnectArray or self._plug_DataPlugConnectArray

        plug_DataPlug=_plug_DataPlugConnectArray.getDataPlug()
        source_DataPlug=_plug_DataPlugConnectArray.getSourceDataPlug()
        self.__connectDataPlug_edit_func(source_DataPlug,plug_DataPlug)
    
    def targetConnect(self,dataPlugConnectArray=None):
        _plug_DataPlugConnectArray=dataPlugConnectArray or self._plug_DataPlugConnectArray

        plug_DataPlug=_plug_DataPlugConnectArray.getDataPlug()
        target_DataPlugs=_plug_DataPlugConnectArray.getTargetDataPlugs()
        for target_DataPlug in target_DataPlugs:
            self.__connectDataPlug_edit_func(plug_DataPlug,target_DataPlug)

class SelfPlug(aLB.AppOpenMayaBase):
    def __init__(self):
        super(SelfPlug,self).__init__()
        self._plug_DataPlug=None
        self._target_DataPlug=None
        self._source_DataPlug=None
        self._anim_DataKeys=[]
        self._value_DataValueType=None

    #Private Function
    def __dataPlug_create_MPlug(self,plug_DataPlug):
        plug_DataNode=plug_DataPlug.getDataNode()
        plug_DataAttribute=plug_DataPlug.getDataAttribute()

        plug_MObject=self.node_query_MObject(plug_DataNode.getName())
        plug_MPlug=self.nodeAttr_query_MPlug(plug_MObject,plug_DataAttribute.getName())
        return plug_MPlug

    def __connectDataPlug_edit_func(self,source_DataPlug,target_DataPlug):
        source_MPlug=self.__dataPlug_create_MPlug(source_DataPlug)
        target_MPlug=self.__dataPlug_create_MPlug(target_DataPlug)
        
        MDGModifier=om2.MDGModifier()
        MDGModifier.connect(source_MPlug,target_MPlug)
        MDGModifier.doIt()

    #Setting Function
    def setDataPlug(self,variable):
        self._plug_DataPlug=variable
        return self._plug_DataPlug
    def getDataPlug(self):
        return self._plug_DataPlug
    
    def setTargetDataPlug(self,variable):
        self._target_DataPlug=variable
        return self._target_DataPlug
    def getTargetDataPlug(self):
        return self._target_DataPlug

    def setSourceDataPlug(self,variable):
        self._source_DataPlug=variable
        return self._source_DataPlug
    def getSourceDataPlug(self):
        return self._source_DataPlug

    def setAnimDataKeys(self,variables):
        self._anim_DataKeys=variables
        return self._anim_DataKeys
    def addAnimDataKeys(self,variables):
        self._anim_DataKeys+=variables
        return self._anim_DataKeys
    def getAnimDataKeys(self):
        return self._anim_DataKeys
    
    def setDataValueType(self,variable):
        self._value_DataValueType=variable
        return self._value_DataValueType
    def currentDataValueType(self):
        pass
    def getDataValueType(self):
        return self._value_DataValueType

    #Public Function
    def createAttr(self,dataPlug=None):
        _plug_DataPlug=dataPlug or self._plug_DataPlug
        
        node_DataNode=_plug_DataPlug.getDataNode()
        node_MObject=self.node_query_MObject(node_DataNode.getName())
        node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)

        node_DataAttribute=_plug_DataPlug.getDataAttribute()
        attr_MFnNumericAttribute=om2.MFnNumericAttribute()
        attr_MObject=attr_MFnNumericAttribute.create(
            node_DataAttribute.getName(),
            node_DataAttribute.getShortName(),
            node_DataAttribute.getValueType(),
            node_DataAttribute.getDefaultValue()
        )
        #attr_MFnNumericAttribute.channelBox=not node_DataAttribute.getChannelHideState()
        #attr_MFnNumericAttribute.isProxyAttribute=node_DataAttribute.getProxyAttrState()

        node_MFnDependencyNode.addAttribute(attr_MObject)
        node_MPlug=node_MFnDependencyNode.findPlug(attr_MObject,False)
        node_MPlug.isChannelBox=not node_DataAttribute.getChannelHideState()
        node_MPlug.isKeyable=not node_DataAttribute.getKeyLockState()
        node_MPlug.isLocked=node_DataAttribute.getValueLockState()
        
        newPlug_DataPlug=dLB.DataPlug(node_MPlug)
        return newPlug_DataPlug

    def editAttr(self,value=None,dataPlug=None):
        _plug_DataPlug=dataPlug or self._plug_DataPlug

        plug_MPlug=self._dataPlug_create_MPlug(_plug_DataPlug)

        if isinstance(value,int):
            plug_MPlug.setInt(value)
        elif isinstance(value,float):
            plug_MPlug.setFloat(value)
        elif isinstance(value,str):
            plug_MPlug.setString(value)
        elif isinstance(value,bool):
            plug_MPlug.setBool(value)

    def connectTarget(self,dataPlug=None,targetDataPlug=None):
        _plug_DataPlug=dataPlug or self._plug_DataPlug
        _target_DataPlug=targetDataPlug or self._target_DataPlug

        self.__connectDataPlug_edit_func(_plug_DataPlug,_target_DataPlug)
    
    def connectSource(self,sourceDataPlug=None,dataPlug=None):
        _source_DataPlug=sourceDataPlug or self._source_DataPlug
        _plug_DataPlug=dataPlug or self._plug_DataPlug

        self.__connectDataPlug_edit_func(_plug_DataPlug,_source_DataPlug)

    def createAnimKey(self):
        pass

    def deleteAnimKey(self):
        pass