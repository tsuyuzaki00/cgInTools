# -*- coding: iso-8859-15 -*-
import pickle
import cgInTools as cit
from . import pathLB as pLB
cit.reloads([pLB])

class SelfSerialize(object):
    def __init__(self):
        self._selfpy_SelfPath=pLB.SelfPath()
        self._write_SelfObject=None
        self._write_SelfObjects=[]

    #Single Function
    def serialize_query_SelfObject(self,path):
        with open(path,'rb') as f:
            object_SelfObject=pickle.load(f)
            return object_SelfObject

    def serialize_create_func(self,path,object):
        with open(path,'wb') as f:
            pickle.dump(object,f)

    #Setting Function
    def setDataPath(self,variable):
        self._selfpy_SelfPath.setDataPath(variable)
        return self._selfpy_SelfPath.getDataPath()
    def getDataPath(self):
        return self._selfpy_SelfPath.getDataPath()
    
    def setWriteSelfObject(self,variable):
        self._write_SelfObject=variable
        return self._write_SelfObject
    def getWriteSelfObject(self):
        return self._write_SelfObject

    def setWriteSelfObjects(self,variables):
        self._write_SelfObjects=variables
        return self._write_SelfObjects
    def addWriteSelfObjects(self,variables):
        self._write_SelfObjects+=variables
        return self._write_SelfObjects
    def getWriteSelfObjects(self):
        return self._write_SelfObjects

    #Public Function
    def read(self,dataPath=None):
        absolute_path=self._selfpy_SelfPath.queryAbsolutePath(dataPath)
        read_SelfObject=self.serialize_query_SelfObject(absolute_path)
        return read_SelfObject

    def write(self,dataPath=None,selfObject=None):
        _write_SelfObject=selfObject or self._write_SelfObject

        absolute_path=self._selfpy_SelfPath.queryAbsolutePath(dataPath)
        self.serialize_create_func(absolute_path,_write_SelfObject)

    def writes(self,dataPath=None,selfObjects=None):
        _write_SelfObjects=selfObjects or self._write_SelfObjects

        absolute_path=self._selfpy_SelfPath.queryAbsolutePath(dataPath)
        self.serialize_create_func(absolute_path,_write_SelfObjects)


def readSelfObject(directory,file,extension="selfpy"):
    data_DataPath=pLB.DataPath()
    data_DataPath.setAbsoluteDirectory(directory)
    data_DataPath.setFile(file)
    data_DataPath.setExtension(extension)

    data_SelfObject=SelfSerialize()
    data_SelfObject.setDataPath(data_DataPath)
    selfpy_SelfObject=data_SelfObject.read()
    return selfpy_SelfObject

def writeSelfObject(directory,file,extension="selfpy",write=None):
    data_DataPath=pLB.DataPath()
    data_DataPath.setAbsoluteDirectory(directory)
    data_DataPath.setFile(file)
    data_DataPath.setExtension(extension)
    
    data_SelfObject=SelfSerialize()
    data_SelfObject.setDataPath(data_DataPath)
    data_SelfObject.setWriteSelfObject(write)
    data_SelfObject.write()

def writeSelfObjects(directory,file,extension="selfpyPack",writes=[]):
    data_DataPath=pLB.DataPath()
    data_DataPath.setAbsoluteDirectory(directory)
    data_DataPath.setFile(file)
    data_DataPath.setExtension(extension)
    
    data_SelfObject=SelfSerialize()
    data_SelfObject.setDataPath(data_DataPath)
    data_SelfObject.setWriteSelfObjects(writes)
    data_SelfObject.writes()