# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import json,os

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
        self.writePackDicts=[]
        self.readDict={}
        self.readPackDicts=[]

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
            self.writePackDicts=[{"fileName":file,"dataDict":variable}]
            return self.writePackDicts
        else:
            self.writePackDicts=[{"fileName":self.file,"dataDict":variable}]
            return self.writePackDicts

    def addPackDicts(self,variable,file=None):
        if self.__getFileJudge(file):
            self.writePackDicts.append({"fileName":file,"dataDict":variable})
            return self.writePackDicts
        else:
            self.writePackDicts.append({"fileName":self.file,"dataDict":variable})
            return self.writePackDicts

    def getPackDicts(self):
        return self.writePackDicts

    def read(self):
        self.readDict=self.readJson_quary_dict(self.path,self.file,self.extension)
        return self.readDict

    def readPacks(self):
        self.readPackDicts=self.readPack_quary_list(self.path,self.file,self.extension)
        return self.readPackDicts

    def write(self):
        self.writeJson_create_func(self.path,self.file,self.extension,self.writeDict)

    def writePacks(self):
        self.writePack_create_func(self.writePackDicts,self.path,self.file,self.extension)

    # Jsonファイル名及びパスの設定をする関数
    def pathSetting_create_str(self,path,json_name,extension="json",new_folder=None):
        if new_folder == None:
            json_file = os.path.join(path,json_name+"."+extension)
            return json_file
        else:
            json_file = os.path.join(path,new_folder,json_name+"."+extension)
            return json_file

    # 単体読み込み関数
    def readJson_quary_dict(self,path,file,extension):
        data_file=self.pathSetting_create_str(path,file,extension)
        with open(data_file, 'r') as f:
            data_dict = json.load(f)
            return data_dict

    # パック読み込み関数
    def readPack_quary_list(self,path,file,extension):
        #self.thisPack_check_str(path,file,extension,"packFiles")
        pack_dict=self.readJson_quary_dict(path,file,extension+"Pack")
        data_dicts=[]
        for data_str in pack_dict["packFiles"]:
            data_dict=self.readJson_quary_dict(path,data_str,extension)
            data_dicts.append(data_dict)
        return data_dicts

    # 読み込んだdict内に"packFiles"があるか確認する関数
    def thisPack_check_str(self,path,file,extension,checkDict):
        pack_dict=self.readJson_quary_dict(path,file,extension+"Pack")
        try:
            pack_dict[checkDict]
            return pack_dict
        except:
            cmds.error("setFile is No packFiles.")

    # 単体書き出し関数
    def writeJson_create_func(self,path,file,extension,write_dict):
        data_file=self.pathSetting_create_str(path,file,extension)
        with open(data_file, 'w') as f:
            json.dump(write_dict,f,indent=4,ensure_ascii=False)

    # パック書き出し関数
    def writePack_create_func(self,pack_dicts,path,file,extension):
        pack_file=self.pathSetting_create_str(path,file,extension+"Pack")
        packFiles=[]
        for pack_dict in pack_dicts:
            packFiles.append(pack_dict["fileName"])
            data_file = os.path.join(path,pack_dict["fileName"]+"."+extension)
            self.writeJson_create_func(data_file,pack_dict["dataDict"])
        write_dict={"packFiles":packFiles}
        self.writeJson_create_func(pack_file,write_dict)