# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

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