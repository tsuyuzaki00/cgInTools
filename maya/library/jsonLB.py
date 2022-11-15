# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import json,os

from cgInTools.maya.library import setBaseLB as sb
import cgInTools as cit
cit.verReload(sb)

class Json(sb.SetFile):
    def __init__(self):
        """
        self._path # string
        self._file # string
        self._extension="json"
        """
        self._writeDict={}
        self._writePackDicts=[]
        self._readDict={}
        self._readPackDicts=[]

    def setWriteDict(self,variable):
        self._writeDict=variable
        return self._writeDict
    def getWriteDict(self):
        return self._writeDict

    def getPackDicts(self):
        return self._writePackDicts

    def setDictInPack(self,variable,file=None):
        file=file or self._file
        _writePackDicts=[{"fileName":file,"dataDict":variable}]
        return _writePackDicts

    def addDictInPack(self,variable,file=None):
        file=file or self._file
        self._writePackDicts.append({"fileName":file,"dataDict":variable})
        return self._writePackDicts
        
    def read(self):
        self.readDict=self.readJson_quary_dict(self._path,self._file,self._extension)
        return self.readDict

    def readPacks(self):
        self.readPackDicts=self.readPack_quary_list(self._path,self._file,self._extension)
        return self.readPackDicts

    def write(self):
        self.writeJson_create_func(self._path,self._file,self._extension,self._writeDict)

    def writePacks(self):
        self.writePack_create_func(self._writePackDicts,self._path,self._file,self._extension)

#Private function
    def pathSetting_create_str(self,path,json_name,extension="json",new_folder=None):
        if new_folder == None:
            json_file = os.path.join(path,json_name+"."+extension)
            return json_file
        else:
            json_file = os.path.join(path,new_folder,json_name+"."+extension)
            return json_file

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

    def thisPack_check_func(self,path,file,extension,checkDict):
        pack_dict=self.readJson_quary_dict(path,file,extension+"Pack")
        try:
            print(pack_dict[checkDict])
        except:
            cmds.error("setFile is No packFiles.")

    def writeJson_create_func(self,path,file,extension,write_dict):
        data_file=self.pathSetting_create_str(path,file,extension)
        with open(data_file, 'w') as f:
            json.dump(write_dict,f,indent=4,ensure_ascii=False)

    def writePack_create_func(self,pack_dicts,path,file,extension):
        pack_file=self.pathSetting_create_str(path,file,extension+"Pack")
        packFiles=[]
        for pack_dict in pack_dicts:
            packFiles.append(pack_dict["fileName"])
            data_file = os.path.join(path,pack_dict["fileName"]+"."+extension)
            self.writeJson_create_func(data_file,pack_dict["dataDict"])
        write_dict={"packFiles":packFiles}
        self.writeJson_create_func(pack_file,write_dict)