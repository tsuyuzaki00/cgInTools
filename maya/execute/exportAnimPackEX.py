import maya.cmds as cmds

import cgInTools as cit
from ..library import animationKeyLB as akLB
from ..library import jsonLB as jLB
from ..library import windowLB as wLB
cit.reloads([akLB,jLB,wLB])

EXTENSION="anim"

def main():
    path,file=wLB.mayaFileDialog_query_path_file("export",0,EXTENSION)
    exportJson=jLB.Json()
    exportJson.setPath(path)
    exportJson.setFile(file)
    exportJson.setExtension(EXTENSION)
    objs=cmds.ls(sl=True)
    for obj in objs:
        name=obj.split(":")[-1]
        keyObj=akLB.EditKey()
        keyObj.setObject(obj)
        key_dict=keyObj.getKeyObjectDicts()
        print(key_dict)
        exportJson.addWritePackDict(key_dict,file=name)
    print(exportJson.getWritePackDicts())
    exportJson.writePacks()