# -*- coding: iso-8859-15 -*-
import maya.api.OpenMaya as om2
import sys,math

import cgInTools as cit
from ...library import baseLB as bLB
from . import matrixLB as mLB
cit.reloads([bLB,mLB])

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
        if dataValueEnum is None:
            self._valueType_str=None
        elif type(dataValueEnum) is DataValueEnum:
            pass

class DataAttribute(bLB.SelfOrigin):
    def __init__(self,dataAttribute=None):
        super(DataAttribute,self).__init__()
        if dataAttribute is None:
            self._longName_str=None
            self._shortName_str=None
            self._valueType_str=None # om2.MFnNumericData.kFloat,
            self._value_DataValueType=None
            self._default_value=None
            self._keyLock_bool=False
            self._valueLock_bool=False
            self._channelHide_bool=False
            self._proxyAttr_bool=False
        elif type(dataAttribute) is DataAttribute:
            self._longName_str=dataAttribute.getName()
            self._shortName_str=dataAttribute.getShortName()
            self._valueType_str=dataAttribute.getValueType()
            self._value_DataValueType=dataAttribute.getDataValueType()
            self._default_value=None
            self._keyLock_bool=dataAttribute.getKeyLockState()
            self._valueLock_bool=dataAttribute.getValueLockState()
            self._channelHide_bool=dataAttribute.getChannelHideState()
            self._proxyAttr_bool=dataAttribute.getProxyAttrState()
        elif type(dataAttribute) is om2.MObject:
            attr_MFnNumericAttribute=om2.MFnNumericAttribute(dataAttribute)

            self._longName_str=attr_MFnNumericAttribute.name
            self._shortName_str=attr_MFnNumericAttribute.shortName
            self._valueType_str=attr_MFnNumericAttribute.numericType()
            self._value_DataValueType=None
            self._default_value=None
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
    
    def setDefaultValue(self,variable):
        self._default_value=variable
        return self._default_value
    def getDefaultValue(self):
        return self._default_value
    
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
    
    def setChannelHideState(self,variable):
        self._channelHide_bool=variable
        return self._channelHide_bool
    def getChannelHideState(self):
        return self._channelHide_bool
    
    def setProxyAttrState(self,variable):
        self._proxyAttr_bool=variable
        return self._proxyAttr_bool
    def getProxyAttrState(self):
        return self._proxyAttr_bool

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

class SelfDGNode(bLB.SelfOrigin):
    def __init__(self,selfDGNode=None):
        super(SelfDGNode,self).__init__()
        if type(selfDGNode) is SelfDGNode:
            self._node_DataNode=selfDGNode.getDataNode()
            self._name_DataName=selfDGNode.getDataName()
            self._attrName_str=None
        else:
            self._node_DataNode=None
            self._name_DataName=None
            self._attrName_str=None
        self._dataChoice_strs+=[
            "DataNode",
            "DataName",
            "AttributeName"
        ]
        self._doIt_strs+=[
            "createNode",
            "duplicateNode",
            "rename",
            "searchDataAttribute",
            "searchDataPlug"
        ]
    
    #Single Function
    def node_query_MObject(self,node):
        if node == None:
            return None
        elif not isinstance(node,str):
            om2.MGlobal.displayError("Please insert one string in value")
            sys.exit()
        node_MSelectionList=om2.MGlobal.getSelectionListByName(node)
        node_MObject=node_MSelectionList.getDependNode(0)
        return node_MObject
    
    def node_create_func(self,nodeName_str,nodeType_str):
        node_MFnDependencyNode=om2.MFnDependencyNode()
        node_MFnDependencyNode.create(nodeType_str)
        node_MFnDependencyNode.setName(nodeName_str)

    def findAttr_create_DataAttribute(self,node_MObject,attrName_str):
        node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)
        attr_MObject=node_MFnDependencyNode.findAlias(attrName_str)
        plug_DataAttribute=DataAttribute(attr_MObject)
        return plug_DataAttribute
    
    def findPlug_create_DataPlug(self,node_MObject,attrName_str):
        node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)
        plug_MPlug=node_MFnDependencyNode.findPlug(attrName_str,False)
        plug_DataPlug=DataPlug(plug_MPlug)
        return plug_DataPlug

    #Setting Function
    def setDataNode(self,variable):
        self._node_DataNode=variable
        return self._node_DataNode
    def getDataNode(self):
        return self._node_DataNode

    def setDataName(self,variable):
        self._name_DataName=variable
        return self._name_DataName
    def getDataName(self):
        return self._name_DataName
    
    def setAttributeName(self,variable):
        self._attrName_str=variable
        return self._attrName_str
    def getAttributeName(self):
        return self._attrName_str
    
    #Public Function
    def createNode(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode

        self.node_create_func(_node_DataNode.getName(),_node_DataNode.getType())

    def duplicateNode(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode

    def rename(self):
        pass

    def searchDataAttribute(self,dataNode=None,attrName=None):
        _node_DataNode=dataNode or self._node_DataNode
        _attrName_str=attrName or self._attrName_str

        node_MObject=self.node_query_MObject(_node_DataNode.getName())
        attr_DataAttribute=self.findAttr_create_DataAttribute(node_MObject,_attrName_str)
        return attr_DataAttribute

    def searchDataPlug(self,node_DataNode=None,attrName=None):
        _node_DataNode=node_DataNode or self._node_DataNode
        _attrName_str=attrName or self._attrName_str

        node_MObject=self.node_query_MObject(_node_DataNode.getName())
        plug_DataPlug=self.findPlug_create_DataPlug(node_MObject,_attrName_str)
        return plug_DataPlug

    def queryName(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode

        nodeName_str=_node_DataNode.getName()
        return nodeName_str

    def queryUUID(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode

        nodeName_str=_node_DataNode.getName()
        node_MObject=self.node_query_MObject(nodeName_str)
        node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)
        uuid_MUuid=node_MFnDependencyNode.uuid()
        return uuid_MUuid

class SelfDAGNode(SelfDGNode):
    def __init__(self):
        super(SelfDAGNode,self).__init__()
        #self._node_DataNode=None
        #self._name_DataName=None
        #self._attrName_strs=[]
        self._translate_MVector=None
        self._rotate_MEulerRotation=None
        self._quaternion_MQuaternion=None
        self._scale_list3=None
        self._matrix_DataMatrix=None
        self._parent_DataNode=None
        self._child_DataNodes=[]
        self._match_DataNode=None
        self._pivot_DataNode=None

        self._dataChoice_strs+=[
            "DataMatrix",
        ]
        self._doIt_strs+=[
            "parent",
            "replaceByParent",
            "replaceByChild",
            "replaceByShape"
        ]
    
    #Single Function
    def convertMObject_query_MDagPath(self,node_MObject):
        node_MDagPath=om2.MDagPath().getAPathTo(node_MObject)
        return node_MDagPath
    
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

    def convertMDagPathToNormalMatrix_query_MMatrix(self,node_MDagPath):
        node_MFnDagNode=om2.MFnDagNode(node_MDagPath)
        node_MMatrix=node_MFnDagNode.transformationMatrix()
        return node_MMatrix
    
    def convertMDagPathToWorldMatrix_query_MMatrix(self,node_MDagPath):
        node_MMatrix=node_MDagPath.inclusiveMatrix()
        return node_MMatrix
    
    def convertMDagPathToParentMatrix_query_MMatrix(self,node_MDagPath):
        node_MMatrix=node_MDagPath.exclusiveMatrix()
        return node_MMatrix
    
    def convertMDagPathToInverseNormalMatrix_query_MMatrix(self,node_MDagPath):
        node_MFnDagNode=om2.MFnDagNode(node_MDagPath)
        normal_MMatrix=node_MFnDagNode.transformationMatrix()
        normal_MTransformationMatrix=om2.MTransformationMatrix(normal_MMatrix)
        node_MMatrix=normal_MTransformationMatrix.asMatrixInverse()
        return node_MMatrix
    
    def convertMDagPathToInverseWorldMatrix_query_MMatrix(self,node_MDagPath):
        world_MMatrix=node_MDagPath.inclusiveMatrix()
        world_MTransformationMatrix=om2.MTransformationMatrix(world_MMatrix)
        node_MMatrix=world_MTransformationMatrix.asMatrixInverse()
        return node_MMatrix
    
    def convertMDagPathToInverseParentMatrix_query_MMatrix(self,node_MDagPath):
        parent_MMatrix=node_MDagPath.exclusiveMatrix()
        parent_MTransformationMatrix=om2.MTransformationMatrix(parent_MMatrix)
        node_MMatrix=parent_MTransformationMatrix.asMatrixInverse()
        return node_MMatrix
    
    #Multi Function
    def _dataNodeToNormalMatrix_query_DataMatrix(self,node_DataNode):
        node_MObject=self.node_query_MObject(node_DataNode.getName())
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        node_MFnDagNode=om2.MFnDagNode(node_MDagPath)
        node_MMatrix=node_MFnDagNode.transformationMatrix()
        node_DataMatrix=mLB.DataMatrix(node_MMatrix)
        return node_DataMatrix
    
    def _dataNodeToWorldMatrix_query_DataMatrix(self,node_DataNode):
        node_MObject=self.node_query_MObject(node_DataNode.getName())
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        node_MMatrix=node_MDagPath.inclusiveMatrix()
        node_DataMatrix=mLB.DataMatrix(node_MMatrix)
        return node_DataMatrix
    
    def _dataNodeToParentMatrix_query_DataMatrix(self,node_DataNode):
        node_MObject=self.node_query_MObject(node_DataNode.getName())
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        node_MMatrix=node_MDagPath.exclusiveMatrix()
        node_DataMatrix=mLB.DataMatrix(node_MMatrix)
        return node_DataMatrix
    
    def _dataNodeToInverseNormalMatrix_query_DataMatrix(self,node_DataNode):
        node_MObject=self.node_query_MObject(node_DataNode.getName())
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        node_MFnDagNode=om2.MFnDagNode(node_MDagPath)
        normal_MMatrix=node_MFnDagNode.transformationMatrix()
        normal_MTransformationMatrix=om2.MTransformationMatrix(normal_MMatrix)
        node_MMatrix=normal_MTransformationMatrix.asMatrixInverse()
        node_DataMatrix=mLB.DataMatrix(node_MMatrix)
        return node_DataMatrix
    
    def _dataNodeToInverseWorldMatrix_query_DataMatrix(self,node_DataNode):
        node_MObject=self.node_query_MObject(node_DataNode.getName())
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        world_MMatrix=node_MDagPath.inclusiveMatrix()
        world_MTransformationMatrix=om2.MTransformationMatrix(world_MMatrix)
        node_MMatrix=world_MTransformationMatrix.asMatrixInverse()
        node_DataMatrix=mLB.DataMatrix(node_MMatrix)
        return node_DataMatrix
    
    def _dataNodeToInverseParentMatrix_query_DataMatrix(self,node_DataNode):
        node_MObject=self.node_query_MObject(node_DataNode.getName())
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        parent_MMatrix=node_MDagPath.exclusiveMatrix()
        parent_MTransformationMatrix=om2.MTransformationMatrix(parent_MMatrix)
        node_MMatrix=parent_MTransformationMatrix.asMatrixInverse()
        node_DataMatrix=mLB.DataMatrix(node_MMatrix)
        return node_DataMatrix

    #Setting Function
    def setTranslate(self,variable3):
        self._translate_MVector=om2.MVector(variable3)
        return self._translate_MVector
    def addTranslate(self,variable):
        MVector=om2.MVector(variable)
        add_MMatrix=om2.MMatrix()
        add_MMatrix.setElement(3,0,MVector.x)
        add_MMatrix.setElement(3,1,MVector.y)
        add_MMatrix.setElement(3,2,MVector.z)
        have_MMatrix=self.initialNoneMMatrix_check_MMatrix(self._MMatrix)  or self._MMatrix
        self._MMatrix=have_MMatrix*add_MMatrix
        return self._MMatrix
    def getTranslate(self):
        MTransformationMatrix=om2.MTransformationMatrix(self._MMatrix)
        MVector=MTransformationMatrix.translation(self._MSpace)
        return MVector

    def setRotate(self,variable):
        radian=[math.radians(variable[0]),math.radians(variable[1]),math.radians(variable[2])]
        MEulerRotation=om2.MEulerRotation(radian,self._rotateOrder)
        self._MMatrix=MEulerRotation.asMatrix()
        return self._MMatrix
    def addRotate(self,variable):
        radian=[math.radians(variable[0]),math.radians(variable[1]),math.radians(variable[2])]
        MEulerRotation=om2.MEulerRotation(radian,self._rotateOrder)
        add_MMatrix=MEulerRotation.asMatrix()
        have_MMatrix=self.initialNoneMMatrix_check_MMatrix(self._MMatrix)  or self._MMatrix
        self._MMatrix=have_MMatrix*add_MMatrix
        return self._MMatrix
    def getRotate(self,radian=True):
        MTransformationMatrix=om2.MTransformationMatrix(self._MMatrix)
        MEulerRotation=MTransformationMatrix.rotation(asQuaternion=False)
        if not radian:
            MEulerRotation.x=math.degrees(MEulerRotation.x)
            MEulerRotation.y=math.degrees(MEulerRotation.y)
            MEulerRotation.z=math.degrees(MEulerRotation.z)
        return MEulerRotation
    
    def setQuaternion(self,variable):
        MQuaternion=om2.MQuaternion(variable)
        self._MMatrix=MQuaternion.asMatrix()
        return self._MMatrix
    def addQuaternion(self,variable):
        MQuaternion=om2.MQuaternion(variable)
        add_MMatrix=MQuaternion.asMatrix()
        have_MMatrix=self.initialNoneMMatrix_check_MMatrix(self._MMatrix) or self._MMatrix
        self._MMatrix=have_MMatrix*add_MMatrix
        return self._MMatrix
    def getQuaternion(self):
        MTransformationMatrix=om2.MTransformationMatrix(self._MMatrix)
        MQuaternion=MTransformationMatrix.rotation(asQuaternion=True)
        return MQuaternion

    def setAxisAngle(self,bend=(1,0,0),twist=0):
        bend_MVector=om2.MVector(bend)
        MQuaternion=om2.MQuaternion(twist,bend)
        add_MMatrix=MQuaternion.asMatrix()
        have_MMatrix=self.initialNoneMMatrix_check_MMatrix(self._MMatrix)
        self._MMatrix=have_MMatrix*add_MMatrix
        return self._MMatrix
    def addAxisAngle(self,bend=(1,0,0),twist=0):
        bend_MVector=om2.MVector(bend)
        MQuaternion=om2.MQuaternion(twist,bend)
        self._MMatrix=MQuaternion.asMatrix()
        return self._MMatrix
    def getAxisAngle(self,radian=True):
        MTransformationMatrix=om2.MTransformationMatrix(self._MMatrix)
        MQuaternion=MTransformationMatrix.rotation(asQuaternion=True)
        bend_MVector,twist_float,=MQuaternion.asAxisAngle()
        if not radian:
            twist_float=math.degrees(twist_float)
        return bend_MVector,twist_float

    def setScale(self,variable):
        scale_list3=self.vector3_check_vector3(variable)
        MTransformationMatrix=om2.MTransformationMatrix()
        MTransformationMatrix.setScale(scale_list3,self._MSpace)
        self._MMatrix=MTransformationMatrix.asMatrix()
        return self._MMatrix
    def addScale(self,variable):
        scale_list3=self.vector3_check_vector3(variable)
        MTransformationMatrix=om2.MTransformationMatrix()
        MTransformationMatrix.setScale(scale_list3,self._MSpace)
        add_MMatrix=MTransformationMatrix.asMatrix()
        have_MMatrix=self.initialNoneMMatrix_check_MMatrix(self._MMatrix) or self._MMatrix
        self._MMatrix=have_MMatrix*add_MMatrix
        return self._MMatrix
    def getScale(self):
        MTransformationMatrix=om2.MTransformationMatrix(self._MMatrix)
        scale_list=MTransformationMatrix.scale(self._MSpace)
        return scale_list

    def setDataMatrix(self,variable):
        self._matrix_DataMatrix=variable
        return self._matrix_DataMatrix
    def getDataMatrix(self):
        return self._matrix_DataMatrix
    
    def setParentDataNode(self,variable):
        self._parent_DataNode=variable
        return self._parent_DataNode
    def getParentDataNode(self):
        return self._parent_DataNode
    
    def setChildDataNodes(self,variables):
        self._child_DataNodes=variables
        return self._child_DataNodes
    def addChildDataNodes(self,variables):
        self._child_DataNodes+=variables
        return self._child_DataNodes
    def getChildDataNodes(self):
        return self._child_DataNodes
    
    def setMatchDataNode(self,variable):
        self._match_DataNode=variable
        return self._match_DataNode
    def getMatchDataNode(self):
        return self._match_DataNode
    
    def setPivotDataNode(self,variable):
        self._pivot_DataNode=variable
        return self._pivot_DataNode
    def getPivotDataNode(self):
        return self._pivot_DataNode
    
    #Public Function
    def doParent(self,dataNode=None,parentDataNode=None):
        _node_DataNode=dataNode or self._node_DataNode
        nodeName_str=_node_DataNode.getName()
        node_MObject=self.node_query_MObject(nodeName_str)
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)

        _parent_DataNode=parentDataNode or self._parent_DataNode
        parentName_str=_parent_DataNode.getName()
        parent_MObject=self.node_query_MObject(parentName_str)
        parent_MDagPath=self.convertMObject_query_MDagPath(parent_MObject)

        parent_MDagModifier=om2.MDagModifier()
        parent_MDagModifier.reparentNode(node_MDagPath,parent_MDagPath)
        parent_MDagModifier.doIt()

    def doChilds(self,dataNode=None,childDataNodes=None):
        _node_DataNode=dataNode or self._node_DataNode
        nodeName_str=_node_DataNode.getName()
        node_MObject=self.node_query_MObject(nodeName_str)
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)

        _child_DataNodes=childDataNodes or self._child_DataNodes
        for _child_DataNode in _child_DataNodes:
            childName_str=_child_DataNode.getName()
            child_MObject=self.node_query_MObject(childName_str)
            child_MDagPath=self.convertMObject_query_MDagPath(child_MObject)

            child_MDagModifier=om2.MDagModifier()
            child_MDagModifier.reparentNode(child_MDagPath,node_MDagPath)
            child_MDagModifier.doIt()

    def queryFullPathName(self):
        nodeName_str=self._node_DataNode.getName()
        node_MObject=self.node_query_MObject(nodeName_str)
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)

        name_str=node_MDagPath.fullPathName()
        return name_str

    def queryShapeSelfDAGNode(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode

        nodeName_str=_node_DataNode.getName()
        node_MObject=self.node_query_MObject(nodeName_str)
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        shape_MObject=self.shape_query_MObject(node_MDagPath)
        shape_DataNode=DataNode(shape_MObject)

        shape_SelfDAGNode=SelfDAGNode()
        shape_SelfDAGNode.setDataNode(shape_DataNode)
        return shape_SelfDAGNode

    def queryParentSelfDAGNode(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode

        nodeName_str=_node_DataNode.getName()
        node_MObject=self.node_query_MObject(nodeName_str)
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        parent_MObject=self.parent_query_MObject(node_MDagPath)
        parent_DataNode=DataNode(parent_MObject)

        parent_SelfDAGNode=SelfDAGNode()
        parent_SelfDAGNode.setDataNode(parent_DataNode)
        return parent_SelfDAGNode
    
    def queryChildSelfDAGNodes(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode

        nodeName_str=_node_DataNode.getName()
        node_MObject=self.node_query_MObject(nodeName_str)
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        child_MObjects=self.child_query_MObjects(node_MDagPath,shapeOnly=False)

        child_SelfDAGNodes=[]
        for child_MObject in child_MObjects:
            child_DataNode=DataNode(child_MObject)
            child_SelfDAGNode=SelfDAGNode()
            child_SelfDAGNode.setDataNode(child_DataNode)
            child_SelfDAGNodes.append(child_SelfDAGNode)

        return child_SelfDAGNodes
    
    def editTransform(self):
        pass

    def editTranslate(self):
        pass

    def editRotation(self):
        pass

    def editQuaternion(self):
        pass

    def editScale(self):
        pass

    def editShear(self):
        pass

    def matchTransform(self):
        pass
    
    def matchTranslate(self):
        pass

    def matchRotation(self):
        pass
    
    def matchQuaternion(self):
        pass
    
    def matchAimVector(self):
        pass
    
    def matchScale(self):
        pass
    
    def matchShear(self):
        pass

    def mirrorTransform(self):
        pass

    def mirrorTranslate(self):
        pass
    
    def mirrorRotation(self):
        pass

    def mirrorQuaternion(self):
        pass
    
    def mirrorShear(self):
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

class SelfPlug(bLB.SelfOrigin):
    def __init__(self):
        self._plug_DataPlug=None
        self._target_DataPlug=None
        self._source_DataPlug=None
        self._anim_DataKeys=[]
        self._value_value=None

    #Single Function
    def node_query_MObject(self,node):
        if node == None:
            return None
        elif not isinstance(node,str):
            om2.MGlobal.displayError("Please insert one string in value")
            sys.exit()
        node_MSelectionList=om2.MGlobal.getSelectionListByName(node)
        node_MObject=node_MSelectionList.getDependNode(0)
        return node_MObject

    def nodeAttr_create_MPlug(self,node_MObject,attr):
        node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)
        node_MPlug=node_MFnDependencyNode.findPlug(attr,False)
        return node_MPlug

    #Multi Function
    def _dataPlug_create_MPlug(self,plug_DataPlug):
        plug_DataNode=plug_DataPlug.getDataNode()
        plug_DataAttribute=plug_DataPlug.getDataAttribute()
        plug_MObject=self.node_query_MObject(plug_DataNode.getName())
        plug_MPlug=self.nodeAttr_create_MPlug(plug_MObject,plug_DataAttribute.getLongName())
        return plug_MPlug

    def _connectDataPlug_edit_func(self,source_DataPlug,target_DataPlug):
        source_MPlug=self._dataPlug_create_MPlug(source_DataPlug)
        target_MPlug=self._dataPlug_create_MPlug(target_DataPlug)
        
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
    
    def setValue(self,variable):
        self._value_value=variable
        return self._value_value
    def getValue(self):
        return self._value_value

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
        
        newPlug_DataPlug=DataPlug(node_MPlug)
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
    
    def queryAttr(self,dataPlug=None):
        _plug_DataPlug=dataPlug or self._plug_DataPlug

        plug_MPlug=self._dataPlug_create_MPlug(_plug_DataPlug)

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

    def connectTarget(self,dataPlug=None,targetDataPlug=None):
        _plug_DataPlug=dataPlug or self._plug_DataPlug
        _target_DataPlug=targetDataPlug or self._target_DataPlug

        self._connectDataPlug_edit_func(_plug_DataPlug,_target_DataPlug)
    
    def connectSource(self,sourceDataPlug=None,dataPlug=None):
        _source_DataPlug=sourceDataPlug or self._source_DataPlug
        _plug_DataPlug=dataPlug or self._plug_DataPlug

        self._connectDataPlug_edit_func(_plug_DataPlug,_source_DataPlug)

    def createAnimKey(self):
        pass

    def deleteAnimKey(self):
        pass

class AppConnect(bLB.SelfOrigin):
    def __init__(self):
        self._source_SelfPlug=None
        self._target_SelfPlug=None
        self._proxy_bool=False

    #Setting Function
    def setSourceSelfPlug(self,variable):
        self._source_SelfPlug=variable
        return self._source_SelfPlug
    def getSourceSelfPlug(self):
        return self._source_SelfPlug
        
    def setTargetSelfPlug(self,variable):
        self._target_SelfPlug=variable
        return self._target_SelfPlug
    def getTargetSelfPlug(self):
        return self._target_SelfPlug
    
    #Public Function
    def connectPlug(self):
        pass

class AppParent(bLB.SelfOrigin):
    def __init__(self):
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