# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

def delThree_edit_func():
    sels = cmds.ls(sl=True,dag=True,tr=True)
    for sel in sels:
        unlocks_edit_func(sel)#Prevention of unlock errors
    for sel in sels:
        cmds.makeIdentity(sel,apply=True,t=True,r=True,s=True,pn=True)#Freeze Transformations
        cmds.makeIdentity(sel,apply=False,t=True,r=True,s=True)#Reset Transformations
        cmds.delete(sel,ch = True)#Delete by Type History
        cmds.select(cl=True)

def unlocks_edit_func(sel):
    attrs = ["tx","ty","tz","rx","ry","rz","sx","sy","sz","visibility"]
    for attr in attrs:
        cmds.setAttr(sel+"."+attr,l=False)

def delUnknownNode_edit_func():
    unknown_nodes = cmds.ls(type = 'unknown')
    cmds.delete(unknown_nodes)
    unknown_plugins = cmds.unknownPlugin(q=True, l=True)
    if unknown_plugins:
        for p in unknown_plugins:
            cmds.unknownPlugin(p, r=True)
            print('Removed unknown plugin : {}'.format(p))
