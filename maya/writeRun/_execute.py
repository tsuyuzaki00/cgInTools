# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
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
    obj=cmds.ls(sl=True)[0]
    pCube=oLB.SelfNode("pCube1")
    pCube.setNode(obj)
    pCube.setConnectionNodeTypeToFind("skinCluster")
    print(pCube.getConnectionNodeTypeToFind())

main()