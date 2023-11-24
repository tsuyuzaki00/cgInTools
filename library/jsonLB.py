# -*- coding: iso-8859-15 -*-
import json
import cgInTools as cit
from . import dataLB as dLB
from . import pathLB as pLB
cit.reloads([pLB])

class AppJson(object):
    def __init__(self):
        self._json_DataJson=None#dLB.DataJson()

    #Single Function
    def jsonPath_query_dict(self,path):
        with open(path,"r") as f:
            read_dict=json.load(f)
            return read_dict
            
    def jsonPath_create_func(self,path,write_dict):
        with open(path,"w") as f:
            json.dump(write_dict,f,indent=4,ensure_ascii=False)

    #Setting Function
    def setDataJson(self,variable):
        self._json_DataJson=variable
        return self._json_DataJson
    def getDataJson(self):
        return self._json_DataJson
    
    #Public Function
    def read(self,dataJson=None):
        _json_DataJson=dataJson or self._json_DataJson
        
        json_AppPath=pLB.AppPath()
        absolute_path=json_AppPath.queryAbsolutePath(_json_DataJson)
        read_dict=self.jsonPath_query_dict(absolute_path)
        return read_dict

    def write(self,dataJson=None):
        _json_DataJson=dataJson or self._json_DataJson

        json_AppPath=pLB.AppPath()
        json_AppPath.setDataPath(_json_DataJson)
        absolute_path=json_AppPath.queryAbsolutePath()
        self.jsonPath_create_func(absolute_path,_json_DataJson.getJsonDict())

    def check(self,dataJson=None):
        _json_DataJson=dataJson or self._json_DataJson

        json_AppPath=pLB.AppPath()
        json_AppPath.setDataPath(_json_DataJson)
        absolutePath_bool=json_AppPath.checkAbsolutePath()
        return absolutePath_bool
    
class AppJsonArray(object):
    def __init__(self):
        self._jsonPack_DataJsonArray=None

    #Private Function
    def __readPack_query_dicts(self,_jsonPack_DataJsonArray):
        pack_DataPath=_jsonPack_DataJsonArray.getDataPath()
        pack_AppPath=pLB.AppPath()
        pack_AppPath.setDataPath(pack_DataPath)
        if pack_DataPath.getFile() is None or pack_DataPath.getExtension() is None:
            folder_DataPathArray=pack_AppPath.queryInFolder()
            read_dicts=[]
            for folder_DataPath in folder_DataPathArray:
                read_AppJson=AppJson()
                read_AppJson.setDataJson(folder_DataPath)
                read_dict=read_AppJson.read()
                read_dicts.append(read_dict)
            return read_dicts
        elif pack_AppPath.checkAbsolutePath():
            pack_DataPath=pack_AppPath.getDataPath()
            read_AppJson=AppJson()
            read_AppJson.setDataJson(pack_DataPath)
            pack_dict=read_AppJson.read()

            read_dicts=[]
            for fileExt_dict in pack_dict["packFiles"]:
                read_DataJson=dLB.DataPath()
                read_DataJson.setAbsoluteDirectory(pack_DataPath.getAbsoluteDirectory())
                read_DataJson.setRelativeDirectory(pack_DataPath.getRelativeDirectory())
                read_DataJson.setFile(fileExt_dict["file"])
                read_DataJson.setExtension(fileExt_dict["extension"])

                read_dicts.append(read_dict)
            return read_dicts
            
    def __writePack_create_func(self,write_DataJsonArray):
        pack_DataPath=write_DataJsonArray.getDataPath()
        if pack_DataPath.getFile() is None or pack_DataPath.getExtension() is None:
            for write_DataJson in write_DataJsonArray:
                write_AppJson=AppJson()
                write_AppJson.setDataJson(write_DataJson)
                write_AppJson.write()
        elif type(pack_DataPath.getFile()) is str and type(pack_DataPath.getExtension()) is str:
            write_dicts=[]
            for write_DataJson in write_DataJsonArray:
                write_AppJson=AppJson()
                write_AppJson.setDataJson(write_DataJson)
                write_AppJson.write()
                
                write_DataJson.setDataChoices(["File","Extension"])
                write_dict=write_DataJson.getDataDict()
                write_dicts.append(write_dict)
            
            pack_DataJson=dLB.DataJson()
            pack_DataJson.setDataPath(pack_DataPath)
            pack_DataJson.setJsonDict({"packFiles":write_dicts})

            pack_AppPath=AppJson()
            pack_AppPath.setDataJson(pack_DataJson)
            pack_AppPath.write()
    
    #Setting Function
    def setDataJsonArray(self,variables):
        self._jsonPack_DataJsonArray=variables
        return self._jsonPack_DataJsonArray
    def getDataJsonArray(self):
        return self._jsonPack_DataJsonArray

    #Public Function
    def readPack(self,dataJsonArray=None):
        _jsonPack_DataJsonArray=dataJsonArray or self._jsonPack_DataJsonArray

        readPack_dicts=self.__readPack_query_dicts(_jsonPack_DataJsonArray)
        return readPack_dicts

    def writePack(self,dataJsonArray=None):
        _jsonPack_DataJsonArray=dataJsonArray or self._jsonPack_DataJsonArray

        self.__writePack_create_func(_jsonPack_DataJsonArray)

def readJson(absolute,relative=None,file="init",extension="json"):
    json_DataPath=dLB.DataPath()
    json_DataPath.setAbsoluteDirectory(absolute)
    json_DataPath.setRelativeDirectory(relative)
    json_DataPath.setFile(file)
    json_DataPath.setExtension(extension)

    json_AppJson=AppJson()
    json_AppJson.setDataJson(json_DataPath)
    json_dict=json_AppJson.read()
    return json_dict

def writeJson(absolute,relative=None,file="init",extension="json",write={}):
    json_DataJson=dLB.DataJson()
    json_DataJson.setAbsoluteDirectory(absolute)
    json_DataJson.setRelativeDirectory(relative)
    json_DataJson.setFile(file)
    json_DataJson.setExtension(extension)
    json_DataJson.setJsonDict(write)

    json_AppJson=AppJson()
    json_AppJson.setDataJson(json_DataJson)
    json_AppJson.write()