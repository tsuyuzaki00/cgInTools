# -*- coding: iso-8859-15 -*-
import math
import maya.api.OpenMaya as om2

import cgInTools as cit
from . import appLB as aLB
from . import dataLB as dLB
from . import matrixLB as mdLB
cit.reloads([aLB,dLB,mdLB])

class AppNode(aLB.AppOpenMayaBase):
    def __init__(self):
        super(AppNode,self).__init__()
        self._main_DataNode=None
        self._sub_DataNodes=[]

    #Single Function
    def node_create_DataNode(self,nodeType_str,nodeName_str):
        node_MFnDependencyNode=om2.MFnDependencyNode()
        node_MObject=node_MFnDependencyNode.create(nodeType_str,nodeName_str)
        node_DataNode=dLB.DataNode(node_MObject)
        return node_DataNode
    
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

    #Setting Function
    def setMainDataNode(self,variable):
        self._main_DataNode=variable
        return self._main_DataNode
    def getMainDataNode(self):
        return self._main_DataNode
    
    def setSubDataNodes(self,variables):
        self._sub_DataNodes=variables
        return self._sub_DataNodes
    def getSubDataNodes(self):
        return self._sub_DataNodes
    
    def create(self):
        self.node_create_DataNode(self._main_DataNode.getType(),self._main_DataNode.getName())

    def moveParent(self):
        pass

    def addChilds(self):
        pass

    def removeChilds(self):
        pass

    def queryParent(self):
        pass

    def queryChilds(self):
        pass

class AppDGNode(aLB.AppOpenMayaBase):
    def __init__(self,selfDGNode=None):
        super(AppDGNode,self).__init__()
        if selfDGNode is None:
            self._node_DataNode=None
            self._name_DataName=None
            self._plug_DataPlugs=[]
            self._attrName_str=None
        elif type(selfDGNode) is AppDGNode:
            self._node_DataNode=selfDGNode.getDataNode()
            self._name_DataName=selfDGNode.getDataName()
            self._plug_DataPlugs=selfDGNode.getDataPlugs()
            self._attrName_str=None
    
    #Single Function
    def node_create_DataNode(self,nodeType_str,nodeName_str):
        node_MFnDependencyNode=om2.MFnDependencyNode()
        node_MObject=node_MFnDependencyNode.create(nodeType_str,nodeName_str)
        node_DataNode=dLB.DataNode(node_MObject)
        return node_DataNode
    
    def nameChoice_query_strs(self,name_dataName):
        orderName_strs=[]
        for orderName_str in name_dataName.getOrders():
            if orderName_str is "Title":
                orderName_strs.append(name_dataName.getTitle())
            elif orderName_str is "NodeType":
                orderName_strs.append(name_dataName.getNodeType())
            elif orderName_str is "Side":
                orderName_strs.append(name_dataName.getSide())
            elif orderName_str is "Number":
                orderName_strs.append(name_dataName.getNumbers()[0])
            elif orderName_str is "Hierarchy":
                orderName_strs.append(name_dataName.getHierarchys()[0])
            elif orderName_str is "Custom":
                orderName_strs.append(name_dataName.getCustoms()[0])
            else:
                continue
        orderName_strs=[orderName_str for orderName_str in orderName_strs if not orderName_str is None]
        return orderName_strs
        
    def findAttr_create_DataAttribute(self,node_MObject,attrName_str):
        node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)
        attr_MObject=node_MFnDependencyNode.findAlias(attrName_str)
        plug_DataAttribute=dLB.DataAttribute(attr_MObject)
        return plug_DataAttribute
    
    def findPlug_create_DataPlug(self,node_MObject,attrName_str):
        node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)
        plug_MPlug=node_MFnDependencyNode.findPlug(attrName_str,False)
        plug_DataPlug=dLB.DataPlug(plug_MPlug)
        return plug_DataPlug
    
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

    #Private Function
    def __orderName_create_str(self,name_dataName):
        orderName_strs=self.nameChoice_query_strs(name_dataName)
        orderName_str="_".join(orderName_strs)
        return orderName_str

    #Test Function
    def _queryMObject(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode

        node_MObject=self.node_query_MObject(str(_node_DataNode))
        return node_MObject

    #Setting Function
    def setDataNode(self,variable):
        self._node_DataNode=variable
        return self._node_DataNode
    def getDataNode(self):
        return self._node_DataNode

    def setDataName(self,variable):
        self._node_DataName=variable
        return self._node_DataName
    def getDataName(self):
        return self._node_DataName
    
    def setDataPlugs(self,variables):
        self._plug_DataPlugs=variables
        return self._plug_DataPlugs
    def addDataPlugs(self,variables):
        self._plug_DataPlugs+=variables
        return self._plug_DataPlugs
    def getDataPlugs(self):
        return self._plug_DataPlugs

    def setAttributeName(self,variable):
        self._attrName_str=variable
        return self._attrName_str
    def getAttributeName(self):
        return self._attrName_str
    
    #Public Function
    def createNode(self,dataNode=None,dataName=None):
        _node_DataNode=dataNode or self._node_DataNode
        _node_DataName=dataName or self._node_DataName

        orderName_str=self.__orderName_create_str(_node_DataName)
        node_MObject=self.node_create_DataNode(_node_DataNode.getType(),orderName_str)
        return dLB.DataNode(node_MObject)

    def createAttr(self,dataPlugs=[]):
        _plug_DataPlugs=dataPlugs or self._plug_DataPlugs

        for _plug_DataPlug in _plug_DataPlugs:
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

    def editAttr(self,dataPlugs=[]):
        _plug_DataPlugs=dataPlugs or self._plug_DataPlugs

        for _plug_DataPlug in _plug_DataPlugs:
            node_DataNode=_plug_DataPlug.getDataNode()
            attr_DataAttribute=_plug_DataPlug.getDataAttribute()

            node_MObject=self.node_query_MObject(node_DataNode.getName())
            node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)

            node_MPlug=node_MFnDependencyNode.findPlug(attr_DataAttribute.getName(),False)
            
            if type(attr_DataAttribute) is dLB.DataAttributeBoolean:
                node_MPlug.setBool(attr_DataAttribute.getValue())
            elif type(attr_DataAttribute) is dLB.DataAttributeInt:
                node_MPlug.setInt(attr_DataAttribute.getValue())
            elif type(attr_DataAttribute) is dLB.DataAttributeFloat:
                node_MPlug.setFloat(attr_DataAttribute.getValue())
            elif type(attr_DataAttribute) is dLB.DataAttributeString:
                node_MPlug.setString(attr_DataAttribute.getValue())
            elif type(attr_DataAttribute) is dLB.DataAttributeVector:
                array_MPlug=node_MPlug.array()
            
    
    def rename(self,dataNode=None,dataName=None):
        _node_DataNode=dataNode or self._node_DataNode
        _node_DataName=dataName or self._node_DataName
        
        node_MObject=self.node_query_MObject(str(_node_DataNode))
        node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)
        orderName_str=self.__orderName_create_str(_node_DataName)
        node_MFnDependencyNode.setName(orderName_str)
        rename_MObject=node_MFnDependencyNode.object()
        return dLB.DataNode(rename_MObject)

    def searchDataAttribute(self,dataNode=None,attrName=None):
        _node_DataNode=dataNode or self._node_DataNode
        _attrName_str=attrName or self._attrName_str

        node_MObject=self.node_query_MObject(str(_node_DataNode))
        attr_DataAttribute=self.findAttr_create_DataAttribute(node_MObject,_attrName_str)
        return attr_DataAttribute

    def searchDataPlug(self,node_DataNode=None,attrName=None):
        _node_DataNode=node_DataNode or self._node_DataNode
        _attrName_str=attrName or self._attrName_str

        node_MObject=self.node_query_MObject(str(_node_DataNode))
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

class AppDAGNode(AppDGNode):
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
        self._source_DataNode=None
        self._target_DataNode=None
        self._pivot_DataNode=None
        self._mirrorAxis_str="x"
        self._mirrorOrientVector_str="z"

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

    def convertMDagPathToNormalMatrix_query_DataMatrix(self,node_MDagPath):
        node_MFnDagNode=om2.MFnDagNode(node_MDagPath)
        node_MMatrix=node_MFnDagNode.transformationMatrix()
        node_DataMatrix=mLB.DataMatrix(node_MMatrix)
        return node_DataMatrix
    
    def convertMDagPathToWorldMatrix_query_DataMatrix(self,node_MDagPath):
        node_MMatrix=node_MDagPath.inclusiveMatrix()
        node_DataMatrix=mLB.DataMatrix(node_MMatrix)
        return node_DataMatrix
    
    def convertMDagPathToParentMatrix_query_DataMatrix(self,node_MDagPath):
        node_MMatrix=node_MDagPath.exclusiveMatrix()
        node_DataMatrix=mLB.DataMatrix(node_MMatrix)
        return node_DataMatrix
    
    def convertMDagPathToInverseNormalMatrix_query_DataMatrix(self,node_MDagPath):
        node_MFnDagNode=om2.MFnDagNode(node_MDagPath)
        normal_MMatrix=node_MFnDagNode.transformationMatrix()
        normal_MTransformationMatrix=om2.MTransformationMatrix(normal_MMatrix)
        node_MMatrix=normal_MTransformationMatrix.asMatrixInverse()
        node_DataMatrix=mLB.DataMatrix(node_MMatrix)
        return node_DataMatrix
    
    def convertMDagPathToInverseWorldMatrix_query_DataMatrix(self,node_MDagPath):
        world_MMatrix=node_MDagPath.inclusiveMatrix()
        world_MTransformationMatrix=om2.MTransformationMatrix(world_MMatrix)
        node_MMatrix=world_MTransformationMatrix.asMatrixInverse()
        node_DataMatrix=mLB.DataMatrix(node_MMatrix)
        return node_DataMatrix
    
    def convertMDagPathToInverseParentMatrix_query_DataMatrix(self,node_MDagPath):
        parent_MMatrix=node_MDagPath.exclusiveMatrix()
        parent_MTransformationMatrix=om2.MTransformationMatrix(parent_MMatrix)
        node_MMatrix=parent_MTransformationMatrix.asMatrixInverse()
        node_DataMatrix=mLB.DataMatrix(node_MMatrix)
        return node_DataMatrix
    
    #Private Function
    def __dataNodeToNormalMatrix_query_DataMatrix(self,node_DataNode):
        node_MObject=self.node_query_MObject(str(node_DataNode))
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        node_DataMatrix=self.convertMDagPathToNormalMatrix_query_DataMatrix(node_MDagPath)
        return node_DataMatrix
    
    def __dataNodeToWorldMatrix_query_DataMatrix(self,node_DataNode):
        node_MObject=self.node_query_MObject(str(node_DataNode))
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        node_DataMatrix=self.convertMDagPathToWorldMatrix_query_DataMatrix(node_MDagPath)
        return node_DataMatrix
    
    def __dataNodeToParentMatrix_query_DataMatrix(self,node_DataNode):
        node_MObject=self.node_query_MObject(str(node_DataNode))
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        node_DataMatrix=self.convertMDagPathToParentMatrix_query_DataMatrix(node_MDagPath)
        return node_DataMatrix
    
    def __dataNodeToInverseNormalMatrix_query_DataMatrix(self,node_DataNode):
        node_MObject=self.node_query_MObject(str(node_DataNode))
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        node_DataMatrix=self.convertMDagPathToInverseNormalMatrix_query_DataMatrix(node_MDagPath)
        return node_DataMatrix
    
    def __dataNodeToInverseWorldMatrix_query_DataMatrix(self,node_DataNode):
        node_MObject=self.node_query_MObject(str(node_DataNode))
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        node_DataMatrix=self.convertMDagPathToInverseWorldMatrix_query_DataMatrix(node_MDagPath)
        return node_DataMatrix
    
    def __dataNodeToInverseParentMatrix_query_DataMatrix(self,node_DataNode):
        node_MObject=self.node_query_MObject(str(node_DataNode))
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        node_DataMatrix=self.convertMDagPathToInverseParentMatrix_query_DataMatrix(node_MDagPath)
        return node_DataMatrix

    #Test Function
    def _queryMDagPath(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode

        node_MObject=self.node_query_MObject(str(_node_DataNode))
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        return node_MDagPath

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
    
    def setSourceDataNode(self,variable):
        self._source_DataNode=variable
        return self._source_DataNode
    def getSourceDataNode(self):
        return self._source_DataNode
    
    def setTargetDataNode(self,variable):
        self._target_DataNode=variable
        return self._target_DataNode
    def getTargetDataNode(self):
        return self._target_DataNode
    
    def setPivotDataNode(self,variable):
        self._pivot_DataNode=variable
        return self._pivot_DataNode
    def getPivotDataNode(self):
        return self._pivot_DataNode
    
    def setMirrorAxis(self,variable):
        self._mirrorAxis_str=variable
        return self._mirrorAxis_str
    def getMirrorAxis(self):
        return self._mirrorAxis_str

    def setMirrorOrientVector(self,variable):
        self._mirrorOrientVector_str=variable
        return self._mirrorOrientVector_str
    def getMirrorOrientVector(self):
        return self._mirrorOrientVector_str

    #Public Function
    def doParent(self,dataNode=None,parentDataNode=None):
        _node_DataNode=dataNode or self._node_DataNode
        _parent_DataNode=parentDataNode or self._parent_DataNode
        
        node_MObject=self.node_query_MObject(str(_node_DataNode))
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)

        parent_MObject=self.node_query_MObject(str(_parent_DataNode))
        parent_MDagPath=self.convertMObject_query_MDagPath(parent_MObject)

        parent_MDagModifier=om2.MDagModifier()
        parent_MDagModifier.reparentNode(node_MDagPath,parent_MDagPath)
        parent_MDagModifier.doIt()

    def doChilds(self,dataNode=None,childDataNodes=None):
        _node_DataNode=dataNode or self._node_DataNode
        _child_DataNodes=childDataNodes or self._child_DataNodes
        
        node_MObject=self.node_query_MObject(str(_node_DataNode))
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)

        for _child_DataNode in _child_DataNodes:
            child_MObject=self.node_query_MObject(str(_child_DataNode))
            child_MDagPath=self.convertMObject_query_MDagPath(child_MObject)

            child_MDagModifier=om2.MDagModifier()
            child_MDagModifier.reparentNode(child_MDagPath,node_MDagPath)
            child_MDagModifier.doIt()

    def queryFullPathName(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode

        node_MObject=self.node_query_MObject(str(_node_DataNode))
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)

        name_str=node_MDagPath.fullPathName()
        return name_str

    def queryShapeSelfDAGNode(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode

        node_MObject=self.node_query_MObject(str(_node_DataNode))
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        shape_MObject=self.shape_query_MObject(node_MDagPath)
        shape_DataNode=dLB.DataNode(shape_MObject)

        shape_SelfDAGNode=SelfDAGNode()
        shape_SelfDAGNode.setDataNode(shape_DataNode)
        return shape_SelfDAGNode

    def queryParentSelfDAGNode(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode

        node_MObject=self.node_query_MObject(str(_node_DataNode))
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        parent_MObject=self.parent_query_MObject(node_MDagPath)
        parent_DataNode=dLB.DataNode(parent_MObject)

        parent_SelfDAGNode=SelfDAGNode()
        parent_SelfDAGNode.setDataNode(parent_DataNode)
        return parent_SelfDAGNode
    
    def queryChildSelfDAGNodes(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode

        node_MObject=self.node_query_MObject(str(_node_DataNode))
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        child_MObjects=self.child_query_MObjects(node_MDagPath,shapeOnly=False)

        child_SelfDAGNodes=[]
        for child_MObject in child_MObjects:
            child_DataNode=dLB.DataNode(child_MObject)
            child_SelfDAGNode=SelfDAGNode()
            child_SelfDAGNode.setDataNode(child_DataNode)
            child_SelfDAGNodes.append(child_SelfDAGNode)

        return child_SelfDAGNodes
    
    def queryNormalDataMatrix(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode

        node_DataMatrix=self.__dataNodeToNormalMatrix_query_DataMatrix(_node_DataNode)
        return node_DataMatrix
    
    def queryWorldDataMatrix(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode

        node_DataMatrix=self.__dataNodeToWorldMatrix_query_DataMatrix(_node_DataNode)
        return node_DataMatrix
    
    def queryParentDataMatrix(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode

        node_DataMatrix=self.__dataNodeToParentMatrix_query_DataMatrix(_node_DataNode)
        return node_DataMatrix
    
    def queryInverseNormalDataMatrix(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode

        node_DataMatrix=self.__dataNodeToInverseNormalMatrix_query_DataMatrix(_node_DataNode)
        return node_DataMatrix
    
    def queryInverseWorldDataMatrix(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode

        node_DataMatrix=self.__dataNodeToInverseWorldMatrix_query_DataMatrix(_node_DataNode)
        return node_DataMatrix
    
    def queryInverseParentDataMatrix(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode

        node_DataMatrix=self.__dataNodeToInverseParentMatrix_query_DataMatrix(_node_DataNode)
        return node_DataMatrix

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

    def matchTargetTransform(self,sourceNode=None,targetNode=None,mirrorAxis=None,mirrorOrientVector=None,matrix=None):
        _matrix_DataMatrix=matrix or self._matrix_DataMatrix
        _source_DataNode=sourceNode or self._node_DataNode or self._source_DataNode
        _target_DataNode=targetNode or self._target_DataNode
        _mirrorAxis_str=mirrorAxis or self._mirrorAxis_str
        _mirrorOrientVector_str=mirrorOrientVector or self._mirrorOrientVector_str

        if not _matrix_DataMatrix is None:
            source_DataMatrix=_matrix_DataMatrix
        else:
            source_DataMatrix=self.__dataNodeToWorldMatrix_query_DataMatrix(_source_DataNode)

        target_MObject=self.node_query_MObject(str(_target_DataNode))
        target_MDagPath=self.convertMObject_query_MDagPath(target_MObject)
        target_DataMatrix=self.convertMDagPathToInverseParentMatrix_query_DataMatrix(target_MDagPath)

        mirror_SelfMatrix=mLB.SelfMatrix()
        mirror_SelfMatrix.setDataMatrix(source_DataMatrix)
        mirror_SelfMatrix.setSubjectDataMatrix(target_DataMatrix)
        mirror_DataMatrix=mirror_SelfMatrix.match()

        targetNode_MFnTransform=om2.MFnTransform(target_MDagPath)
        targetMirror_MTransformationMatrix=om2.MTransformationMatrix(mirror_DataMatrix)
        targetNode_MFnTransform.setTransformation(targetMirror_MTransformationMatrix)
    
    def matchTargetTranslate(self):
        pass

    def matchTargetRotation(self):
        pass
    
    def matchTargetQuaternion(self):
        pass
    
    def matchTargetAimVector(self):
        pass
    
    def matchTargetScale(self):
        pass
    
    def matchTargetShear(self):
        pass

    def mirrorTargetTransform(self,sourceNode=None,targetNode=None,mirrorAxis=None,mirrorOrientVector=None,matrix=None):
        _matrix_DataMatrix=matrix or self._matrix_DataMatrix
        _source_DataNode=sourceNode or self._node_DataNode or self._source_DataNode
        _target_DataNode=targetNode or self._target_DataNode
        _mirrorAxis_str=mirrorAxis or self._mirrorAxis_str
        _mirrorOrientVector_str=mirrorOrientVector or self._mirrorOrientVector_str

        if not _matrix_DataMatrix is None:
            source_DataMatrix=_matrix_DataMatrix
        else:
            source_DataMatrix=self.__dataNodeToWorldMatrix_query_DataMatrix(_source_DataNode)

        target_MObject=self.node_query_MObject(str(_target_DataNode))
        target_MDagPath=self.convertMObject_query_MDagPath(target_MObject)
        target_DataMatrix=self.convertMDagPathToInverseParentMatrix_query_DataMatrix(target_MDagPath)

        mirror_SelfMatrix=mLB.SelfMatrix()
        mirror_SelfMatrix.setDataMatrix(source_DataMatrix)
        mirror_SelfMatrix.setSubjectDataMatrix(target_DataMatrix)
        mirror_SelfMatrix.setMirrorAxis(_mirrorAxis_str)
        mirror_SelfMatrix.setMirrorOrientVector(_mirrorOrientVector_str)
        mirror_DataMatrix=mirror_SelfMatrix.mirror()

        targetMirror_MTransformationMatrix=om2.MTransformationMatrix(mirror_DataMatrix)
        targetNode_MFnTransform=om2.MFnTransform(target_MDagPath)
        targetNode_MFnTransform.setTransformation(targetMirror_MTransformationMatrix)

    def mirrorTargetTranslate(self):
        pass
    
    def mirrorTargetRotation(self):
        pass

    def mirrorTargetQuaternion(self):
        pass
    
    def mirrorTargetShear(self):
        pass

