# -*- coding: iso-8859-15 -*-
import json
import cgInTools as cit
from . import pathLB as pLB
cit.reloads([pLB])

class AppJson(object):
    def __init__(self):
        self._path_DataPath=None
        self._json_dict={}

    #Single Function
    def jsonPath_query_dict(self,path):
        with open(path,"r") as f:
            read_dict=json.load(f)
            return read_dict
            
    def jsonPath_create_func(self,path,write_dict):
        with open(path,"w") as f:
            json.dump(write_dict,f,indent=4,ensure_ascii=False)

    #Setting Function
    def setDataPath(self,variable):
        self._path_DataPath=variable
        return self._path_DataPath
    def getDataPath(self):
        return self._path_DataPath

    def setJsonDict(self,variable):
        self._json_dict=variable
        return self._json_dict
    def getJsonDict(self):
        return self._json_dict
    
    #Public Function
    def read(self,dataPath=None):
        _path_DataPath=dataPath or self._path_DataPath
        
        path_AppPath=pLB.AppPath()
        absolute_path=path_AppPath.queryAbsolutePath(_path_DataPath)
        read_dict=self.jsonPath_query_dict(absolute_path)
        return read_dict

    def write(self,dataPath=None,jsonDict=None):
        _path_DataPath=dataPath or self._path_DataPath
        _json_dict=jsonDict or self._json_dict

        path_AppPath=pLB.AppPath()
        path_AppPath.setDataPath(_path_DataPath)
        absolute_path=path_AppPath.queryAbsolutePath()
        self.jsonPath_create_func(absolute_path,_json_dict)

    def check(self,dataPath=None):
        _path_DataPath=dataPath or self._path_DataPath

        path_AppPath=pLB.AppPath()
        path_AppPath.setDataPath(_path_DataPath)
        absolutePath_bool=path_AppPath.checkAbsolutePath()
        return absolutePath_bool

def textParaGraph(text_dict,indent=4):
    text_str=json.dumps(text_dict,indent=indent)
    return text_str