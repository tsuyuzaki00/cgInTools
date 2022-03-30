# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

from ..library import selectBindJoints as SBJ
def main():
    objs = cmds.ls(sl=True,l=True)
    if len(objs) < 2:
        cmds.warning("At less 2 objects must be selected")
        return None
    else:
        source = objs[0]
        targets = objs[1:]
    _Weights = SBJ.ListBindJoints()
    normal_targets,cluster_targets = _Weights.geoBindSplit_edit_tuple_list2(targets)
    _Weights.copyJointWeights_edit_func(source,normal_targets)
    _Weights.copySkinWeights_edit_func(source,normal_targets)
    #_Weights.addJointWeights_edit_func(source,cluster_targets)
    _Weights.copySkinWeights_edit_func(source,cluster_targets)