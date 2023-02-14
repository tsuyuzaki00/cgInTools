# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from ..library import skinLB as sLB
cit.reloads([sLB])

def main():
    obj=cmds.ls(sl=True)[0]
    removeJoint=sLB.CopySkinWeight()
    removeJoint.setSourceNode(obj)
    removeJoint.removeInfluenceJoint()