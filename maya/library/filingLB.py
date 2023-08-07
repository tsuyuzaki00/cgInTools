# -*- coding: iso-8859-15 -*-
import os
import shutil
import maya.cmds as cmds
import maya.api.OpenMaya as om2

import cgInTools as cit
from . import setBaseLB as sbLB
from . import cleanLB as cLB
from . import checkLB as chLB
from . import jsonLB as jLB
cit.reloads([sbLB,cLB,chLB,jLB])

RULE_DICT=jLB.getJson(cit.mayaSettings_dir,"library")
PROJECTFOLDER=cit.mayaDefSetProject_dir

class Path(sbLB.BasePath):
    def __init__(self):
        super(Path,self).__init__()
        scene=cmds.file(q=True,sceneName=True).split("/")[-1]
        self._file=scene.split(".")[0]
        self._extension=scene.split(".")[1]

    def __str__(self):
        pass

    def __loading(self):
        self._path=os.path.normpath(self._path)

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

class Project():
    def __init__(self):
        self._defSetProjectFolder=PROJECTFOLDER
        
        self._absoluteDirectory=None
        self._relativeDirectory=None
        self._projectName="_newProject"
    
    def __str__(self):
        projectDirectory=self.projectDirectory_create_str(self._absoluteDirectory,self._relativeDirectory,self._projectName)
        return projectDirectory

    #Single Function
    def projectDirectory_create_str(self,absoluteDirectory,relativeDirectory,projectName):
        if absoluteDirectory is None:
            absoluteDirectory="D:"
        if relativeDirectory is None:
            relativeDirectory=""
        projectDirectory=os.path.join(absoluteDirectory,relativeDirectory,projectName)
        return projectDirectory

    def setProject_edit_str(self,projectDirectory,create=False):
        if create:
            shutil.copytree(self._defSetProjectFolder,projectDirectory)
        cmds.workspace(projectDirectory,o=True)
        projectDirectory=cmds.workspace(q=True,rd=True)
        return projectDirectory

    def isPath_check_str(self,path):
        boolean=os.path.isdir(path)
        if boolean:
            return path
        else :
            cmds.error(path+" path does not exist.")

    #Setting Function
    def getDirectory(self):
        if self._absoluteDirectory is None:
            absoluteDirectory="D:"
        else:
            absoluteDirectory=self._absoluteDirectory
        if self._relativeDirectory is None:
            relativeDirectory=""
        else:
            relativeDirectory=self._relativeDirectory
        directory=os.path.join(absoluteDirectory,relativeDirectory)
        return directory

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

    def setProjectName(self,variable):
        self._projectName=variable
        return self._projectName
    def getProjectName(self):
        return self._projectName

    #Public Function
    def createProject(self,absoluteDirectory=None,relativeDirectory=None,projectName=None):
        _absoluteDirectory=absoluteDirectory or self._absoluteDirectory
        _relativeDirectory=relativeDirectory or self._relativeDirectory
        _projectName=projectName or self._projectName

        #self._isPathAndSamePath_check_func(self._path,self._projectName)
        projectDirectory=self.projectDirectory_create_str(_absoluteDirectory,_relativeDirectory,_projectName)
        workDirectory=self.setProject_edit_str(projectDirectory,create=True)
        return workDirectory

    def editProject(self,absoluteDirectory=None,relativeDirectory=None,projectName=None):
        _absoluteDirectory=absoluteDirectory or self._absoluteDirectory
        _relativeDirectory=relativeDirectory or self._relativeDirectory
        _projectName=projectName or self._projectName
        
        #self._isPathAndSamePath_check_func(self._path,self._projectName)
        projectDirectory=self.projectDirectory_create_str(_absoluteDirectory,_relativeDirectory,_projectName)
        workDirectory=self.setProject_edit_str(projectDirectory)
        return workDirectory
 
class File():
    def __init__(self):
        self._fileType_dict=RULE_DICT["fileType_dict"]

        self._absoluteDirectory=None
        self._relativeDirectory=None
        self._file=None
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