# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import maya.api.OpenMayaAnim as oma2
import cgInTools as cit
from cgInTools.maya.library import setBaseLB as sb
cit.verReload(sb)

def objsSkin_export_list(self,path,objs):
    pass

def objsSkinPack_export_list(self,path,objs,file="skin"):
    pass

    objs = cmds.ls(sl=True,l=True)
    if len(objs) < 2:
        cmds.warning("At less 2 objects must be selected")
        return None
    else:
        source = objs[0]
        targets = objs[1:]

class CTransferBind():
    def __init__(self,sourceObj,targetObjs):
        self.source = sourceObj
        self.targets = targetObjs

    def run(self):
        normal_targets,cluster_targets = self.geoBindSplit_edit_tuple_list2(self.targets)
        self.copyJointWeights_edit_func(self.source,normal_targets)
        self.copySkinWeights_edit_func(self.source,normal_targets)
        #self.addJointWeights_edit_func(self.source,cluster_targets)
        self.copySkinWeights_edit_func(self.source,cluster_targets)
        
    # オブジェクトにskinClusterがあれば取得する関数
    def geoSkinCluster_query_node(self,obj):
        shape = cmds.listRelatives(obj,c=True,f=True)
        histories = cmds.listHistory(shape[0], pruneDagObjects=True, interestLevel=2)
        try:
            skinCluster_node = cmds.ls(histories, type="skinCluster")[0]
        except IndexError:
            return None
        else:
            return skinCluster_node

    # オブジェクトにバインドされているジョイントを取得する関数
    def geoBindJoints_query_list(self,obj):
        skinCluster = self.geoSkinCluster_query_node(obj)
        influences = cmds.skinCluster(skinCluster, q=True, influence=True)
        if influences is None:
            cmds.error('There is no'+ obj +'of bind joints.')
        return influences

    # clusterがあるかないかを2種類に区別する関数
    def geoBindSplit_edit_tuple_list2(self,targets):
        cluster_meshs = []
        normal_meshs = []
        for target in targets:
            skinCluster_node = self.geoSkinCluster_query_node(target)
            if skinCluster_node == None:
                normal_meshs.append(target)
            elif cmds.nodeType(skinCluster_node) == "skinCluster":
                cluster_meshs.append(target)
            else:
                cmds.warning('There may be history in '+ target +'.')
        return normal_meshs,cluster_meshs

    # ソースのオブジェクトからジョイントを取得して複数のターゲットにバインドする関数
    def copyJointWeights_edit_func(self,source,targets):
        joints = self.geoBindJoints_query_list(source)
        for target in targets:
            target_name = self.clusterRename_edit_obj(target)
            target_part = target_name.split("|") # parent1|child1|child2
            cmds.skinCluster(target,joints,n=target_part[-1],tsb=True)

    # 複数のターゲットにコピースキンウェイトする関数
    def copySkinWeights_edit_func(self,source,targets,sa="closestPoint",ia="closestJoint"):
        source_obj = self.geoSkinCluster_query_node(source)
        for target in targets:
            destination_obj = self.geoSkinCluster_query_node(target)
            cmds.copySkinWeights(ss=source_obj,ds=destination_obj,sa=sa,ia=ia,noMirror=True)
    
    # 複数のジョイントをウェイトに新しく追加する関数
    def addInfluences_edit_func(self,obj,joints):
        skinCluster = self.geoSkinCluster_query_node(obj)
        for joint in joints:
            cmds.skinCluster(skinCluster,ai=joint,e=True,ug=True,dr=4,ps=0,ns=10,lw=True,wt=0)

    # 複数のジョイントをウェイトから除外する関数
    def removeInfluences_edit_func(self,obj,joints):
        skinCluster = self.geoSkinCluster_query_node(obj)
        for joint in joints:
            cmds.skinCluster(skinCluster,ri=joint,e=True)

    # 元々バインドされているジオメトリにジョイントを追加する関数
    def addJointWeights_edit_func(self,source,targets):
        source_joints = self.geoBindJoints_query_list(source)
        for target in targets:
            target_joints = self.geoBindJoints_query_list(target)
            add_joints = set(source_joints) ^ set(target_joints)
            self.addInfluences_edit(target,list(add_joints))

    # ジオメトリと複数のジョイントを選択してバインドする関数
    def renameBindSkin_edit_func(self,geo,joints):
        skc_name=self.clusterRename_edit_obj(geo)
        cmds.skinCluster(geo,joints,n=skc_name,tsb=True)

    # ジオメトリ名を取得してclusterの名前を変更します   
    def clusterRename_edit_obj(self,obj):
        renamers = [
            {"source":"Geo","rename":"Skc"},
            {"source":"geo","rename":"skc"},
            {"source":"cage","rename":"sskc"},
        ]
        for renamer in renamers:
            if renamer["source"] in obj:
                fix_name = obj.replace(renamer["source"],renamer["rename"])
                return fix_name
            

class CopyVertexSkinWeights(sb.SetPair):
    def __init__(self):
        """
        self.sourceNode # string
        self.targetNode # string
        self.sourceAttr # string
        self.targetAttr # string
        self.sourceComponent # int only
        self.targetComponent # int only
        self.sourceParameter # float or string
        self.targetParameter # float or string
        self.sourceJoint # string
        self.targetJoint # string
        """

    def run(self):
        sourceSkc_node=self.getSkc_query_node(self.sourceNode)
        sourceJointID_dict=self.getJointIDAtJoint_query_dict(sourceSkc_node)
        sourceJointID_int=sourceJointID_dict[self.sourceJoint]
        source_MFnSkinCluster=self.replaceSkcNode_query_MFnSkinCluster(sourceSkc_node)
        sourceMesh_MDagPath=self.getMesh_query_MDagPath(self.sourceNode)
        sourceVertex_MObject=self.singleIdComp_query_MObject(self.sourceComponent)

        targetSkc_node=self.getSkc_query_node(self.targetNode)
        targetJointID_dict=self.getJointIDAtJoint_query_dict(targetSkc_node)
        targetJointID_int=targetJointID_dict[self.targetJoint]
        target_MFnSkinCluster=self.replaceSkcNode_query_MFnSkinCluster(targetSkc_node)
        targetMesh_MDagPath=self.getMesh_query_MDagPath(self.targetNode)
        targetVertex_MObject=self.singleIdComp_query_MObject(self.targetComponent)

        # shapes_MDagPath       (MDagPath) - メッシュ
        # vertexComp_MObject   (MObject) - 頂点MObject
        # influence        (int) - 何番目のジョイント
        weightData=source_MFnSkinCluster.getWeights(sourceMesh_MDagPath,sourceVertex_MObject)
        #DagPathのVertexにて何番目のジョイントにウェイトを振るか
        target_MFnSkinCluster.setWeights(targetMesh_MDagPath,targetVertex_MObject,targetJointID_int,weightData[0][sourceJointID_int],normalize=True)

    def querySourceWeights(self):
        sourceSkc_node=self.getSkc_query_node(self.sourceNode)
        source_MFnSkinCluster=self.replaceSkcNode_query_MFnSkinCluster(sourceSkc_node)
        sourceMesh_MDagPath=self.getMesh_query_MDagPath(self.sourceNode)
        sourceVertex_MObject=self.singleIdComp_query_MObject(self.sourceComponent)

        weightData=source_MFnSkinCluster.getWeights(sourceMesh_MDagPath,sourceVertex_MObject)
        weight_list=[self.sourceNode+".vtx["+str(self.sourceComponent)+"]",list(weightData[0])]        
        return weight_list

    def querySourceWeightsDict(self):
        sourceSkc_node=self.getSkc_query_node(self.sourceNode)
        source_MFnSkinCluster=self.replaceSkcNode_query_MFnSkinCluster(sourceSkc_node)
        sourceMesh_MDagPath=self.getMesh_query_MDagPath(self.sourceNode)
        sourceVertex_MObject=self.singleIdComp_query_MObject(self.sourceComponent)
        sourceJointID_dict=self.getJointAtJointID_query_dict(sourceSkc_node)

        weightData=source_MFnSkinCluster.getWeights(sourceMesh_MDagPath,sourceVertex_MObject)
        weight_dict={}
        jointValue_dict={}
        nodeAttr_string=self.sourceNode+".vtx["+str(self.sourceComponent)+"]"
        for num in range(len(list(weightData[0]))):
            add_dict={sourceJointID_dict[num]:weightData[0][num]}
            jointValue_dict.update(add_dict)
        weight_dict[nodeAttr_string]=jointValue_dict
        return weight_dict

    def queryTargetWeights(self):
        targetSkc_node=self.getSkc_query_node(self.targetNode)
        target_MFnSkinCluster=self.replaceSkcNode_query_MFnSkinCluster(targetSkc_node)
        targetMesh_MDagPath=self.getMesh_query_MDagPath(self.targetNode)
        targetVertex_MObject=self.singleIdComp_query_MObject(self.targetComponent)

        weightData=target_MFnSkinCluster.getWeights(targetMesh_MDagPath,targetVertex_MObject)
        weight_list=[self.targetNode+".vtx["+str(self.targetComponent)+"]",list(weightData[0])]        
        return weight_list

    def queryTargetWeightsDict(self):
        targetSkc_node=self.getSkc_query_node(self.targetNode)
        target_MFnSkinCluster=self.replaceSkcNode_query_MFnSkinCluster(targetSkc_node)
        targetMesh_MDagPath=self.getMesh_query_MDagPath(self.targetNode)
        targetVertex_MObject=self.singleIdComp_query_MObject(self.targetComponent)
        targetJointID_dict=self.getJointAtJointID_query_dict(targetSkc_node)

        weightData=target_MFnSkinCluster.getWeights(targetMesh_MDagPath,targetVertex_MObject)
        weight_dict={}
        jointValue_dict={}
        nodeAttr_string=self.targetNode+".vtx["+str(self.targetComponent)+"]"
        for num in range(len(list(weightData[0]))):
            add_dict={targetJointID_dict[num]:weightData[0][num]}
            jointValue_dict.update(add_dict)
        weight_dict[nodeAttr_string]=jointValue_dict
        return weight_dict
        
# private functions
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

# OpenMaya functions
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