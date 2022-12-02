# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import cgInTools as cit
from ..library import ctrlConnectLB as ccLB
cit.reloads([ccLB])

def main():
    ctrl=ccLB.CtrlParent()
    isJoint=cmds.ls(sl=True,typ="joint")[0]
    joints=cmds.ls(sl=True,typ="joint")[1:]
    parentJoint=cmds.listRelatives(isJoint,p=True,typ="joint")
    if parentJoint == None:
        ctrl.setObject(isJoint)
        ctrl.offsetCtrlRoot()
    else:
        joints=cmds.ls(sl=True,typ="joint")
    for joint in joints:
        ctrl.setObject(joint)
        ctrl.offsetCtrl()