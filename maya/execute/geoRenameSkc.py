#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import maya.cmds as cmds
from ..library import selectBindJoints as SBJ;

def main():
    _GeoRenameCluster = SBJ.ListBindJoints()
    sels = cmds.ls(sl = True)
    for sel in sels:
        cluster_node = _GeoRenameCluster.geoSkinCluster_query_node(sel)
        fix_str = _GeoRenameCluster.clusterRename_edit_obj(sel)
        cmds.rename(cluster_node,fix_str)