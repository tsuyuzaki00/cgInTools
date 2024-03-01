# -*- coding: iso-8859-15 -*-
import os,shutil

class AppPath(object):
    def __init__(self):
        self._path_DataPath=None
        self._destination_DataPath=None

    def __str__(self):
        absolutePath_path=self.queryAbsolutePath()
        return absolutePath_path

    def __rshift__(self,variable):
        self.destinationDataPathMove(destination_DataPath=variable)

    def __irshift__(self,variable):
        self.destinationDataPathCopy(destination_DataPath=variable)

    def __lshift__(self,variable):
        self.destinationDataPathMove(dataPath=variable)
    
    def __ilshift__(self,variable):
        self.destinationDataPathCopy(dataPath=variable)

    #Single Function
    @staticmethod
    def mergeDirectory_create_dir(upperDirectory_dir,lowerDirectory_dir):
        if upperDirectory_dir is None:
            upperDirectory_dir=""
        if lowerDirectory_dir is None:
            lowerDirectory_dir=""
        mergeDirectory_dir=os.path.join(upperDirectory_dir,lowerDirectory_dir)
        mergeDirectory_dir=mergeDirectory_dir.replace(os.sep,'/')
        return mergeDirectory_dir

    @staticmethod
    def mergePath_create_path(directory_dir,file_str,extension_ext):
        if file_str is None or extension_ext is None:
            return directory_dir
        else:
            mergePath_path=os.path.join(directory_dir,file_str+"."+extension_ext)
            mergePath_path=mergePath_path.replace(os.sep,'/')
        return mergePath_path

    @staticmethod
    def folder_query_dicts(directory_dir):
        fileExt_strs=[f for f in os.listdir(directory_dir) if os.path.isfile(os.path.join(directory_dir,f)) and not f in "init.json"]
        fileExt_dicts=[{"file":fileExt_str.split(".")[0],"extension":fileExt_str.split(".")[-1]} for fileExt_str in fileExt_strs]
        return fileExt_dicts

    #Multi Function
    def _dataPathToAbsolutePath_create_path(self,path_DataPath):
        mergeDirectory_dir=self.mergeDirectory_create_dir(path_DataPath.getAbsoluteDirectory(),path_DataPath.getRelativeDirectory())
        absolutePath_path=self.mergePath_create_path(mergeDirectory_dir,path_DataPath.getFile(),path_DataPath.getExtension())
        return absolutePath_path

    #Setting Function
    def setDataPath(self,variable):
        self._path_DataPath=variable
        return self._path_DataPath
    def getDataPath(self):
        return self._path_DataPath
    
    def setDestinationDataPath(self,variable):
        self._destination_DataPath=variable
        return self._destination_DataPath
    def getDestinationDataPath(self):
        return self._destination_DataPath
    
    #Public Function
    def createFileExt(self,dataPath=None):
        _path_DataPath=dataPath or self._path_DataPath

        absolutePath_path=self._dataPathToAbsolutePath_create_path(_path_DataPath)
        with open(absolutePath_path,'w') as f:
            pass
    
    def deleteFileExt(self,dataPath=None):
        _path_DataPath=dataPath or self._path_DataPath

        absolutePath_path=self._dataPathToAbsolutePath_create_path(_path_DataPath)
        os.remove(absolutePath_path)
    
    def createDirectory(self,dataPath=None):
        _path_DataPath=dataPath or self._path_DataPath

        mergeDirectory_dir=self.mergeDirectory_create_dir(_path_DataPath.getAbsoluteDirectory(),_path_DataPath.getRelativeDirectory())
        if not os.path.exists(mergeDirectory_dir) and not os.path.isdir(mergeDirectory_dir):
            os.makedirs(mergeDirectory_dir)

    def createEnvironmentVariable(self,dataPath=None):
        _path_DataPath=dataPath or self._path_DataPath

        mergeDirectory_dir=self.mergeDirectory_create_dir(_path_DataPath.getAbsoluteDirectory(),_path_DataPath.getRelativeDirectory())
        environRename_str=_path_DataPath.getRelativeDirectory().replace("/","_").replace("\\","_").upper()
        os.environ[environRename_str+"_DIRECTORY"]=os.path.join(mergeDirectory_dir)
        return mergeDirectory_dir

    def checkDirectory(self,dataPath=None):
        _path_DataPath=dataPath or self._path_DataPath

        mergeDirectory_dir=self.mergeDirectory_create_dir(_path_DataPath.getAbsoluteDirectory(),_path_DataPath.getRelativeDirectory())
        isDirectory_bool=os.path.isdir(mergeDirectory_dir)
        return isDirectory_bool
    
    def checkAbsolutePath(self,dataPath=None):
        _path_DataPath=dataPath or self._path_DataPath

        absolutePath_path=self._dataPathToAbsolutePath_create_path(_path_DataPath)
        isAbsolutePath_bool=os.path.exists(absolutePath_path)
        return isAbsolutePath_bool

    def destinationDataPathMove(self,dataPath=None,destination_DataPath=None):
        _path_DataPath=dataPath or self._path_DataPath
        _destination_DataPath=destination_DataPath or self._destination_DataPath

        absolutePath_path=self._dataPathToAbsolutePath_create_path(_path_DataPath)
        absolutePathTarget_path=self._dataPathToAbsolutePath_create_path(_destination_DataPath)

        shutil.move(absolutePath_path,absolutePathTarget_path)

    def destinationDataPathCopy(self,dataPath=None,destination_DataPath=None,):
        _path_DataPath=dataPath or self._path_DataPath
        _destination_DataPath=destination_DataPath or self._destination_DataPath

        absolutePath_path=self._dataPathToAbsolutePath_create_path(_path_DataPath)
        absolutePathTarget_path=self._dataPathToAbsolutePath_create_path(_destination_DataPath)
        
        shutil.copy2(absolutePath_path,absolutePathTarget_path)

    def queryDirectory(self,dataPath=None):
        _path_DataPath=dataPath or self._path_DataPath

        mergeDirectory_dir=self.mergeDirectory_create_dir(_path_DataPath.getAbsoluteDirectory(),_path_DataPath.getRelativeDirectory())
        return mergeDirectory_dir

    def queryAbsolutePath(self,dataPath=None):
        _path_DataPath=dataPath or self._path_DataPath

        absolutePath_path=self._dataPathToAbsolutePath_create_path(_path_DataPath)
        return absolutePath_path
    
    def queryRelativePath(self,dataPath=None):
        _path_DataPath=dataPath or self._path_DataPath
        
        relativePath_path=self.mergePath_create_path(_path_DataPath.getRelativeDirectory(),_path_DataPath.getFile(),_path_DataPath.getExtension())
        return relativePath_path
    
    def querySequencePath(self,dataPath=None):
        _path_DataPath=dataPath or self._path_DataPath

        mergeDirectory_dir=self.mergeDirectory_create_dir(_path_DataPath.getAbsoluteDirectory(),_path_DataPath.getRelativeDirectory())
        splitDirectorys=mergeDirectory_dir.split("/")
        splitDirectorys.append(_path_DataPath.getFile())
        splitDirectorys.append(_path_DataPath.getExtension())
        return splitDirectorys

    def queryInFolder(self,dataPath=None):
        _path_DataPath=dataPath or self._path_DataPath

        absolute_dir=_path_DataPath.getAbsoluteDirectory()
        relative_dir=_path_DataPath.getRelativeDirectory()
        directory_dir=self.mergeDirectory_create_dir(absolute_dir,relative_dir)
        fileExt_dicts=self.folder_query_dicts(directory_dir)

        import cgInTools as cit
        from . import dataLB as dLB
        cit.reloads([dLB])
        folder_DataPaths=[]

        for fileExt_dict in fileExt_dicts:
            folder_DataPath=dLB.DataPath()
            folder_DataPath.setAbsoluteDirectory(absolute_dir)
            folder_DataPath.setRelativeDirectory(relative_dir)
            folder_DataPath.setFile(fileExt_dict.get("file"))
            folder_DataPath.setExtension(fileExt_dict.get("extension"))
        
            folder_DataPaths.append(folder_DataPath)
        return folder_DataPaths