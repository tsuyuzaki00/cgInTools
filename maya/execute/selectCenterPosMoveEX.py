# -*- coding: iso-8859-15 -*-

import maya.cmds as cmds
from ..library import sourceToTargetLB as sttLB

def main():
    obj=cmds.ls(sl=True,fl=True)
    targetSet=sttLB.SourceToTarget()
    targetSet.setTargetNode(obj[0])
    targetSet.setSourceNode(obj[1])
    targetSet.moveToTarget()