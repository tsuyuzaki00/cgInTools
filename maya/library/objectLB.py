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

class SelfNode(bLB.SelfOrigin):
    def __init__(self):
        super(SelfNode,self).__init__()
        self._node_MObject=None
        self._attr_str=None
        self._value=None
        self._valueType="double"
        self._setChoices+=[
            "Node",
            "Attr",
            "Value",
            "ValueType"
        ]
        self._doIts+=[
            "editAttr",
            "queryAttr"
        ]
    
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

    def nodeAttr_create_MPlug(self,node_MObject,attr):
        node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)
        node_MPlug=node_MFnDependencyNode.findPlug(attr,False)
        return node_MPlug

    def editAttr_edit_func(self,node_MPlug,value):
        if isinstance(value,int):
            node_MPlug.setInt(value)
        elif isinstance(value,float):
            node_MPlug.setFloat(value)
        elif isinstance(value,str):
            node_MPlug.setString(value)
        elif isinstance(value,bool):
            node_MPlug.setBool(value)
        else:
            pass

    def queryAttr_query_value(self,node_MPlug,valueType="double"):
        if valueType == "double" or valueType == "Double":
            value=node_MPlug.asDouble()
            return value
        elif valueType == "int" or valueType == "Int":
            value=node_MPlug.asInt()
            return value
        elif valueType == "float" or valueType == "Float":
            value=node_MPlug.asFloat()
            return value
        elif valueType == "str" or valueType == "Str" or valueType == "string" or valueType == "String":
            value=node_MPlug.asString()
            return value
        elif valueType == "bool" or valueType == "Bool" or valueType == "boolean" or valueType == "Boolean":
            value=node_MPlug.asBool()
            return value
        else:
            pass
    
    #Setting Function
    def setNode(self,variable):
        self._node_MObject=self.selectNode_create_MObject(variable)
    def getNode(self):
        node_MFnDependencyNode=om2.MFnDependencyNode(self._node_MObject)
        name_str=node_MFnDependencyNode.name()
        return name_str

    def setAttr(self,variable):
        self._attr_str=variable
    def getAttr(self):
        return self._attr_str

    def setValue(self,variable):
        self._value=variable
    def getValue(self):
        return self._value
    
    def setValueType(self,variable):
        self._valueType=variable
    def getValueType(self):
        return self._valueType
    
    #Public Function
    def editAttr(self,node=None,attr=None,value=None):
        _node_MObject=self.selectNode_create_MObject(node) or self._node_MObject
        _attr_str=attr or self._attr_str
        _value=value or self._value
        if not _attr_str == None or not _value == None:
            node_MPlug=self.nodeAttr_create_MPlug(_node_MObject,_attr_str)
            self.editAttr_edit_func(node_MPlug,_value)

    def queryAttr(self,node=None,attr=None,valueType=None):
        _node_MObject=self.selectNode_create_MObject(node) or self._node_MObject
        _attr_str=attr or self._attr_str
        _valueType=valueType or self._valueType
        if not _attr_str == None:
            node_MPlug=self.nodeAttr_create_MPlug(_node_MObject,_attr_str)
            value=self.queryAttr_query_value(node_MPlug,_valueType)
            return value

    def queryNodeType(self,node=None):
        _node_MObject=self.selectNode_create_MObject(node) or self._node_MObject
        objectType_str=self.nodeType_query_str(_node_MObject)
        return objectType_str

class SelfDagNode(SelfNode):
    def __init__(self):
        super(SelfDagNode,self).__init__()
        self._parent_MObject=None
        self._fullPath_bool=False
        self._firstOnly_bool=False
        self._firstAddress_int=0
        self._setChoices+=[
            "FullPath",
            "FirstOnly",
            "FirstAddress",
        ]
        self._doIts+=[
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

class SelfDGNode(bLB.SelfOrigin):
    pass

class SelfComponent(bLB.SelfOrigin):
    def __init__(self):
        super(SelfComponent,self).__init__()
        self._MFn_int=None
        self._shape_MDagPath=None
        self._component_MObject=None
        self._setChoices+=[
            "MFn",
            "Shape",
            "ComponentID"
        ]
        self._doIts+=[
            "queryShapeType"
        ]
        
    #Single Function
    def selectComponent_create_MDagPath_MObject(self,node):
        if node == None:
            return None
        elif not isinstance(node,str):
            om2.MGlobal.displayError("Please insert one string in value")
            sys.exit()
        component_MSelectionList=om2.MSelectionList()
        component_MSelectionList.add(node)
        shape_MDagPath,components_MObject=component_MSelectionList.getComponent(0)
        return shape_MDagPath,components_MObject
    
    def shape_create_MDagPath(self,shape):
        if shape == None:
            return None
        elif not isinstance(shape,str):
            om2.MGlobal.displayError("Please insert one string in value")
            sys.exit()
        component_MSelectionList=om2.MSelectionList()
        component_MSelectionList.add(shape)
        shape_MDagPath=component_MSelectionList.getDagPath(0)
        shape_MDagPath.extendToShape()
        return shape_MDagPath
    
    def convertToInt_create_MObject(self,componentID_int,MFn_int):
        component_MFnSingleIndexedComponent=om2.MFnSingleIndexedComponent()
        components_MObject=component_MFnSingleIndexedComponent.create(MFn_int)
        component_MFnSingleIndexedComponent.addElement(componentID_int)
        return components_MObject

    def componentID_query_int(self,components_MObject):
        component_MFnSingleIndexedComponent=om2.MFnSingleIndexedComponent(components_MObject)
        componentID_int=component_MFnSingleIndexedComponent.getElements()[0]
        return componentID_int

    def shapeType_query_str(self,shape_MDagPath):
        node_MFnDagNode=om2.MFnDagNode(shape_MDagPath)
        nodeType_str=node_MFnDagNode.typeName
        return nodeType_str

    #Setting Function
    def setComponent(self,variable):
        self._shape_MDagPath,self._components_MObject=self.selectComponent_create_MDagPath_MObject(variable)
        self._MFn_int=self._components_MObject.apiType()

    def setMFn(self,variable):
        self._MFn_int=variable
    def getMFn(self):
        return self._MFn_int

    def setShape(self,variable):
        self._shape_MDagPath=self.shape_create_MDagPath(variable)
    def getShape(self):
        shape_MFnDagNode=om2.MFnDagNode(self._shape_MDagPath)
        shape_str=shape_MFnDagNode.name()
        return shape_str
    
    def setComponentID(self,variable,MFn=None):
        _MFn_int=MFn or self._MFn_int
        self._component_MObject=self.convertToInt_create_MObject(variable,_MFn_int)
    def getComponentID(self):
        componentID_int=self.componentID_query_int(self._component_MObject)
        return componentID_int
    
    #Public Function
    def queryShapeType(self):
        objectType_str=self.shapeType_query_str(self._shape_MDagPath)
        return objectType_str
    
class SelfConnectNode(SelfNode):
    def __init__(self):
        super(SelfConnectNode,self).__init__()
        self._operationNode_MObject=None
        self._operationAttr_str=None
        self._findType_str=None
        self._findEnum_str="NodeType" # or MFn
        self._findSource_bool=True
        self._findTarget_bool=True
        self._setChoices+=[
            "OperationNode",
            "OperationAttr",
            "FindType",
            "FindEnum",
            "FindSource",
            "FindTarget"
        ]
        self._doIts+=[
            "connectAttr"
        ]

    #Single Function
    def replaceMObjectToNode_query_strs(self,connectNode_MObjects):
        if connectNode_MObjects == None or connectNode_MObjects == []:
            return None
        connectNode_strs=[]
        for connectNode_MObject in connectNode_MObjects:
            connectNode_MFnDependencyNode=om2.MFnDependencyNode(connectNode_MObject)
            connectNode_str=connectNode_MFnDependencyNode.name()
            connectNode_strs.append(connectNode_str)
        return connectNode_strs
    
    def connectionNode_query_MPlugs(self,node_MObject,source=True,target=True):
        node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)
        connections_MPlugArray=node_MFnDependencyNode.getConnections()
        
        connectedTo_MPlugs=[]
        for connection_MPlug in connections_MPlugArray:
            connectedTo_MPlugArray=connection_MPlug.connectedTo(source,target)
            for connectedTo_MPlug in connectedTo_MPlugArray:
                connectedTo_MPlugs.append(connectedTo_MPlug)
        if connectedTo_MPlugs == []:
            return None
        else:
            return connectedTo_MPlugs
    
    #Multi Function
    def _findType_query_MObjects(self,node_MObject,find,findEnum="NodeType",source=True,target=True):
        #findEnum="MFn" or "NodeType"
        connectedTo_MPlugs=self.connectionNode_query_MPlugs(node_MObject,source,target)
        findConnectedTo_MObjects=[]
        for connectedTo_MPlug in connectedTo_MPlugs:
            connectedTo_MObject=connectedTo_MPlug.node()
            if findEnum == "NodeType":
                if om2.MFnDependencyNode(connectedTo_MObject).typeName == find:
                    findConnectedTo_MObjects.append(connectedTo_MObject)
            elif findEnum == "MFn":
                if connectedTo_MObject.hasFn(find):
                    findConnectedTo_MObjects.append(connectedTo_MObject)
            else:
                om2.MGlobal.displayError('Please set "findEnum" to "MFn" or "NodeType".')
                sys.exit()
        if findConnectedTo_MObjects == []:
            return None
        else:
            return findConnectedTo_MObjects

    #Inheritance Function
    def _findAttrConect_query_MObjects(self,node_MObject,attr,source=True,target=True):
        find_MPlug=self.nodeAttr_create_MPlug(node_MObject,attr)
        
        targets_MPlugArray=find_MPlug.connectedTo(source,target)
        findConnectedTo_MObjects=[target_MPlug.node() for target_MPlug in targets_MPlugArray]
        if findConnectedTo_MObjects == []:
            return None
        else:
            return findConnectedTo_MObjects
    
    #Setting Function
    def setOperationNode(self,variable):
        self._operationNode_MObject=self.selectNode_create_MObject(variable)
    def getOperationNode(self):
        node_MFnDependencyNode=om2.MFnDependencyNode(self._operationNode_MObject)
        operationNode_str=node_MFnDependencyNode.name()
        return operationNode_str

    def setOperationAttr(self,variable):
        self._operationAttr_str=variable
    def getOperationAttr(self):
        return self._operationAttr_str
    
    def setFindType(self,variable):
        self._findType_str=variable
    def getFindType(self):
        return self._findType_str
    
    def setFindEnum(self,variable):
        self._findEnum_str=variable
    def getFindEnum(self):
        return self._findEnum_str

    def setFindSource(self,variable):
        self._findSource_bool=variable
    def getFindSource(self):
        return self._findSource_bool

    def setFindTarget(self,variable):
        self._findTarget_bool=variable
    def getFindTarget(self):
        return self._findTarget_bool

    #Public Function
    def connectAttr(self,node=None,attr=None,operationNode=None,operationAttr=None):
        _node_MObject=self.selectNode_create_MObject(node) or self._node_MObject
        _attr_str=attr or self._attr_str
        _operationNode_MObject=self.selectNode_create_MObject(operationNode) or self._operationNode_MObject
        _operationAttr_str=operationAttr or self._operationAttr_str

        node_MPlug=self.nodeAttr_create_MPlug(_node_MObject,_attr_str)
        sourceNode_MPlug=self.nodeAttr_create_MPlug(_operationNode_MObject,_operationAttr_str)
        
        MDGModifier=om2.MDGModifier()
        MDGModifier.connect(sourceNode_MPlug,node_MPlug)
        MDGModifier.doIt()

    def queryConnectionNodes(self,node=None,source=None,target=None):
        _node_MObject=node or self._node_MObject
        _findSource_bool=source or self._findSource_bool
        _findTarget_bool=target or self._findTarget_bool

        connectedTo_MPlugs=self.connectionNode_query_MPlugs(_node_MObject,_findSource_bool,_findTarget_bool)
        connectNode_MObjects=[connectedTo_MPlug.node() for connectedTo_MPlug in connectedTo_MPlugs]
        connectNodes=self.replaceMObjectToNode_query_strs(connectNode_MObjects)
        return connectNodes

    def queryConnectionNodeAttrToFind(self,node=None,attr=None,source=None,target=None):
        _node_MObject=self.selectNode_create_MObject(node) or self._node_MObject
        _attr_str=attr or self._attr_str
        _findSource_bool=source or self._findSource_bool
        _findTarget_bool=target or self._findTarget_bool

        connectNode_MObjects=self._findAttrConect_query_MObjects(_node_MObject,_attr_str,_findSource_bool,_findTarget_bool)
        connectNodes=self.replaceMObjectToNode_query_strs(connectNode_MObjects)
        return connectNodes

    def queryConnectionNodeTypeOrMFnToFind(self,node=None,findType=None,findEnum=None,source=None,target=None):
        _node_MObject=self.selectNode_create_MObject(node) or self._node_MObject
        _findType_str=findType or self._findType_str
        _findEnum_str=findEnum or self._findEnum_str
        _findSource_bool=source or self._findSource_bool
        _findTarget_bool=target or self._findTarget_bool

        connectNode_MObjects=self._findType_query_MObjects(_node_MObject,_findType_str,_findEnum_str,_findSource_bool,_findTarget_bool)
        connectNodes=self.replaceMObjectToNode_query_strs(connectNode_MObjects)
        return connectNodes

class SelfTransNode(bLB.SelfOrigin):
    def __init__(self):
        super(SelfTransNode,self).__init__()

class SelfGeometry(bLB.SelfOrigin):
    def __init__(self):
        super(SelfGeometry,self).__init__()

class SelfJoint(bLB.SelfOrigin):
    def __init__(self):
        super(SelfJoint,self).__init__()

class SelfCurve(bLB.SelfOrigin):
    def __init__(self):
        super(SelfCurve,self).__init__()

class SelfSurface(bLB.SelfOrigin):
    def __init__(self):
        super(SelfSurface,self).__init__()

class SelfLight(bLB.SelfOrigin):
    def __init__(self):
        super(SelfLight,self).__init__()

class SelfCamera(bLB.SelfOrigin):
    def __init__(self):
        super(SelfCamera,self).__init__()
