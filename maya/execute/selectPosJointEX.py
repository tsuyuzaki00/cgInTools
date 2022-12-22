# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from cgInTools.maya.library import jointLB as jntLB
cit.reloads([jntLB])

def main():
    objs=cmds.ls(sl=True)
    if objs == []:
        jntLB.jointOnly()
        cmds.select(cl=True)
    else :
        for obj in objs:
            trs=cmds.xform(obj,q=True,ws=True,t=True)
            jntLB.jointOnly(p=trs)