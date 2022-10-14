# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
from cgInTools.maya.library import cMirror as ps; reload(ps);

loc=ps.MatrixMirror()
objs=cmds.ls(sl=True)
for obj in objs:
    targetName=obj.replace("_L","_R")
    loc.setSourceNode(obj)
    loc.setTargetNode(targetName)
    loc.translateOnly()