# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import json,os
import pprint

class CJson():
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
            connect_list = json.load(f)
            return connect_list

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
    def writePack_create_func(self,packs,path,pack_file,extension="jsonPack"):
        packFiles=[]
        for pack in packs:
            packFiles.append(pack["json_file"])
            json_file = os.path.join(path,pack["json_file"])
            self.writeJson_create_func(json_file,pack["write_dict"])
        write_dict={"packFiles":packFiles}
        filePath=self.pathSetting_create_str(path,pack_file,extension)
        self.writeJson_create_func(filePath,write_dict)
