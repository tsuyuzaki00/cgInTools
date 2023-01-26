import maya.cmds as cmds

import cgInTools as cit
from ..library import windowLB as wLB
from ..library import jsonLB as jLB
from ..library import objectLB as oLB
cit.reloads([wLB,jLB,oLB])

EXTENSION="anim"

def main():
    path,file=wLB.mayaFileDialog_query_path_file("import",1,EXTENSION+"Pack")
    importJson=jLB.Json()
    importJson.setPath(path)
    importJson.setFile(file)
    importJson.setExtension(EXTENSION)
    anim_dicts=importJson.readPacks()
    for anim_dict in anim_dicts:
        for keyObject_dict in anim_dict["keys"]:
            try:
                keyObject=oLB.KeyObject(keyObject_dict["object"])
                keyObject.setAttr(keyObject_dict["attr"])
                keyObject.setValue(keyObject_dict["value"])
                keyObject.setTime(keyObject_dict["time"])
                keyObject.setInType(keyObject_dict["inTangentType"])
                keyObject.setOutType(keyObject_dict["outTangentType"])
                keyObject.setInAngle(keyObject_dict["inAngle"])
                keyObject.setOutAngle(keyObject_dict["outAngle"])
                keyObject.setKey()
            except RuntimeError as e:
                print(e)