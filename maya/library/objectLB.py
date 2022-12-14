# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

transMFn_list=[
    110,# kTransform
    121,# kJoint
]

shapeMFn_list=[
    296,# kMesh
    267,# kNurbsCurve
    294,# kNurbsSurface
    250,# kCamera
    281,# kLocator
    308,# kDirectionalLight
    305,# kAreaLight
    303,# kAmbientLight
]

nodeTypeToMFn_dict={
    "skinCluster":686 # kDagPose
}

class TrsObject(object):
    def __init__(self,obj):
        self._fullPath_bool=False
        self._object=obj
        self._objectType=cmds.nodeType(self._object)
        self._shape_list=self.childs_query_list(self._object,self._fullPath_bool,shapeMFn_list)
        self._shapeType_list=self.nodeTypes_query_list(self._shape_list)
        
        self._parent_str=self.parent_query_str(self._object,self._fullPath_bool)
        self._child_list=self.childs_query_list(self._object,self._fullPath_bool,transMFn_list)
        
        self._subject=None

    def __loading(self):
        self._objectType=cmds.nodeType(self._object)
        self._shape_list=self.childs_query_list(self._object,self._fullPath_bool,shapeMFn_list)
        self._shapeType_list=self.nodeTypes_query_list(self._shape_list)
        self._parent_str=self.parent_query_str(self._object,fullPath=self._fullPath_bool)
        self._child_list=self.childs_query_list(self._object,self._fullPath_bool,transMFn_list)

        self._subjectType=cmds.nodeType(self._subject)
        self._subShape_list=self.childs_query_list(self._subject,self._fullPath_bool,shapeMFn_list)
        self._subShapeType_list=self.nodeTypes_query_list(self._shape_list)
        self._subParent_str=self.parent_query_str(self._subject,fullPath=self._fullPath_bool)
        self._subChild_list=self.childs_query_list(self._subject,self._fullPath_bool,transMFn_list)

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

    def nodeTypeToMFnConverter_query_int(self,nodeType,converter=nodeTypeToMFn_dict):
        return converter[nodeType]

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

    def getShapes(self):
        self.__loading()
        return self._shape_list
    def getShapeTypes(self):
        self.__loading()
        return self._shapeType_list

    def getParent(self):
        self.__loading()
        return self._parent_str

    def getChilds(self):
        self.__loading()
        return self._child_list

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
        self._vertexs=[]
        self._value=0

    def __loading(self):
        super().loading()
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

def sample():
    geo="test_geo"
    objs=cmds.ls(sl=True)
    for obj in objs:
        test=JointWeight(obj)
        test.setSubject(geo)
        print(test.getParent())
        print(test.getChilds())
        print(test.getSubShapes())
        print(test.getSkinClusters())

#sample()