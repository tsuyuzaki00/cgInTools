# -*- coding: iso-8859-15 -*-
import json
import cgInTools as cit
from . import pathLB as pLB
cit.reloads([pLB])

class SelfJson(object):
    def __init__(self):
        self._json_SelfPath=pLB.SelfPath()
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
    def setDataPath(self,variable):
        variable.setExtension("json")
        self._json_SelfPath=pLB.SelfPath()
        self._json_SelfPath.setDataPath(variable)
        return self._json_SelfPath.getDataPath()
    def getDataPath(self):
        return self._json_SelfPath.getDataPath()
    
    def setWriteDict(self,variable):
        self._write_dict=variable
        return self._write_dict
    def getWriteDict(self):
        return self._write_dict

    #Public Function
    def read(self,absolute=None,relative=None,file=None,extension=None):
        absolute_path=self._json_SelfPath.queryAbsolutePath(absolute,relative,file,extension)
        read_dict=self.jsonPath_query_dict(absolute_path)
        return read_dict

    def write(self,absolute=None,relative=None,file=None,extension=None,write=None):
        _write_dict=write or self._write_dict

        absolute_path=self._json_SelfPath.queryAbsolutePath(absolute,relative,file,extension)
        self.jsonPath_create_func(absolute_path,_write_dict)
    
class AppJsonPack(object):
    def __init__(self):
        self._jsonPack_SelfJson=SelfJson()
        self._writePack_SelfJsons=[]

    #Private Function
    def __readPack_query_dicts(self,pack_SelfJson):
        pack_dict=pack_SelfJson.read()

        read_dicts=[]
        for fileEX_dict in pack_dict["packFiles"]:
            read_DataJson=pLB.DataPath()
            read_DataJson.setAbsoluteDirectory(pack_SelfJson.getDataPath().getAbsoluteDirectory())
            read_DataJson.setRelativeDirectory(pack_SelfJson.getDataPath().getRelativeDirectory())
            read_DataJson.setFile(fileEX_dict["file"])
            read_DataJson.setExtension(fileEX_dict["extension"])

            read_SelfJson=SelfJson()
            read_SelfJson.setDataPath()
            read_dict=read_SelfJson.read()
            read_dicts+=read_dict
        return read_dicts

    def __writePack_create_func(self,pack_SelfJson,write_SelfJsons):
        packFiles=[]
        for write_SelfJson in write_SelfJsons:
            write_SelfJson.write()
            
            write_DataPath=write_SelfJson.getDataPath()
            file_str=write_DataPath.getFile()
            extension_str=write_DataPath.getExtension()
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
    data_DataPath=pLB.DataPath()
    data_DataPath.setAbsoluteDirectory(directory)
    data_DataPath.setFile(file)
    data_DataPath.setExtension("json")

    data_SelfJson=SelfJson()
    data_SelfJson.setDataPath(data_DataPath)
    json_dict=data_SelfJson.read()
    return json_dict

def writeJson(directory,file,write):
    data_DataPath=pLB.DataPath()
    data_DataPath.setAbsoluteDirectory(directory)
    data_DataPath.setFile(file)
    data_DataPath.setExtension("json")

    data_SelfJson=SelfJson()
    data_SelfJson.setDataPath(data_DataPath)
    data_SelfJson.setWriteDict(write)
    data_SelfJson.write()