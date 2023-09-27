# -*- coding: iso-8859-15 -*-
import json
import cgInTools as cit
from . import baseLB as bLB
from . import pathLB as pLB
cit.reloads([bLB,pLB])

class SelfJson(bLB.SelfOrigin):
    def __init__(self):
        self._json_SelfPath=pLB.SelfPath()
        self._json_SelfPath.setExtension("json")
        self._write_dict={}

    #Single Function
    def jsonPath_query_dict(self,path):
        with open(path,"r") as f:
            read_dict=json.load(f)
            return read_dict
            
    def jsonPath_create_func(self,path,write_dict):
        with open(path,"w") as f:
            json.dump(write_dict,f,indent=4,ensure_ascii=False)

    #Setting Function
    def setAbsoluteDirectory(self,variable):
        _absoluteDirectory_str=self._json_SelfPath.setAbsoluteDirectory(variable)
        return _absoluteDirectory_str
    def getAbsoluteDirectory(self):
        return self._json_SelfPath.getAbsoluteDirectory()
    
    def setRelativeDirectory(self,variable):
        _relativeDirectory_str=self._json_SelfPath.setRelativeDirectory(variable)
        return _relativeDirectory_str
    def getRelativeDirectory(self):
        return self._json_SelfPath.getRelativeDirectory()

    def setFile(self,variable):
        _file_str=self._json_SelfPath.setFile(variable)
        return _file_str
    def getFile(self):
        return self._json_SelfPath.getFile()

    def setExtension(self,variable):
        _extension_str=self._json_SelfPath.setExtension(variable)
        return _extension_str
    def getExtension(self):
        return self._json_SelfPath.getExtension()

    def setWriteDict(self,variable):
        self._write_dict=variable
        return self._write_dict
    def getWriteDict(self):
        return self._write_dict

    def setDataPath(self,variable):
        self._json_SelfPath=pLB.SelfPath()
        self._json_SelfPath.setDataPath(variable)
        self._json_SelfPath.setExtension("json")
        return self._json_SelfPath
    def getDataPath(self):
        return self._json_SelfPath.getDataPath()

    #Public Function
    def read(self,absolute=None,relative=None,file=None,extension=None):
        absolute_path=self._json_SelfPath.queryAbsolutePath(absolute,relative,file,extension)
        read_dict=self.jsonPath_query_dict(absolute_path)
        return read_dict

    def write(self,absolute=None,relative=None,file=None,extension=None,write=None):
        _write_dict=write or self._write_dict

        absolute_path=self._json_SelfPath.queryAbsolutePath(absolute,relative,file,extension)
        self.jsonPath_create_func(absolute_path,_write_dict)
    
class AppJsonPack(bLB.SelfOrigin):
    def __init__(self):
        self._jsonPack_SelfJson=SelfJson()
        self._writePack_SelfJsons=[]

    #Private Function
    def __readPack_query_dicts(self,pack_SelfJson):
        pack_dict=pack_SelfJson.read()

        read_dicts=[]
        for fileEX_dict in pack_dict["packFiles"]:
            read_Json=SelfJson()
            pack_Json.setAbsoluteDirectory(pack_SelfJson.getAbsoluteDirectory())
            pack_Json.setRelativeDirectory(pack_SelfJson.getRelativeDirectory())
            read_Json.setFile(fileEX_dict["file"])
            read_Json.setExtension(fileEX_dict["extension"])
            read_dict=read_Json.read()
            read_dicts+=read_dict
        return read_dicts

    def __writePack_create_func(self,pack_SelfJson,write_SelfJsons):
        path_DataPath=path_SelfPath.getDataPath()

        packFiles=[]
        for write_SelfJson in write_SelfJsons:
            write_SelfJson.write()
            file_str=write_SelfJson.getFile()
            extension_str=write_SelfJson.getExtension()
            packFiles+={"file":file_str,"extension":extension_str}
        write_dict={"packFiles":packFiles}

        pack_SelfJson.setWriteDict(write_dict)
        pack_SelfJson.write()
    
    #Setting Function
    def setPackSelfJson(self,variable):
        self._jsonPack_SelfJson=variable
        return self._jsonPack_SelfJson
    def getPackSelfJson(self):
        return self._jsonPack_SelfJson

    def setSelfJsons(self,variables):
        self._writePack_SelfJsons=variables
        return self._writePack_SelfJsons
    def addSelfJsons(self,variables):
        self._writePack_SelfJsons+=variables
        return self._writePack_SelfJsons
    def getSelfJsons(self):
        return self._writePack_SelfJsons

    #Public Function
    def readPack(self,jsonPack_SelfJson=None):
        _jsonPack_SelfJson=jsonPack_SelfJson or self._jsonPack_SelfJson

        readPack_dicts=self.__readPack_query_dicts(_jsonPack_SelfJson)
        return readPack_dicts

    def writePack(self,jsonPack_SelfJson=None,write_SelfJsons=None):
        _jsonPack_SelfJson=jsonPack_SelfJson or self._jsonPack_SelfJson
        _writePack_SelfJsons=write_SelfJsons or self._writePack_SelfJsons

        self.__writePack_create_func(_jsonPack_SelfJson,_writePack_SelfJsons)

def readJson(directory,file):
    data=SelfJson()
    data.setAbsoluteDirectory(directory)
    data.setFile(file)
    data.setExtension("json")
    json_dict=data.read()
    return json_dict

def writeJson(directory,file,write):
    data=SelfJson()
    data.setAbsoluteDirectory(directory)
    data.setFile(file)
    data.setExtension("json")
    data.setWriteDict(write)
    data.write()