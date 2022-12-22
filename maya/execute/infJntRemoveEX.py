# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from ..library import skinLB as sLB
cit.reloads([sLB])

def main():
    obj=cmds.ls(sl=True)[0]
    removeJoint=sLB.CopySkinWeight()
    skc_bool=removeJoint.geoSkinCluster_check_bool(obj)
    if skc_bool:
        curCtx=cmds.currentCtx()
        if(curCtx=='artAttrSkinContext'):
            skc_node=removeJoint._geoSkinCluster_query_node(obj)
            infJnt=cmds.artAttrSkinPaintCtx(curCtx,q=True,inf=True)
            cmds.skinCluster(skc_node,e=True,ri=infJnt)
    else:
        cmds.error("No skin cluster in this "+obj+".")