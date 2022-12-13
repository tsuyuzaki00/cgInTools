# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import json,os

import cgInTools as cit
from . import setBaseLB as sbLB
cit.reloads([sbLB])

class Json(sbLB.BaseFile):
    def __init__(self):
        super(Json,self).__init__()

    #Single Function
    def pathSetting_create_str(self,path,name,extension="json",new_folder=None):
        if new_folder == None:
            json_file=os.path.join(path,name+"."+extension)
            return json_file
        else:
            json_file=os.path.join(path,new_folder,name+"."+extension)
            return json_file

    #Multi Function
    def thisPack_check_func(self,path,file,extension,checkDict):
        pack_dict=self.readJson_quary_dict(path,file,extension+"Pack")
        try:
            print(pack_dict[checkDict])
        except:
            cmds.error("setFile is No packFiles.")

    def readJson_quary_dict(self,path,file,extension):
        data_file=self.pathSetting_create_str(path,file,extension)
        with open(data_file, 'r') as f:
            data_dict = json.load(f)
            return data_dict

    def readPack_quary_list(self,path,file,extension):
        self.thisPack_check_func(path,file,extension,"packFiles")
        pack_dict=self.readJson_quary_dict(path,file,extension+"Pack")
        data_dicts=[]
        for data_str in pack_dict["packFiles"]:
            data_dict=self.readJson_quary_dict(path,data_str,extension)
            data_dicts.append(data_dict)
        return data_dicts

    def writeJson_create_func(self,path,file,extension,write_dict):
        data_file=self.pathSetting_create_str(path,file,extension)
        with open(data_file, 'w') as f:
            json.dump(write_dict,f,indent=4,ensure_ascii=False)

    def writePack_create_func(self,path,file,extension,pack_dicts):
        pack_file=self.pathSetting_create_str(path,file,extension+"Pack")
        packFiles=[]
        for pack_dict in pack_dicts:
            packFiles.append(pack_dict["fileName"])
            data_file = os.path.join(path,pack_dict["fileName"]+"."+extension)
            self.writeJson_create_func(data_file,pack_dict["dataDict"])
        write_dict={"packFiles":packFiles}
        self.writeJson_create_func(pack_file,write_dict)
    
    #Public Function
    def read(self):
        self._readDict=self.readJson_quary_dict(self._path,self._file,self._extension)
        return self._readDict

    def readPacks(self):
        self._readPack_dicts=self.readPack_quary_list(self._path,self._file,self._extension)
        return self._readPack_dicts

    def write(self):
        self.writeJson_create_func(self._path,self._file,self._extension,self._write_dict)

    def writePacks(self):
        self.writePack_create_func(self._path,self._file,self._extension,self._writePack_dicts)

def getJson(path,file):
    data=Json()
    data.setPath(path)
    data.setFile(file)
    data.setExtension("json")
    json_dict=data.read()
    return json_dict