# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

import cgInTools as cit
#from cgInTools.maya.library import _testPath as TP
from ...library import pathLB as pLB
from ...library import serializeLB as sLB
from ...library import _testLB as tLB
from ..library import dataLB as dLB
from ..library import nodeAttrLB as naLB
from ..library import matrixLB as mLB
#from cgInTools.maya.manager import equipmentSettingsMN as MN
#from cgInTools.maya.option import autoRenameOP as OP
#from cgInTools.maya.execute import exportAnimPackEX as EX
cit.reloads([pLB,sLB,tLB,dLB,naLB,mLB])

def main():
    #TP.main()
    #MN.main()
    #OP.main()
    #EX.main()
    
    node_DataNode=dLB.DataNode()
    node_DataNode.setName("test_trs_C")
    node_DataNode.setType("transform")
    node_DataName=dLB.DataName()
    node_DataName.setTitle("test")
    node_DataName.setNodeType("trs")
    node_DataName.setSide("C")
    node_DataName.setOrders(["Side","NodeType","Title"])
    
    node_SelfDGNode=naLB.SelfDGNode()
    node_SelfDGNode.setDataNode(node_DataNode)
    node_SelfDGNode.setDataName(node_DataName)
    node_SelfDGNode.rename()

main()