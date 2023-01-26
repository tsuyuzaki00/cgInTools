import maya.cmds as cmds

import cgInTools as cit
from ..library import windowLB as wLB
from ..library import jsonLB as jLB
from ..library import animationKeyLB as akLB
cit.reloads([wLB,jLB,akLB])

EXTENSION="anim"

def main():
    path,file=wLB.mayaFileDialog_query_path_file("export",0,EXTENSION+"Pack")
    exportJson=jLB.Json()
    exportJson.setPath(path)
    exportJson.setFile(file)
    exportJson.setExtension(EXTENSION)
    objs=cmds.ls(sl=True)
    for obj in objs:
        name=obj.split(":")[-1]
        keyObj=akLB.KeyObjects()
        keyObj.setObject(obj)
        key_dict=keyObj.createKeyObjectDict()
        exportJson.addWritePackDict(key_dict,file=name)
    exportJson.writePacks()