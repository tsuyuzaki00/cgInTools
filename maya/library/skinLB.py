# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import maya.api.OpenMayaAnim as oma2
import cgInTools as cit
from . import setBaseLB as sbLB
from . import objectLB as oLB
cit.reloads([sbLB,oLB])


class CopySkinWeight(sbLB.BasePair):
    def __init__(self):
        self._sourceNode=""
        self._targetNode=""

    #Single Function
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

    def geoSkinCluster_query_str(self,geo):
        shape_list=cmds.listRelatives(geo,c=True,f=True)
        histories=cmds.listHistory(shape_list[0],pruneDagObjects=True,interestLevel=2)
        skinCluster_node=cmds.ls(histories,type="skinCluster")
        if not skinCluster_node == []:
            return skinCluster_node[0]
        else:
            return None

    def skcBindJoints_query_list(self,skc):
        joints=cmds.skinCluster(skc,q=True,influence=True)
        if not joints is None:
            return joints
        else:
            return None

    def jointDifference_query_joints(self,sourceJoints,targetJoints):
        new_targetJoints=[]
        for sourceJoint in sourceJoints:
            if sourceJoint in targetJoints:
                new_targetJoints.append(sourceJoint)
        diffJoints=set(new_targetJoints) ^ set(sourceJoints)
        return diffJoints

    #Multi Function
    def _jointDifference_query_joints(self,geoSource,geoTarget):
        skcSource=self.geoSkinCluster_query_str(geoSource)
        skcTarget=self.geoSkinCluster_query_str(geoTarget)
        if skcSource is None or skcTarget is None:
            cmds.error("No skin cluster in this "+skcSource+" or "+skcTarget+".")
        sourceJoints=self.skcBindJoints_query_list(skcSource)
        targetJoints=self.skcBindJoints_query_list(skcTarget)

        diffJoints=self.jointDifference_query_joints(sourceJoints,targetJoints)
        return diffJoints
        
    def _copyBindJoint_edit_func(self,geoSource,geoTarget):
        skcSource=self.geoSkinCluster_query_str(geoSource)
        if skcSource is None:
            cmds.error("No skin cluster in this "+skcSource+".")
        sourceJoints=self.skcBindJoints_query_list(skcSource)
        skcName_str=self.clusterRename_create_str(geoTarget)
        skcPart_str=skcName_str.split("|") # parent1|child1|child2
        cmds.skinCluster(geoTarget,sourceJoints,n=skcPart_str[-1],tsb=True)

    def _copySkinWeights_edit_func(self,geoSource,geoTarget,sa="closestPoint",ia="closestJoint"):
        skcSource=self.geoSkinCluster_query_str(geoSource)
        if skcSource is None:
            cmds.error("No skin cluster in this "+skcSource+".")
        skcTarget=self.geoSkinCluster_query_str(geoTarget)
        if skcSource is None:
            cmds.error("No skin cluster in this "+skcTarget+".")
        cmds.copySkinWeights(ss=skcSource,ds=skcTarget,sa=sa,ia=ia,noMirror=True)
    
    def _addInfluences_edit_func(self,geo,joints):
        skc=self.geoSkinCluster_query_str(geo)
        if skc is None:
            cmds.error("No skin cluster in this "+skc+".")
        for joint in joints:
            cmds.skinCluster(skc,ai=joint,e=True,ug=False,dr=4,ps=0,ns=10,lw=True,wt=0)

    def _removeInfluences_edit_func(self,geo,joints):
        skc=self.geoSkinCluster_query_str(geo)
        if skc is None:
            cmds.error("No skin cluster in this "+skc+".")
        for joint in joints:
            cmds.skinCluster(skc,ri=joint,e=True)

    #Public Function
    def copyBind(self):
        self._copyBindJoint_edit_func(self._sourceNode,self._targetNode)
        self._copySkinWeights_edit_func(self._sourceNode,self._targetNode)

    def copySkinWeights(self):
        diffJoints=self._jointDifference_query_joints(self._sourceNode,self._targetNode)
        if not diffJoints == None:
            self._addInfluences_edit_func(self._targetNode,diffJoints)
        self._copySkinWeights_edit_func(self._sourceNode,self._targetNode)

    def targetRemoveJoints(self):
        diffJoints=self._jointDifference_query_joints(self._targetNode,self._sourceNode)
        self._removeInfluences_edit_func(self._targetNode,diffJoints)

    def removeInfluenceJoint(self):
        curCtx=cmds.currentCtx()
        if(curCtx=='artAttrSkinContext'):
            infJnt=cmds.artAttrSkinPaintCtx(curCtx,q=True,inf=True)
            self._removeInfluences_edit_func(self._sourceNode,[infJnt])


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

class SkinWeightByJoint():
    def __init__(self):
        super().__init__()
        self._weights=[]
    
    #Single Function
    def addWeights_create_JointWeights(self,joint,geo):
        getSkc=oLB.JointWeight(joint)
        getSkc.setSubject(geo)
        vertex_int=cmds.polyEvaluate(geo,v=1)

        valueVertex_lists=[]
        value_list=[]
        for num in range(vertex_int):
            vertex=geo+".vtx["+str(num)+"]"
            value=cmds.skinPercent(getSkc.getSkinClusters()[0],vertex,q=True,transform=getSkc.getObject())
            value_list.append(value)
            valueVertex_lists.append([value,vertex])  
        
        value_list=list(set(value_list))
        #value_list.remove(1.0)
        value_list.remove(0.0)

        group_dict={}
        for value in value_list:
            group_dict[value]=[]

        for valueVertex_list in valueVertex_lists:
            if valueVertex_list[0] in value_list:
                group_dict[valueVertex_list[0]].append(valueVertex_list[1])

        for value,vertexs in group_dict.items():
            weight=oLB.JointWeight(joint)
            weight.setSubject(geo)
            weight.setUseJoint(True)
            weight.setValue(value)
            weight.setVertexs(vertexs)
            self._weights.append(weight)
        return self._weights

    def replaceDictWithWeights_query_JointWeights(self,read):
        for weight in read["weights"]:
            joint=oLB.JointWeight(weight["object"])
            joint.setSubject(weight["subject"])
            joint.setUseJoint(weight["use"])
            joint.setValue(weight["value"])
            joint.setVertexs(weight["vertexs"])
            self._weights.append(joint)
        return self._weights

    def replaceWeightsWithDict_create_dict(self,weights):
        weight_list=[]
        
        return write_dict

    def useSkinCluster_check_bool(self,weight):
        if not weight.getSkinClusters() is None:
            return True
        else:
            return False
    
    #Multi Function
    def _weightUnLock_edit_weights(self,weight):
        skinCluster_bool=self.useSkinCluster_check_bool(weight)
        if skinCluster_bool:
            cmds.setAttr(weight.getObject()+".liw",0)
        else:
            cmds.error(weight.getSubject()+" is not skin bind")

    #Public Function
    def setWeights(self,variable):
        self._weights=variable
        return self._weights
    def getWeights(self):
        return self._weights

    def run(self):
        for weight in  self._weights:
            self._weightUnLock_edit_weights(weight)
        for weight in self._weights:
            if not weight.getUseJoint() == True:
                return 0
            else:
                cmds.skinPercent(weight.getSkinClusters(),weight.getVertexs(),transformValue=[(weight.getObject(),weight.getValue())],nrm=True)

    def importWeights(self):
        self._readDict=super().read()
        self._weights=self.replaceDictWithWeights_query_list(self._readDict)
        return self._weights

    def exportWeights(self):
        self._writeDict={"weights":self._weights}
        super().write()