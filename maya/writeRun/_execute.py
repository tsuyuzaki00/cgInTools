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

    node=cmds.ls(sl=True)[0]
    nodeM=oLB.SelfNode(node)
    print(nodeM.getNode())
    #nodeM.setAttr("translateX")
    #nodeM.setValue(1)
    #nodeM.doIt("editAttr")
    #print(nodeM.addQuaternionMMatrix(variable=(-0.005,-0.221,0.104,0.970)))

main()