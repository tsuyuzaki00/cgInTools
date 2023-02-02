# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import maya.api.OpenMayaAnim as oma2

import cgInTools as cit
from . import jsonLB as jLB
cit.reloads([jLB])

RULES_DICT=jLB.getJson(cit.mayaSettings_dir,"openLibrary")

class TrsObject(object):
    def __init__(self,obj):
        self._transMFn_list=RULES_DICT["transMFn_list"]
        self._shapeMFn_list=RULES_DICT["shapeMFn_list"]
        self._nodeTypeToMFn_dict=RULES_DICT["nodeTypeToMFn_dict"]

        self._fullPath_bool=False

        self._object_MObject,self._object_MDagPath=self.selectOpenMaya_create_MObject_MDagPath(obj)
        self._objectType_str=self.nodeType_query_str(self._object_MObject)

        self._shape_MObjects=self.child_query_MObjects(self._object_MDagPath,self._shapeMFn_list)
        self._shapeType_strs=self.nodeType_query_strs(self._shape_MObjects)
        
        self._parent_MObject=self.parent_query_MObject(self._object_MDagPath)
        self._child_MObjects=self.child_query_MObjects(self._object_MDagPath,self._transMFn_list)
        
        self._subject_bool=False
        self._subject_MObject=None
        self._subject_MDagPath=None

    #Single Function
    def selectOpenMaya_create_MObject_MDagPath(self,node):
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
        self._object_MObject,self._object_MDagPath=self.selectOpenMaya_create_MObject_MDagPath(variable)
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
        self._subject_MObject,self._subject_MDagPath=self.selectOpenMaya_create_MObject_MDagPath(variable)
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
        self._time=oma2.MAnimControl.currentTime()
        self._transKey_bool=False
        self._rotateKey_bool=False
        self._scaleKey_bool=False
        self._otherKey_bool=False
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

    #Private Function
    def _trsKey_edit_func(self):
        if self._transKey_bool:
            translates=["translateX","translateY","translateZ"]
            for translate in translates:
                cmds.setKeyframe(self._object,at=translate)
        if self._rotateKey_bool:
            rotates=["rotateX","rotateY","rotateZ"]
            for rotate in rotates:
                cmds.setKeyframe(self._object,at=rotate)
        if self._scaleKey_bool:
            scales=["scaleX","scaleY","scaleZ"]
            for scale in scales:
                cmds.setKeyframe(self._object,at=scale)
        if self._otherKey_bool:
            if not self._otherValue_dicts == [] or not self._otherValue_dicts == None:
                for _otherValue_dict in self._otherValue_dicts:
                    cmds.setKeyframe(_otherValue_dict["node"],at=_otherValue_dict["attr"],v=_otherValue_dict["value"])

    #Public Function
    def __loading(self):
        self._normal_MMatrix=self.matrix_query_MMatrix(self._object_MDagPath,type="normal")
        self._world_MMatrix=self.matrix_query_MMatrix(self._object_MDagPath,type="world")
        self._parent_MMatrix=self.matrix_query_MMatrix(self._object_MDagPath,type="parent")

    def setRunMatrix(self,variable):
        self._runMatrix_str=variable
        return self._runMatrix_str
    def getRunMatrix(self):
        return self._runMatrix_str

    def setNormalMatrix(self,variable):
        self._normal_MMatrix=variable
        return self._normal_MMatrix
    def getNormalMatrix(self):
        return self._normal_MMatrix
    
    def setWorldMatrix(self,variable):
        self._world_MMatrix=variable
        return self._world_MMatrix
    def getWorldMatrix(self):
        return self._world_MMatrix
    
    def setParentMatrix(self,variable):
        self._parent_MMatrix=variable
        return self._parent_MMatrix
    def getParentMatrix(self):
        return self._parent_MMatrix

    def setTime(self,variable):
        fpsUnitType_int=om2.MTime.uiUnit()
        MTime=om2.MTime(variable,fpsUnitType_int)
        self._time=MTime
        return self._time
    def setCurrentTime(self):
        MTime=oma2.MAnimControl.currentTime()
        self._time=MTime
        return self._time
    def getTime(self,unit=None):
        fpsUnitType_int=unit or om2.MTime.uiUnit()
        time=self._time.asUnits(fpsUnitType_int)
        return time
    
    def setTransKeyBool(self,variable):
        self._transKey_bool=variable
        return self._transKey_bool
    def getTransKeyBool(self):
        return self._transKey_bool

    def setRotateKeyBool(self,variable):
        self._rotateKey_bool=variable
        return self._rotateKey_bool
    def getRotateKeyBool(self):
        return self._rotateKey_bool

    def setScaleKeyBool(self,variable):
        self._scaleKey_bool=variable
        return self._scaleKey_bool
    def getScaleKeyBool(self):
        return self._scaleKey_bool
    
    def setAttrKeyBool(self,variable):
        self._otherKey_bool=variable
        return self._otherKey_bool
    def getAttrKeyBool(self):
        return self._otherKey_bool

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
            cmds.xform(self._object,m=self._normal_MMatrix)
        elif self._runMatrix_str == "world":
            cmds.xform(self._object,m=self._world_MMatrix)
        elif self._runMatrix_str == "parent":
            cmds.xform(self._object,m=self._parent_MMatrix)
        else:
            cmds.error('please setRunMatrix with the strings "normal" or "world" or "parent".')
        if not self._otherValue_dicts == [] or not self._otherValue_dicts == None:
            for _otherValue_dict in self._otherValue_dicts:
                cmds.setAttr(_otherValue_dict["node"]+"."+_otherValue_dict["attr"],_otherValue_dict["value"])

    def normalMovement(self):
        cmds.xform(self._object,m=self._normal_MMatrix)
        if not self._otherValue_dicts == [] or not self._otherValue_dicts == None:
            self.setAttrDict_edit_func(self._otherValue_dicts)

    def worldMovement(self):
        cmds.xform(self._object,m=self._world_MMatrix)
        if not self._otherValue_dicts == [] or not self._otherValue_dicts == None:
            self.setAttrDict_edit_func(self._otherValue_dicts)
    
    def parentMovement(self):
        cmds.xform(self._object,m=self._parent_MMatrix)
        if not self._otherValue_dicts == [] or not self._otherValue_dicts == None:
            self.setAttrDict_edit_func(self._otherValue_dicts)

    def currentKeyFrame(self):
        self._trsKey_edit_func()

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

        if not objAttr_MPlug.isConnected:
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