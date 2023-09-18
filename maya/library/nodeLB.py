# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import sys,math

import cgInTools as cit
from ...library import baseLB as bLB
from ...library import jsonLB as jLB
cit.reloads([bLB,jLB])

class Node(object):
    def __init__(self):
        self._node_MObject=None
        self._attributeName_str=None
        self._rename_Rename=None

    #Single Function
    def selectNode_create_MObject(self,node):
        if node == None:
            return None
        elif not isinstance(node,str):
            om2.MGlobal.displayError("Please insert one string in value")
            sys.exit()
        node_MSelectionList=om2.MGlobal.getSelectionListByName(node)
        node_MObject=node_MSelectionList.getDependNode(0)
        return node_MObject
    
    def nodeType_query_str(self,node_MObject):
        node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)
        nodeType_str=node_MFnDependencyNode.typeName
        return nodeType_str
    
    def findAttr_create_Plug(self,node_MObject,attribute_str):
        node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)
        
        node_Plug=Plug()
        node_Plug.setNode(node_MFnDependencyNode.name())
        node_Plug.findAttribute(attribute_str)
        return node_Plug
    
    #Setting Function
    def setNodeName(self,variable):
        self._node_MObject=self.selectNode_create_MObject(variable)
        return self._node_MObject
    def getNodeName(self):
        node_MFnDependencyNode=om2.MFnDependencyNode(self._node_MObject)
        name_str=node_MFnDependencyNode.name()
        return name_str
    
    def setAttributeName(self,variable):
        self._attributeName_str=variable
        return self._attributeName_str
    def getAttributeName(self):
        return self._attributeName_str
    
    def setRename(self,variable):
        self._rename_Rename=variable
        return self._rename_Rename
    def getRename(self):
        return self._rename_Rename

    #Public Function
    def queryNodeType(self,node=None):
        _node_MObject=self.selectNode_create_MObject(node) or self._node_MObject

        nodeType_str=self.nodeType_query_str(_node_MObject)
        return nodeType_str

    def queryPlug(self,node=None,attr=None):
        _node_MObject=self.selectNode_create_MObject(node) or self._node_MObject
        _attributeName_str=attr or self._attributeName_str

        node_Plug=self.findAttr_create_Plug(_node_MObject,_attributeName_str)
        return node_Plug

    def rename(self):
        pass

class Attribute(object):
    def __init__(self):
        self._longName_str=None
        self._shortName_str=None
        self._niceName_str=None
        self._defValue_value=None
        self._createType_str=None
        self._keyLock_bool=False
        self._valueLock_bool=False
        self._hide_bool=False
        self._min_bool=False
        self._max_bool=False
        self._min_float=None
        self._max_float=None

    def __str__(self):
        return self._longName_str
    
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

class Plug(bLB.SelfOrigin):
    def __init__(self):
        super(Plug,self).__init__()
        self._node_Node=None
        self._attr_Attribute=None
        self._value_value=None
        self._animKey_Keys=[]
        self._drivenKey_Keys=[]
        self._target_Plugs=[]
        self._source_Plug=None
        self._proxy_bool=False
        self._dataChoice_strs+=[
            "Node",
            "Attribute",
            "Value",
            "AnimKeys",
            "DrivenKeys",
            "TargetPlugs",
            "SourcePlug",
            "ProxyState"
        ]
        self._doIt_strs+=[
            "editAttr",
            "queryAttr"
        ]

    #Setting Function
    def setNode(self,variable):
        self._node_Node=variable
        return self._node_Node
    def findNode(self,variable):
        self._node_Node=Node()
        self._node_Node.setNodeName(variable)
        return self._node_Node
    def getNode(self):
        return self._node_Node
    
    def setAttribute(self,variable):
        self._attr_Attribute=variable
        return self._attr_Attribute
    def findAttribute(self,variable):
        self._attr_Attribute=Attribute()
        self._attr_Attribute.setLongName(variable)
        return self._attr_Attribute
    def getAttribute(self):
        return self._attr_Attribute
    
    def setValue(self,variable):
        self._value_value=variable
        return self._value_value
    def getValue(self):
        return self._value_value
    
    def setAnimKeys(self,variables):
        self._animKey_Keys=variables
        return self._animKey_Keys
    def addAnimKeys(self,variables):
        self._animKey_Keys+=variables
        return self._animKey_Keys
    def getAnimKeys(self):
        return self._animKey_Keys
    
    def setDrivenKeys(self,variables):
        self._drivenKey_Keys=variables
        return self._drivenKey_Keys
    def addDrivenKeys(self,variables):
        self._drivenKey_Keys+=variables
        return self._drivenKey_Keys
    def getDrivenKeys(self):
        return self._drivenKey_Keys

    def setTargetPlugs(self,variables):
        self._target_Plugs=variables
        return self._target_Plugs
    def addTargetPlugs(self,variables):
        self._target_Plugs+=variables
        return self._target_Plugs
    def getTargetPlugs(self):
        return self._target_Plugs

    def setSourcePlug(self,variable):
        self._source_Plug=variable
        return self._source_Plug
    def getSourcePlug(self):
        return self._source_Plug

    def setProxyState(self,variable):
        self._proxy_bool=variable
        return self._proxy_bool
    def getProxyState(self):
        return self._proxy_bool
    
    #Public Function
    def createAttr(self):
        pass

    def editAttr(self):
        pass

    def editValue(self):
        pass
    
    def queryValue(self):
        pass

    def connectTargets(self):
        pass
    
    def connectSource(self):
        pass

    def createAnimKeys(self):
        pass

    def deleteAnimKeys(self):
        pass
    
    def createDrivenKeys(self):
        pass

    def deleteDrivenKeys(self):
        pass