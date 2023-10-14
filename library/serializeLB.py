# -*- coding: iso-8859-15 -*-
import pickle
import cgInTools as cit
from . import pathLB as pLB
cit.reloads([pLB])

class SelfSerialize(object):
    def __init__(self):
        self._selfpy_SelfPath=pLB.SelfPath()
        self._write_SelfObject=None

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
        variable.setExtension("selfpy")
        self._selfpy_SelfPath=pLB.SelfPath()
        self._selfpy_SelfPath.setDataPath(variable)
        return self._selfpy_SelfPath.getDataPath()
    def getDataPath(self):
        return self._selfpy_SelfPath
    
    def setWriteSelfObject(self,variable):
        self._write_SelfObject=variable
        return self._write_SelfObject
    def getWriteSelfObject(self):
        return self._write_SelfObject

    #Public Function
    def read(self,absolute=None,relative=None,file=None,extension=None):
        absolute_path=self._selfpy_SelfPath.queryAbsolutePath(absolute,relative,file,extension)
        read_SelfObject=self.serialize_query_SelfObject(absolute_path)
        return read_SelfObject

    def write(self,absolute=None,relative=None,file=None,extension=None,selfObject=None):
        _write_SelfObject=selfObject or self._write_SelfObject

        absolute_path=self._selfpy_SelfPath.queryAbsolutePath(absolute,relative,file,extension)
        self.serialize_create_func(absolute_path,_write_SelfObject)

def readSelfObject(directory,file):
    data_DataPath=pLB.DataPath()
    data_DataPath.setAbsoluteDirectory(directory)
    data_DataPath.setFile(file)
    data_DataPath.setExtension("selfpy")

    data_SelfObject=SelfSerialize()
    data_SelfObject.setDataPath(data_DataPath)
    selfpy_SelfObject=data_SelfObject.read()
    return selfpy_SelfObject

def writeSelfObject(directory,file,write):
    data_DataPath=pLB.DataPath()
    data_DataPath.setAbsoluteDirectory(directory)
    data_DataPath.setFile(file)
    data_DataPath.setExtension("selfpy")
    
    data_SelfObject=SelfSerialize()
    data_SelfObject.setDataPath(data_DataPath)
    data_SelfObject.setWriteSelfObject(write)
    data_SelfObject.write()