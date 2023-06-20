# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

import cgInTools as cit
#from cgInTools.maya.library import _testPath as TP
#from cgInTools.maya.manager import equipmentSettingsMN as MN
#from cgInTools.maya.option import autoRenameOP as OP
from cgInTools.maya.library import objectLB as oLB
#from cgInTools.maya.library import constrainLB as LB
#from cgInTools.maya.execute import exportAnimPackEX as EX
cit.reloads([oLB])

def main():
    #OP.main()
    #MN.main()
    #EX.main()
    #TP.main()

    #node=cmds.ls(sl=True)[0]
    nodeM=oLB.SelfTransformNode()
    nodeM.setNode("pCube1")
    nodeM.setMatchNode("pCube2")
    nodeM.matchToTranslate()
    nodeM.matchToQuaternion()
    #nodeM.translate([3,0,0])

main()