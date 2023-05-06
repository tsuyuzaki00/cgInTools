# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import json

import cgInTools as cit
#from cgInTools.maya.library import _testPath as TP
#from cgInTools.maya.manager import equipmentSettingsMN as MN
#from cgInTools.maya.option import autoRenameOP as OP
from cgInTools.maya.library import objectLB as oLB
#from cgInTools.maya.library import constrainLB as LB
#from cgInTools.maya.execute import exportAnimPackEX as EX
cit.reloads([oLB])

def writeJson_create_func(path,write_dict):
    with open(path,"w") as f:
        json.dump(write_dict,f,indent=4,ensure_ascii=False)

def main():
    #OP.main()
    #MN.main()
    #EX.main()
    #TP.main()

    #node=cmds.ls(sl=True)[0]
    nodeM=oLB.SelfComponent()
    nodeM.setComponent("pCube1.vtx[2]")
    nodeM.setMFn(554)
    nodeM.setComponentID(5)
    print(nodeM.getComponentID())
    #print(type(nodeM.getMSpace()))
    #print(type(nodeM.getRotateOrder()))
    #test_dict=nodeM.writeDict()
    #print(test_dict)

    #writeJson_create_func("D:/test.json",test)

main()