# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

from ..Library import selectBindJoints as sbj; reload(sbj);

def skinClusterRename_edit(obj):
    _weights = sbj.ListBindJoints()
    skinCluster_node = _weights.geoSkinCluster_query(obj)
    skinClusterRename_name = _weights.clusterName_edit(obj)
    cmds.rename(skinCluster_node,skinClusterRename_name)

def main():
    objs = cmds.ls(sl=True)
    for obj in objs:
        skinClusterRename_edit(obj)