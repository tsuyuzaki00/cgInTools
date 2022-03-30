# -*- coding: iso-8859-15 -*-

import json,os
import pprint

class SimpleJson():
    # 読み込み関数
    def read_json(self,json_file):
        with open(json_file, 'r') as f:
            connect_list = json.load(f)
            return connect_list

    # 上書き書き出し関数
    def write_run(self,json_file,dict):
        with open(json_file, 'w') as f:
            json.dump(dict,f,indent=4,ensure_ascii=False)

    # Jsonファイル名及びパスの設定をする関数
    def path_setting(self,path,json_name,new_folder=None):
        if new_folder == None:
            json_file = os.path.join(path,json_name+".json")
            return json_file
        else:
            json_file = os.path.join(path,new_folder,json_name+".json")
            return json_file


 