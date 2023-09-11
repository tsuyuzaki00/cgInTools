# -*- coding: iso-8859-15 -*-
import json
import cgInTools as cit
from . import pathLB as pLB
cit.reloads([pLB])

class Json(object):
    def __init__(self):
        self._json_Path=pLB.Path()
        self._json_Path.setExtension("json")
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
        _absoluteDirectory_str=self._json_Path.setAbsoluteDirectory(variable)
        return _absoluteDirectory_str
    def getAbsoluteDirectory(self):
        return self._json_Path.getAbsoluteDirectory()
    
    def setRelativeDirectory(self,variable):
        _relativeDirectory_str=self._json_Path.setRelativeDirectory(variable)
        return _relativeDirectory_str
    def getRelativeDirectory(self):
        return self._json_Path.getRelativeDirectory()

    def setFile(self,variable):
        _file_str=self._json_Path.setFile(variable)
        return _file_str
    def getFile(self):
        return self._json_Path.getFile()

    def setExtension(self,variable):
        _extension_str=self._json_Path.setExtension(variable)
        return _extension_str
    def getExtension(self):
        return self._json_Path.getExtension()

    def setWriteDict(self,variable):
        self._write_dict=variable
        return self._write_dict
    def getWriteDict(self):
        return self._write_dict

    #Public Function
    def read(self,absolute=None,relative=None,file=None,extension=None):
        absolute_path=self._json_Path.queryAbsolutePath(absolute,relative,file,extension)
        read_dict=self.jsonPath_query_dict(absolute_path)
        return read_dict

    def write(self,absolute=None,relative=None,file=None,extension=None,write=None):
        _write_dict=write or self._write_dict

        absolute_path=self._json_Path.queryAbsolutePath(absolute,relative,file,extension)
        self.jsonPath_create_func(absolute_path,_write_dict)
    
class JsonPack(object):
    def __init__(self):
        self._jsonPack_Path=pLB.Path()
        self._jsonPack_Path.setExtension("jsonPack")
        self._writePack_Jsons=[]

    #Private Function
    def __readPack_query_dicts(self,absolute,relative,file,extension):
        pack_Json=Json()
        pack_Json.setAbsoluteDirectory(absolute)
        pack_Json.setRelativeDirectory(relative)
        pack_Json.setFile(file)
        pack_Json.setExtension(extension)
        pack_dict=pack_Json.read()

        read_dicts=[]
        for fileEX_dict in pack_dict["packFiles"]:
            read_Json=Json()
            pack_Json.setAbsoluteDirectory(absolute)
            pack_Json.setRelativeDirectory(relative)
            read_Json.setFile(fileEX_dict["file"])
            read_Json.setExtension(fileEX_dict["extension"])
            read_dict=read_Json.read()
            read_dicts+=read_dict
        return read_dicts

    def __writePack_create_func(self,absolute,relative,file,extension,write_Jsons):
        packFiles=[]
        for write_Json in write_Jsons:
            write_Json.write()
            file_str=write_Json.getFile()
            extension_str=write_Json.getExtension()
            packFiles.append({"file":file_str,"extension":extension_str})
        write_dict={"packFiles":packFiles}

        pack_Json=Json()
        pack_Json.setAbsoluteDirectory(absolute)
        pack_Json.setRelativeDirectory(relative)
        pack_Json.setFile(file)
        pack_Json.setExtension(extension)
        pack_Json.setWriteDict(write_dict)
        pack_Json.write()
    
    #Setting Function
    def setAbsoluteDirectory(self,variable):
        _absoluteDirectory_str=self._jsonPack_Path.setAbsoluteDirectory(variable)
        return _absoluteDirectory_str
    def getAbsoluteDirectory(self):
        return self._jsonPack_Path.getAbsoluteDirectory()
    
    def setRelativeDirectory(self,variable):
        _relativeDirectory_str=self._jsonPack_Path.setRelativeDirectory(variable)
        return _relativeDirectory_str
    def getRelativeDirectory(self):
        return self._jsonPack_Path.getRelativeDirectory()

    def setFile(self,variable):
        _file_str=self._jsonPack_Path.setFile(variable)
        return _file_str
    def getFile(self):
        return self._jsonPack_Path.getFile()

    def setExtension(self,variable):
        _extension_str=self._jsonPack_Path.setExtension(variable)
        return _extension_str
    def getExtension(self):
        return self._jsonPack_Path.getExtension()

    def setJsonObjects(self,variables):
        self._writePack_Jsons=variables
        return self._writePack_Jsons
    def addJsonObjects(self,variables):
        self._writePack_Jsons+=variables
        return self._writePack_Jsons
    def getJsonObjects(self):
        return self._writePack_Jsons

    #Public Function
    def readPack(self,absolute=None,relative=None,file=None,extension=None):
        _absolute_str=absolute or self._jsonPack_Path.getAbsoluteDirectory()
        _relative_str=relative or self._jsonPack_Path.getRelativeDirectory()
        _file_str=file or self._jsonPack_Path.getFile()
        _extension_str= extension or self._jsonPack_Path.getExtension()

        readPack_dicts=self.__readPack_query_dicts(_absolute_str,_relative_str,_file_str,_extension_str)
        return readPack_dicts

    def writePack(self,absolute=None,relative=None,file=None,extension=None,writePack=None):
        _absolute_str=absolute or self._jsonPack_Path.getAbsoluteDirectory()
        _relative_str=relative or self._jsonPack_Path.getRelativeDirectory()
        _file_str=file or self._jsonPack_Path.getFile()
        _extension_str= extension or self._jsonPack_Path.getExtension()
        _writePack_Jsons=writePack or self._writePack_Jsons

        self.__writePack_create_func(_absolute_str,_relative_str,_file_str,_extension_str,_writePack_Jsons)

def readJson(directory,file):
    data=Json()
    data.setAbsoluteDirectory(directory)
    data.setFile(file)
    data.setExtension("json")
    json_dict=data.read()
    return json_dict

def writeJson(directory,file,write):
    data=Json()
    data.setAbsoluteDirectory(directory)
    data.setFile(file)
    data.setExtension("json")
    data.setWriteDict(write)
    data.write()