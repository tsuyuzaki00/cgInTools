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
    test=oLB.JointWeight("joint1")
    test.setSubject(obj)
    #test.setFullPathSwitch(True)
    print(test.getSubject())
    print(test.getSubShapes())
    print(test.getSubShapes(True))
    print(test.getSubShapeTypes())
    print(test.getSubShapeTypes(True))
    print(test.getSubParent())
    print(test.getSubChilds())
    print(test.getSubChilds(True))
    print(test.getSkinClusters())

main()