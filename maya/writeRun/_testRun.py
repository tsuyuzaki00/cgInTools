# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import cgInTools as cit
from cgInTools.maya.library import ctrlConnectLB as ccLB
cit.reloads([ccLB])

def offset():
    ctrl=ccLB.CtrlParent()
    isJoint=cmds.ls(sl=True,typ="joint")[0]
    joints=cmds.ls(sl=True,typ="joint")[1:]
    parentJoint=cmds.listRelatives(isJoint,p=True,typ="joint")
    if parentJoint==None:
        ctrl.setObject(isJoint)
        ctrl.offsetCtrlRoot()
    else:
        joints=cmds.ls(sl=True,typ="joint")
    for joint in joints:
        ctrl.setObject(joint)
        ctrl.offsetCtrl()

def aimset():
    ctrl=ccLB.CtrlParent()
    root=cmds.ls(sl=True)[0]
    joints=cmds.ls(sl=True)[1:]
    ctrl.setObject(root)
    ctrl.aimsetCtrlRoot()
    for joint in joints:
        ctrl.setObject(joint)
        ctrl.aimsetCtrl()

#offset()
aimset()