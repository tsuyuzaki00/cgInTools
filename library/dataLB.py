# -*- coding: iso-8859-15 -*-
import os
import cgInTools as cit
from . import baseLB as bLB
cit.reloads([bLB])

#Definition Data
class DataPath(bLB.SelfOrigin):
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

    #Single Function
    def mergeDirectory_create_dir(self,upperDirectory_dir,lowerDirectory_dir):
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

class DataJson(DataPath):
    def __init__(self,dataJson=None):
        super(DataJson,self).__init__(dataJson)
        if dataJson is None:
            self._json_dict={}
        elif type(dataJson) is DataJson:
            self._json_dict=dataJson.getJsonDict()

    #Setting Function
    def setJsonDict(self,variable):
        self._json_dict=variable
        return self._json_dict
    def getJsonDict(self):
        return self._json_dict
    
class DataSerialize(DataPath):
    def __init__(self,dataSerialize=None):
        super(DataSerialize,self).__init__(dataSerialize)
        if dataSerialize is None:
            self._selfpy_ClassSelf=None
        elif type(dataSerialize) is DataSerialize:
            self._selfpy_ClassSelf=dataSerialize.getClassSelf()

    #Setting Function
    def setClassSelf(self,variable):
        self._selfpy_ClassSelf=variable
        return self._selfpy_ClassSelf
    def getClassSelf(self):
        return self._selfpy_ClassSelf

#DefinitionArray Data
class DataPathArray(bLB.SelfOrigin):
    def __init__(self,dataPathArray=None):
        super(DataPathArray,self).__init__()
        if dataPathArray is None:
            self._path_DataPathArray=None
        if type(dataPathArray) is DataPathArray:
            self._path_DataPathArray=dataPathArray.getDataPaths()

    #Setting Function
    def setDataPaths(self,variables):
        self._json_DataPaths=variables
        return self._json_DataPaths
    def addDataPaths(self,variables):
        self._json_DataPaths+=variables
        return self._json_DataPaths
    def getDataPaths(self):
        return self._json_DataPaths

class DataJsonArray(bLB.SelfOrigin):
    def __init__(self,dataJsonArray=None):
        super(DataJsonArray,self).__init__(dataJsonArray)
        if dataJsonArray is None:
            self._json_DataPath=None
            self._json_DataJsons=[]
        elif type(dataJsonArray) is DataJsonArray:
            self._json_DataPath=dataJsonArray.getDataPath()
            self._json_DataJsons=dataJsonArray.getDataJsons()

    #Setting Function
    def setDataPath(self,variable):
        self._json_DataPath=variable
        return self._json_DataPath
    def getDataPath(self):
        return self._json_DataPath
    
    def setDataJsons(self,variables):
        self._json_DataJsons=variables
        return self._json_DataJsons
    def addDataJsons(self,variables):
        self._json_DataJsons+=variables
        return self._json_DataJsons
    def getDataJsons(self):
        return self._json_DataJsons

class DataSerializeArray(bLB.SelfOrigin):
    def __init__(self,dataSerializeArray=None):
        super(DataSerializeArray,self).__init__(dataSerializeArray)
        if dataSerializeArray is None:
            self._selfpy_DataPath=None
            self._selfpy_DataSerializes=[]
        elif type(dataSerializeArray) is DataSerializeArray:
            self._selfpy_DataPath=dataSerializeArray.getDataPath()
            self._selfpy_DataSerializes=dataSerializeArray.getDataSerializes()

    #Setting Function
    def setDataPath(self,variable):
        self._selfpy_DataPath=variable
        return self._selfpy_DataPath
    def getDataPath(self):
        return self._selfpy_DataPath
    
    def setDataSerializes(self,variables):
        self._selfpy_DataSerializes=variables
        return self._selfpy_DataSerializes
    def addDataSerializes(self,variables):
        self._selfpy_DataSerializes+=variables
        return self._selfpy_DataSerializes
    def getDataSerializes(self):
        return self._selfpy_DataSerializes