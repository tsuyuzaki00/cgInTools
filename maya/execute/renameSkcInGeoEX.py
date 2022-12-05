# -*- coding: iso-8859-15 -*-

import maya.cmds as cmds
from ..library import skinLB as sLB

def main():
    objs=cmds.ls(sl=True)
    renameSkc=sLB.CopySkinWeight()
    for obj in objs:
        skc_bool=renameSkc.geoSkinCluster_check_bool(obj)
        if not skc_bool == None:
            cluster_node=renameSkc._geoSkinCluster_query_node(obj)
            fix_str=renameSkc.clusterRename_create_str(obj)
            cmds.rename(cluster_node,fix_str)