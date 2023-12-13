# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

import cgInTools as cit
#from cgInTools.maya.library import _testPath as TP
from ...library import pathLB as pLB
from ...library import serializeLB as sLB
from ...library import _testLB as tLB
from ..library import dataLB as dLB
from ..library import nameLB as nLB
from ..library import matrixLB as mLB
#from cgInTools.maya.manager import equipmentSettingsMN as MN
#from cgInTools.maya.option import autoRenameOP as OP
#from cgInTools.maya.execute import exportAnimPackEX as EX
cit.reloads([pLB,sLB,tLB,dLB,nLB,mLB])

def main():
    #TP.main()
    #MN.main()
    #OP.main()
    #EX.main()
    test_DataName=dLB.DataName()
    test_DataName.setTitle("spine")
    test_DataName.setNodeType("jnt")
    #test_DataName.setSide("C")
    test_DataName.setNumbers([0])
    test_DataName.setHierarchys(["A"])
    test_DataName.setOrders(["Title_Hierarchys_0","NodeType","Side_Numbers_0"])
    test_DataName.setIncrease("Numbers_0")

    for joint in ["joint1","joint2","joint3","joint4"]:
        test_DataNode=dLB.DataNode()
        test_DataNode.setName(joint)

        test_AppName=nLB.AppNodeName()
        test_AppName.setDataName(test_DataName)
        test_AppName.setDataNode(test_DataNode)
        test=test_AppName.rename()
        print(test)


main()