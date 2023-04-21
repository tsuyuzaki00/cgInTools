# -*- coding: iso-8859-15 -*-
import json,os

import cgInTools as cit
cit.reloads([])

class Json(object):
    def __init__(self):
        self._directory=None
        self._file=None
        self._extension="json"
        self._read_dict={}
        self._readPack_dicts=[]
        self._write_dict={}
        self._writePack_dicts=[]# {"dataDict":{},"file":""}

    #Single Function
    def path_create_str(self,directory,file,extension="json",newFolder=None):
        if newFolder == None:
            path=os.path.join(directory,file+"."+extension)
            return path
        else:
            path=os.path.join(directory,newFolder,file+"."+extension)
            return path

    def readJson_quary_dict(self,path):
        with open(path,"r") as f:
            read_dict=json.load(f)
            return read_dict
            
    def writeJson_create_func(self,path,write_dict):
        with open(path,"w") as f:
            json.dump(write_dict,f,indent=4,ensure_ascii=False)

    #Multi Function
    def _thisPack_check_func(self,directory,file,extension):
        try:
            path=self.path_create_str(directory,file,extension+"Pack")
            self.readJson_quary_dict(path)
        except:
            print('setFile is No packFiles.')

    def _readPack_quary_list(self,directory,file,extension):
        imPackPath=self.path_create_str(directory,file,extension+"Pack")
        pack_dict=self.readJson_quary_dict(imPackPath)
        data_dicts=[]
        for fileEX_dict in pack_dict["packFiles"]:
            imPath=self.path_create_str(directory,fileEX_dict["file"],fileEX_dict["extension"])
            data_dict=self.readJson_quary_dict(imPath)
            data_dicts.append(data_dict)
        return data_dicts

    def _writePack_create_func(self,directory,file,extension,pack_dicts):
        packPath=self.path_create_str(directory,file,extension+"Pack")
        packFiles=[]
        for pack_dict in pack_dicts:
            packFiles.append({"file":pack_dict["file"],"extension":pack_dict["extension"]})
            exPath=os.path.join(directory,pack_dict["file"]+"."+pack_dict["extension"])
            self.writeJson_create_func(exPath,pack_dict["dataDict"])#create a normal json file
        write_dict={"packFiles":packFiles}
        self.writeJson_create_func(packPath,write_dict)#create a pack json file
    
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

    def setWritePackDict(self,variable,file=None):
        file=file or self._file
        self._writePack_dicts=[{"file":file,"extension":self._extension,"dataDict":variable}]
        return self._writePack_dicts
    def addWritePackDict(self,variable,file=None):
        file=file or self._file
        self._writePack_dicts.append({"file":file,"extension":self._extension,"dataDict":variable})
        return self._writePack_dicts
    def getWritePackDicts(self):
        return self._writePack_dicts

    #Public Function
    def read(self,path=None):
        if not path == None:
            self._read_dict=self.readJson_quary_dict(path)
        else:
            path=self.path_create_str(self._directory,self._file,self._extension)
            self._read_dict=self.readJson_quary_dict(path)
        return self._read_dict

    def write(self,path=None,write_dict=None):
        _write_dict=write_dict or self._write_dict
        if not path == None:
            self.writeJson_create_func(path,_write_dict)
        else:
            path=self.path_create_str(self._directory,self._file,self._extension)
            self.writeJson_create_func(path,_write_dict)

    def readPacks(self):
        self._thisPack_check_func(self._directory,self._file,self._extension)
        self._readPack_dicts=self._readPack_quary_list(self._directory,self._file,self._extension)
        return self._readPack_dicts

    def writePacks(self):
        self._writePack_create_func(self._directory,self._file,self._extension,self._writePack_dicts)

def getJson(directory,file):
    data=Json()
    data.setDirectory(directory)
    data.setFile(file)
    data.setExtension("json")
    json_dict=data.read()
    return json_dict