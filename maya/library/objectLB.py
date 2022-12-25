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

    def __loading(self):
        super(JointWeight,self).loading()
        mFn_int=self.nodeTypeToMFnConverter_query_int("skinCluster")
        self._skinCluster_list=self.findConnect_query_list(self._subShape_list[0],mFnID=mFn_int)
    
    #Public Function
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
        self._normal_matrix=self.matrix_query_dict(self._object)["normal"]
        self._world_matrix=self.matrix_query_dict(self._object)["world"]
        self._parent_matrix=self.matrix_query_dict(self._object)["parent"]
        self._time=oma2.MAnimControl.currentTime()
        self._transKey_bool=False
        self._rotateKey_bool=False
        self._scaleKey_bool=False
        self._attrKey_bool=False
        self._attrValue_dicts=[]# {"shape":"","attr":"","value":0}

    def __loading(self):
        self._normal_matrix=self.matrix_query_dict(self._object)["normal"]
        self._world_matrix=self.matrix_query_dict(self._object)["world"]
        self._parent_matrix=self.matrix_query_dict(self._object)["parent"]

    #Single Function
    def matrix_query_dict(self,node):
        if node == None:
            return None
        node_MSelectionList=om2.MSelectionList().add(node)
        node_MDagPath=node_MSelectionList.getDagPath(0)
        normal_MMatrix=om2.MFnDagNode(node_MDagPath).transformationMatrix()
        world_MMatrix=node_MDagPath.inclusiveMatrix()
        parent_MMatrix=node_MDagPath.exclusiveMatrix()
        matrix_dict={"normal":normal_MMatrix,"world":world_MMatrix,"parent":parent_MMatrix}
        return matrix_dict

    def attrValueDict_edit_func(self,setAttr_dicts):
        if not setAttr_dicts == [] or not setAttr_dicts == None:
            for setAttr_dict in setAttr_dicts:
                cmds.setAttr(setAttr_dict["shape"]+"."+setAttr_dict["attr"],setAttr_dict["value"])

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
        if not self._attrValue_dicts == [] or not self._attrValue_dicts == None:
            if self._setAttrKey_bool:
                for _attrValue_dict in self._attrValue_dicts:
                    cmds.setKeyframe(_attrValue_dict["shape"],at=_attrValue_dict["attr"],v=_attrValue_dict["value"])

    #Public Function
    def setRunMatrix(self,variable):
        self._runMatrix_str=variable
        return self._runMatrix_str
    def getRunMatrix(self):
        return self._runMatrix_str

    def setNormalMatrix(self,variable):
        self._normal_matrix=variable
        return self._normal_matrix
    def getNormalMatrix(self):
        return self._normal_matrix
    
    def setWorldMatrix(self,variable):
        self._world_matrix=variable
        return self._world_matrix
    def getWorldMatrix(self):
        return self._world_matrix
    
    def setParentMatrix(self,variable):
        self._parent_matrix=variable
        return self._parent_matrix
    def getParentMatrix(self):
        return self._parent_matrix

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
        self._attrKey_bool=variable
        return self._attrKey_bool
    def getAttrKeyBool(self):
        return self._attrKey_bool

    def setAttrValueDict(self,variable):
        self._attrValue_dicts=[variable]
        return self._attrValue_dicts
    def addAttrValueDict(self,variable):
        self._attrValue_dicts.append(variable)
        return self._attrValue_dicts
    def getAttrValueDicts(self):
        return self._attrValue_dicts

    def loading(self):
        self.__loading()

    def runMovement(self):
        if self._runMatrix_str == "normal":
            cmds.xform(self._object,m=self._normal_matrix)
        elif self._runMatrix_str == "world":
            cmds.xform(self._object,m=self._world_matrix)
        elif self._runMatrix_str == "parent":
            cmds.xform(self._object,m=self._parent_matrix)
        else:
            cmds.error('please setRunMatrix with the strings "normal" or "world" or "parent".')
        if not self._attrValue_dicts == [] or not self._attrValue_dicts == None:
            self.attrValueDict_edit_func(self._attrValue_dicts)

    def normalMovement(self):
        cmds.xform(self._object,m=self._normal_matrix)
        if not self._attrValue_dicts == [] or not self._attrValue_dicts == None:
            self.setAttrDict_edit_func(self._attrValue_dicts)

    def worldMovement(self):
        cmds.xform(self._object,m=self._world_matrix)
        if not self._attrValue_dicts == [] or not self._attrValue_dicts == None:
            self.setAttrDict_edit_func(self._attrValue_dicts)
    
    def parentMovement(self):
        cmds.xform(self._object,m=self._parent_matrix)
        if not self._attrValue_dicts == [] or not self._attrValue_dicts == None:
            self.setAttrDict_edit_func(self._attrValue_dicts)

class KeyObject(TrsObject):
    def __init__(self,obj):
        super(KeyObject,self).__init__(obj)
        self._time=0
        self._attr=""
        self._value=0
        self._inAngle=""
        self._outAngle=""
        self._inType=""
        self._outType=""

    def __loading(self):
        self._value=cmds.getAttr(self._object+"."+self._attr)
        self._inAngle=cmds.keyTangent(self._object,q=True,at=self._attr,t=(self._time,self._time),ia=True)
        self._outAngle=cmds.keyTangent(self._object,q=True,at=self._attr,t=(self._time,self._time),oa=True)
        self._inType=cmds.keyTangent(self._object,q=True,at=self._attr,t=(self._time,self._time),itt=True)
        self._outType=cmds.keyTangent(self._object,q=True,at=self._attr,t=(self._time,self._time),ott=True)

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
    def setCurrentValue(self):
        self._value=cmds.getAttr(self._object+"."+self._attr)
        return self._value
    def getValue(self):
        return self._value
    
    def setInAngle(self,variable):
        self._inAngle=variable
        return self._inAngle
    def setCurrentInAngle(self):
        self._inAngle=cmds.keyTangent(self._object,q=True,at=self._attr,t=(self._time,self._time),ia=True)
        return self._inAngle
    def getInAngle(self):
        return self._inAngle
    
    def setOutAngle(self,variable):
        self._outAngle=variable
        return self._outAngle
    def setCurrentOutAngle(self):
        self._outAngle=cmds.keyTangent(self._object,q=True,at=self._attr,t=(self._time,self._time),oa=True)
        return self._outAngle
    def getOutAngle(self):
        return self._outAngle

    def setInType(self,variable):
        self._inType=variable
        return self._inType
    def setCurrentInType(self):
        self._inType=cmds.keyTangent(self._object,q=True,at=self._attr,t=(self._time,self._time),itt=True)
        return self._inType
    def getInType(self):
        return self._inType
    
    def setOutType(self,variable):
        self._outType=variable
        return self._outType
    def setCurrentOutType(self):
        self._outType=cmds.keyTangent(self._object,q=True,at=self._attr,t=(self._time,self._time),ott=True)
        return self._outType
    def getOutType(self):
        return self._outType