# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import cgInTools as cit
from cgInTools.maya.library import checkLB as chLB
cit.reloads([chLB])

def main():
    check=chLB.Check()
    objs=cmds.ls(sl=True)
    for obj in objs:
        check.setNode(obj)
        print(check.overlappingUV())
        #cmds.select(check.ngon()["ngon"],add=True)
main()