# -*- coding: iso-8859-15 -*-
import os,shutil

class Path(object):
    def __init__(self):
        self._absolute_dir=None
        self._relative_dir=None
        self._file_str=None
        self._extension_ext=None

        self._target_Path=None
        self._source_Path=None

    def __str__(self):
        absolutePath_path=self.queryAbsolutePath()
        return absolutePath_path

    def __rshift__(self,variable):
        self.targetPathMove(variable)

    def __irshift__(self,variable):
        self.targetPathCopy(variable)

    def __lshift__(self,variable):
        self.sourcePathMove(variable)
    
    def __ilshift__(self,variable):
        self.sourcePathCopy(variable)

    #Single Function
    def mergeDirectory_create_dir(self,upperDirectory_dir,lowerDirectory_dir):
        if upperDirectory_dir is None:
            upperDirectory_dir=""
        if lowerDirectory_dir is None:
            lowerDirectory_dir=""
        mergeDirectory_dir=os.path.join(upperDirectory_dir,lowerDirectory_dir)
        mergeDirectory_dir=mergeDirectory_dir.replace(os.sep,'/')
        return mergeDirectory_dir

    def mergePath_create_path(self,directory_dir,file_str,extension_ext):
        if file_str is None or extension_ext is None:
            return directory_dir
        else:
            mergePath_path=os.path.join(directory_dir,file_str+"."+extension_ext)
            mergePath_path=mergePath_path.replace(os.sep,'/')
        return mergePath_path

    #Setting Function
    def setAbsoluteDirectory(self,variable):
        self._absolute_dir=variable
        return self._absolute_dir
    def addAbsoluteDirectory(self,variable):
        self._absolute_dir=self.mergeDirectory_create_dir(self._absolute_dir,variable)
        return self._absolute_dir
    def getAbsoluteDirectory(self):
        return self._absolute_dir
    
    def setRelativeDirectory(self,variable):
        self._relative_dir=variable
        return self._relative_dir
    def addRelativeDirectory(self,variable):
        self._relative_dir=self.mergeDirectory_create_dir(self._relative_dir,variable)
        return self._relative_dir
    def getRelativeDirectory(self):
        return self._relative_dir

    def setFile(self,variable):
        self._file_str=variable
        return self._file_str
    def getFile(self):
        return self._file_str
    
    def setExtension(self,variable):
        self._extension_ext=variable
        return self._extension_ext
    def getExtension(self):
        return self._extension_ext

    def setTargetPath(self,variable):
        self._target_Path=variable
        return self._target_Path
    def getTargetPath(self):
        return self._target_Path

    def setSourcePath(self,variable):
        self._source_Path=variable
        return self._source_Path
    def getSourcePath(self):
        return self._source_Path

    #Public Function
    def queryDirectory(self,absolute=None,relative=None):
        _absolute_dir=absolute or self._absolute_dir
        _relative_dir=relative or self._relative_dir

        mergeDirectory_dir=self.mergeDirectory_create_dir(_absolute_dir,_relative_dir)
        return mergeDirectory_dir

    def queryAbsolutePath(self,absolute=None,relative=None,file=None,ext=None):
        _absolute_dir=absolute or self._absolute_dir
        _relative_dir=relative or self._relative_dir
        _file_str=file or self._file_str
        _extension_ext=ext or self._extension_ext

        mergeDirectory_dir=self.mergeDirectory_create_dir(_absolute_dir,_relative_dir)
        absolutePath_path=self.mergePath_create_path(mergeDirectory_dir,_file_str,_extension_ext)
        return absolutePath_path
    
    def queryRelativePath(self,relative=None,file=None,ext=None):
        _relative_dir=relative or self._relative_dir
        _file_str=file or self._file_str
        _extension_ext=ext or self._extension_ext

        relativePath_path=self.mergePath_create_path(_relative_dir,_file_str,_extension_ext)
        return relativePath_path
    
    def querySequencePath(self,absolute=None,relative=None,file=None,ext=None):
        _absolute_dir=absolute or self._absolute_dir
        _relative_dir=relative or self._relative_dir
        _file_str=file or self._file_str
        _extension_ext=ext or self._extension_ext

        mergeDirectory_dir=self.mergeDirectory_create_dir(_absolute_dir,_relative_dir)
        splitDirectorys=mergeDirectory_dir.split("/")
        splitDirectorys.append(_file_str)
        splitDirectorys.append(_extension_ext)
        return splitDirectorys

    def createFileExt(self,absolute=None,relative=None,file=None,ext=None):
        _absolute_dir=absolute or self._absolute_dir
        _relative_dir=relative or self._relative_dir
        _file_str=file or self._file_str
        _extension_ext=ext or self._extension_ext

        mergeDirectory_dir=self.mergeDirectory_create_dir(_absolute_dir,_relative_dir)
        absolutePath_path=self.mergePath_create_path(mergeDirectory_dir,_file_str,_extension_ext)
        with open(absolutePath_path,'w') as f:
            pass
    
    def deleteFileExt(self,absolute=None,relative=None,file=None,ext=None):
        _absolute_dir=absolute or self._absolute_dir
        _relative_dir=relative or self._relative_dir
        _file_str=file or self._file_str
        _extension_ext=ext or self._extension_ext

        mergeDirectory_dir=self.mergeDirectory_create_dir(_absolute_dir,_relative_dir)
        absolutePath_path=self.mergePath_create_path(mergeDirectory_dir,_file_str,_extension_ext)
        os.remove(absolutePath_path)
    
    def createDirectory(self,absolute=None,relative=None):
        _absolute_dir=absolute or self._absolute_dir
        _relative_dir=relative or self._relative_dir

        mergeDirectory_dir=self.mergeDirectory_create_dir(_absolute_dir,_relative_dir)
        if not os.path.exists(mergeDirectory_dir) and not os.path.isdir(mergeDirectory_dir):
            os.makedirs(mergeDirectory_dir)

    def createEnvironmentVariable(self,directory=None,environName=None):
        _absolute_dir=directory or self._absolute_dir
        _relative_dir=environName or self._relative_dir

        mergeDirectory_dir=self.mergeDirectory_create_dir(_absolute_dir,_relative_dir)
        environRename_str=_relative_dir.replace("/","_").replace("\\","_").upper()
        os.environ[environRename_str+"_DIRECTORY"]=os.path.join(mergeDirectory_dir)
        return mergeDirectory_dir

    def targetPathMove(self,targetPath=None,absolute=None,relative=None,file=None,ext=None):
        _targetPath_Path=targetPath or self._target_Path
        _absolute_dir=absolute or self._absolute_dir
        _relative_dir=relative or self._relative_dir
        _file_str=file or self._file_str
        _extension_ext=ext or self._extension_ext

        mergeDirectory_dir=self.mergeDirectory_create_dir(_absolute_dir,_relative_dir)
        absolutePath_path=self.mergePath_create_path(mergeDirectory_dir,_file_str,_extension_ext)
        shutil.move(absolutePath_path,str(_targetPath_Path))

    def targetPathCopy(self,targetPath=None,absolute=None,relative=None,file=None,ext=None):
        _targetPath_Path=targetPath or self._target_Path
        _absolute_dir=absolute or self._absolute_dir
        _relative_dir=relative or self._relative_dir
        _file_str=file or self._file_str
        _extension_ext=ext or self._extension_ext

        mergeDirectory_dir=self.mergeDirectory_create_dir(_absolute_dir,_relative_dir)
        absolutePath_path=self.mergePath_create_path(mergeDirectory_dir,_file_str,_extension_ext)
        shutil.copy2(absolutePath_path,str(_targetPath_Path))

    def sourcePathMove(self,sourcePath=None,absolute=None,relative=None,file=None,ext=None):
        _sourcePath_Path=sourcePath or self._source_Path
        _absolute_dir=absolute or self._absolute_dir
        _relative_dir=relative or self._relative_dir
        _file_str=file or self._file_str
        _extension_ext=ext or self._extension_ext

        mergeDirectory_dir=self.mergeDirectory_create_dir(_absolute_dir,_relative_dir)
        absolutePath_path=self.mergePath_create_path(mergeDirectory_dir,_file_str,_extension_ext)
        shutil.move(str(_sourcePath_Path),absolutePath_path)

    def sourcePathCopy(self,sourcePath=None,absolute=None,relative=None,file=None,ext=None):
        _sourcePath_Path=sourcePath or self._source_Path
        _absolute_dir=absolute or self._absolute_dir
        _relative_dir=relative or self._relative_dir
        _file_str=file or self._file_str
        _extension_ext=ext or self._extension_ext

        mergeDirectory_dir=self.mergeDirectory_create_dir(_absolute_dir,_relative_dir)
        absolutePath_path=self.mergePath_create_path(mergeDirectory_dir,_file_str,_extension_ext)
        shutil.copy2(str(_sourcePath_Path),absolutePath_path)