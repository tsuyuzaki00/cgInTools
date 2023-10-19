# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

import cgInTools as cit
#from cgInTools.maya.library import _testPath as TP
from ...library import pathLB as pLB
from ...library import serializeLB as sLB
from ...library import _testLB as tLB
from ..library import nodeAttrLB as naLB
#from cgInTools.maya.manager import equipmentSettingsMN as MN
#from cgInTools.maya.option import autoRenameOP as OP
#from cgInTools.maya.execute import exportAnimPackEX as EX
cit.reloads([pLB,sLB,tLB,naLB])

def main():
    #TP.main()
    #MN.main()
    #OP.main()
    #EX.main()
    node_DataNode=naLB.DataNode()
    node_DataNode.setName("test")
    node_DataNode.setType("joint")

    node_SelfNode=naLB.SelfDGNode()
    node_SelfNode.setDataNode(node_DataNode)
    node_SelfNode.createNode()

main()