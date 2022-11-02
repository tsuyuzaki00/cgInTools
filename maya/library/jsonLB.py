# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import json,os
import pprint

from cgInTools.maya.library import setBaseLB as sb
import cgInTools as cit
cit.verReload(sb)

class Json(sb.SetFile):
    def __init__(self):
        """
        self.path # string
        self.file # string
        """
        self.extension="json" # string
        self.writeDict={}
        self.packDicts=[]

    def setWriteDict(self,variable):
        self.writeDict=variable
        return self.writeDict

    def getWriteDict(self):
        return self.writeDict

    def __getFileJudge(self,file):
        if type(file) is str:
            return True
        elif file is None:
            return False
        else:
            cmds.warning("Please give me a string type.")

    def setPackDicts(self,variable,file=None):
        if self.__getFileJudge(file):
            self.packDicts=[{file:variable}]
            return self.packDicts
        else:
            self.packDicts=[{self.file:variable}]
            return self.packDicts

    def addPackDicts(self,variable,file=None):
        if self.__getFileJudge(file):
            self.packDicts.append({file:variable})
            return self.packDicts
        else:
            self.packDicts.append({self.file:variable})
            return self.packDicts

    def getPackDicts(self):
        return self.packDicts

    def read(self):
        data_file=self.pathSetting_create_str(self.path,self.file,self.extension)
        data_dict=self.readJson_quary_dict(data_file)
        return data_dict

    def readPacks(self):
        pack_file=self.pathSetting_create_str(self.path,self.file,self.extension)
        data_files=self.readPack_quary_list(pack_file)
        data_dicts=[]
        for data_file in data_files:
            data_dict=self.readJson_quary_dict(data_file)
            data_dicts.append(data_dict)
        return data_dicts

    def write(self):
        data_file=self.pathSetting_create_str(self.path,self.file,self.extension)
        self.writeJson_create_func(data_file,self.writeDict)

    def writePacks(self):
        data_file=self.pathSetting_create_str(self.path,self.file,self.extension+"Pack")
        data_packs=self.packDict_create_list(self.file,self.extension,self.writeDict)
        self.writePack_create_func(data_packs,data_file)

    # Jsonファイル名及びパスの設定をする関数
    def pathSetting_create_str(self,path,json_name,extension="json",new_folder=None):
        if new_folder == None:
            json_file = os.path.join(path,json_name+"."+extension)
            return json_file
        else:
            json_file = os.path.join(path,new_folder,json_name+"."+extension)
            return json_file

    # 単体読み込み関数
    def readJson_quary_dict(self,json_file):
        with open(json_file, 'r') as f:
            data_dict = json.load(f)
            return data_dict

    # パック読み込み関数
    def readPack_quary_list(self,pack_file):
        pack_list = self.thisPack_check_str(pack_file)
        path_list=[]
        for pack in pack_list:
            filePath = os.path.join(os.path.split(pack_file)[0], pack)
            path_list.append(filePath)
        return path_list

    # 読み込んだdict内に"packFiles"があるか確認する関数
    def thisPack_check_str(self,pack_file):
        pack_dict = self.readJson_quary_dict(pack_file)
        try:
            pack_dict["packFiles"]
            return pack_dict["packFiles"]
        except:
            cmds.error("There are No packFiles.")

    # 単体書き出し関数
    def writeJson_create_func(self,json_file,write_dict):
        with open(json_file, 'w') as f:
            json.dump(write_dict,f,indent=4,ensure_ascii=False)

    # packを作成する関数
    def packDict_create_list(self,subject,extension,write_dict):
        element_dict={"json_file":subject+"."+extension,"write_dict":write_dict}
        return element_dict
        #{"json_file":name.json,"write_dict":{write:...}}

    # パック書き出し関数
    def writePack_create_func(self,packs,json_file):
        packFiles=[]
        for pack in packs:
            packFiles.append(pack["json_file"])
            json_file = os.path.join(self.path,pack["json_file"])
            self.writeJson_create_func(json_file,pack["write_dict"])
        write_dict={"packFiles":packFiles}
        self.writeJson_create_func(json_file,write_dict)