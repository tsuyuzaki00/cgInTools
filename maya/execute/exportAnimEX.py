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
    
    obj=cmds.ls(sl=True)[0]
    keyObj=akLB.KeyObjects()
    keyObj.setObject(obj)
    key_dict=keyObj.createKeyObjectDict()
    exportJson.setWriteDict(key_dict)
    exportJson.write()