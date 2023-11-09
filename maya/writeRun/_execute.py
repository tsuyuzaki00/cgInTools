# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

import cgInTools as cit
#from cgInTools.maya.library import _testPath as TP
from ...library import pathLB as pLB
from ...library import serializeLB as sLB
from ...library import _testLB as tLB
from ..library import nodeAttrLB as naLB
from ..library import matrixLB as mLB
#from cgInTools.maya.manager import equipmentSettingsMN as MN
#from cgInTools.maya.option import autoRenameOP as OP
#from cgInTools.maya.execute import exportAnimPackEX as EX
cit.reloads([pLB,sLB,tLB,naLB,mLB])

def main():
    #TP.main()
    #MN.main()
    #OP.main()
    #EX.main()
    
    source_DataNode=naLB.DataNode()
    source_DataNode.setName("joint1")
    target_DataNode=naLB.DataNode()
    target_DataNode.setName("joint2")
    
    worldMatrix=cmds.getAttr("pCube1.worldMatrix[0]")
    source_DataMatrix=mLB.DataMatrix(worldMatrix)
    
    source_SelfDAGNode=naLB.SelfDAGNode()
    source_SelfDAGNode.setDataNode(source_DataNode)
    #source_SelfDAGNode.setDataMatrix(source_DataMatrix)
    source_SelfDAGNode.setTargetDataNode(target_DataNode)
    source_SelfDAGNode.mirrorTargetTransform()

main()