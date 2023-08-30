# -*- coding: iso-8859-15 -*-
import json,os

class Json(object):
    def __init__(self):
        self._directory_str=None
        self._file_str=None
        self._extension_str="json"
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
        self._directory_str=variable
        return self._directory_str
    def getDirectory(self):
        return self._directory_str

    def setFile(self,variable):
        self._file_str=variable
        return self._file_str
    def getFile(self):
        return self._file_str

    def setExtension(self,variable):
        self._extension_str=variable
        return self._extension_str
    def getExtension(self):
        return self._extension_str

    def setWriteDict(self,variable):
        self._write_dict=variable
        return self._write_dict
    def getWriteDict(self):
        return self._write_dict

    #Public Function
    def read(self,directory=None,file=None,extension=None):
        _directory_str=directory or self._directory_str
        _file_str=file or self._file_str
        _extension_str= extension or self._extension_str

        path=self.path_create_str(_directory_str,_file_str,_extension_str)
        read_dict=self.jsonPath_query_dict(path)
        return read_dict

    def write(self,directory=None,file=None,extension=None,write=None):
        _directory_str=directory or self._directory_str
        _file_str=file or self._file_str
        _extension_str= extension or self._extension_str
        _write_dict=write or self._write_dict

        path=self.path_create_str(_directory_str,_file_str,_extension_str)
        self.jsonPath_create_func(path,_write_dict)
    
class JsonPack(object):
    def __init__(self):
        self._directory_str=None
        self._file_str=None
        self._extension_str="jsonPack"
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
        self._directory_str=variable
        return self._directory_str
    def getDirectory(self):
        return self._directory_str

    def setFile(self,variable):
        self._file_str=variable
        return self._file_str
    def getFile(self):
        return self._file_str

    def setExtension(self,variable):
        self._extension_str=variable
        return self._extension_str
    def getExtension(self):
        return self._extension_str

    def setJsonObjects(self,variables):
        self._writePack_Jsons=variables
        return self._writePack_Jsons
    def addJsonObjects(self,variables):
        self._writePack_Jsons+=variables
        return self._writePack_Jsons
    def getJsonObjects(self):
        return self._writePack_Jsons

    #Public Function
    def readPack(self,directory=None,file=None,extension=None):
        _directory_str=directory or self._directory_str
        _file_str=file or self._file_str
        _extension_str= extension or self._extension_str

        readPack_dicts=self.__readPack_query_dicts(_directory_str,_file_str,_extension_str)
        return readPack_dicts

    def writePack(self,directory=None,file=None,extension=None,writePack=None):
        _directory_str=directory or self._directory_str
        _file_str=file or self._file_str
        _extension_str=extension or self._extension_str
        _writePack_Jsons=writeJson or self._writePack_Jsons

        self.__writePack_create_func(_directory_str,_file_str,_extension_str,_writePack_Jsons)

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