# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

import cgInTools as cit
#from cgInTools.maya.library import _testPath as TP
from ...library import pathLB as pLB
from ...library import serializeLB as sLB
from ...library import _testLB as tLB
from ..library import nodeAttrLB as naLB
from ..library import deformLB as dLB
#from cgInTools.maya.manager import equipmentSettingsMN as MN
#from cgInTools.maya.option import autoRenameOP as OP
#from cgInTools.maya.execute import exportAnimPackEX as EX
cit.reloads([pLB,sLB,tLB,naLB,dLB])

def main():
    #TP.main()
    #MN.main()
    #OP.main()
    #EX.main()
    node_DataNode=naLB.DataNode()
    node_DataNode.setName("skinCluster1")
    node_DataNode.setType("skinCluster")

    deform_SelfDeformation=dLB.SelfDeformation()
    deform_SelfDeformation.setNode(node_DataNode)
    deform_DataDeformations=deform_SelfDeformation.queryWeights()
    for deform_DataDeformation in deform_DataDeformations:
        for deform_DataWeight in deform_DataDeformation.getDataWeights():
            print(deform_DataWeight.getIndex())
            print(deform_DataWeight.getValue())


main()