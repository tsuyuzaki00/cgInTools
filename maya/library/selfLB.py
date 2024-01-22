# -*- coding: iso-8859-15 -*-
import cgInTools as cit
from ...library import baseLB as bLB
from . import dataLB as dLB
from . import mayaMenuLB as mmLB
from . import nodeLB as nLB
from . import nameLB as naLB
from . import projectLB as pjLB
cit.reloads([bLB,dLB,mmLB,nLB,naLB,pjLB])

class SelfMenu(bLB.SelfOrigin):
    def __init__(self,selfObject=None):
        super(SelfMenu,self).__init__(selfObject)
        if selfObject is None:
            self._menu_DataMenu=None
        elif isinstance(selfObject,SelfMenu):
            self._menu_DataMenu=selfObject.getDataMenu()

    #Setting Function
    def setDataMenu(self,variable):
        self._menu_DataMenu=variable
        return self._menu_DataMenu
    def getDataMenu(self):
        return self._menu_DataMenu
    
    #Public Function
    def create(self,dataMenu=None):
        _menu_DataMenu=dataMenu or self._menu_DataMenu

        menu_AppMenu=mmLB.AppMenu()
        menu_AppMenu.setDataMenu(_menu_DataMenu)
        menu_AppMenu.create()

    def updata(self,dataMenu=None):
        pass

class SelfDGNode(bLB.SelfOrigin):
    def __init__(self,selfObject=None):
        super(SelfDGNode,self).__init__(selfObject)
        if selfObject is None:
            self._node_DataNode=None
            self._name_DataName=None
            self._create_DataNode=None
            self._create_DataPlug=None
            self._create_DataPlugArray=None
            self._edit_DataPlug=None
            self._edit_DataPlugArray=None
            self._connect_DataConnectPlug=None
            self._connect_DataConnectPlugArray=None
            self._anim_DataKeyable=None
            self._driven_DataKeyable=None
        elif isinstance(selfObject,SelfDGNode):
            self._node_DataNode=selfObject.getDataNode()
            self._name_DataName=selfObject.getDataName()
            self._create_DataNode=selfObject.getCreateDataNode()
            self._create_DataPlug=selfObject.getCreateDataPlug()
            self._create_DataPlugArray=selfObject.getCreateDataPlugArray()
            self._edit_DataPlug=selfObject.getEditDataPlug()
            self._edit_DataPlugArray=selfObject.getEditDataPlugArray()
            self._connect_DataPlugConnect=selfObject.getDataConnectPlug()
            self._connect_DataPlugConnectArray=selfObject.getDataConnectPlugArray()
            self._anim_DataKeyable=selfObject.getAnimDataKeyable()
            self._driven_DataKeyable=selfObject.getDrivenDataKeyable()

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

    def setCreateDataNode(self,variable):
        self._create_DataNode=variable
        return self._create_DataNode
    def getCreateDataNode(self):
        return self._create_DataNode
    
    def setCreateDataPlug(self,variable):
        self._create_DataPlug=variable
        return self._create_DataPlug
    def getCreateDataPlug(self):
        return self._create_DataPlug
    
    def setCreateDataPlugArray(self,variable):
        self._create_DataPlugArray=variable
        return self._create_DataPlugArray
    def getCreateDataPlugArray(self):
        return self._create_DataPlugArray

    def setEditDataPlug(self,variable):
        self._edit_DataPlug=variable
        return self._edit_DataPlug
    def getEditDataPlug(self):
        return self._edit_DataPlug
    
    def setEditDataPlugArray(self,variable):
        self._edit_DataPlugArray=variable
        return self._edit_DataPlugArray
    def getEditDataPlugArray(self):
        return self._edit_DataPlugArray

    def setDataConnectPlug(self,variable):
        self._connect_DataConnectPlug=variable
        return self._connect_DataConnectPlug
    def getDataConnectPlug(self):
        return self._connect_DataConnectPlug
    
    def setDataConnectPlugArray(self,variable):
        self._connect_DataConnectPlugArray=variable
        return self._connect_DataConnectPlugArray
    def getDataConnectPlugArray(self):
        return self._connect_DataConnectPlugArray
    
    def setAnimDataKeyable(self,variable):
        self._anim_DataKeyable=variable
        return self._anim_DataKeyable
    def getAnimDataKeyable(self):
        return self._anim_DataKeyable
        
    def setDrivenDataKeyable(self,variable):
        self._driven_DataDrivenKey=variable
        return self._driven_DataDrivenKey
    def getDrivenDataKeyable(self):
        return self._driven_DataDrivenKey

    #Public Function
    def createNode(self,dataNode=None,dataName=None):
        _create_DataNode=dataNode or self._create_DataNode
        _name_DataName=dataName or self._name_DataName

        name_AppName=naLB.AppNodeName()
        name_AppName.setDataName(_name_DataName)
        name_str=name_AppName.create()
        _create_DataNode.setName(name_str)

        node_AppNode=nLB.AppNode()
        node_AppNode.setDataNode(_create_DataNode)
        self._node_DataNode=node_AppNode.create()
        return self._node_DataNode
    
    def createNodeNormal(self,dataNode=None):
        _create_DataNode=dataNode or self._create_DataNode

        node_AppNode=nLB.AppNode()
        node_AppNode.setDataNode(_create_DataNode)
        self._node_DataNode=node_AppNode.create()
        return self._node_DataNode

    def rename(self,dataNode=None,dataName=None):
        _node_DataNode=dataNode or self._node_DataNode
        _name_DataName=dataName or self._name_DataName

        rename_AppNodeName=naLB.AppNodeName()
        rename_AppNodeName.setDataNode(_node_DataNode)
        rename_AppNodeName.setDataName(_name_DataName)
        rename_str=rename_AppNodeName.rename()
        return rename_str
    
    def editRename(self,dataNode=None,dataName=None):
        _node_DataNode=dataNode or self._node_DataNode
        _name_DataName=dataName or self._name_DataName

        rename_AppNodeName=naLB.AppNodeName()
        rename_AppNodeName.setDataNode(_node_DataNode)
        rename_AppNodeName.setDataName(_name_DataName)
        rename_str=rename_AppNodeName.editRename()
        return rename_str

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
    def __init__(self,selfObject=None):
        super(SelfDAGNode,self).__init__(selfObject)
        if selfObject is None:
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
        elif isinstance(selfObject,SelfDAGNode):
            self._parent_DataNode=selfObject.getDataNodeForParent()
            self._child_DataNodeArray=selfObject.getDataNodeArrayForChild()
            self._shape_DataNodeArray=selfObject.getDataNodeArrayForShape()
            self._edit_DataMatrix=selfObject.getDataMatrix()
            self._translate_DataTranslate=selfObject.getDataTranslate()
            self._rotate_DataRotation=selfObject.getDataRotation()
            self._quaternion_DataQuaternion=selfObject.getDataQuaternion()
            self._scale_DataScale=selfObject.getDataScale()
            self._match_DataMatch=selfObject.getDataMatch()
            self._mirror_DataMirror=selfObject.getDataMirror()
    
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
        _node_DataNode=self._node_DataNode
        _edit_DataMatrix=self._edit_DataMatrix

        edit_AppDAGNode=nLB.AppDAGNode()
        edit_AppDAGNode.setDataNode(_node_DataNode)
        edit_AppDAGNode.setDataMatrix(_edit_DataMatrix)
        edit_AppDAGNode.editTransform()

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
    def __init__(self,selfObject=None):
        super(SelfJoint,self).__init__(selfObject)
        if selfObject is None:
            pass
        elif isinstance(selfObject,SelfJoint):
            pass
    
    #Public Function
    def createJoint(self,):
        pass

class SelfLight(SelfDAGNode):
    def __init__(self,selfObject=None):
        super(SelfLight,self).__init__(selfObject)
        if selfObject is None:
            pass
        elif isinstance(selfObject,SelfLight):
            pass

    #Public Function
    def createLight(self):
        pass

class SelfCamera(SelfDAGNode):
    def __init__(self,selfObject=None):
        super(SelfCamera,self).__init__(selfObject)
        if selfObject is None:
            pass
        elif isinstance(selfObject,SelfCamera):
            pass

    #Public Function
    def createCamera(self):
        pass

class SelfGeometry(SelfDAGNode):
    def __init__(self,selfObject=None):
        super(SelfGeometry,self).__init__(selfObject)
        if selfObject is None:
            self._create_DataMesh=None
            self._edit_DataMesh=None
            self._material_DataMaterial=None
            self._skin_DataBind=None
        elif isinstance(selfObject,SelfGeometry):
            self._create_DataMesh=selfObject.getCreateDataMesh()
            self._edit_DataMesh=selfObject.getEditDataMesh()
            self._material_DataMaterial=selfObject.getDataMaterial()
            self._skin_DataBind=selfObject.getDataBind()

    #Setting Function
    def setCreateDataMesh(self,variable):
        self._create_DataMesh=variable
        return self._create_DataMesh
    def getCreateDataMesh(self):
        return self._create_DataMesh
    
    def setEditDataMesh(self,variable):
        self._edit_DataMesh=variable
        return self._edit_DataMesh
    def getEditDataMesh(self):
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
    def __init__(self,selfObject=None):
        super(SelfSurface,self).__init__(selfObject)
        if selfObject is None:
            self._create_DataSurface=None
            self._edit_DataSurface=None
            self._skin_DataBind=None
        elif isinstance(selfObject,SelfSurface):
            self._create_DataSurface=selfObject.getCreateDataSurface()
            self._edit_DataSurface=selfObject.getEditDataSurface()
            self._skin_DataBind=selfObject.getDataBind()

    #Setting Function
    def setCreateDataSurface(self,variable):
        self._create_DataSurface=variable
        return self._create_DataSurface
    def getCreateDataSurface(self):
        return self._create_DataSurface
    
    def setEditDataSurface(self,variable):
        self._edit_DataSurface=variable
        return self._edit_DataSurface
    def getEditDataSurface(self):
        return self._edit_DataSurface
    
    def setDataBind(self,variable):
        self._skin_DataBind=variable
        return self._skin_DataBind
    def getDataBind(self):
        return self._skin_DataBind

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
    def __init__(self,selfObject=None):
        super(SelfCurve,self).__init__(selfObject)
        if selfObject is None:
            self._create_DataCurve=None
            self._edit_DataCurve=None
            self._skin_DataBind=None
            self._skin_DataWeight=None
        elif isinstance(selfObject,SelfCurve):
            self._create_DataCurve=selfObject.getCreateDataCurve()
            self._edit_DataCurve=selfObject.getEditDataCurve()
            self._skin_DataBind=selfObject.getDataBind()

    #Setting Function
    def setCreateDataCurve(self,variable):
        self._create_DataCurve=variable
        return self._create_DataCurve
    def getCreateDataCurve(self):
        return self._create_DataCurve
    
    def setEditDataCurve(self,variable):
        self._edit_DataCurve=variable
        return self._edit_DataCurve
    def getEditDataCurve(self):
        return self._edit_DataCurve

    def setDataBind(self,variable):
        self._skin_DataBind=variable
        return self._skin_DataBind
    def getDataBind(self):
        return self._skin_DataBind

    #Public Function
    def createCurve(self):
        pass

    def editCurve(self):
        pass

    def skinBind(self):
        pass

    def editSkinWeight(self):
        pass

class SelfProject(bLB.SelfOrigin):
    def __init__(self,selfObject=None):
        super(SelfProject,self).__init__(selfObject)
        if selfObject is None:
            self._project_DataPath=None
        elif isinstance(selfObject,SelfProject):
            self._project_DataPath=selfObject.getProjectDataPath()

    #Setting Function
    def setProjectDataPath(self,variable):
        self._project_DataPath=variable
        return self._project_DataPath
    def currentProjectDataPath(self):
        current_AppProject=pjLB.AppProject()
        self._project_DataPath=current_AppProject.currentDataPath()
        return self._project_DataPath
    def getProjectDataPath(self):
        return self._project_DataPath

    #Public Function
    def createProject(self,dataPath=None):
        _project_DataPath=dataPath or self._project_DataPath
        
        project_AppProject=pjLB.AppProject()
        project_AppProject.setDataPath(_project_DataPath)
        workSpace_dir=project_AppProject.createProject()
        return workSpace_dir

    def editProject(self,dataPath=None):
        _project_DataPath=dataPath or self._project_DataPath

        project_AppProject=pjLB.AppProject()
        project_AppProject.setDataPath(_project_DataPath)
        workSpace_dir=project_AppProject.editProject()
        return workSpace_dir

    def queryProject(self):
        project_AppProject=pjLB.AppProject()
        project_AppProject.setDataPath(self._project_DataPath)
        workSpace_dir=project_AppProject.queryProject()
        return workSpace_dir