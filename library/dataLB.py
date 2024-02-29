# -*- coding: iso-8859-15 -*-
import os
import cgInTools as cit
from . import baseLB as bLB
cit.reloads([bLB])

class DataPath(bLB.DataOrigin):
    def __init__(self,dataPath=None):
        super(DataPath,self).__init__()
        if dataPath is None:
            self._absolute_dir=None
            self._relative_dir=None
            self._file_str=None
            self._extension_ext=None
        elif type(dataPath) is DataPath:
            self._absolute_dir=dataPath.getAbsoluteDirectory()
            self._relative_dir=dataPath.getRelativeDirectory()
            self._file_str=dataPath.getFile()
            self._extension_ext=dataPath.getExtension()

    @staticmethod
    def mergeDirectory_create_dir(upperDirectory_dir,lowerDirectory_dir):
        if upperDirectory_dir is None:
            upperDirectory_dir=""
        if lowerDirectory_dir is None:
            lowerDirectory_dir=""
        mergeDirectory_dir=os.path.join(upperDirectory_dir,lowerDirectory_dir)
        mergeDirectory_dir=mergeDirectory_dir.replace(os.sep,'/')
        return mergeDirectory_dir
    
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
