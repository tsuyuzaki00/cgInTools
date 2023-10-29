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
    node_DataNode.setName("pCube1")
    node_DataNode.setType("transform")

    attr_DataAttr=naLB.DataAttribute()
    attr_DataAttr.setName("Ytest")
    attr_DataAttr.setShortName("Ytt")
    attr_DataAttr.setValueType(11)
    attr_DataAttr.setDefaultValue(0.0)

    plug_DataPlug=naLB.DataPlug()
    plug_DataPlug.setDataNode(node_DataNode)
    plug_DataPlug.setDataAttribute(attr_DataAttr)

    plug_SelfPlug=naLB.SelfPlug()
    plug_SelfPlug.setDataPlug(plug_DataPlug)
    plug_SelfPlug.createAttr()

main()