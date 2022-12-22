# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from ..library import skinLB as sLB
cit.reloads([sLB])

def main():
    objs=cmds.ls(sl=True,l=True)
    if len(objs) < 2:
        cmds.warning("At less 2 objects must be selected")
        return None
    else:
        source=objs[0]
        targets=objs[1:]

    copy=sLB.CopySkinWeight()
    copy.setSourceNode(source)
    for target in targets:
        copy.setTargetNode(target)
        copy.copyBindAndSkinWeights()