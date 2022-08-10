# -*- coding: iso-8859-15 -*-

import json,os
import pprint

class CJson():
    # 読み込み関数
    def readJson_quary_dict(self,json_file):
        with open(json_file, 'r') as f:
            connect_list = json.load(f)
            return connect_list

    # 上書き書き出し関数
    def writeJson_create_func(self,json_file,dict):
        with open(json_file, 'w') as f:
            json.dump(dict,f,indent=4,ensure_ascii=False)

    # Jsonファイル名及びパスの設定をする関数
    def pathSetting_create_str(self,path,json_name,extension="json",new_folder=None):
        if new_folder == None:
            json_file = os.path.join(path,json_name+"."+extension)
            return json_file
        else:
            json_file = os.path.join(path,new_folder,json_name+"."+extension)
            return json_file
    