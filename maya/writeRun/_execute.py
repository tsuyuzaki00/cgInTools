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

    selfConnect_dicts=[
        {
            "inputAttr":"translate",
            "sourceNode":"pCube2",
            "outputAttr":"translate",
        },
        {
            "inputAttr":"rotate",
            "sourceNode":"pCube2",
            "outputAttr":"rotate",
        },
        {
            "inputAttr":"scale",
            "sourceNode":"pCube2",
            "outputAttr":"scale",
        }
    ]
    
    selfNode=oLB.SelfNode("null1")
    for selfConnect_dict in selfConnect_dicts:
        selfConnect=oLB.SelfNode("pCube1")
        selfConnect.setInputAttr(selfConnect_dict["inputAttr"])
        selfConnect.setSourceNode(selfConnect_dict["sourceNode"])
        selfConnect.setOutputAttr(selfConnect_dict["outputAttr"])
        selfNode.addSelfConnects([selfConnect])
    selfNode.standAloneConnection()
    for selfConnect in selfNode.getSelfConnects():
        print(selfConnect.getInputAttr())
        print(selfConnect.getSourceNode())
        print(selfConnect.getOutputAttr())

    """
    obj=cmds.ls(sl=True)[0]
    pCube=oLB.SelfNode("pCube1")
    pCube.setNode(obj)
    pCube.setConnectionNodeTypeToFind("skinCluster")
    print(pCube.getConnectionNodeTypeToFind())
    """

main()