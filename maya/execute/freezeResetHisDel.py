# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

def delThree_edit_func():
    sels = cmds.ls(sl=True,dag=True,tr=True)
    for sel in sels:
        unlocks(sel)#Prevention of unlock errors
    for sel in sels:
        cmds.makeIdentity(sel,apply=True,t=True,r=True,s=True,pn=True)#Freeze Transformations
        cmds.makeIdentity(sel,apply=False,t=True,r=True,s=True)#Reset Transformations
        cmds.delete(sel,ch = True)#Delete by Type History
        cmds.select(cl=True)

def unlocks(sel):
    attrs = ["tx","ty","tz","rx","ry","rz","sx","sy","sz","visibility"]
    for attr in attrs:
        cmds.setAttr(sel+"."+attr,l=False)

def main():
    delThree_edit_func()