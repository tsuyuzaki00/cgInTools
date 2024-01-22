# -*- coding: iso-8859-15 -*-
import pickle
import cgInTools as cit
from . import pathLB as pLB
cit.reloads([pLB])

class AppSerialize(object):
    def __init__(self):
        self._path_DataPath=None
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
        self._path_DataPath=variable
        return self._path_DataPath
    def getDataPath(self):
        return self._path_DataPath
    
    def setWriteSelfObject(self,variable):
        self._write_SelfObject=variable
        return self._write_SelfObject
    def getWriteSelfObject(self):
        return self._write_SelfObject

    #Public Function
    def read(self,dataPath=None):
        _path_DataPath=dataPath or self._path_DataPath

        path_AppPath=pLB.AppPath()
        absolute_path=path_AppPath.queryAbsolutePath(_path_DataPath)
        read_SelfObject=self.serialize_query_SelfObject(absolute_path)
        return read_SelfObject

    def write(self,dataPath=None,selfObject=None):
        _path_DataPath=dataPath or self._path_DataPath
        _write_SelfObject=selfObject or self._write_SelfObject

        path_AppPath=pLB.AppPath()
        absolute_path=path_AppPath.queryAbsolutePath(_path_DataPath)
        self.serialize_create_func(absolute_path,_write_SelfObject)
