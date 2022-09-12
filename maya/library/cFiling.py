# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import os
import shutil
import cClean as cc

class Path():
    def __init__(self):
        self.wrkDir=cmds.workspace(q=True,rd=True,o=True)
        self.setDir=os.path.abspath(os.path.join(self.wrkDir,".."))
        self.projectName= "_newProject"

#Public function
    def rootPath(self):
        print(self.wrkDir)
        return self.wrkDir

    def setProjectName(self,name):
        self.projectName=name
        return self.projectName

    def setPath(self,path):
        self.setDir=path
        return self.setDir

    def addPath(self,add):
        self.setDir=os.path.abspath(os.path.join(self.setDir,add))
        return self.setDir

    def queryPath(self):
        return self.setDir

    def createProject(self):
        self.wrkDir=self.setProject_create_path(self.setDir,self.projectName)
        return self.wrkDir

    def editProject(self):
        self.wrkDir=self.setProject_edit_path(self.setDir,self.projectName)
        return self.wrkDir

    def upCreateProject(self):
        self.wrkDir=self.upSetProject_create_path(self.projectName)
        return self.wrkDir

#Private function
    def setProject_create_path(self,setDir,name):
        root_path = os.path.dirname(__file__) #.../cgInTools/maya/library
        maya_path = os.path.abspath(os.path.join(root_path,".."))
        maya_defSetProject_path = os.path.join(maya_path,"_defSetProject")
        setDir=self.isPath_check_path(setDir)
        wrkDir=os.path.join(setDir,name)
        wrkDir=self.notSamePath_check_path(wrkDir)
        shutil.copytree(maya_defSetProject_path,wrkDir)
        cmds.workspace(wrkDir,o=True)
        wrkDir=cmds.workspace(q=True,rd=True)
        return wrkDir
    
    def setProject_edit_path(self,setDir,name):
        wrkDir=os.path.join(setDir,name)
        wrkDir=self.isPath_check_path(wrkDir)
        cmds.workspace(wrkDir,o=True)
        wrkDir=cmds.workspace(q=True,rd=True)
        return wrkDir

    def upSetProject_create_path(self,name):
        rootDir=cmds.workspace(q=True,rd=True)
        upDir=os.path.abspath(os.path.join(rootDir,".."))
        wrkDir=self.setProject_create_path(upDir,name)
        return wrkDir

    def isPath_check_path(self,path):
        bool=os.path.isdir(path)
        if bool:
            return path
        else :
            cmds.error(path + " path does not exist.")

    def notSamePath_check_path(self,path):
        bool=os.path.isdir(path)
        if bool:
            cmds.error(path + " folder with the same name already exists")
        else :
            return path
        
class File():
    def __init__(self):
        wrkDir=cmds.workspace(q=True,sn=True)
        self.path=wrkDir
        self.name=wrkDir.split("/")[-1]
        self.fileType=("ma","mayaAscii")
        self.objs=[]

#Public function
    def setPath(self,path):
        self.path = path
        return path

    def setName(self,name):
        self.name=name
        return self.name

    def setType(self,ex):
        fileType_dict={"ma":"mayaAscii","mb":"mayaBinary","obj":"OBJexport","fbx":"FBX export"}
        self.fileType=ex,fileType_dict[ex]
        return self.fileType

    def setObjs(self,objs):
        self.objs=objs
        return self.objs

    def addObjs(self,objs):
        self.objs.append(objs)
        return self.objs

    def addPath(self,add):
        self.path=os.path.abspath(os.path.join(self.path,add))
        return self.path

    def save(self):
        self.fileSave_edit_str(self.name,self.fileType[1])

    def exportFile(self):
        if self.fileType[0] is "ma" or "mb":
            self.exportMAMB_create_func(self.objs,self.path,self.name,self.fileType[0],self.fileType[1])
        elif self.fileType[0] is "obj" or "fbx":
            self.exportOBJFBX_create_func(self.objs,self.path,self.name,self.fileType[0],self.fileType[1])

    def grpsExport(self):
        dupObjs=self.grpsDuplicate_create_list(self.objs)
        cc.delThree_edit_func(dupObjs)
        if self.fileType[0] is "ma" or "mb":
            self.exportMAMB_create_func(dupObjs,self.path,self.name,self.fileType[0],self.fileType[1])
        elif self.fileType[0] is "obj" or "fbx":
            self.exportOBJFBX_create_func(dupObjs,self.path,self.name,self.fileType[0],self.fileType[1])
        self.undoDuplicate_edit_func(self.objs,dupObjs)
        
#Private function
    def fileSave_edit_str(self,name,exType="mayaAscii"):
        currentScenePath=cmds.file(q=True,sn=True)
        root=os.path.dirname(currentScenePath)
        if root == "":
            cmds.file(rename=name)
            cmds.file(save=True,op="v=0",type=exType)
        else:
            cmds.file(save=True,op="v=0",type=exType)

    def exportMAMB_create_func(self,objs,path,name,ex="ma",exType="mayaAscii"):
        cmds.select(objs)
        fullPath=os.path.join(path,name+"."+ex)
        cmds.file(fullPath,f=True,options="v=0;",typ=exType,pr=True,es=True)
    
    def exportOBJFBX_create_func(self,objs,path,name,ex="obj",exType="OBJexport"):
        cmds.select(objs)
        fullPath=os.path.join(path,name+"."+ex)
        cmds.file(fullPath,f=True,options="v=0;",groups=1,ptgroups=1,materials=1,smoothing=1,normals=1,typ=exType,pr=True,es=True)
    
    def grpsDuplicate_create_list(self,grps):
        exportGrps=[]
        for grp in grps:
            print(grp)
            cmds.rename(grp,grp+"_original")
            cmds.duplicate(grp+"_original")
            exportGrp=cmds.rename(grp+"_original1",grp)
            exportGrps.append(exportGrp)
            return exportGrps

    def undoDuplicate_edit_func(self,grps,exportGrps):
        cmds.delete(exportGrps)
        for grp in grps:
            cmds.rename(grp+"_original",grp)