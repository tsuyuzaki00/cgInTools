# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import cgInTools as cit
from cgInTools.maya.library import constrainLB as LB
cit.reloads([LB])

def main():
    sourceNode=cmds.ls(sl=True)[0]
    targetNode=cmds.ls(sl=True)[1]

    replace=LB.Constrain()
    replace.setSourceNode(sourceNode)
    replace.setTargetNode(targetNode)
    replace.proximityPin()

main()