# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from ..library import ctrlConnectLB as ccLB
cit.reloads([ccLB])

def main():
    ctrl=ccLB.CtrlParent()
    root=cmds.ls(sl=True)[0]
    joints=cmds.ls(sl=True)[1:]
    ctrl.setObject(root)
    ctrl.aimsetCtrlRoot()
    for joint in joints:
        ctrl.setObject(joint)
        ctrl.aimsetCtrl()