import maya.cmds as cmds

import cgInTools as cit
from ..library import namingLB as nLB
from ..library import jsonLB as jLB
cit.reloads([nLB,jLB])

def main():
    rules_dict=jLB.getJson(cit.mayaData_path,"autoRename")
    uuidObjs=cmds.ls(sl=True,uuid=True)
    model=nLB.Naming()
    model.setOrders(rules_dict["nameOrders"])
    model.setSwitch(rules_dict["modeSwitch"])
    model.setCustom(rules_dict["customText"])
    model.setNode(rules_dict["nodeText"])
    model.setSide(rules_dict["sideText"])
    for uuidObj in uuidObjs:
        obj=cmds.ls(uuidObj)[0]
        model.setObject(obj)
        model.rename()