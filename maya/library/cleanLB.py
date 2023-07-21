# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

def delFRHThree_edit_func(obj):
    unlocks_edit_func(obj)#Prevention of unlock errors
    cmds.makeIdentity(obj,apply=True,t=True,r=True,s=True,pn=True)#Freeze Transformations
    cmds.makeIdentity(obj,apply=False,t=True,r=True,s=True)#Reset Transformations
    cmds.delete(obj,ch=True)#Delete by Type History
    cmds.select(cl=True)

def unlocks_edit_func(node,attrs=["tx","ty","tz","rx","ry","rz","sx","sy","sz","visibility"]):
    for attr in attrs:
        cmds.setAttr(node+"."+attr,l=False)

def delUnknownNode_edit_func():
    unknown_nodes=cmds.ls(type="unknown")
    cmds.delete(unknown_nodes)
    unknown_plugins=cmds.unknownPlugin(q=True,l=True)
    if unknown_plugins:
        for p in unknown_plugins:
            cmds.unknownPlugin(p,r=True)
            print("Removed unknown plugin : {}".format(p))

def defaultMaterial_edit_func(obj,defMaterial="initialShadingGroup"):
    cmds.lockNode(defMaterial,l=False,lu=False)
    cmds.sets(obj,e=True,forceElement=defMaterial)

def delGarbageReference_edit_func():
    count=0
    refs=cmds.ls(type="reference")
    for ref in refs:
        try:
            cmds.referenceQuery(ref,f=True)
        except Exception as e:
            if type(e) == RuntimeError and 'is not associated with a reference file' in e.message:
                print(e+" Deleting: "+ ref)
                cmds.lockNode(ref,lock=False)
                cmds.delete(ref)
                count += 1

    print("Total errors found: " + str(count))

def nodeUnLocked_edit_tuple2(node="initialShadingGroup"):
    pastNode_bools=cmds.lockNode(node,q=True)
    cmds.lockNode(node,l=False,lu=False)
    lockNode_bools=cmds.lockNode(node,q=True)
    return lockNode_bools,pastNode_bools