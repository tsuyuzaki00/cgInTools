# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

def main():
    sels = cmds.ls(sl = True)
    for sel in sels:
        unlocks(sel)
        cmds.makeIdentity(sel,apply = True, t = 1, r = 1, s = 1, pn = 1)
        cmds.makeIdentity(sel,apply = False, t = 1, r = 1, s = 1)
        cmds.delete(sel,ch = True)

def unlocks(sel):
    attrs = ["tx","ty","tz","rx","ry","rz","sx","sy","sz","visibility"]
    for attr in attrs:
        cmds.setAttr(sel+"."+attr,l=False)