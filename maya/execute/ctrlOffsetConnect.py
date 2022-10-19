# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
from cgInTools.maya.library import cConstraint as cct
from cgInTools.maya.library import cNaming as cn


def main():
    offctrl=cct.CtrlParent()
    joint,offJoint=cmds.ls(sl=True)
    offctrl.setTargetObj(joint)
    offctrl.setOffsetJoint(offJoint)

    null=joint.replace("jnt","null")
    space=joint.replace("jnt","space")
    trs=joint.replace("jnt","trs")
    offset=joint.replace("jnt","offset")
    ctrl=joint.replace("jnt","ctrl")

    offctrl.setSourceObj(trs)
    offctrl.setOffsetObj(offset)

    offctrl.setSpaceNames([null,space])
    offctrl.setTrsName(trs)
    offctrl.setOffsetName(offset)
    offctrl.setCtrlName(ctrl)

    offctrl.createOffsetConnect()