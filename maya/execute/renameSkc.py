# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
from ..library import cSkin as cs

def skinClusterRename_edit(obj):
    _weights = cs.CTransferBind()
    skinCluster_node = _weights.geoSkinCluster_query_node(obj)
    skinClusterRename_name = _weights.clusterRename_edit_obj(obj)
    cmds.rename(skinCluster_node,skinClusterRename_name)

def main():
    objs = cmds.ls(sl=True)
    for obj in objs:
        skinClusterRename_edit(obj)