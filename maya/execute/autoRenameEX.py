import maya.cmds as cmds

import cgInTools as cit
from ..library import namingLB as nLB
from ..library import jsonLB as jLB
cit.reloads([nLB,jLB])

def main():
    RULES_DICT=jLB.getJson(cit.mayaData_dir,"autoRename")
    model=nLB.Naming()
    model.setSwitch(RULES_DICT["modeSwitch"])
    model.setOrderList(RULES_DICT["nameOrderList"])
    model.setCustom(RULES_DICT["customText"])
    model.setNode(RULES_DICT["nodeText"])
    model.setSide(RULES_DICT["sideText"])
    uuidObjs=cmds.ls(sl=True,uuid=True)
    for uuidObj in uuidObjs:
        model.setTitle(RULES_DICT["titleText"])
        obj=cmds.ls(uuidObj)[0]
        model.setObject(obj)
        model.rename()