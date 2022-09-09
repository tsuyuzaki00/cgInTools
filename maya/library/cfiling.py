# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import os
import shutil

import sys
sys.path.append('../')
import cgInTools as sf

class Path():
    def __init__(self):
        self.wrkDir=cmds.workspace(q=True,rd=True,o=True)

    def rootDir_quary_path(self):
        wrkDir=cmds.workspace(q=True,rd=True)
        return wrkDir

    def setPath_quary_path(self):
        return self.wrkDir

    def addPath_edit_path(self,add):
        self.wrkDir=os.path.abspath(os.path.join(self.wrkDir,add))
        return self.wrkDir

    def setProject_create_path(self,setDir):
        root_path = os.path.dirname(__file__) #.../cgInTools/maya/library
        maya_path = os.path.abspath(os.path.join(root_path,".."))
        maya_defSetProject_path = os.path.join(maya_path,"_defSetProject")
        try:
            shutil.copytree(maya_defSetProject_path,setDir)
            self.wrkDir=cmds.workspace(setDir,o=True)
        except WindowsError:
            cmds.error("A folder with the same name already exists.")
    
    def setProject_edit_path(self,wrkDir):
        self.wrkDir=cmds.workspace(wrkDir,o=True)
        return self.wrkDir

    def upSetProject_create_path(self,name):
        rootDir=self.rootDir_quary_path()
        upDir=os.path.abspath(os.path.join(rootDir,".."))
        setDir=os.path.join(upDir,name)
        self.setProject_create_path(setDir)
        return self.wrkDir
        
    
class File():
    def __init__(self):
        wrkDir=cmds.workspace(q=True,sn=True)
        self.name=wrkDir.split("/")[-1]
        self.path=wrkDir

    def setFileName_quary_str(self):
        return self.name

    def setFileName_edit_str(self,name):
        self.name=name
        return self.name
    
    def fileSave_edit_str(self,name):
        currentScenePath=cmds.file(q=True,sn=True)
        root=os.path.dirname(currentScenePath)
        if root == "":
            cmds.file(rename=name)
            cmds.file(save=True,op="v=0",type='mayaAscii')
        else:
            cmds.file(save=True,op="v=0",type='mayaAscii')

    def exportMA_create_func(self,selGrps,path,name):
        cmds.select(selGrps)
        fullPath=os.path.join(path,name+".ma")
        cmds.file(fullPath,f=True,options="v=0;",typ="mayaAscii",pr=True,es=True)

    def grpsExport_create_func(self,grps,path,name,ex="ma"):
        exportGrps=[]
        for grp in grps:
            cmds.rename(grp,grp+"_original")
            cmds.duplicate(grp+"_original")
            exportGrp=cmds.rename(grp+"_original1",grp)
            exportGrps.append(exportGrp)
        
        if ex=="ma":
            self.exportMA_create_func(selGrps=exportGrps,path=path,name=name)
            cmds.delete(exportGrps)
            for grp in grps:
                cmds.rename(grp+"_original",grp)