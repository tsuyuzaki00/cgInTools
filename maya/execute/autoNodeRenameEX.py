import maya.cmds as cmds

import cgInTools as cit
from ...library import jsonLB as jLB
from ..library import dataLB as dLB
from ..library import selfLB as sLB
cit.reloads([dLB,sLB,jLB])

DATAFOLDER="autoNodeRename"
RESETDIR,DATADIR=cit.checkScriptsData(DATAFOLDER,cit.mayaSettings_dir,cit.mayaData_dir)

def main():
    execute_dict=jLB.readJson(DATADIR,file="execute")
    node_DataName=dLB.DataName()
    node_DataName.setDataDict(execute_dict)
    node_DataName.readDict()
    
    objs=cmds.ls(sl=True)
    for obj in objs:
        node_DataNode=dLB.DataNode()
        node_DataNode.setName(obj)

        node_AppNodeName=sLB.SelfDGNode()
        node_AppNodeName.setDataNode(node_DataNode)
        node_AppNodeName.setDataName(node_DataName)
        node_AppNodeName.setDoIts(execute_dict.get("DoIts"))
        node_AppNodeName.doIt()