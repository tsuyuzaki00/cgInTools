# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import cgInTools as cit
from cgInTools.maya.library import ctrlConnectLB as ccLB
cit.verReload(ccLB)

def offset():
    ctrl=ccLB.CtrlParent()
    root=cmds.ls(sl=True)[0]
    ctrl.setObject(root)
    ctrl.offsetCtrlRoot()

    joints=cmds.listRelatives(root,ad=True,typ="joint")
    joints.reverse()
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