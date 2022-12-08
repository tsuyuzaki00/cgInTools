# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import maya.api.OpenMayaAnim as oma2
import cgInTools as cit
from . import setBaseLB as sbLB
cit.reloads([sbLB])

def objsSkin_export_list(self,path,objs):
    pass

def objsSkinPack_export_list(self,path,objs,file="skin"):
    pass

class CopySkinWeight(sbLB.BasePair):
    def __init__(self):
        self._sourceNode=""
        self._targetNode=""

    #Single Function
    def geoSkinCluster_check_bool(self,geo):
        shape_list=cmds.listRelatives(geo,c=True,f=True)
        histories=cmds.listHistory(shape_list[0],pruneDagObjects=True,interestLevel=2)
        if not histories == None:
            for historie in histories:
                if cmds.nodeType(historie) == "skinCluster":
                    return True
                else:
                    cmds.error("No skin cluster in this "+geo+".")
        else:
            return False

    def clusterRename_create_str(self,obj):
        __renamers = [
            {"source":"Geo","rename":"Skc"},
            {"source":"geo","rename":"skc"},
            {"source":"cage","rename":"sskc"},
        ]
        for __renamer in __renamers:
            if __renamer["source"] in obj:
                fixName_str=obj.replace(__renamer["source"],__renamer["rename"])
                return fixName_str    
        fixName_str=obj+"_skc"
        return fixName_str

    #Multi Function
    def _geoSkinCluster_query_node(self,geo):
        skc_bool=self.geoSkinCluster_check_bool(geo)
        if skc_bool:
            shape_list=cmds.listRelatives(geo,c=True,f=True)
            histories=cmds.listHistory(shape_list[0],pruneDagObjects=True,interestLevel=2)
            skinCluster_node=cmds.ls(histories,type="skinCluster")[0]
            return skinCluster_node

    def _geoBindJoints_check_bool(self,geo):
        skc_node=self._geoSkinCluster_query_node(geo)
        influences=cmds.skinCluster(skc_node,q=True,influence=True)
        if not influences is None:
            return True
        else:
            return False
        
    def _geoBindJoints_query_joints(self,geo):
        influences_bool=self._geoBindJoints_check_bool(geo)
        if influences_bool:
            skc_node=self._geoSkinCluster_query_node(geo)
            joints=cmds.skinCluster(skc_node,q=True,influence=True)
            return joints
        else:
            cmds.error('There is no'+ geo +'of bind joints.')

    def _jointDifference_query_joints(self,geoSource,geoTarget):
        new_targetJoints=[]
        sourceJoints=self._geoBindJoints_query_joints(geoSource)
        targetJoints=self._geoBindJoints_query_joints(geoTarget)
        for sourceJoint in sourceJoints:
            if sourceJoint in targetJoints:
                new_targetJoints.append(sourceJoint)
        diffJoints=set(new_targetJoints) ^ set(sourceJoints)
        return diffJoints
        
    def _copyBindJoint_edit_func(self,geoSource,geoTarget):
        joints=self._geoBindJoints_query_joints(geoSource)
        skcName_str=self.clusterRename_create_str(geoTarget)
        skcPart_str=skcName_str.split("|") # parent1|child1|child2
        cmds.skinCluster(geoTarget,joints,n=skcPart_str[-1],tsb=True)

    def _copySkinWeights_edit_func(self,geoSource,geoTarget,sa="closestPoint",ia="closestJoint"):
        sourceSkc_node=self._geoSkinCluster_query_node(geoSource)
        targteSkc_node=self._geoSkinCluster_query_node(geoTarget)
        cmds.copySkinWeights(ss=sourceSkc_node,ds=targteSkc_node,sa=sa,ia=ia,noMirror=True)
    
    def _addInfluences_edit_func(self,geo,joints):
        skc_node=self._geoSkinCluster_query_node(geo)
        for joint in joints:
            cmds.skinCluster(skc_node,ai=joint,e=True,ug=False,dr=4,ps=0,ns=10,lw=True,wt=0)

    def _removeInfluences_edit_func(self,geo,joints):
        skc_node=self._geoSkinCluster_query_node(geo)
        for joint in joints:
            cmds.skinCluster(skc_node,ri=joint,e=True)

    #Public Function
    def copyBindAndSkinWeights(self):
        targetSkc_bool=self.geoSkinCluster_check_bool(self._targetNode)
        if targetSkc_bool:
            diffJoints=self._jointDifference_query_joints(self._sourceNode,self._targetNode)
            if not diffJoints == None:
                self._addInfluences_edit_func(self._targetNode,diffJoints)
            self._copySkinWeights_edit_func(self._sourceNode,self._targetNode)
        else:
            self._copyBindJoint_edit_func(self._sourceNode,self._targetNode)
            self._copySkinWeights_edit_func(self._sourceNode,self._targetNode)

    def targetRemoveJoints(self):
        targetSkc_bool=self.geoSkinCluster_check_bool(self._targetNode)
        if targetSkc_bool:
            diffJoints=self._jointDifference_query_joints(self._targetNode,self._sourceNode)
            self._removeInfluences_edit_func(self._targetNode,diffJoints)
        else:
            cmds.error('There is no'+ geo +'of bind joints.')

class CopyVertexSkinWeights(sbLB.BasePair):
    def __init__(self):
        self._sourceNode="" # string
        self._targetNode="" # string
        self._sourceAttr="" # string
        self._targetAttr="" # string
        self._sourceComponent=0 # int only
        self._targetComponent=0 # int only
        self._sourceValue="" # float or string
        self._targetValue="" # float or string
        self._sourceJoint="" # string
        self._targetJoint="" # string

    def run(self):
        sourceSkc_node=self.getSkc_query_node(self._sourceNode)
        sourceJointID_dict=self.getJointIDAtJoint_query_dict(sourceSkc_node)
        sourceJointID_int=sourceJointID_dict[self._sourceJoint]
        source_MFnSkinCluster=self.replaceSkcNode_query_MFnSkinCluster(sourceSkc_node)
        sourceMesh_MDagPath=self.getMesh_query_MDagPath(self._sourceNode)
        sourceVertex_MObject=self.singleIdComp_query_MObject(self._sourceComponent)

        targetSkc_node=self.getSkc_query_node(self._targetNode)
        targetJointID_dict=self.getJointIDAtJoint_query_dict(targetSkc_node)
        targetJointID_int=targetJointID_dict[self._targetJoint]
        target_MFnSkinCluster=self.replaceSkcNode_query_MFnSkinCluster(targetSkc_node)
        targetMesh_MDagPath=self.getMesh_query_MDagPath(self._targetNode)
        targetVertex_MObject=self.singleIdComp_query_MObject(self._targetComponent)

        # shapes_MDagPath       (MDagPath) - メッシュ
        # vertexComp_MObject   (MObject) - 頂点MObject
        # influence        (int) - 何番目のジョイント
        weightData=source_MFnSkinCluster.getWeights(sourceMesh_MDagPath,sourceVertex_MObject)
        #DagPathのVertexにて何番目のジョイントにウェイトを振るか
        target_MFnSkinCluster.setWeights(targetMesh_MDagPath,targetVertex_MObject,targetJointID_int,weightData[0][sourceJointID_int],normalize=True)

    def querySourceWeights(self):
        sourceSkc_node=self.getSkc_query_node(self._sourceNode)
        source_MFnSkinCluster=self.replaceSkcNode_query_MFnSkinCluster(sourceSkc_node)
        sourceMesh_MDagPath=self.getMesh_query_MDagPath(self._sourceNode)
        sourceVertex_MObject=self.singleIdComp_query_MObject(self._sourceComponent)

        weightData=source_MFnSkinCluster.getWeights(sourceMesh_MDagPath,sourceVertex_MObject)
        weight_list=[self._sourceNode+".vtx["+str(self._sourceComponent)+"]",list(weightData[0])]        
        return weight_list

    def querySourceWeightsDict(self):
        sourceSkc_node=self.getSkc_query_node(self._sourceNode)
        source_MFnSkinCluster=self.replaceSkcNode_query_MFnSkinCluster(sourceSkc_node)
        sourceMesh_MDagPath=self.getMesh_query_MDagPath(self._sourceNode)
        sourceVertex_MObject=self.singleIdComp_query_MObject(self._sourceComponent)
        sourceJointID_dict=self.getJointAtJointID_query_dict(sourceSkc_node)

        weightData=source_MFnSkinCluster.getWeights(sourceMesh_MDagPath,sourceVertex_MObject)
        weight_dict={}
        jointValue_dict={}
        nodeAttr_string=self._sourceNode+".vtx["+str(self._sourceComponent)+"]"
        for num in range(len(list(weightData[0]))):
            add_dict={sourceJointID_dict[num]:weightData[0][num]}
            jointValue_dict.update(add_dict)
        weight_dict[nodeAttr_string]=jointValue_dict
        return weight_dict

    def queryTargetWeights(self):
        targetSkc_node=self.getSkc_query_node(self._targetNode)
        target_MFnSkinCluster=self.replaceSkcNode_query_MFnSkinCluster(targetSkc_node)
        targetMesh_MDagPath=self.getMesh_query_MDagPath(self._targetNode)
        targetVertex_MObject=self.singleIdComp_query_MObject(self._targetComponent)

        weightData=target_MFnSkinCluster.getWeights(targetMesh_MDagPath,targetVertex_MObject)
        weight_list=[self._targetNode+".vtx["+str(self._targetComponent)+"]",list(weightData[0])]        
        return weight_list

    def queryTargetWeightsDict(self):
        targetSkc_node=self.getSkc_query_node(self._targetNode)
        target_MFnSkinCluster=self.replaceSkcNode_query_MFnSkinCluster(targetSkc_node)
        targetMesh_MDagPath=self.getMesh_query_MDagPath(self._targetNode)
        targetVertex_MObject=self.singleIdComp_query_MObject(self._targetComponent)
        targetJointID_dict=self.getJointAtJointID_query_dict(targetSkc_node)

        weightData=target_MFnSkinCluster.getWeights(targetMesh_MDagPath,targetVertex_MObject)
        weight_dict={}
        jointValue_dict={}
        nodeAttr_string=self._targetNode+".vtx["+str(self._targetComponent)+"]"
        for num in range(len(list(weightData[0]))):
            add_dict={targetJointID_dict[num]:weightData[0][num]}
            jointValue_dict.update(add_dict)
        weight_dict[nodeAttr_string]=jointValue_dict
        return weight_dict
        
    #Single Functions
    def getSkc_query_node(self,obj):
        nodeList_MSelectionList=om2.MGlobal.getSelectionListByName(obj)
        sourceMesh_MDagPath=nodeList_MSelectionList.getDagPath(0)
        sourceMesh_MDagPath.extendToShape()
        shapes_MObject=sourceMesh_MDagPath.node()
        mesh_MFnDependencyNode=om2.MFnDependencyNode(shapes_MObject)
        inMesh_MPlug=mesh_MFnDependencyNode.findPlug("inMesh",False)
        skc_MPlug=inMesh_MPlug.connectedTo(True,False)[0]
        skc_nodeAttr=skc_MPlug.name()
        skc_node=skc_nodeAttr.split(".")[0]
        return skc_node

    def getJointIDAtJoint_query_dict(self,skc_node):
        MFnSkinCluster=self.replaceSkcNode_query_MFnSkinCluster(skc_node)
        joint_MDagPathArray=MFnSkinCluster.influenceObjects()
        jointID_dict={}
        for num in range(len(joint_MDagPathArray)):
            jointID_dict[str(joint_MDagPathArray[num])]=num
        return jointID_dict

    def getJointAtJointID_query_dict(self,skc_node):
        MFnSkinCluster=self.replaceSkcNode_query_MFnSkinCluster(skc_node)
        joint_MDagPathArray=MFnSkinCluster.influenceObjects()
        jointID_dict={}
        for num in range(len(joint_MDagPathArray)):
            jointID_dict[num]=str(joint_MDagPathArray[num])
        return jointID_dict

    #OpenMaya Functions
    def replaceSkcNode_query_MFnSkinCluster(self,skc_node):
        skcList_MSelectionList=om2.MGlobal.getSelectionListByName(skc_node)
        skc_MObject=skcList_MSelectionList.getDependNode(0)
        skc_MFnSkinCluster=oma2.MFnSkinCluster(skc_MObject)
        return skc_MFnSkinCluster

    def getMesh_query_MDagPath(self,obj):
        nodeList_MSelectionList=om2.MGlobal.getSelectionListByName(obj)
        sourceMesh_MDagPath=nodeList_MSelectionList.getDagPath(0)
        sourceMesh_MDagPath.extendToShape()
        return sourceMesh_MDagPath
    
    def singleIdComp_query_MObject(self,vertexID):
        singleIdComp_MFnSingleIndexedComponent=om2.MFnSingleIndexedComponent()
        vertexComp_MObject=singleIdComp_MFnSingleIndexedComponent.create(om2.MFn.kMeshVertComponent)
        singleIdComp_MFnSingleIndexedComponent.addElements([vertexID])
        return vertexComp_MObject

