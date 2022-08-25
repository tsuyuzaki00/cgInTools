# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

from ..library import cBindJoint as SBJ

def main():
    sel = cmds.ls(sl=True)
    _Weights = SBJ.ListBindJoints()
    cluster_string = _Weights.geoSkinCluster_query_node(sel[0])
    curCtx = cmds.currentCtx()
    if(curCtx=='artAttrSkinContext'):
        infJnt = cmds.artAttrSkinPaintCtx(curCtx,q=True,inf=True)
        cmds.skinCluster(cluster_string,e=True,ri=infJnt)