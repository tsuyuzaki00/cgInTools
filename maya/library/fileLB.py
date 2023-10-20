# -*- coding: iso-8859-15 -*-
import os
import shutil
import maya.cmds as cmds
import maya.api.OpenMaya as om2

import cgInTools as cit
from ...library import jsonLB as jLB
from ...library import pathLB as pLB
from ...library import baseLB as bLB
from . import cleanLB as cLB
cit.reloads([jLB,pLB,bLB,cLB])

RULE_DICT=jLB.readJson(cit.mayaSettings_dir,"library")
PROJECTFOLDER=cit.mayaDefSetProject_dir

class SelfProject(bLB.SelfOrigin):
    def __init__(self):
        self._defSetProjectFolder=PROJECTFOLDER
        self._project_DataPath=pLB.DataPath()
        self._project_SelfPath=pLB.SelfPath()
    
    def __str__(self):
        self._project_SelfPath.setDataPath(self._project_DataPath)
        project_dir=self._project_SelfPath.queryDirectory()
        return project_dir

    #Single Function
    def setProject_edit_str(self,project_dir,create=False):
        if create:
            shutil.copytree(self._defSetProjectFolder,project_dir)
        cmds.workspace(project_dir,o=True)
        project_dir=cmds.workspace(q=True,rd=True)
        return project_dir

    #Setting Function
    def setDataPath(self,variable):
        self._project_DataPath=variable
        return self._project_DataPath
    def currentDataPath(self):
        project_dir=cmds.workspace(q=True,rd=True)
        
        absoluteDirectorys=project_dir.split("/")[:-2]
        absolute_dir=os.path.join(*absoluteDirectorys)
        self._project_DataPath.setAbsoluteDirectory(absolute_dir)
        
        projectName_str=project_dir.split("/")[-2]
        self._project_DataPath.setRelativeDirectory(projectName_str)
        return self._project_DataPath
    def getDataPath(self):
        return self._project_DataPath

    #Public Function
    def createProject(self,dataPath=None):
        _project_DataPath=dataPath or self._project_DataPath

        self._project_SelfPath.setDataPath(_project_DataPath)
        project_dir=self._project_SelfPath.queryDirectory()
        workSpace_dir=self.setProject_edit_str(project_dir,create=True)
        return workSpace_dir

    def editProject(self,dataPath=None):
        _project_DataPath=dataPath or self._project_DataPath
        
        self._project_SelfPath.setDataPath(_project_DataPath)
        project_dir=self._project_SelfPath.queryDirectory()
        workSpace_dir=self.setProject_edit_str(project_dir)
        return workSpace_dir

    def queryProject(self):
        self._project_SelfPath.setDataPath(self._project_DataPath)
        project_dir=self._project_SelfPath.queryDirectory()
        return project_dir
 
class SelfFile():
    def __init__(self):
        self._file_DataPath=pLB.DataPath()
        self._file_SelfPath=pLB.SelfPath()

        self._fileType_dict=RULE_DICT["fileType_dict"]
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
    def setDataPath(self,variable):
        self._project_DataPath=variable
        return self._project_DataPath
    def getDataPath(self):
        return self._project_DataPath

    def setExType(self,variable):
        self._exType=variable
        return self._exType
    def getExType(self):
        return self._exType

    #Public Function
    def addPath(self,variable):
        addPath=os.path.abspath(os.path.join(self._path,variable))
        return addPath

    def save(self,dataPath=None):
        _file_DataPath=dataPath or self._file_DataPath
        self._file_SelfPath.setDataPath(_file_DataPath)

        file_dir=self._file_SelfPath.queryDirectory()
        file_str=self._file_DataPath.getFile()
        exType_str=self._fileType_dict.get(self._file_DataPath.getExtension())
        self.fileSave_edit_func(file_dir,file_str,exType_str)

    def open(self,dataPath=None):
        _file_DataPath=dataPath or self._file_DataPath
        self._file_SelfPath.setDataPath(_file_DataPath)

        file_dir=self._file_SelfPath.queryDirectory()
        file_str=self._file_DataPath.getFile()
        file_ext=self._file_DataPath.getExtension()

        self.fileOpen_edit_func(file_dir,file_str,file_ext)

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