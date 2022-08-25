# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import os

def wrkDir_create_path(wrkDir="",addFolder=""):
    wrkDir=wrkDir or cmds.workspace(q=True,rd=True)
    cmds.workspace(wrkDir,openWorkspace=True)
    newPath=os.path.join(wrkDir,addFolder)
    return newPath

def file_save_str(name):
    currentScenePath=cmds.file(q=True,sn=True)
    root=os.path.dirname(os.path.dirname(currentScenePath))
    if root == "":
        cmds.file(rename=name)
        cmds.file(save=True,op="v=0",type='mayaAscii')
    else:
        cmds.file(save=True,op="v=0",type='mayaAscii')

def grpsExport_edit_func(grps,path,name,ex="ma"):
    originalGrps=[]
    exportGrps=[]
    for grp in grps:
        originalGrp=cmds.rename(grp,grp+"_original")
        cmds.duplicate(grp+"_original")
        exportGrp=cmds.rename(grp+"_original1",grp)
        originalGrps.append(originalGrp)
        exportGrps.append(exportGrp)
    
    if ex=="ma":
        exportMA_export_func(selGrps=exportGrps,path=path,name=name)
        cmds.delete(exportGrps)
        for grp in grps:
            cmds.rename(grp+"_original",grp)

def exportMA_export_func(selGrps,path,name):
    cmds.select(selGrps)
    fullPath=os.path.join(path,name+".ma")
    cmds.file(fullPath,f=True,options="v=0;",typ="mayaAscii",pr=True,es=True)

def main():
    grps_obj=cmds.ls(sl=True)
    setPath=cmds.workspace(q=True,rd=True)
    path=os.path.join(setPath,"polite","middle","base","cage")
    name="cage"
    grpsExport_edit_func(grps=grps_obj,path=path,name=name,ex="ma")