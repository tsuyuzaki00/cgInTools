# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

from ..library import cBindJoint as cbj; reload(cbj);
def main():
    objs = cmds.ls(sl=True,l=True)
    if len(objs) < 2:
        cmds.warning("At less 2 objects must be selected")
        return None
    else:
        source = objs[0]
        targets = objs[1:]
    normal_targets,cluster_targets = cbj.geoBindSplit_edit_tuple_list2(targets)
    cbj.copyJointWeights_edit_func(source,normal_targets)
    cbj.copySkinWeights_edit_func(source,normal_targets)
    #cbj.addJointWeights_edit_func(source,cluster_targets)
    cbj.copySkinWeights_edit_func(source,cluster_targets)