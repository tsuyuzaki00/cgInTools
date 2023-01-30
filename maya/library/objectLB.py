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
        self._object=obj
        self._objectType=cmds.nodeType(self._object)
        self._shapes=self.childs_query_list(self._object,self._fullPath_bool,self._shapeMFn_list)
        self._shapeTypes=self.nodeTypes_query_list(self._shapes)
        
        self._parent_str=self.parent_query_str(self._object,self._fullPath_bool)
        self._childs=self.childs_query_list(self._object,self._fullPath_bool,self._transMFn_list)
        
        self._subject=None

    #Single Function
    def parent_query_str(self,node,fullPath=False):
        if node == None:
            return None
        node_MSelectionList=om2.MSelectionList().add(node)
        node_MDagPath=node_MSelectionList.getDagPath(0)
        node_MFnDagNode=om2.MFnDagNode(node_MDagPath)
        parent_MObject=node_MFnDagNode.parent(0)
        parent_MFnDagNode=om2.MFnDagNode(parent_MObject)
        if parent_MFnDagNode.name() == "world":
            return None
        if fullPath:
            return parent_MFnDagNode.fullPathName()
        else:
            return parent_MFnDagNode.name()

    def childs_query_list(self,node,fullPath=False,childMFn_list=[]):
        if node == None:
            return None
        node_MSelectionList=om2.MSelectionList().add(node)
        node_MDagPath=node_MSelectionList.getDagPath(0)
        node_MFnDagNode=om2.MFnDagNode(node_MDagPath)
        childs=[]
        for num in range(node_MFnDagNode.childCount()):
            child_MObject=node_MFnDagNode.child(num)
            #print(child_MObject.apiType())
            if child_MObject.apiType() in childMFn_list:
                child_MFnDagNode=om2.MFnDagNode(child_MObject)
                if fullPath:
                    child_str=child_MFnDagNode.fullPathName()
                    childs.append(child_str)
                else:
                    child_str=child_MFnDagNode.name()
                    childs.append(child_str)
        if childs == []:
           return None
        else:
            return childs

    def findConnect_query_list(self,node,source=True,target=True,mFnID=0):
        if node == None:
            return None
        findConnectedTo_list=[]
        node_MSelectionList=om2.MSelectionList().add(node)
        node_MObject=node_MSelectionList.getDependNode(0)
        node_MFnDagNode=om2.MFnDagNode(node_MObject)
        connections_MPlugArray=node_MFnDagNode.getConnections()
        for connection_MPlug in connections_MPlugArray:
            targets_MPlugArray=connection_MPlug.connectedTo(source,target)
            for target_MPlug in targets_MPlugArray:
                target_MObject=target_MPlug.node()
                #print(target_MObject.apiType())
                if target_MObject.hasFn(mFnID):
                    skc_MFnDependencyNode=om2.MFnDependencyNode(target_MObject)
                    findConnectedTo_list.append(skc_MFnDependencyNode.name())
        findNodes=list(set(findConnectedTo_list))
        if findNodes == []:
            return None
        else:
            return findNodes

    def nodeTypes_query_list(self,nodes):
        if nodes == None:
            return nodes
        nodeTypes=[]
        for node in nodes:
            nodeTypes.append(cmds.nodeType(node))
        if nodeTypes == []:
            return None
        else:
            return nodeTypes
    
    #Private Function
    def nodeTypeToMFnConverter_query_int(self,nodeType):
        return self._nodeTypeToMFn_dict[nodeType]

    #Public Function
    def __loading(self):
        self._objectType=cmds.nodeType(self._object)
        self._shapes=self.childs_query_list(self._object,self._fullPath_bool,self._shapeMFn_list)
        self._shapeTypes=self.nodeTypes_query_list(self._shapes)
        self._parent_str=self.parent_query_str(self._object,fullPath=self._fullPath_bool)
        self._childs=self.childs_query_list(self._object,self._fullPath_bool,self._transMFn_list)

        self._subjectType=cmds.nodeType(self._subject)
        self._subShape_list=self.childs_query_list(self._subject,self._fullPath_bool,self._shapeMFn_list)
        self._subShapeType_list=self.nodeTypes_query_list(self._shapes)
        self._subParent_str=self.parent_query_str(self._subject,fullPath=self._fullPath_bool)
        self._subChild_list=self.childs_query_list(self._subject,self._fullPath_bool,self._transMFn_list)

    def setFullPathSwitch(self,variable):
        self._fullPath_bool=variable
        return self._fullPath_bool
    def getFullPathSwitch(self):
        return self._fullPath_bool

    def setObject(self,variable):
        self._object=variable
        return self._object
    def getObject(self):
        return self._object
    def getObjectType(self):
        return self._objectType

    def getShapes(self):
        self.__loading()
        return self._shapes
    def getShapeTypes(self):
        self.__loading()
        return self._shapeTypes

    def getParent(self):
        self.__loading()
        return self._parent_str

    def getChilds(self):
        self.__loading()
        return self._childs

    def setSubject(self,variable):
        self._subject=variable
        return self._subject
    def getSubject(self):
        return self._subject

    def getSubShapes(self):
        self.__loading()
        return self._subShape_list
    def getSubShapeTypes(self):
        self.__loading()
        return self._subShapeType_list

    def getSubParent(self):
        self.__loading()
        return self._subParent_str

    def getSubChilds(self):
        self.__loading()
        return self._subChild_list

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
        mFn_int=self.nodeTypeToMFnConverter_query_int("skinCluster")
        self._skinCluster_list=self.findConnect_query_list(self._subShape_list[0],mFnID=mFn_int)

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
        return self._skinCluster_list

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
    def matrix_query_MMatrix(self,node,type="normal"):
        # type=normal or world or parent
        if node == None:
            return None
        node_MSelectionList=om2.MSelectionList().add(node)
        node_MDagPath=node_MSelectionList.getDagPath(0)
        if type == "normal":
            normal_MMatrix=om2.MFnDagNode(node_MDagPath).transformationMatrix()
            return normal_MMatrix
        elif type == "world":
            world_MMatrix=node_MDagPath.inclusiveMatrix()
            return world_MMatrix
        elif type == "parent":
            parent_MMatrix=node_MDagPath.exclusiveMatrix()
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
        self._normal_MMatrix=self.matrix_query_MMatrix(self._object,type="normal")
        self._world_MMatrix=self.matrix_query_MMatrix(self._object,type="world")
        self._parent_MMatrix=self.matrix_query_MMatrix(self._object,type="parent")

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
        self._time=0
        self._attr=""
        self._value=0
        self._inType=""
        self._inTangentType=11
        self._outTangentType=11
        self._animCurve=8

        self._animTangentReplaceID_dict=RULES_DICT["animTangentReplaceID_dict"]
        self._animTangentReplaceType_list=RULES_DICT["animTangentReplaceType_list"]
        self._animCurveReplaceID_dict=RULES_DICT["animCurveReplaceID_dict"]
        self._animCurveReplaceType_list=RULES_DICT["animCurveReplaceType_list"]

    #Single Function
    def objAttr_query_MFnAnimCurve(self,obj,attr,MTime):
        obj_MSelectionList=om2.MSelectionList().add(obj)
        obj_MObject=obj_MSelectionList.getDependNode(0)
        obj_MFnDependencyNode=om2.MFnDependencyNode(obj_MObject)
        objAttr_MPlug=obj_MFnDependencyNode.findPlug(attr,False)
        objAttr_MPlug.setMTime(MTime)
        objAttr_MFnAnimCurve=oma2.MFnAnimCurve(objAttr_MPlug)
        return objAttr_MFnAnimCurve

    def currentTime_query_MTime(self):
        MTime=oma2.MAnimControl.currentTime()
        fpsUnitType_int=om2.MTime.uiUnit()
        time=MTime.asUnits(fpsUnitType_int)
        return MTime

    #Multi Function
    def _inTangentType_query_int(self,obj,attr,MTime):
        objAttr_MFnAnimCurve=self.objAttr_query_MFnAnimCurve(obj,attr,MTime)
        inTangentTypeID_int=objAttr_MFnAnimCurve.inTangentType(0)
        return inTangentTypeID_int

    def _outTangentType_query_int(self,obj,attr,MTime):
        objAttr_MFnAnimCurve=self.objAttr_query_MFnAnimCurve(obj,attr,MTime)
        outTangentTypeID_int=objAttr_MFnAnimCurve.outTangentType(0)
        return outTangentTypeID_int

    def _keyFrame_create_func(self,obj,attr,value,MTime,inTangentTypeID,outTangentTypeID,animCurve):
        obj_MSelectionList=om2.MSelectionList().add(obj)
        obj_MObject=obj_MSelectionList.getDependNode(0)
        obj_MFnDependencyNode=om2.MFnDependencyNode(obj_MObject)
        objAttr_MPlug=obj_MFnDependencyNode.findPlug(attr,False)
        
        if not objAttr_MPlug.isConnected:
            animCurve_MFnAnimCurve=oma2.MFnAnimCurve()
            animCurve_MObject=animCurve_MFnAnimCurve.create(animCurve)
            animCurve_MFnDependencyNode=om2.MFnDependencyNode(animCurve_MObject)
            animCurve_MFnDependencyNode.setName(obj+"_"+attr)
            animCurve_MPlug=animCurve_MFnDependencyNode.findPlug("output",False)

            keyConnect_MDGModifier=om2.MDGModifier()
            keyConnect_MDGModifier.connect(animCurve_MPlug,objAttr_MPlug)
            keyConnect_MDGModifier.doIt()
        
        objAttr_MFnAnimCurve=oma2.MFnAnimCurve(objAttr_MPlug)
        objAttr_MFnAnimCurve.addKey(MTime,value,inTangentTypeID,outTangentTypeID)

    #Public Function
    def __loading(self):
        fpsUnitType_int=om2.MTime.uiUnit()
        time=self._time.asUnits(fpsUnitType_int)
        self._value=cmds.getAttr(self._object+"."+self._attr,t=time)
        self._inTangentType=self._inTangentType_query_int(self._object,self._attr,self._time)
        self._outTangentType=self._outTangentType_query_int(self._object,self._attr,self._time)
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
        MTime=oma2.MAnimControl.currentTime()
        self._time=Mtime
        return self._time
    def getTime(self,unit=None):
        fpsUnitType_int=unit or om2.MTime.uiUnit()
        time=self._time.asUnits(fpsUnitType_int)
        return time

    def setValue(self,variable):
        self._value=variable
        return self._value
    def setCurrentValue(self,unit=None):
        MTime=self.currentTime_query_MTime()
        fpsUnitType_int=unit or om2.MTime.uiUnit()
        time=MTime.asUnits(fpsUnitType_int)
        self._value=cmds.getAttr(self._object+"."+self._attr,t=time)
        return self._value
    def getValue(self):
        return self._value

    def setInTangentType(self,variable):
        self._inTangentType=self._animTangentReplaceID_dict[variable]
        return self._inTangentType
    def setCurrentInTangentType(self):
        MTime=self.currentTime_query_MTime()
        self._inTangentType=self._inTangentType_query_int(self._object,self._attr,MTime)
        return self._inTangentType
    def getInTangentType(self):
        inTangentType=self._animTangentReplaceType_list[self._inTangentType]
        return inTangentType
    
    def setOutTangentType(self,variable):
        self._outTangentType=self._animTangentReplaceID_dict[variable]
        return self._outTangentType
    def setCurrentOutTangentType(self):
        MTime=self.currentTime_query_MTime()
        self._outTangentType=self._outTangentType_query_int(self._object,self._attr,MTime)
        return self._outTangentType
    def getOutTangentType(self):
        outTangentType=self._animTangentReplaceType_list[self._outTangentType]
        return outTangentType
    
    def setAnimCurve(self,variable):
        self._animCurve=self._animCurveReplaceID_dict[variable]
        return self._animCurve
    def setCurrentAnimCurve(self):
        objAttr_MFnAnimCurve=self.objAttr_query_MFnAnimCurve(self._object,self._attr,self._time)
        self._animCurve=objAttr_MFnAnimCurve.animCurveType
        return self._animCurve
    def getAnimCurve(self):
        animCurve=self._animCurveReplaceType_list[self._animCurve]
        return animCurve

    def loading(self):
        self.__loading()

    def setKey(self):
        self._keyFrame_create_func(self._object,self._attr,self._value,self._time,self._inTangentType,self._outTangentType,self._animCurve)