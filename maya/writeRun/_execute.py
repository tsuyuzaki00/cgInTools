# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

import cgInTools as cit
from ...library import baseLB as bLB
from ..library import dataLB as dLB
from ..library import selfLB as sLB
from ..library import nodeLB as nLB
cit.reloads([bLB,dLB,sLB,nLB])

def main():
    node_DataNode=dLB.DataNode()
    node_DataNode.setName("pCube1")
    
    node_SelfDAGNode=sLB.SelfDAGNode()
    node_SelfDAGNode.setDataNode(node_DataNode)
    print(node_SelfDAGNode.queryFullPathChildNames())

main()