# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import cgInTools as cit
from ..library import cMirror as cm
cit.verReload(cm)

def main():
    selMirrorX=cm.MatrixMirror()
    objs=cmds.ls(sl=True)
    selMirrorX.setSourceNode(objs[0])
    selMirrorX.setTargetNode(objs[1])
    selMirrorX.translateOnly()