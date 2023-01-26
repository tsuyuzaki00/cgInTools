# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import json,os

import cgInTools as cit
from . import setBaseLB as sbLB
cit.reloads([sbLB])

class Json(sbLB.BaseJson):
    def __init__(self):
        super(Json,self).__init__()

    #Single Function
    def pathSetting_create_str(self,path,file,extension="json",new_folder=None):
        if new_folder == None:
            exPath=os.path.join(path,file+"."+extension)
            return exPath
        else:
            exPath=os.path.join(path,new_folder,file+"."+extension)
            return exPath

    def readJson_quary_dict(self,exPath):
        with open(exPath,'r') as f:
            read_dict=json.load(f)
            return read_dict
            
    def writeJson_create_func(self,exPath,write_dict):
        with open(exPath,'w') as f:
            json.dump(write_dict,f,indent=4,ensure_ascii=False)

    #Multi Function
    def _thisPack_check_func(self,path,file,extension):
        try:
            imPath=self.pathSetting_create_str(path,file,extension+"Pack")
            self.readJson_quary_dict(imPath)
        except:
            cmds.error("setFile is No packFiles.")

    def _readPack_quary_list(self,path,file,extension):
        imPackPath=self.pathSetting_create_str(path,file,extension+"Pack")
        pack_dict=self.readJson_quary_dict(imPackPath)
        data_dicts=[]
        for fileEX_dict in pack_dict["packFiles"]:
            imPath=self.pathSetting_create_str(path,fileEX_dict["file"],fileEX_dict["extension"])
            data_dict=self.readJson_quary_dict(imPath)
            data_dicts.append(data_dict)
        return data_dicts

    def _writePack_create_func(self,path,file,extension,pack_dicts):
        packPath=self.pathSetting_create_str(path,file,extension+"Pack")
        packFiles=[]
        for pack_dict in pack_dicts:
            packFiles.append({"file":pack_dict["file"],"extension":pack_dict["extension"]})
            exPath=os.path.join(path,pack_dict["file"]+"."+pack_dict["extension"])
            self.writeJson_create_func(exPath,pack_dict["dataDict"])#create a normal json file
        write_dict={"packFiles":packFiles}
        self.writeJson_create_func(packPath,write_dict)#create a pack json file
    
    #Public Function
    def read(self):
        exPath=self.pathSetting_create_str(self._path,self._file,self._extension)
        self._readDict=self.readJson_quary_dict(exPath)
        return self._readDict

    def write(self):
        exPath=self.pathSetting_create_str(self._path,self._file,self._extension)
        self.writeJson_create_func(exPath,self._write_dict)

    def readPacks(self):
        self._thisPack_check_func(self._path,self._file,self._extension)
        self._readPack_dicts=self._readPack_quary_list(self._path,self._file,self._extension)
        return self._readPack_dicts

    def writePacks(self):
        self._writePack_create_func(self._path,self._file,self._extension,self._writePack_dicts)

def getJson(path,file):
    data=Json()
    data.setPath(path)
    data.setFile(file)
    data.setExtension("json")
    json_dict=data.read()
    return json_dict