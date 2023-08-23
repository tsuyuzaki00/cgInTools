# -*- coding: iso-8859-15 -*-
import json,os

import cgInTools as cit
cit.reloads([])

class Json(object):
    def __init__(self):
        self._directory=None
        self._file=None
        self._extension="json"
        self._write_dict={}

    #Single Function
    def path_create_str(self,directory,file,extension="json",newFolder=None):
        if newFolder == None:
            path=os.path.join(directory,file+"."+extension)
            return path
        else:
            path=os.path.join(directory,newFolder,file+"."+extension)
            return path

    def jsonPath_query_dict(self,path):
        with open(path,"r") as f:
            read_dict=json.load(f)
            return read_dict
            
    def jsonPath_create_func(self,path,write_dict):
        with open(path,"w") as f:
            json.dump(write_dict,f,indent=4,ensure_ascii=False)

    #Setting Function
    def setDirectory(self,variable):
        self._directory=variable
        return self._directory
    def getDirectory(self):
        return self._directory

    def setFile(self,variable):
        self._file=variable
        return self._file
    def getFile(self):
        return self._file

    def setExtension(self,variable):
        self._extension=variable
        return self._extension
    def getExtension(self):
        return self._extension

    def setWriteDict(self,variable):
        self._write_dict=variable
        return self._write_dict
    def getWriteDict(self):
        return self._write_dict

    #Public Function
    def read(self,path=None):
        if not path == None:
            read_dict=self.jsonPath_query_dict(path)
        else:
            path=self.path_create_str(self._directory,self._file,self._extension)
            read_dict=self.jsonPath_query_dict(path)
        return read_dict

    def write(self,path=None,write=None):
        _write_dict=write or self._write_dict
        if not path == None:
            self.jsonPath_create_func(path,_write_dict)
        else:
            path=self.path_create_str(self._directory,self._file,self._extension)
            self.jsonPath_create_func(path,_write_dict)
    
class JsonPack(object):
    def __init__(self):
        self._directory=None
        self._file=None
        self._extension="jsonPack"
        self._writePack_Jsons=[]

    #Private Function
    def __readPack_query_dicts(self,directory,file,extension):
        pack_Json=Json()
        pack_Json.setDirectory(directory)
        pack_Json.setFile(file)
        pack_Json.setExtension(extension)
        pack_dict=pack_Json.read()

        read_dicts=[]
        for fileEX_dict in pack_dict["packFiles"]:
            read_Json=Json()
            read_Json.setDirectory(directory)
            read_Json.setFile(fileEX_dict["file"])
            read_Json.setExtension(fileEX_dict["extension"])
            read_dict=read_Json.read()

            read_dicts+=read_dict
        return read_dicts

    def __writePack_create_func(self,directory,file,extension,write_Jsons):
        packFiles=[]
        for write_Json in write_Jsons:
            write_Json.write()
            file_str=write_Json.getFile()
            extension_str=write_Json.getExtension()
            packFiles.append({"file":file_str,"extension":extension_str})
        write_dict={"packFiles":packFiles}

        pack_Json=Json()
        pack_Json.setDirectory(directory)
        pack_Json.setFile(file)
        pack_Json.setExtension(extension)
        pack_Json.setWriteDict(write_dict)
        pack_Json.write()
    
    #Setting Function
    def setDirectory(self,variable):
        self._directory=variable
        return self._directory
    def getDirectory(self):
        return self._directory

    def setFile(self,variable):
        self._file=variable
        return self._file
    def getFile(self):
        return self._file

    def setExtension(self,variable):
        self._extension=variable
        return self._extension
    def getExtension(self):
        return self._extension

    def setJsonObjects(self,variables):
        self._writePack_Jsons=variables
    def addJsonObjects(self,variables):
        self._writePack_Jsons+=variables
    def getJsonObjects(self):
        return self._writePack_Jsons

    #Public Function
    def readPack(self):
        readPack_dicts=self.__readPack_query_dicts(self._directory,self._file,self._extension)
        return readPack_dicts

    def writePack(self):
        self.__writePack_create_func(self._directory,self._file,self._extension,self._writePack_Jsons)


def readJson(directory,file):
    data=Json()
    data.setDirectory(directory)
    data.setFile(file)
    data.setExtension("json")
    json_dict=data.read()
    return json_dict

def writeJson(directory,file,write):
    data=Json()
    data.setDirectory(directory)
    data.setFile(file)
    data.setExtension("json")
    data.setWriteDict(write)
    data.write()