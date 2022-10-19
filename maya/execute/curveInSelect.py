# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

def main():
    exSel=cmds.ls(sl=True)[0]
    inSels=cmds.ls(sl=True)[1:]

    for inSel in inSels:
        nextSel=cmds.duplicate(exSel)
        shapes=cmds.listRelatives(nextSel,type="nurbsCurve")
        cmds.rename(shapes,inSel+"Shape")
        cmds.parent(shapes,inSel,r=True,s=True)
        cmds.delete(nextSel)