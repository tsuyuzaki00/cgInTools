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

class SelfDGNode(bLB.SelfOrigin):
    pass

class SelfAttribute(bLB.SelfOrigin):
    pass

class SelfDAGNode(SelfDGNode):
    def __init__(self):
        super(SelfDAGNode,self).__init__()
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

class SelfGeometry(SelfDAGNode):
    def __init__(self):
        super(SelfGeometry,self).__init__()
class SelfJoint(SelfDAGNode):
    def __init__(self):
        super(SelfJoint,self).__init__()
class SelfCurve(SelfDAGNode):
    def __init__(self):
        super(SelfCurve,self).__init__()
class SelfSurface(SelfDAGNode):
    def __init__(self):
        super(SelfSurface,self).__init__()
class SelfLight(SelfDAGNode):
    def __init__(self):
        super(SelfLight,self).__init__()
class SelfCamera(SelfDAGNode):
    def __init__(self):
        super(SelfCamera,self).__init__()
