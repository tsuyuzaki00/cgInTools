import maya.cmds as cmds

import cgInTools as cit
from ..library import namingLB as nLB
from ..library import jsonLB as jLB
cit.reloads([nLB,jLB])

rules_dict=jLB.getJson(cit.mayaData_path,"autoRenameEX")

def main():
    print(jLB)
    objs=cmds.ls(sl=True)
    model=nLB.Naming()
    model.setOrders(rules_dict["nameOrders"])
    for obj in objs:
        model.setObject(obj)
        model.rename()