import maya.cmds as cmds
import os

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
    path=os.path.join(setPath,"polite","cage","model")
    name="model"
    grpsExport_edit_func(grps=grps_obj,path=path,name=name,ex="ma")

main()