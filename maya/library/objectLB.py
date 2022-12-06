# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

class TrsObject():
    def __init__(self,obj):
        self._object=obj
        self._fullPath=False
        self._parent_str=self.parent_query_str(self._object,self._fullPath)
        self._child_list=self._childObjs_query_list(self._object,self._fullPath)
    
    #Single Function
    def parent_query_str(self,node,fullPath=False):
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

    def childs_query_list(self,node,fullPath=False,childFn_list=[]):
        node_MSelectionList=om2.MSelectionList().add(node)
        node_MDagPath=node_MSelectionList.getDagPath(0)
        node_MFnDagNode=om2.MFnDagNode(node_MDagPath)
        childs=[]
        for num in range(node_MFnDagNode.childCount()):
            child_MObject=node_MFnDagNode.child(num)
            #print(child_MObject.apiType())
            if child_MObject.apiType() in childFn_list:
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

    def findConnect_query_list(self,node,source=True,target=True,type=""):
        nodeTypeFn_dict={
            "skinCluster":686
        }
        findConnectedTo_list=[]
        node_MSelectionList=om2.MSelectionList().add(node)
        node_MObject=node_MSelectionList.getDependNode(0)
        node_MFnDagNode=om2.MFnDagNode(node_MObject)
        connections_MPlugArray=node_MFnDagNode.getConnections()
        for connection_MPlug in connections_MPlugArray:
            targets_MPlugArray=connection_MPlug.connectedTo(source,target)
            for target_MPlug in targets_MPlugArray:
                target_MObject=target_MPlug.node()
                if target_MObject.hasFn(nodeTypeFn_dict[type]):
                    skc_MFnDependencyNode=om2.MFnDependencyNode(target_MObject)
                    findConnectedTo_list.append(skc_MFnDependencyNode.name())
        findNodes=list(set(findConnectedTo_list))
        if findNodes == []:
            return None
        else:
            return findNodes

    #Multi Function
    def _childObjs_query_list(self,node,fullPath):
        childFn_list=[
            110,# kTransform
            121,# kJoint
        ]
        childs=self.childs_query_list(node,fullPath,childFn_list)
        return childs
    
    #Public Function
    def setObject(self,variable):
        self._object=variable
        return self._object
    def getObject(self):
        return self._object

    def setFullPathSwitch(self,variable):
        self._fullPath=variable
        return self._fullPath
    def getFullPathSwitch(self):
        return self._fullPath

    def getParent(self):
        return self._parent_str
    
    def getChilds(self):
        return self._child_list

class Mesh(TrsObject):
    def __init__(self,obj):
        self._object=obj
        self._fullPath=False
        self._parent_str=self.parent_query_str(self._object,self._fullPath)
        self._child_list=self._childObjs_query_list(self._object,self._fullPath)
        self._shape_list=self._childShapes_query_list(self._object,self._fullPath)

    #Private Function
    def _childShapes_query_list(self,node,fullPath):
        childFn_list=[
            296,# kMesh
            267,# kNurbsCurve
            294,# kNurbsSurface
            250,# kCamera
            281,# kLocator
            308,# kDirectionalLight
            305,# kAreaLight
            303,# kAmbientLight
        ]
        childs=self.childs_query_list(node,fullPath,childFn_list)
        return childs

    #Public Function
    def getShapes(self):
        return self._shape_list

class JointWeight(TrsObject):
    def __init__(self,obj):
        self._object=obj
        self._fullPath=False
        self._useJoint=True
        self._vertexsValue_dicts=[]#[{"vertexs":[],"value":0},{"vertexs":["","",...],"value":0}]
        
        self._parent_str=self.parent_query_str(self._object,fullPath=self._fullPath)
        self._child_list=self._childObjs_query_list(self._object,fullPath=self._fullPath)
        self._skinCluster_list=self.findConnect_query_list(self._object,type="skinCluster")

    def __loading(self):
        self._parent_str=self.parent_query_str(self._object,fullPath=self._fullPath)
        self._child_list=self._childObjs_query_list(self._object,fullPath=self._fullPath)
        self._skinCluster_list=self.findConnect_query_list(self._object,type="skinCluster")
    
    #Public Function
    def setVertexsValueDict(self,variable):
        self._vertexsValue_dicts=[variable]
        return self._vertexsValue_dicts
    def addVertexsValueDict(self,variable):
        self._vertexsValue_dicts.append(variable)
        return self._vertexsValue_dicts
    def getVertexsValueDicts(self):
        return self._vertexsValue_dicts

    def setUseJoint(self,variable):
        self._useJoint=variable
        return self._useJoint
    def getUseJoint(self):
        return self._useJoint

    def getParent(self):
        self.__loading()
        return self._parent_str
    
    def getChilds(self):
        self.__loading()
        return self._child_list

    def getSkinClusters(self):
        self.__loading()
        return self._skinCluster_list
    
    def loading(self):
        self.__loading()
