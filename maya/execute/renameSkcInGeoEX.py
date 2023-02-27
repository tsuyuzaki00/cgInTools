# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from ..library import skinLB as sLB
cit.reloads([sLB])

def main():
    objs=cmds.ls(sl=True)
    renameSkc=sLB.CopySkinWeight()
    for obj in objs:
        cluster_node=renameSkc.geoSkinCluster_query_str(obj)
        fix_str=renameSkc.clusterRename_create_str(obj)
        cmds.rename(cluster_node,fix_str)