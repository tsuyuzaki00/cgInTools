# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from ..library import mirrorLB as mLB
cit.reloads([mLB])

def main():
    loc=mLB.MatrixMirror()
    objs=cmds.ls(sl=True)
    for obj in objs:
        targetName=loc.reversedLeftRight_edit_string(obj)
        loc.setSourceNode(obj)
        loc.setTargetNode(targetName)
        loc.translateOnly()