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
        self._plugPair_DataPlugPairArray=None

    #Single Function
    def setDataPlugArray(self,variable):
        self._plug_DataPlugArray=variable
        return self._plug_DataPlugArray
    def getDataPlugArray(self):
        return self._plug_DataPlugArray
    
    def setDataPlugPairArray(self,variable):
        self._plug_DataPlugPairArray=variable
        return self._plug_DataPlugPairArray
    def getDataPlugPairArray(self):
        return self._plug_DataPlugPairArray
    


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

    def __init__(self):
        super(AppParent,self).__init__()
        self._node_SelfDAGNode=None
        self._parent_SelfDAGNode=None
        self._child_SelfDAGNodes=[]

    #Setting Function
    def setSelfDAGNode(self,variable):
        self._node_SelfDAGNode=variable
        return self._node_SelfDAGNode
    def getSelfDAGNode(self):
        return self._node_SelfDAGNode
        
    def setParentSelfDAGNode(self,variable):
        self._parent_SelfDAGNode=variable
        return self._parent_SelfDAGNode
    def getParentSelfDAGNode(self):
        return self._parent_SelfDAGNode
    
    def setChildSelfDAGNodes(self,variables):
        self._child_SelfDAGNodes=variables
        return self._child_SelfDAGNodes
    def addChildSelfDAGNodes(self,variables):
        self._child_SelfDAGNodes+=variables
        return self._child_SelfDAGNodes
    def getChildSelfDAGNodes(self):
        return self._child_SelfDAGNodes
    
    #Public Function
    def parent(self):
        pass

    def childs(self):
        pass