# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from ..library import mirrorLB as mLB
cit.reloads([mLB])

def main():
    selMirrorX=mLB.MatrixMirror()
    objs=cmds.ls(sl=True)
    selMirrorX.setSourceNode(objs[0])
    selMirrorX.setTargetNode(objs[1])
    selMirrorX.translateOnly()