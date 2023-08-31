# -*- coding: iso-8859-15 -*-
import os
import shutil
import maya.cmds as cmds
import maya.api.OpenMaya as om2

import cgInTools as cit
from cgInTools.library import jsonLB as jLB
from cgInTools.library import pathLB as pLB
from . import cleanLB as cLB
cit.reloads([jLB,pLB,cLB])

RULE_DICT=jLB.readJson(cit.mayaSettings_dir,"library")
PROJECTFOLDER=cit.mayaDefSetProject_dir
class Project():
    def __init__(self):
        self._defSetProjectFolder=PROJECTFOLDER
        self._project_Path=pLB.Path()
    
    def __str__(self):
        project_dir=self._project_Path.queryDirectory()
        return project_dir

    #Single Function
    def setProject_edit_str(self,project_dir,create=False):
        if create:
            shutil.copytree(self._defSetProjectFolder,project_dir)
        cmds.workspace(project_dir,o=True)
        project_dir=cmds.workspace(q=True,rd=True)
        return project_dir

    #Setting Function
    def setDirectory(self,variable):
        _directory_dir=self._project_Path.setAbsoluteDirectory(variable)
        return _directory_dir
    def currentDirectory(self):
        project_dir=cmds.workspace(q=True,rd=True)
        absoluteDirectorys=project_dir.split("/")[:-2]
        absolute_dir=os.path.join(*absoluteDirectorys)
        _directory_dir=self._project_Path.setAbsoluteDirectory(absolute_dir)
        return _directory_dir
    def getDirectory(self):
        return self._project_Path.getAbsoluteDirectory()
    
    def setProjectName(self,variable):
        _projectName_str=self._project_Path.setRelativeDirectory(variable)
        return _projectName_str
    def currentProjectName(self):
        project_dir=cmds.workspace(q=True,rd=True)
        projectName_str=project_dir.split("/")[-2]
        projectName_str=self._project_Path.setRelativeDirectory(projectName_str)
        return projectName_str
    def getProjectName(self):
        return self._project_Path.getRelativeDirectory()

    #Public Function
    def createProject(self,directory=None,name=None):
        if not directory is None:
            self._project_Path.setAbsoluteDirectory(directory)
        if not name is None:
            self._project_Path.setRelativeDirectory(name)

        project_dir=self._project_Path.queryDirectory()
        workSpace_dir=self.setProject_edit_str(project_dir,create=True)
        return workSpace_dir

    def editProject(self,directory=None,name=None):
        if not directory is None:
            self._project_Path.setAbsoluteDirectory(directory)
        if not name is None:
            self._project_Path.setRelativeDirectory(name)
        
        project_dir=self._project_Path.queryDirectory()
        workSpace_dir=self.setProject_edit_str(project_dir)
        return workSpace_dir

    def queryProject(self):
        project_dir=self._project_Path.queryDirectory()
        return project_dir
 
class File():
    def __init__(self):
        self._fileType_dict=RULE_DICT["fileType_dict"]

        self._absoluteDirectory=None
        self._relativeDirectory=None
        self._file=None
        self._extension=None
        self._exType=None

    #Single Function
    def fileSave_edit_func(self,directory,file,exType):
        if file is None:
            file="_spaceSave"
        if exType is None:
            exType="mayaAscii"
        path=os.path.join(directory,file)
        cmds.file(rename=path)
        cmds.file(save=True,op="v=0",type=exType)

    def fileOpen_edit_func(self,directory,file,ex):
        if ex is None:
            ex="ma"
        path=os.path.join(directory,file)
        cmds.file(path+"."+ex,open=True,force=True)

    def newDirectory_create_str(self,absoluteDirectory,relativeDirectory):
        if absoluteDirectory is None:
            absoluteDirectory="D:"
        if relativeDirectory is None:
            relativeDirectory=""
        newDirectory=os.path.join(absoluteDirectory,relativeDirectory)
        return newDirectory

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

    #Multi Function
    def _judgeFileType_create_func(objs,path,file,extension,fileType_dict):
        fileType=fileType_dict[extension]
        if extension is "ma" or extension is "mb":
            self.exportMAMB_create_func(objs,path,file,extension,fileType)
        elif extension is "obj" or extension is "fbx":
            self.exportOBJFBX_create_func(objs,path,file,extension,fileType)

    #Setting Function
    def setAbsoluteDirectory(self,variable):
        self._absoluteDirectory=variable
        return self._absoluteDirectory
    def getAbsoluteDirectory(self):
        return self._absoluteDirectory
    
    def setRelativeDirectory(self,variable):
        self._relativeDirectory=variable
        return self._relativeDirectory
    def getRelativeDirectory(self):
        return self._relativeDirectory

    def setFile(self,variable):
        self._file=variable
        return self._file
    def getFile(self):
        return self._file
    
    def setExtension(self,variable):
        self._extension=variable
        return self._extension
    def getExtension(self):
        return self._extension

    def setExType(self,variable):
        self._exType=variable
        return self._exType
    def getExType(self):
        return self._exType

    #Public Function
    def addPath(self,variable):
        addPath=os.path.abspath(os.path.join(self._path,variable))
        return addPath

    def save(self,absolute=None,relative=None,name=None,exType=None):
        _absoluteDirectory=absolute or self._absoluteDirectory
        _relativeDirectory=relative or self._relativeDirectory
        _file=name or self._file
        _exType=exType or self._exType

        _directory=self.newDirectory_create_str(_absoluteDirectory,_relativeDirectory)
        self.fileSave_edit_func(_directory,_file,_exType)

    def open(self,absolute=None,relative=None,name=None,ex=None):
        _absoluteDirectory=absolute or self._absoluteDirectory
        _relativeDirectory=relative or self._relativeDirectory
        _file=name or self._file
        _extension=ex or self._extension

        _directory=self.newDirectory_create_str(_absoluteDirectory,_relativeDirectory)
        self.fileOpen_edit_func(_directory,_file,_extension)

    def exportFile(self):
        self._judgeFileType_create_func(self._objs,self._path,self._file,self._extension,self._fileType_dict)

    def grpsExport(self):
        uncleanObjs=[]
        dupGrps=self.grpsDuplicate_create_list(self._objs)
        for dupGrp in dupGrps:
            uncleans=cmds.listRelatives(dupGrp,c=True,f=True)
            uncleanObjs=uncleanObjs+uncleans
        cLB.delFRHThree_edit_func(uncleanObjs)
        cLB.defaultMaterial_edit_func(uncleanObjs)
        self._judgeFileType_create_func(self._objs,self._path,self._file,self._extension,self._fileType_dict)
        self.undoDuplicate_edit_func(self._objs,dupGrps)