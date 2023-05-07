# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import maya.api.OpenMayaAnim as oma2
import sys,math

import cgInTools as cit
from ...library import jsonLB as jLB
cit.reloads([jLB])

RULES_DICT=jLB.getJson(cit.mayaSettings_dir,"openLibrary")

class SelfOrigin(object):
    def __init__(self):
        self._nodeTypeToMFn_dict=RULES_DICT["nodeTypeToMFn_dict"]
        self._read_dict={}
        self._setChoices=["DoIts"]
        self._doIts=[]
    
    #Setting Function
    def setReadDict(self,variable):
        self._read_dict=variable
    def getReadDict(self):
        return self._read_dict
    
    def setSetChoices(self,variables):
        self._setChoices=variables
    def getSetChoices(self):
        return self._setChoices
    
    def setDoIts(self,variables):
        self._doIts=variables
    def getDoIts(self):
        return self._doIts
    
    #Public Function
    def writeDict(self,setChoices=None):
        _setChoices=setChoices or self._setChoices

        write_dict={}
        for _selfChoice in _setChoices:
            #print(_selfChoice)
            variable=eval('self.get'+_selfChoice+'()')
            write_dict[_selfChoice]=variable
        return write_dict

    def readDict(self,read_dict=None):
        _read_dict=read_dict or self._read_dict

        setFunctions=list(_read_dict.keys())
        for setFunction in setFunctions:
            #print(_read_dict[setFunction])
            if isinstance(_read_dict[setFunction],str):
                variable='"'+_read_dict[setFunction]+'"'
            else:
                variable=str(_read_dict[setFunction])
            eval('self.set'+setFunction+'('+variable+')')

    def doIt(self,doIts=None):
        _doIts=doIts or self._doIts

        if _doIts == None:
            return
        else:
            for _doIt in _doIts:
                eval("self."+_doIt+"()")

class SelfNode(SelfOrigin):
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
        node_MSelectionList=om2.MSelectionList()
        node_MSelectionList.add(node)
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

class SelfComponent(SelfOrigin):
    def __init__(self):
        super(SelfComponent,self).__init__()
        self._MFn_int=None
        self._shape_MDagPath=None
        self._component_MObject=None
        self._setChoices+=[]
        self._doIts+=[]
        
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

    #Private Function
    def _findAttrConect_query_MObjects(self,node_MObject,attr,source=True,target=True):
        find_MPlug=self.nodeAttr_create_MPlug(node_MObject,attr)
        
        targets_MPlugArray=find_MPlug.connectedTo(source,target)
        findConnectedTo_MObjects=[target_MPlug.node() for target_MPlug in targets_MPlugArray]
        if findConnectedTo_MObjects == []:
            return None
        else:
            return findConnectedTo_MObjects

    def _nodeTypeToMFnConverter_query_int(self,nodeType):
        return self._nodeTypeToMFn_dict[nodeType]
    
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

    #Private Function
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

    def setDoParent(self,variable):
        self._parent_MObject=self.selectNode_create_MObject(variable)
    def getDoParent(self,fullPath=None):
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

class SelfMatrixNode(SelfDagNode):
    def __init__(self):
        super(SelfMatrixNode,self).__init__()
        self._MMatrix=None
        self._MSpace=om2.MSpace.kTransform #1
        self._rotateOrder=om2.MEulerRotation.kXYZ #0
        self._setChoices+=[
            "Matrix",
            "MSpace",
            "RotateOrder",
            "TranslateMMatrix",
            "RotateMMatrix",
            "QuaternionMMatrix",
            "AxisAngleMMatrix",
            "ScaleMMatrix"
        ]
        self._doIts+=[]

    #Single Function
    def vector3_check_vector3(self,variable):
        if isinstance(variable,tuple) and len(variable) == 3 or isinstance(variable,list) and len(variable) == 3:
            return variable
        else:
            return None
    
    def initialNoneMMatrix_check_MMatrix(self,MMatrix):
        if isinstance(MMatrix,om2.MMatrix):
            return MMatrix
        elif MMatrix == None:
            MMatrix=om2.MMatrix([1,0,0,0, 0,1,0,0, 0,0,1,0, 0,0,0,1])
            return MMatrix
        else:
            MMatrix = None
            return MMatrix

    #Private Function
    def _nodeToNormalMMatrix_query_MMatrix(self,node_MObject):
        node_MDagPath=self.convertMObject_create_MDagPath(node_MObject)
        node_MFnDagNode=om2.MFnDagNode(node_MDagPath)
        MMatrix=node_MFnDagNode.transformationMatrix()
        return MMatrix
    
    def _nodeToWorldMMatrix_query_MMatrix(self,node_MObject):
        node_MDagPath=self.convertMObject_create_MDagPath(node_MObject)
        MMatrix=node_MDagPath.inclusiveMatrix()
        return MMatrix
    
    def _nodeToParentMMatrix_query_MMatrix(self,node_MObject):
        node_MDagPath=self.convertMObject_create_MDagPath(node_MObject)
        MMatrix=node_MDagPath.exclusiveMatrix()
        return MMatrix
    
    def _nodeToInverseNormalMMatrix_query_MMatrix(self,node_MObject):
        node_MDagPath=self.convertMObject_create_MDagPath(node_MObject)
        node_MFnDagNode=om2.MFnDagNode(node_MDagPath)
        normal_MMatrix=node_MFnDagNode.transformationMatrix()
        normal_MTransformationMatrix=om2.MTransformationMatrix(normal_MMatrix)
        MMatrix=normal_MTransformationMatrix.asMatrixInverse()
        return MMatrix
    
    def _nodeToInverseWorldMMatrix_query_MMatrix(self,node_MObject):
        node_MDagPath=self.convertMObject_create_MDagPath(node_MObject)
        world_MMatrix=node_MDagPath.inclusiveMatrix()
        world_MTransformationMatrix=om2.MTransformationMatrix(world_MMatrix)
        MMatrix=world_MTransformationMatrix.asMatrixInverse()
        return MMatrix
    
    def _nodeToInverseParentMMatrix_query_MMatrix(self,node_MObject):
        node_MDagPath=self.convertMObject_create_MDagPath(node_MObject)
        parent_MMatrix=node_MDagPath.exclusiveMatrix()
        parent_MTransformationMatrix=om2.MTransformationMatrix(parent_MMatrix)
        MMatrix=parent_MTransformationMatrix.asMatrixInverse()
        return MMatrix

    #Setting Function
    def setNode(self,variable):
        super(SelfMatrixNode,self).setNode(variable)
        self._MMatrix=self._nodeToNormalMMatrix_query_MMatrix(self._node_MObject)

    def setMatrix(self,variable):
        node_MMatrix=om2.MMatrix(variable)
        self._MMatrix=node_MMatrix
    def getMatrix(self):
        matrix=list(self._MMatrix)
        return matrix
    
    def setMSpace(self,variable):
        self._MSpace=variable
    def getMSpace(self):
        return self._MSpace

    def setRotateOrder(self,variable):
        self._rotateOrder=variable
    def getRotateOrder(self):
        return self._rotateOrder

    def currentNormalMMatrix(self):
        self._MMatrix=self._nodeToNormalMMatrix_query_MMatrix(self._node_MObject)
        return self._MMatrix
    def currentWorldMMatrix(self):
        self._MMatrix=self._nodeToWorldMMatrix_query_MMatrix(self._node_MObject)
        return self._MMatrix
    def currentParentMMatrix(self):
        self._MMatrix=self._nodeToParentMMatrix_query_MMatrix(self._node_MObject)
        return self._MMatrix
    def currentInverseNormalMMatrix(self):
        self._MMatrix=self._nodeToInverseNormalMMatrix_query_MMatrix(self._node_MObject)
        return self._MMatrix
    def currentInverseWorldMMatrix(self):
        self._MMatrix=self._nodeToInverseWorldMMatrix_query_MMatrix(self._node_MObject)
        return self._MMatrix
    def currentInverseParentMMatrix(self):
        self._MMatrix=self._nodeToInverseParentMMatrix_query_MMatrix(self._node_MObject)
        return self._MMatrix

    def setTranslateMMatrix(self,variable):
        trans_MVector=om2.MVector(variable)
        self._MMatrix=om2.MMatrix()
        self._MMatrix.setElement(3,0,trans_MVector.x)
        self._MMatrix.setElement(3,1,trans_MVector.y)
        self._MMatrix.setElement(3,2,trans_MVector.z)
        return self._MMatrix
    def addTranslateMMatrix(self,variable):
        MVector=om2.MVector(variable)
        add_MMatrix=om2.MMatrix()
        add_MMatrix.setElement(3,0,MVector.x)
        add_MMatrix.setElement(3,1,MVector.y)
        add_MMatrix.setElement(3,2,MVector.z)
        have_MMatrix=self.initialNoneMMatrix_check_MMatrix(self._MMatrix)  or self._MMatrix
        self._MMatrix=have_MMatrix*add_MMatrix
        return self._MMatrix
    def getTranslateMMatrix(self):
        MTransformationMatrix=om2.MTransformationMatrix(self._MMatrix)
        MVector=MTransformationMatrix.translation(self._MSpace)
        return MVector

    def setRotateMMatrix(self,variable):
        radian=[math.radians(variable[0]),math.radians(variable[1]),math.radians(variable[2])]
        MEulerRotation=om2.MEulerRotation(radian,self._rotateOrder)
        self._MMatrix=MEulerRotation.asMatrix()
        return self._MMatrix
    def addRotateMMatrix(self,variable):
        radian=[math.radians(variable[0]),math.radians(variable[1]),math.radians(variable[2])]
        MEulerRotation=om2.MEulerRotation(radian,self._rotateOrder)
        add_MMatrix=MEulerRotation.asMatrix()
        have_MMatrix=self.initialNoneMMatrix_check_MMatrix(self._MMatrix)  or self._MMatrix
        self._MMatrix=have_MMatrix*add_MMatrix
        return self._MMatrix
    def getRotateMMatrix(self,radian=False):
        MTransformationMatrix=om2.MTransformationMatrix(self._MMatrix)
        MEulerRotation=MTransformationMatrix.rotation(asQuaternion=False)
        if not radian:
            MEulerRotation.x=math.degrees(MEulerRotation.x)
            MEulerRotation.y=math.degrees(MEulerRotation.y)
            MEulerRotation.z=math.degrees(MEulerRotation.z)
        return MEulerRotation
    
    def setQuaternionMMatrix(self,variable):
        MQuaternion=om2.MQuaternion(variable)
        self._MMatrix=MQuaternion.asMatrix()
        return self._MMatrix
    def addQuaternionMMatrix(self,variable):
        MQuaternion=om2.MQuaternion(variable)
        add_MMatrix=MQuaternion.asMatrix()
        have_MMatrix=self.initialNoneMMatrix_check_MMatrix(self._MMatrix) or self._MMatrix
        self._MMatrix=have_MMatrix*add_MMatrix
        return self._MMatrix
    def getQuaternionMMatrix(self):
        MTransformationMatrix=om2.MTransformationMatrix(self._MMatrix)
        MQuaternion=MTransformationMatrix.rotation(asQuaternion=True)
        return MQuaternion

    def setAxisAngleMMartix(self,bend=(1,0,0),twist=0):
        bend_MVector=om2.MVector(bend)
        MQuaternion=om2.MQuaternion(twist,bend)
        add_MMatrix=MQuaternion.asMatrix()
        have_MMatrix=self.initialNoneMMatrix_check_MMatrix(self._MMatrix)
        self._MMatrix=have_MMatrix*add_MMatrix
        return self._MMatrix
    def addAxisAngleMMatrix(self,bend=(1,0,0),twist=0):
        bend_MVector=om2.MVector(bend)
        MQuaternion=om2.MQuaternion(twist,bend)
        self._MMatrix=MQuaternion.asMatrix()
        return self._MMatrix
    def getAxisAngleMMatrix(self,radian=False):
        MTransformationMatrix=om2.MTransformationMatrix(self._MMatrix)
        MQuaternion=MTransformationMatrix.rotation(asQuaternion=True)
        bend_MVector,twist_float,=MQuaternion.asAxisAngle()
        if not radian:
            twist_float=math.degrees(twist_float)
        return bend_MVector,twist_float

    def setScaleMMatrix(self,variable):
        scale_MVector=om2.MVector(variable)
        MTransformationMatrix=om2.MTransformationMatrix()
        MTransformationMatrix.setScale(scale_MVector)
        self._MMatrix=MTransformationMatrix.asMatrix()
        return self._MMatrix
    def addScaleMMatrix(self,variable):
        scale_MVector=om2.MVector(variable)
        MTransformationMatrix=om2.MTransformationMatrix()
        MTransformationMatrix.setScale(scale_MVector,self._MSpace)
        add_MMatrix=MTransformationMatrix.asMatrix()
        have_MMatrix=self.initialNoneMMatrix_check_MMatrix(self._MMatrix) or self._MMatrix
        self._MMatrix=have_MMatrix*add_MMatrix
        return self._MMatrix
    def getScaleMMatrix(self):
        MTransformationMatrix=om2.MTransformationMatrix(self._MMatrix)
        scale_list=MTransformationMatrix.scale(self._MSpace)
        return scale_list

    #Public Function
    def queryDirectionX(self):
        MVectorX=om2.MVector(self._MMatrix[0],self._MMatrix[1],self._MMatrix[2])
        return MVectorX
    
    def queryDirectionY(self):
        MVectorY=om2.MVector(self._MMatrix[4],self._MMatrix[5],self._MMatrix[6])
        return MVectorY
    
    def queryDirectionZ(self):
        MVectorZ=om2.MVector(self._MMatrix[8],self._MMatrix[9],self._MMatrix[10])
        return MVectorZ

class SelfLocationNode(SelfMatrixNode):
    def __init__(self,node):
        super(SelfLocationNode,self).__init__(node)
        self._matchNode_MObject=None
        self._setChoices+=[
            "TransformNode",
        ]
        self._doIts+=[
            "nodeTranslate",
            "translate"
        ]

    #Setting Function
    def setMatchNode(self,variable):
        self._matchNode_MObject=variable
    def getMatchNode(self):
        return self._matchNode_MObject

    #Public Function
    def matchToTranslateNode(self,node=None,matchNode=None):
        _node_MObject=self.selectNode_create_MObject(node) or self._node_MObject
        _matchNode_MObject=self.selectNode_create_MObject(matchNode) or self._matchNode_MObject
        
        myInverseWorld_MMatrix=self._nodeToInverseWorldMMatrix_query_MMatrix(_node_MObject)
        worldTransForm_MMatrix=self._nodeToWorldMMatrix_query_MMatrix(_matchNode_MObject)

        transform_MMatrix=worldTransForm_MMatrix*myInverseWorld_MMatrix

        self.setMatrix(transform_MMatrix)
        worldTranslate_MVector=self.getTranslate()

        node_MFnTransform=om2.MFnTransform(_node_MObject)
        node_MFnTransform.translateBy(worldTranslate_MVector,self._MSpace)

    def matchToRotateNode(self,node=None,matchNode=None):
        _node_MObject=self.selectNode_create_MObject(node) or self._node_MObject
        _matchNode_MObject=self.selectNode_create_MObject(matchNode) or self._matchNode_MObject
        
        myInverseWorld_MMatrix=self._nodeToInverseWorldMMatrix_query_MMatrix(_node_MObject)
        worldTransForm_MMatrix=self._nodeToWorldMMatrix_query_MMatrix(_matchNode_MObject)

        transform_MMatrix=worldTransForm_MMatrix*myInverseWorld_MMatrix

        self.setMatrix(transform_MMatrix)
        worldRotate_MEulerRotation=self.getRotate()

    def matchToQuaternionNode(self,node=None,matchNode=None):
        _node_MObject=self.selectNode_create_MObject(node) or self._node_MObject
        _matchNode_MObject=self.selectNode_create_MObject(matchNode) or self._matchNode_MObject
        
        myInverseWorld_MMatrix=self._nodeToInverseWorldMMatrix_query_MMatrix(_node_MObject)
        worldTransForm_MMatrix=self._nodeToWorldMMatrix_query_MMatrix(_matchNode_MObject)

        transform_MMatrix=worldTransForm_MMatrix*myInverseWorld_MMatrix

        self.setMatrix(transform_MMatrix)
        worldQuaternion_MQuaternion=self.getQuaternion()

    def matchToScaleNode(self,node=None,matchNode=None):
        _node_MObject=self.selectNode_create_MObject(node) or self._node_MObject
        _matchNode_MObject=self.selectNode_create_MObject(matchNode) or self._matchNode_MObject
        
        myInverseWorld_MMatrix=self._nodeToInverseWorldMMatrix_query_MMatrix(_node_MObject)
        worldTransForm_MMatrix=self._nodeToWorldMMatrix_query_MMatrix(_matchNode_MObject)

        transform_MMatrix=worldTransForm_MMatrix*myInverseWorld_MMatrix

        self.setMatrix(transform_MMatrix)
        worldScale_list=self.getScale()

    def translate(self,vector3=None):
        translate_vector3=self.vector3_check_vector3(vector3)
        node_MFnTransform=om2.MFnTransform(self._node_MObject)
        if translate_vector3 == None:
            MTransformationMatrix=om2.MTransformationMatrix(self._MMatrix)
            translate_MVector=MTransformationMatrix.translation(self._MSpace)
        else:
            self.setTranslateMMatrix(vector3)
            translate_MVector=self.getTranslate()
        node_MFnTransform.translateBy(translate_MVector,self._MSpace)

    def rotate(self,vector3=None):
        translate_vector3=self.vector3_check_vector3(vector3)
        node_MFnTransform=om2.MFnTransform(self._node_MObject)
        if translate_vector3 == None:
            MTransformationMatrix=om2.MTransformationMatrix(self._MMatrix)
            translate_MVector=MTransformationMatrix.translation(self._MSpace)
        else:
            self.setTranslateMMatrix(vector3)
            translate_MVector=self.getTranslate()
        node_MFnTransform.rotateBy(translate_MVector,self._MSpace)

    def quaternion(self,vector3=None):
        translate_vector4=[0,0,0,1]
        node_MFnTransform=om2.MFnTransform(self._node_MObject)
        if translate_vector4 == None:
            MTransformationMatrix=om2.MTransformationMatrix(self._MMatrix)
            translate_MVector=MTransformationMatrix.translation(self._MSpace)
        else:
            self.setTranslateMMatrix(vector3)
            translate_MVector=self.getTranslate()
        node_MFnTransform.rotateBy(translate_MVector,self._MSpace)

    def scale(self,vector3=None):
        translate_vector3=self.vector3_check_vector3(vector3)
        node_MFnTransform=om2.MFnTransform(self._node_MObject)
        if translate_vector3 == None:
            MTransformationMatrix=om2.MTransformationMatrix(self._MMatrix)
            translate_MVector=MTransformationMatrix.translation(self._MSpace)
        else:
            self.setTranslateMMatrix(vector3)
            translate_MVector=self.getTranslate()
        node_MFnTransform.scaleBy(translate_MVector,self._MSpace)

    def addParentNull(self):
        pass

    def addOffsetNull(self):
        pass

class SelfAnimNode(SelfMatrixNode):
    def __init__(self,node):
        super(SelfAnimNode,self).__init__(node)

class SelfWeightJoint(SelfConnectNode):
    def __init__(self,node):
        super(SelfWeightJoint,self).__init__(node)

class SelfMeshVertex(SelfComponent):
    def __init__(self):
        super(SelfMeshVertex,self).__init__()

    def meshVertex_query_MPoint(self,node_MDagPath,id_int):
        mesh_MFnMesh=om2.MFnMesh(node_MDagPath)
        vertex_MPoint=mesh_MFnMesh.getPoint(id_int)
        return vertex_MPoint

    def vertexRelativeMove_edit_func(self,node_MDagPath,id_int,move):
        mesh_MFnMesh=om2.MFnMesh(node_MDagPath)
        vertex_MPoint=mesh_MFnMesh.getPoint(id_int)

        move_MVector=om2.MVector(move)
        newVertice_MPoint=vertex_MPoint+move_MVector
        mesh_MFnMesh.setPoint(id_int,newVertice_MPoint)

    def vertexAbsoluteMove_edit_func(node_MDagPath,id_int,move):
        mesh_MFnMesh=om2.MFnMesh(node_MDagPath)
        move_MPoint=om2.MPoint(move)
        mesh_MFnMesh.setPoint(id_int,move_MPoint)

class SelfSurfaceVertex(SelfComponent):
    def __init__(self,components):
        super(SelfSurfaceVertex,self).__init__(components)

class SelfCurveVertex(SelfComponent):
    def __init__(self,components):
        super(SelfCurveVertex,self).__init__(components)

class SelfPolygon(SelfMatrixNode):
    def __init__(self,node):
        super(SelfPolygon,self).__init__(node)

    def getVertexIDFromPos_query_int(self,MDagPath,pos=(0,0,0,1)):
        mesh_MFnMesh=om2.MFnMesh(MDagPath)
        point=om2.MPoint(pos)
        minDistance=float('inf')

        for i in range(mesh_MFnMesh.numVertices):
            distance=(mesh_MFnMesh.getPoint(i)-point).length()
            if distance < minDistance:
                vertexID=i
                minDistance=distance
        return vertexID

class SelfSurface(SelfMatrixNode):
    def __init__(self,node):
        super(SelfSurface,self).__init__(node)

class SelfCreateNode(SelfOrigin):
    def __init__(self):

        pass

class TrsObject(object):
    def __init__(self,obj):
        self._transMFn_list=RULES_DICT["transMFn_list"]
        self._shapeMFn_list=RULES_DICT["shapeMFn_list"]
        self._nodeTypeToMFn_dict=RULES_DICT["nodeTypeToMFn_dict"]

        self._fullPath_bool=False

        self._object_MObject,self._object_MDagPath=self.selectNode_create_MObject_MDagPath(obj)
        self._objectType_str=self.nodeType_query_str(self._object_MObject)

        self._shape_MObjects=self.child_query_MObjects(self._object_MDagPath,self._shapeMFn_list)
        self._shapeType_strs=self.nodeType_query_strs(self._shape_MObjects)
        
        self._parent_MObject=self.parent_query_MObject(self._object_MDagPath)
        self._child_MObjects=self.child_query_MObjects(self._object_MDagPath,self._transMFn_list)
        
        self._subject_bool=False
        self._subject_MObject=None
        self._subject_MDagPath=None

    #Single Function
    def selectNode_create_MObject_MDagPath(self,node):
        if node == None:
            return None
        node_MSelectionList=om2.MSelectionList()
        node_MSelectionList.add(node)
        node_MObject=node_MSelectionList.getDependNode(0)
        node_MDagPath=node_MSelectionList.getDagPath(0)
        return node_MObject,node_MDagPath

    def nodeType_query_str(self,MObject):
        MFnDependencyNode=om2.MFnDependencyNode(MObject)
        nodeType_str=MFnDependencyNode.typeName
        return nodeType_str

    def nodeType_query_strs(self,MObjects):
        if MObjects == None:
            return None
        nodeType_strs=[]
        for MObject in MObjects:
            MFnDependencyNode=om2.MFnDependencyNode(MObject)
            nodeType_str=MFnDependencyNode.typeName
            nodeType_strs.append(nodeType_str)
        if nodeType_strs == []:
            return None
        else:
            return nodeType_strs

    def parent_query_MObject(self,MDagPath):
        node_MFnDagNode=om2.MFnDagNode(MDagPath)
        parent_MObject=node_MFnDagNode.parent(0)
        return parent_MObject

    def child_query_MObjects(self,MDagPath,childMFn_list=[110,121]):
        node_MFnDagNode=om2.MFnDagNode(MDagPath)
        childs=[]
        for num in range(node_MFnDagNode.childCount()):
            child_MObject=node_MFnDagNode.child(num)
            if child_MObject.apiType() in childMFn_list:
                childs.append(child_MObject)
        if childs == []:
            return None
        else:
            return childs

    def findMFnConnect_query_MObjects(self,MObject,source=True,target=True,MFnID=0):
        findConnectedTo_MObjects=[]
        node_MFnDependencyNode=om2.MFnDependencyNode(MObject)
        connections_MPlugArray=node_MFnDependencyNode.getConnections()
        for connection_MPlug in connections_MPlugArray:
            targets_MPlugArray=connection_MPlug.connectedTo(source,target)
            for target_MPlug in targets_MPlugArray:
                target_MObject=target_MPlug.node()
                if target_MObject.hasFn(MFnID):
                    findConnectedTo_MObjects.append(target_MObject)
        if findConnectedTo_MObjects == []:
            return None
        else:
            return findConnectedTo_MObjects

    def fullPath_query_str(self,MObject,fullPath=False):
        if fullPath:
            replace_MDagPath=om2.MDagPath.getAPathTo(MObject)
            name_str=replace_MDagPath.fullPathName()
            return name_str
        else:
            name_str=om2.MFnDependencyNode(MObject).name()
            return name_str
    
    #Private Function
    def nodeTypeToMFnConverter_query_int(self,nodeType):
        return self._nodeTypeToMFn_dict[nodeType]

    #Public Function
    def __loading(self):
        self._objectType_str=self.nodeType_query_str(self._object_MObject)
        self._shape_MObjects=self.child_query_MObjects(self._object_MDagPath,self._shapeMFn_list)
        self._shapeType_strs=self.nodeType_query_strs(self._shape_MObjects)
        self._parent_MObject=self.parent_query_MObject(self._object_MDagPath)
        self._child_MObjects=self.child_query_MObjects(self._object_MDagPath,self._transMFn_list)

        if self._subject_bool:
            self._subjectType_str=self.nodeType_query_str(self._subject_MObject)
            self._subShape_MObjects=self.child_query_MObjects(self._subject_MDagPath,self._shapeMFn_list)
            self._subShapeType_strs=self.nodeType_query_strs(self._subShape_MObjects)
            self._subParent_MObject=self.parent_query_MObject(self._subject_MDagPath)
            self._subChild_MObjects=self.child_query_MObjects(self._subject_MDagPath,self._transMFn_list)

    def setFullPathSwitch(self,variable):
        self._fullPath_bool=variable
        return self._fullPath_bool
    def getFullPathSwitch(self):
        return self._fullPath_bool

    def setObject(self,variable):
        self._object_MObject,self._object_MDagPath=self.selectNode_create_MObject_MDagPath(variable)
        return self._object_MObject
    def getObject(self):
        object_str=self.fullPath_query_str(self._object_MObject,self._fullPath_bool)
        return object_str
    def getObjectType(self):
        return self._objectType_str

    def getShapes(self,only=False):
        self.__loading()
        if self._shape_MObjects == None:
            return None
        if only:
            shape_str=self.fullPath_query_str(self._shape_MObjects[0],self._fullPath_bool)
            return shape_str
        else:
            shape_strs=[]
            for _shape_MObject in self._shape_MObjects:
                shape_str=self.fullPath_query_str(_shape_MObject,self._fullPath_bool)
                shape_strs.append(shape_str)
            return shape_strs
    def getShapeTypes(self,only=False):
        self.__loading()
        if self._shape_MObjects == None:
            return None
        if only:
            return self._shapeType_strs[0]
        else:
            return self._shapeType_strs

    def getParent(self):
        self.__loading()
        parent_str=self.fullPath_query_str(self._parent_MObject,self._fullPath_bool)
        if parent_str == "world" or parent_str == "":
            return None
        else:
            return parent_str

    def getChilds(self,only=False):
        self.__loading()
        if self._child_MObjects == None:
            return None
        if only:
            shape_str=self.fullPath_query_str(self._child_MObjects[0],self._fullPath_bool)
            return shape_str
        else:
            child_strs=[]
            for _child_MObject in self._child_MObjects:
                child_str=self.fullPath_query_str(_child_MObject,self._fullPath_bool)
                child_strs.append(child_str)
            return child_strs

    def setSubject(self,variable):
        self._subject_MObject,self._subject_MDagPath=self.selectNode_create_MObject_MDagPath(variable)
        self._subject_bool=True
        return self._subject_MObject
    def getSubject(self):
        subject_str=self.fullPath_query_str(self._subject_MObject,self._fullPath_bool)
        return subject_str
    def getSubjectType(self):
        return self._subjectType_str

    def getSubShapes(self,only=False):
        self.__loading()
        if self._subShape_MObjects == None:
            return None
        if only:
            shape_str=self.fullPath_query_str(self._subShape_MObjects[0],self._fullPath_bool)
            return shape_str
        else:
            shape_strs=[]
            for _shape_MObject in self._subShape_MObjects:
                shape_str=self.fullPath_query_str(_shape_MObject,self._fullPath_bool)
                shape_strs.append(shape_str)
            return shape_strs
    def getSubShapeTypes(self,only=False):
        self.__loading()
        if self._subShape_MObjects == None:
            return None
        if only:
            return self._subShapeType_strs[0]
        else:
            return self._subShapeType_strs

    def getSubParent(self):
        self.__loading()
        subParent_str=self.fullPath_query_str(self._subParent_MObject,self._fullPath_bool)
        if subParent_str == "world" or subParent_str == "":
            return None
        else:
            return subParent_str

    def getSubChilds(self,only=False):
        self.__loading()
        if self._subChild_MObjects == None:
            return None
        if only:
            shape_str=self.fullPath_query_str(self._subChild_MObjects[0],self._fullPath_bool)
            return shape_str
        else:
            child_strs=[]
            for _child_MObject in self._subChild_MObjects:
                child_str=self.fullPath_query_str(_child_MObject,self._fullPath_bool)
                child_strs.append(child_str)
            return child_strs

    def loading(self):
        self.__loading()

class JointWeight(TrsObject):
    def __init__(self,obj):
        super(JointWeight,self).__init__(obj)
        self._useJoint=True
        self._vertexs=[]#{}
        self._value=0

    #Public Function
    def __loading(self):
        super(JointWeight,self).loading()
        MFn_int=self.nodeTypeToMFnConverter_query_int("skinCluster")
        self._skinCluster_MObjects=self.findMFnConnect_query_MObjects(self._subShape_MObjects[0],MFnID=MFn_int)

    def setUseJoint(self,variable):
        self._useJoint=variable
        return self._useJoint
    def getUseJoint(self):
        return self._useJoint

    def setVertexs(self,variable):
        self._vertexs=variable
        return self._vertexs
    def addVertexs(self,variables):
        for variable in variables:
            self._vertexs.append(variable)
        return self._vertexs
    def getVertexs(self):
        return self._vertexs
    
    def setValue(self,variable):
        self._value=variable
        return self._value
    def getValue(self):
        return self._value

    def getSkinClusters(self):
        self.__loading()
        skinCluster_str=om2.MFnDependencyNode(self._skinCluster_MObjects[0]).name()
        return skinCluster_str

class MatrixObject(TrsObject):
    def __init__(self,obj):
        super(MatrixObject,self).__init__(obj)
        self._runMatrix_str="normal"# "normal", "world", "parent"
        self._normal_MMatrix=None
        self._world_MMatrix=None
        self._parent_MMatrix=None
        self._otherValue_dicts=[]# {"node":"","attr":"","value":0}

    #Single Function
    def matrix_query_MMatrix(self,MDagPath,type="normal"):
        if type == "normal":
            normal_MMatrix=om2.MFnDagNode(MDagPath).transformationMatrix()
            return normal_MMatrix
        elif type == "world":
            world_MMatrix=MDagPath.inclusiveMatrix()
            return world_MMatrix
        elif type == "parent":
            parent_MMatrix=MDagPath.exclusiveMatrix()
            return parent_MMatrix
        else:
            #cmds.error("Please set the type name to normal, world or parent.")
            return None

    def setAttrDict_edit_func(self,setAttr_dicts):
        if not setAttr_dicts == [] or not setAttr_dicts == None:
            for setAttr_dict in setAttr_dicts:
                cmds.setAttr(setAttr_dict["node"]+"."+setAttr_dict["attr"],setAttr_dict["value"])

    def matrixToTransform_edit_func(self,MObject,MMatrix):
        matrix_MTransformationMatrix=om2.MTransformationMatrix(MMatrix)
        transform_MFnTransform=om2.MFnTransform(MObject)
        transform_MFnTransform.setTransformation(matrix_MTransformationMatrix)

    #Summary Function
    def __loading(self):
        self._normal_MMatrix=self.matrix_query_MMatrix(self._object_MDagPath,type="normal")
        self._world_MMatrix=self.matrix_query_MMatrix(self._object_MDagPath,type="world")
        self._parent_MMatrix=self.matrix_query_MMatrix(self._object_MDagPath,type="parent")

    #Public Function
    def setRunMatrix(self,variable):
        self._runMatrix_str=variable
        return self._runMatrix_str
    def getRunMatrix(self):
        return self._runMatrix_str

    def setNormalMatrix(self,variable):
        self._normal_MMatrix=om2.MMatrix(variable)
        return self._normal_MMatrix
    def getNormalMatrix(self):
        return self._normal_MMatrix
    
    def setWorldMatrix(self,variable):
        self._world_MMatrix=om2.MMatrix(variable)
        return self._world_MMatrix
    def getWorldMatrix(self):
        return self._world_MMatrix
    
    def setParentMatrix(self,variable):
        self._parent_MMatrix=om2.MMatrix(variable)
        return self._parent_MMatrix
    def getParentMatrix(self):
        return self._parent_MMatrix
        fpsUnitType_int=unit or om2.MTime.uiUnit()
        time=self._time.asUnits(fpsUnitType_int)
        return time

    def setOtherValueDicts(self,variables):
        self._otherValue_dicts=variables
        return self._otherValue_dicts
    def addOtherValueDicts(self,variables):
        for variable in variables:
            self._otherValue_dicts.append(variable)
        return self._otherValue_dicts
    def getOtherValueDicts(self):
        return self._otherValue_dicts

    def runMovement(self):
        if self._runMatrix_str == "normal":
            self.matrixToTransform_edit_func(self._object_MObject,self._normal_MMatrix)
            #cmds.xform(self._object,m=self._normal_MMatrix)
        elif self._runMatrix_str == "world":
            self.matrixToTransform_edit_func(self._object_MObject,self._world_MMatrix)
            #cmds.xform(self._object,m=self._world_MMatrix)
        elif self._runMatrix_str == "parent":
            self.matrixToTransform_edit_func(self._object_MObject,self._parent_MMatrix)
            #cmds.xform(self._object,m=self._parent_MMatrix)
        else:
            cmds.error('please setRunMatrix with the strings "normal" or "world" or "parent".')
        if not self._otherValue_dicts == [] or not self._otherValue_dicts == None:
            for _otherValue_dict in self._otherValue_dicts:
                cmds.setAttr(_otherValue_dict["node"]+"."+_otherValue_dict["attr"],_otherValue_dict["value"])

    def normalMovement(self):
        self.matrixToTransform_edit_func(self._object_MObject,self._normal_MMatrix)
        if not self._otherValue_dicts == [] or not self._otherValue_dicts == None:
            self.setAttrDict_edit_func(self._otherValue_dicts)

    def worldMovement(self):
        self.matrixToTransform_edit_func(self._object_MObject,self._world_MMatrix)
        if not self._otherValue_dicts == [] or not self._otherValue_dicts == None:
            self.setAttrDict_edit_func(self._otherValue_dicts)
    
    def parentMovement(self):
        self.matrixToTransform_edit_func(self._object_MObject,self._parent_MMatrix)
        if not self._otherValue_dicts == [] or not self._otherValue_dicts == None:
            self.setAttrDict_edit_func(self._otherValue_dicts)

    def loading(self):
        self.__loading()
class KeyObject(TrsObject):
    def __init__(self,obj):
        super(KeyObject,self).__init__(obj)
        self._time=oma2.MAnimControl.currentTime()
        self._attr=""
        self._value=0.0 #Float. Rotation values are in radians.
        self._inTangentType=0
        self._outTangentType=0
        self._animCurve=8

        self._animTangentReplaceID_dict=RULES_DICT["animTangentReplaceID_dict"]
        self._animTangentReplaceType_list=RULES_DICT["animTangentReplaceType_list"]
        self._animCurveReplaceID_dict=RULES_DICT["animCurveReplaceID_dict"]
        self._animCurveReplaceType_list=RULES_DICT["animCurveReplaceType_list"]

    #Single Function
    def objAttr_query_MFnAnimCurve(self,MObject,attr):
        obj_MFnDependencyNode=om2.MFnDependencyNode(MObject)
        objAttr_MPlug=obj_MFnDependencyNode.findPlug(attr,False)
        objAttr_MFnAnimCurve=oma2.MFnAnimCurve(objAttr_MPlug)
        return objAttr_MFnAnimCurve

    #Multi Function
    def _attrValue_query_float(self,MObject,attr,MTime):
        objAttr_MFnAnimCurve=self.objAttr_query_MFnAnimCurve(MObject,attr)
        value=objAttr_MFnAnimCurve.evaluate(MTime)
        return value

    def _inTangentType_query_int(self,MObject,attr,MTime):
        objAttr_MFnAnimCurve=self.objAttr_query_MFnAnimCurve(MObject,attr)
        index=objAttr_MFnAnimCurve.find(MTime)
        inTangentTypeID_int=objAttr_MFnAnimCurve.inTangentType(index)
        return inTangentTypeID_int

    def _outTangentType_query_int(self,MObject,attr,MTime):
        objAttr_MFnAnimCurve=self.objAttr_query_MFnAnimCurve(MObject,attr)
        index=objAttr_MFnAnimCurve.find(MTime)
        outTangentTypeID_int=objAttr_MFnAnimCurve.outTangentType(index)
        return outTangentTypeID_int

    def _keyFrame_create_func(self,MObject,attr,value,MTime,inTangentTypeID,outTangentTypeID,animCurve):
        obj_MFnDependencyNode=om2.MFnDependencyNode(MObject)
        objAttr_MPlug=obj_MFnDependencyNode.findPlug(attr,False)
        object_str=obj_MFnDependencyNode.name()

        if not objAttr_MPlug.isDestination:
            animCurve_MFnAnimCurve=oma2.MFnAnimCurve()
            animCurve_MObject=animCurve_MFnAnimCurve.create(animCurve)
            animCurve_MFnDependencyNode=om2.MFnDependencyNode(animCurve_MObject)
            animCurve_MFnDependencyNode.setName(object_str+"_"+attr)
            animCurve_MPlug=animCurve_MFnDependencyNode.findPlug("output",False)

            keyConnect_MDGModifier=om2.MDGModifier()
            keyConnect_MDGModifier.connect(animCurve_MPlug,objAttr_MPlug)
            keyConnect_MDGModifier.doIt()
        
        objAttr_MFnAnimCurve=oma2.MFnAnimCurve(objAttr_MPlug)
        objAttr_MFnAnimCurve.addKey(MTime,value,inTangentTypeID,outTangentTypeID)

    #Public Function
    def __loading(self):
        self._value=self._attrValue_query_float(self._object_MObject,self._attr,self._time)
        self._inTangentType=self._inTangentType_query_int(self._object_MObject,self._attr,self._time)
        self._outTangentType=self._outTangentType_query_int(self._object_MObject,self._attr,self._time)
        self.setCurrentAnimCurve()

    def setAttr(self,variable):
        self._attr=variable
        return self._attr
    def getAttr(self):
        return self._attr

    def setTime(self,variable):
        fpsUnitType_int=om2.MTime.uiUnit()
        MTime=om2.MTime(variable,fpsUnitType_int)
        self._time=MTime
        return self._time
    def setCurrentTime(self):
        self._time=oma2.MAnimControl.currentTime()
        return self._time
    def getTime(self,unit=None):
        fpsUnitType_int=unit or om2.MTime.uiUnit()
        time=self._time.asUnits(fpsUnitType_int)
        return time

    def setValue(self,variable):
        self._value=variable
        return self._value
    def setCurrentValue(self,unit=None):
        MTime=oma2.MAnimControl.currentTime()
        self._value=self._attrValue_query_float(self._object_MObject,attr,MTime)
        return self._value
    def getValue(self):
        return self._value

    def setInTangentType(self,variable):
        self._inTangentType=self._animTangentReplaceID_dict[variable]
        return self._inTangentType
    def setCurrentInTangentType(self):
        MTime=oma2.MAnimControl.currentTime()
        self._inTangentType=self._inTangentType_query_int(self._object_MObject,self._attr,MTime)
        return self._inTangentType
    def getInTangentType(self):
        inTangentType=self._animTangentReplaceType_list[self._inTangentType]
        return inTangentType
    
    def setOutTangentType(self,variable):
        self._outTangentType=self._animTangentReplaceID_dict[variable]
        return self._outTangentType
    def setCurrentOutTangentType(self):
        MTime=oma2.MAnimControl.currentTime()
        self._outTangentType=self._outTangentType_query_int(self._object_MObject,self._attr,MTime)
        return self._outTangentType
    def getOutTangentType(self):
        outTangentType=self._animTangentReplaceType_list[self._outTangentType]
        return outTangentType
    
    def setAnimCurve(self,variable):
        self._animCurve=self._animCurveReplaceID_dict[variable]
        return self._animCurve
    def setCurrentAnimCurve(self):
        objAttr_MFnAnimCurve=self.objAttr_query_MFnAnimCurve(self._object_MObject,self._attr)
        self._animCurve=objAttr_MFnAnimCurve.animCurveType
        return self._animCurve
    def getAnimCurve(self):
        animCurve=self._animCurveReplaceType_list[self._animCurve]
        return animCurve

    def loading(self):
        self.__loading()

    def setKey(self):
        self._keyFrame_create_func(self._object_MObject,self._attr,self._value,self._time,self._inTangentType,self._outTangentType,self._animCurve)