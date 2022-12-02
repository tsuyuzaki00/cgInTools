# -*- coding: iso-8859-15 -*-
# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import os
import shutil

import cgInTools as cit
from . import setBaseLB as sbLB
from . import cleanLB as cLB
cit.reloads([sbLB,cLB])

class Path(sbLB.BasePath):
    def __init__(self):
        self._path=""
        self._name=""
        self._split="_"
        self._index=0

    def __loading(self):
        self._path=os.path.normpath(self._path)
        pass

#Public Function
    def clean(self):
        self.__loading()

    def getSplitPathOfIndex(self):
        norm_path=os.path.normpath(self._path)
        split_str=norm_path.split("\\")[self._index]
        return split_str

    def getSplitNameOfIndex(self):
        split_str=self._name.split(self._split)[self._index]
        return split_str

#Mulch Function
#Single Function
class Project(sbLB.BasePath):
    def __init__(self):
        self._name=cmds.file(q=True,sceneName=True).split('/')[-1]
        self._work_path=cmds.workspace(q=True,rd=True,o=True)
        self._def_path=os.path.abspath(os.path.join(self._work_path,".."))
        self._projectName_path="_newProject"

    def __loading():
        pass

    def queryInDefPath(self,variable):
        inDefPath=os.path.abspath(os.path.join(self._def_path,variable))
        return inDefPath
        
    def createProject(self):
        self._work_path=self.setProject_create_path(self._def_path,self._projectName_path)
        return self._work_path

    def editProject(self):
        self._work_path=self.setProject_edit_path(self._def_path,self._projectName_path)
        return self._work_path

    def upCreateProject(self):
        self._work_path=self.upSetProject_create_path(self._projectName_path)
        return self._work_path

#Mulch Function
    def upSetProject_create_path(self,name):
        root_path=cmds.workspace(q=True,rd=True)
        up_path=os.path.abspath(os.path.join(root_path,".."))
        work_path=self.setProject_create_path(up_path,name)
        return work_path

#Single Function
    def setProject_create_path(self,path,name):
        defSetProject_path=cit.mayaDefSetProject_path
        path=self.isPath_check_path(path)
        work_path=os.path.join(path,name)
        work_path=self.notSamePath_check_path(work_path)
        shutil.copytree(defSetProject_path,work_path)
        cmds.workspace(work_path,o=True)
        work_path=cmds.workspace(q=True,rd=True)
        return work_path
    
    def setProject_edit_path(self,path,name):
        work_path=os.path.join(path,name)
        work_path=self.isPath_check_path(work_path)
        cmds.workspace(work_path,o=True)
        work_path=cmds.workspace(q=True,rd=True)
        return work_path

    def isPath_check_path(self,path):
        bool=os.path.isdir(path)
        if bool:
            return path
        else :
            cmds.error(path+" path does not exist.")

    def notSamePath_check_path(self,path):
        bool=os.path.isdir(path)
        if bool:
            cmds.error(path+" folder with the same name already exists")
        else :
            return path
        
class File(sbLB.BaseFile):
    def __init__(self):
        work_path=cmds.workspace(q=True,sn=True)
        self._path=work_path
        self._file=work_path.split("/")[-1]
        self._fileType=("ma","mayaAscii")
        self._objs=[]
        self._fileType_dict={
            "ma":"mayaAscii",
            "mb":"mayaBinary",
            "obj":"OBJ export",
            "fbx":"FBX export"
            }

#Public Function
    def addPath(self,variable):
        self._path=os.path.abspath(os.path.join(self._path,variable))
        return self._path

    def save(self):
        self.fileSave_edit_func(self._file,self._fileType[1])

    def exportFile(self):
        if self._fileType[0] is "ma" or self._fileType[0] is "mb":
            self.exportMAMB_create_func(self._objs,self._path,self._file,self._fileType[0],self._fileType[1])
        elif self._fileType[0] is "obj" or self._fileType[0] is "fbx":
            self.exportOBJFBX_create_func(self._objs,self._path,self._file,self._fileType[0],self._fileType[1])

    def grpsExport(self):
        uncleanObjs=[]
        dupGrps=self.grpsDuplicate_create_list(self._objs)
        for dupGrp in dupGrps:
            uncleans=cmds.listRelatives(dupGrp,c=True,f=True)
            uncleanObjs=uncleanObjs+uncleans
        cLB.delFRHThree_edit_func(uncleanObjs)
        cLB.defaultMaterial_edit_func(uncleanObjs)
        if self._fileType[0] is "ma" or self._fileType[0] is "mb":
            self.exportMAMB_create_func(dupGrps,self._path,self._file,self._fileType[0],self._fileType[1])
        elif self._fileType[0] is "obj" or self._fileType[0] is "fbx":
            self.exportOBJFBX_create_func(dupGrps,self._path,self._file,self._fileType[0],self._fileType[1])
        self.undoDuplicate_edit_func(self._objs,dupGrps)
        
#Single Function
    def fileSave_edit_func(self,file,exType="mayaAscii"):
        currentScene_path=cmds.file(q=True,sn=True)
        root=os.path.dirname(currentScene_path)
        if root == "":
            cmds.file(rename=file)
            cmds.file(save=True,op="v=0",type=exType)
        else:
            cmds.file(save=True,op="v=0",type=exType)

    def exportMAMB_create_func(self,objs,path,file,ex="ma",exType="mayaAscii"):
        cmds.select(objs)
        fullPath=os.path.join(path,file+"."+ex)
        cmds.file(fullPath,f=True,options="v=0;",typ=exType,pr=True,es=True)
    
    def exportOBJFBX_create_func(self,objs,path,file,ex="obj",exType="OBJexport"):
        cmds.select(objs)
        fullPath=os.path.join(path,file+"."+ex)
        cmds.file(fullPath,f=True,options="v=0;",groups=1,ptgroups=1,materials=1,smoothing=1,normals=1,typ=exType,pr=True,es=True)
    
    def grpsDuplicate_create_list(self,grps):
        exportGrps=[]
        for grp in grps:
            cmds.rename(grp,grp+"_original")
            cmds.duplicate(grp+"_original")
            exportGrp=cmds.rename(grp+"_original1",grp)
            exportGrps.append(exportGrp)
            return exportGrps

    def undoDuplicate_edit_func(self,grps,delGrps):
        cmds.delete(delGrps)
        for grp in grps:
            cmds.rename(grp+"_original",grp)