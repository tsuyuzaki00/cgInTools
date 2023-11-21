# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import maya.api.OpenMayaAnim as oma2
import sys,math

import cgInTools as cit
from ...library import baseLB as bLB
from . import dataLB as dLB
cit.reloads([bLB,dLB])

class ObjectDGNode(bLB.SelfOrigin):
    def __init__(self,objectDGNode=None):
        super(ObjectDGNode,self).__init__()
        if objectDGNode is None:
            self._node_DataNode=None
            self._name_DataName=None
            self._create_DataNode=None
            self._create_DataPlug=None
            self._create_DataPlugArray=None
            self._edit_DataPlug=None
            self._edit_DataPlugArray=None
            self._connect_DataPlugConnection=None
            self._connect_DataPlugConnectionArray=None
            self._keyable_DataKeyable=None
            self._drivenkey_DataDrivenKey=None
        elif type(objectDGNode) is ObjectDGNode:
            self._node_DataNode=objectDGNode.getDataNode()
            self._name_DataName=objectDGNode.getDataName()
            self._create_DataNode=objectDGNode.getDataNodeForCreate()
            self._create_DataPlug=objectDGNode.getDataPlugForCreate()
            self._create_DataPlugArray=objectDGNode.getDataPlugArrayForCreate()
            self._edit_DataPlug=objectDGNode.getDataPlugForEdit()
            self._edit_DataPlugArray=objectDGNode.getDataPlugArrayForEdit()
            self._connect_DataPlugConnection=objectDGNode.getDataPlugConnection()
            self._connect_DataPlugConnectionArray=objectDGNode.getDataPlugConnectionArray()
            self._keyable_DataKeyable=objectDGNode.getDataKeyable()
            self._drivenkey_DataDrivenKey=objectDGNode.getDataDrivenKey()

        self._dataChoice_strs+=[
            "DataNode",
            "DataName",
            "DataNodeForCreate",
            "DataPlugForCreate",
            "DataPlugArrayForCreate",
            "DataPlugForEdit",
            "DataPlugArrayForEdit",
            "DataPlugConnection",
            "DataPlugConnectionArray",
            "DataKeyable",
            "DataDrivenKey"
        ]
        self._doIt_strs+=[
            "createNode",
            "rename",
            "createAttr",
            "createAttrArray",
            "editAttr",
            "editAttrArray",
            "editConnection",
            "editConnectionArray",
            "editKeyable",
            "editDrivenKey",
            "queryAttr",
            "queryAttrArray",
            "queryConnection",
            "queryConnectionArray",
            "queryKeyable",
            "queryDrivenKey"
        ]

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

    def setDataNodeForCreate(self,variable):
        self._create_DataNode=variable
        return self._create_DataNode
    def getDataNodeForCreate(self):
        return self._create_DataNode
    
    def setDataPlugForCreate(self,variable):
        self._create_DataPlug=variable
        return self._create_DataPlug
    def getDataPlugForCreate(self):
        return self._create_DataPlug
    
    def setDataPlugArrayForCreate(self,variable):
        self._create_DataPlugArray=variable
        return self._create_DataPlugArray
    def getDataPlugArrayForCreate(self):
        return self._create_DataPlugArray

    def setDataPlugForEdit(self,variable):
        self._edit_DataPlug=variable
        return self._edit_DataPlug
    def getDataPlugForEdit(self):
        return self._edit_DataPlug
    
    def setDataPlugArrayForEdit(self,variable):
        self._edit_DataPlugArray=variable
        return self._edit_DataPlugArray
    def getDataPlugArrayForEdit(self):
        return self._edit_DataPlugArray

    def setDataPlugConnection(self,variable):
        self._connect_DataPlugConnection=variable
        return self._connect_DataPlugConnection
    def getDataPlugConnection(self):
        return self._connect_DataPlugConnection
    
    def setDataPlugConnectionArray(self,variable):
        self._connect_DataPlugConnectionArray=variable
        return self._connect_DataPlugConnectionArray
    def getDataPlugConnectionArray(self):
        return self._connect_DataPlugConnectionArray
    
    def setDataKeyable(self,variable):
        self._keyable_DataKeyable=variable
        return self._keyable_DataKeyable
    def getDataKeyable(self):
        return self._keyable_DataKeyable
        
    def setDataDrivenKey(self,variable):
        self._drivenkey_DataDrivenKey=variable
        return self._drivenkey_DataDrivenKey
    def getDataDrivenKey(self):
        return self._drivenkey_DataDrivenKey

    #Public Function
    def createNode(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode

        self.node_create_func(_node_DataNode.getNodeName(),_node_DataNode.getNodeType())

    def rename(self,dataName=None):
        _name_DataName=dataName or self._name_DataName

    def createAttr(self,dataPlug=None):
        pass

    def createAttrArray(self,dataPlugArray=None):
        pass

    def editAttribute(self,dataPlug=None):
        pass

    def editAttributeArray(self,dataPlugArray=None):
        pass
    
    def editConnection(self,dataPlugConnection=None):
        pass

    def editConnectionArray(self,dataPlugConnectionArray=None):
        pass
    
    def editKeyable(self,dataKeyable=None):
        pass
    
    def editDrivenKey(self,dataDrivenKey=None):
        pass

    def queryAttribute(self):
        pass
    
    def queryAttributeArray(self):
        pass

    def queryConnection(self):
        pass

    def queryConnectionArray(self):
        pass

    def queryKeyable(self):
        pass
    
    def queryDrivenKey(self):
        pass

class ObjectDAGNode(ObjectDGNode):
    def __init__(self,objectDAGNode=None):
        super(ObjectDAGNode,self).__init__(objectDAGNode)
        if objectDAGNode is None:
            self._parent_DataNode=None
            self._child_DataNodeArray=None
            self._shape_DataNodeArray=None
            self._edit_DataMatrix=None
            self._translate_DataTranslate=None
            self._rotate_DataRotation=None
            self._quaternion_DataQuaternion=None
            self._scale_DataScale=None
            self._match_DataMatch=None
            self._mirror_DataMirror=None
        elif type(objectDAGNode) is objectDAGNode:
            self._parent_DataNode=objectDAGNode.getDataNodeForParent()
            self._child_DataNodeArray=objectDAGNode.getDataNodeForChildArray()
            self._shape_DataNodeArray=objectDAGNode.getDataNodeForShapeArray()
            self._edit_DataMatrix=objectDAGNode.getDataMatrix()
            self._translate_DataTranslate=objectDAGNode.getDataTranslate()
            self._rotate_DataRotation=objectDAGNode.getDataRotation()
            self._quaternion_DataQuaternion=objectDAGNode.getDataQuaternion()
            self._scale_DataScale=objectDAGNode.getDataScale()
            self._match_DataMatch=objectDAGNode.getDataMatch()
            self._mirror_DataMirror=objectDAGNode.getDataMirror()

        self._dataChoice_strs+=[
            "DataNodeForParent",
            "DataNodeArrayForChild",
            "DataNodeArrayForShape",
            "DataMatrix",
            "DataTranslate",
            "DataRotation",
            "DataQuaternion",
            "DataScale",
            "DataMatch",
            "DataMirror"
        ]
        self._doIt_strs+=[
            "editParent",
            "editChilds",
            "editShapes",
            "editTransform",
            "editTransformByMatrix",
            "editTranslate",
            "editTranslateByMatrix",
            "editRotation",
            "editRotationByMatrix",
            "editQuaternion",
            "editAimVector",
            "editScale",
            "editScaleByMatrix",
            "editShear",
            "matchTransform",
            "matchTransformByMatrix",
            "matchTranslate",
            "matchTranslateByMatrix",
            "matchRotation",
            "matchRotationByMatrix",
            "matchQuaternion",
            "matchAimVector",
            "matchScale",
            "matchScaleByMatrix",
            "matchShear",
            "mirrorTransform",
            "mirrorTranslate",
            "mirrorRotation",
            "mirrorQuaternion",
            "mirrorScale",
            "queryFullPathName",
            "queryParent",
            "queryParentOfDataNode",
            "queryChilds",
            "queryChildOfDataNodes",
            "queryShapes",
            "queryShapeOfDataNodes",
            "queryTranslate",
            "queryDataTranslate",
            "queryRotation",
            "queryDataRotation",
            "queryQuaternion",
            "queryDataQuaternion",
            "queryScale",
            "queryDataScale",
            "queryNormalDataMatrix",
            "queryWorldDataMatrix",
            "queryParentDataMatrix",
            "queryInverseNormalDataMatrix",
            "queryInverseWorldDataMatrix",
            "queryInverseParentDataMatrix"
        ]
    
    #Setting Function
    def setDataNodeForParent(self,variable):
        self._parent_DataNode=variable
        return self._parent_DataNode
    def getDataNodeForParent(self):
        return self._parent_DataNode
    
    def setDataNodeArrayForChildArray(self,variable):
        self._child_DataNodeArray=variable
        return self._child_DataNodeArray
    def getDataNodeArrayForChildArray(self):
        return self._child_DataNodeArray
    
    def setDataNodeArrayForShapeArray(self,variable):
        self._shape_DataNodeArray=variable
        return self._shape_DataNodeArray
    def getDataNodeArrayForShapeArray(self):
        return self._shape_DataNodeArray

    def setDataMatrix(self,variable):
        self._edit_DataMatrix=variable
        return self._edit_DataMatrix
    def getDataMatrix(self):
        return self._edit_DataMatrix
    
    def setDataTranslate(self,variable):
        self._translate_DataTranslate=variable
        return self._translate_DataTranslate
    def getDataTranslate(self):
        return self._translate_DataTranslate
    
    def setDataRotation(self,variable):
        self._rotate_DataRotation=variable
        return self._rotate_DataRotation
    def getDataRotation(self):
        return self._rotate_DataRotation
    
    def setDataQuaternion(self,variable):
        self._quaternion_DataQuaternion=variable
        return self._quaternion_DataQuaternion
    def getDataQuaternion(self):
        return self._quaternion_DataQuaternion
    
    def setDataScale(self,variable):
        self._scale_DataScale=variable
        return self._scale_DataScale
    def getDataScale(self):
        return self._scale_DataScale

    def setDataMatch(self,variable):
        self._match_DataMatch=variable
        return self._match_DataMatch
    def getDataMatch(self):
        return self._match_DataMatch
    
    def setDataMirror(self,variable):
        self._mirror_DataMirror=variable
        return self._mirror_DataMirror
    def getDataMirror(self):
        return self._mirror_DataMirror
    
    #Public Function
    def editParent(self):
        pass

    def editChilds(self):
        pass

    def editShapes(self):
        pass

    def editTransform(self):
        pass
    
    def editTransformByMatrix(self):
        pass

    def editTranslate(self):
        pass
    
    def editTranslateByMatrix(self):
        pass

    def editRotation(self):
        pass
    
    def editRotationByMatrix(self):
        pass

    def editQuaternion(self):
        pass

    def editAimVector(self):
        pass

    def editScale(self):
        pass
    
    def editScaleByMatrix(self):
        pass
    
    def editShear(self):
        pass

    def matchTransform(self):
        pass
    
    def matchTransformByMatrix(self):
        pass
    
    def matchTranslate(self):
        pass
    
    def matchTranslateByMatrix(self):
        pass

    def matchRotation(self):
        pass
    
    def matchRotationByMatrix(self):
        pass
    
    def matchQuaternion(self):
        pass
    
    def matchAimVector(self):
        pass
    
    def matchScale(self):
        pass
    
    def matchScaleByMatrix(self):
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

    def mirrorScale(self):
        pass

    def queryFullPathName(self):
        pass
    
    def queryParent(self):
        pass
    
    def queryParentOfDataNode(self):
        pass

    def queryChilds(self):
        pass
    
    def queryChildOfDataNodes(self):
        pass

    def queryShapes(self):
        pass
    
    def queryShapeOfDataNodes(self):
        pass

    def queryTranslate(self):
        pass
    
    def queryDataTranslate(self):
        pass

    def queryRotation(self):
        pass
    
    def queryDataRotation(self):
        pass

    def queryQuaternion(self):
        pass
    
    def queryDataQuaternion(self):
        pass

    def queryScale(self):
        pass
    
    def queryDataScale(self):
        pass

    def queryNormalDataMatrix(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode
        node_DataMatrix=None
        return node_DataMatrix
    
    def queryWorldDataMatrix(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode
        node_DataMatrix=None
        return node_DataMatrix
    
    def queryParentDataMatrix(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode
        node_DataMatrix=None
        return node_DataMatrix
    
    def queryInverseNormalDataMatrix(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode
        node_DataMatrix=None
        return node_DataMatrix
    
    def queryInverseWorldDataMatrix(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode
        node_DataMatrix=None
        return node_DataMatrix
    
    def queryInverseParentDataMatrix(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode
        node_DataMatrix=None
        return node_DataMatrix

class ObjectJoint(ObjectDAGNode):
    def __init__(self,objectJoint=None):
        super(ObjectJoint,self).__init__(objectJoint)
        if objectJoint is None:
            pass

        self._dataChoice_strs+=[
        ]
        self._doIt_strs+=[
        ]
    
    #Public Function

class ObjectLight(ObjectDAGNode):
    def __init__(self):
        super(ObjectLight,self).__init__()

class ObjectCamera(ObjectDAGNode):
    def __init__(self):
        super(ObjectCamera,self).__init__()

class ObjectGeometry(ObjectDAGNode):
    def __init__(self):
        super(ObjectGeometry,self).__init__()
        self._create_DataMesh=None
        self._edit_DataMesh=None
        self._material_DataMaterial=None
        self._skin_DataBind=None
        self._skin_DataWeight=None

    #Setting Function
    def setDataMeshForCreate(self,variable):
        self._create_DataMesh=variable
        return self._create_DataMesh
    def getDataMeshForCreate(self):
        return self._create_DataMesh
    
    def setDataMeshForEdit(self,variable):
        self._edit_DataMesh=variable
        return self._edit_DataMesh
    def getDataMeshForEdit(self):
        return self._edit_DataMesh

    def setDataMaterial(self,variable):
        self._material_DataMaterial=variable
        return self._material_DataMaterial
    def getDataMaterial(self):
        return self._material_DataMaterial

    def setDataBind(self,variable):
        self._skin_DataBind=variable
        return self._skin_DataBind
    def getDataBind(self):
        return self._skin_DataBind

    def setDataWeightForSkin(self,variables):
        self._skin_DataWeight=variables
        return self._skin_DataWeight
    def getDataWeightForSkin(self):
        return self._skin_DataWeight
    
    #Public Function
    def createGeometry(self):
        pass

    def editGeometry(self):
        pass

    def skinBind(self):
        pass

    def editSkinWeight(self):
        pass

class ObjectSurface(ObjectDAGNode):
    def __init__(self):
        super(ObjectSurface,self).__init__()
        self._create_DataSurface=None
        self._edit_DataSurface=None
        self._skin_DataBind=None
        self._skin_DataWeight=None

    #Setting Function
    def setDataSurfaceForCreate(self,variable):
        self._create_DataSurface=variable
        return self._create_DataSurface
    def getDataSurfaceForCreate(self):
        return self._create_DataSurface
    
    def setDataSurfaceForEdit(self,variable):
        self._edit_DataSurface=variable
        return self._edit_DataSurface
    def getDataSurfaceForEdit(self):
        return self._edit_DataSurface
    
    def setDataBind(self,variable):
        self._skin_DataBind=variable
        return self._skin_DataBind
    def getDataBind(self):
        return self._skin_DataBind

    def setDataWeightForSkin(self,variables):
        self._skin_DataWeight=variables
        return self._skin_DataWeight
    def getDataWeightForSkin(self):
        return self._skin_DataWeight
    

    #Public Function
    def createSurface(self):
        pass

    def editSurface(self):
        pass

    def skinBind(self):
        pass

    def editSkinWeight(self):
        pass

class ObjectCurve(ObjectDAGNode):
    def __init__(self):
        super(ObjectCurve,self).__init__()
        self._create_DataCurve=None
        self._edit_DataCurve=None
        self._skin_DataBind=None
        self._skin_DataWeight=None

    #Setting Function
    def setDataCurveForCreate(self,variable):
        self._create_DataCurve=variable
        return self._create_DataCurve
    def getDataCurveForCreate(self):
        return self._create_DataCurve
    
    def setDataCurveForEdit(self,variable):
        self._edit_DataCurve=variable
        return self._edit_DataCurve
    def getDataCurveForEdit(self):
        return self._edit_DataCurve

    def setDataBind(self,variable):
        self._skin_DataBind=variable
        return self._skin_DataBind
    def getDataBind(self):
        return self._skin_DataBind

    def setDataWeightForSkin(self,variables):
        self._skin_DataWeight=variables
        return self._skin_DataWeight
    def getDataWeightForSkin(self):
        return self._skin_DataWeight
    
    
    #Public Function
    def createCurve(self):
        pass

    def editCurve(self):
        pass

    def skinBind(self):
        pass

    def editSkinWeight(self):
        pass