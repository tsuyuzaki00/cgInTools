# -*- coding: iso-8859-15 -*-

import maya.cmds as cmds
from ..library import cTargetMove as ctm

def main():
    obj=cmds.ls(sl=True,fl=True)
    targetSet = ctm.TargetMove()
    targetSet.setTarget(obj[0])
    targetSet.setSource(obj[1])
    targetSet.run()