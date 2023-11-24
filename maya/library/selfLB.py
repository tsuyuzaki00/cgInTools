# -*- coding: iso-8859-15 -*-
import cgInTools as cit
from ...library import baseLB as bLB
from . import dataLB as dLB
cit.reloads([bLB,dLB])

class SelfDGNode(bLB.SelfOrigin):
    def __init__(self,selfDGNode=None):
        super(SelfDGNode,self).__init__()
        if selfDGNode is None:
            self._node_DataNode=None
            self._name_DataName=None
            self._create_DataNode=None
            self._create_DataPlug=None
            self._create_DataPlugArray=None
            self._edit_DataPlug=None
            self._edit_DataPlugArray=None
            self._connect_DataPlugPair=None
            self._connect_DataPlugPairArray=None
            self._keyable_DataKeyable=None
            self._drivenkey_DataDrivenKey=None
        elif type(selfDGNode) is SelfDGNode:
            self._node_DataNode=selfDGNode.getDataNode()
            self._name_DataName=selfDGNode.getDataName()
            self._create_DataNode=selfDGNode.getDataNodeForCreate()
            self._create_DataPlug=selfDGNode.getDataPlugForCreate()
            self._create_DataPlugArray=selfDGNode.getDataPlugArrayForCreate()
            self._edit_DataPlug=selfDGNode.getDataPlugForEdit()
            self._edit_DataPlugArray=selfDGNode.getDataPlugArrayForEdit()
            self._connect_DataPlugPair=selfDGNode.getDataPlugPair()
            self._connect_DataPlugPairArray=selfDGNode.getDataPlugPairArray()
            self._keyable_DataKeyable=selfDGNode.getDataKeyable()
            self._drivenkey_DataDrivenKey=selfDGNode.getDataDrivenKey()

        self._dataChoice_strs+=[
            "DataNode",
            "DataName",
            "DataNodeForCreate",
            "DataPlugForCreate",
            "DataPlugArrayForCreate",
            "DataPlugForEdit",
            "DataPlugArrayForEdit",
            "DataPlugPair",
            "DataPlugPairArray",
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
            "editPair",
            "editPairArray",
            "editKeyable",
            "editDrivenKey",
            "queryAttr",
            "queryAttrArray",
            "queryPair",
            "queryPairArray",
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

    def setDataPlugPair(self,variable):
        self._connect_DataPlugPair=variable
        return self._connect_DataPlugPair
    def getDataPlugPair(self):
        return self._connect_DataPlugPair
    
    def setDataPlugPairArray(self,variable):
        self._connect_DataPlugPairArray=variable
        return self._connect_DataPlugPairArray
    def getDataPlugPairArray(self):
        return self._connect_DataPlugPairArray
    
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

    def editAttr(self,dataPlug=None):
        pass

    def editAttrArray(self,dataPlugArray=None):
        pass
    
    def editConnect(self,dataPlugPair=None):
        pass

    def editConnectArray(self,dataPlugPairArray=None):
        pass
    
    def editKeyable(self,dataKeyable=None):
        pass
    
    def editDrivenKey(self,dataDrivenKey=None):
        pass

    def queryAttr(self):
        pass
    
    def queryAttributeArray(self):
        pass

    def queryConnect(self):
        pass

    def queryConnectArray(self):
        pass

    def queryKeyable(self):
        pass
    
    def queryDrivenKey(self):
        pass

class SelfDAGNode(SelfDGNode):
    def __init__(self,selfDAGNode=None):
        super(SelfDAGNode,self).__init__(selfDAGNode)
        if selfDAGNode is None:
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
        elif type(selfDAGNode) is SelfDAGNode:
            self._parent_DataNode=selfDAGNode.getDataNodeForParent()
            self._child_DataNodeArray=selfDAGNode.getDataNodeArrayForChild()
            self._shape_DataNodeArray=selfDAGNode.getDataNodeArrayForShape()
            self._edit_DataMatrix=selfDAGNode.getDataMatrix()
            self._translate_DataTranslate=selfDAGNode.getDataTranslate()
            self._rotate_DataRotation=selfDAGNode.getDataRotation()
            self._quaternion_DataQuaternion=selfDAGNode.getDataQuaternion()
            self._scale_DataScale=selfDAGNode.getDataScale()
            self._match_DataMatch=selfDAGNode.getDataMatch()
            self._mirror_DataMirror=selfDAGNode.getDataMirror()

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
    
    def setDataNodeArrayForChild(self,variable):
        self._child_DataNodeArray=variable
        return self._child_DataNodeArray
    def getDataNodeArrayForChild(self):
        return self._child_DataNodeArray
    
    def setDataNodeArrayForShape(self,variable):
        self._shape_DataNodeArray=variable
        return self._shape_DataNodeArray
    def getDataNodeArrayForShape(self):
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

class SelfJoint(SelfDAGNode):
    def __init__(self,objectJoint=None):
        super(SelfJoint,self).__init__(objectJoint)
        if objectJoint is None:
            pass

        self._dataChoice_strs+=[
        ]
        self._doIt_strs+=[
        ]
    
    #Public Function
    def createJoint(self,):
        pass

class SelfLight(SelfDAGNode):
    def __init__(self):
        super(SelfLight,self).__init__()

    #Public Function
    def createLight(self,):
        pass

class SelfCamera(SelfDAGNode):
    def __init__(self):
        super(SelfCamera,self).__init__()

    #Public Function
    def createCamera(self,):
        pass

class SelfGeometry(SelfDAGNode):
    def __init__(self):
        super(SelfGeometry,self).__init__()
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

class SelfSurface(SelfDAGNode):
    def __init__(self):
        super(SelfSurface,self).__init__()
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

class SelfCurve(SelfDAGNode):
    def __init__(self):
        super(SelfCurve,self).__init__()
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