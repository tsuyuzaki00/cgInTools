# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import cgInTools as cit
from cgInTools.maya.library import cJoint as cj
cit.reloads([cj])

def main():
    objs=cmds.ls(sl=True)
    if objs == []:
        cj.jointOnly()
        cmds.select(cl=True)
    else :
        for obj in objs:
            trs=cmds.xform(obj,q=True,ws=True,t=True)
            cj.jointOnly(p=trs)