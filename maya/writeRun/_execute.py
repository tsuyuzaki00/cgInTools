# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

import cgInTools as cit
#from cgInTools.maya.library import _testPath as TP
from cgInTools.maya.library import dataLB as dLB
from cgInTools.maya.library import objectLB as oLB
from maya.library import appLB as mLB
#from cgInTools.maya.manager import equipmentSettingsMN as MN
#from cgInTools.maya.option import autoRenameOP as OP
#from cgInTools.maya.execute import exportAnimPackEX as EX
cit.reloads([oLB,dLB])

def main():
    #TP.main()
    #MN.main()
    #OP.main()
    #EX.main()

    node_DataNode=dLB.DataNode()
    node_DataNode.setNodeName("test")
    node_DataNode.setNodeType("transform")
    
    node_SelfDGNode=oLB.SelfDGNode()
    node_SelfDGNode.setDataNode(node_DataNode)
    #node_SelfDGNode.createNode()
    node_SelfDGNode.setAttributeNames(["visibility"])

    plug_DataPlugs=node_SelfDGNode.searchDataPlugs()
    for plug_DataPlug in plug_DataPlugs:
        print(plug_DataPlug.getDataNode().getNodeName())
        print(plug_DataPlug.getDataAttribute().getLongName())
        print(plug_DataPlug.getDataAttribute().getDataValueType())

main()