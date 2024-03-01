# -*- coding: iso-8859-15 -*-
from xml.etree.ElementTree import * 
import cgInTools as cit
from . import pathLB as pLB
cit.reloads([pLB])

class AppXml(object):
    def __init__(self):
        self._path_DataPath=None
        self._write_xml=None

import os
class Xml(object):
    def __init__(self):
        self._path=""
        self._file=""
        self._extension="xml"
        self._element_list=[]
        self._rootName=""

    def __loading(self):
        self._root_element=Element("Root")
        
        for _element in self._element_list:
            root=Element(_element)

#Public Function
    def read(self):
        self._readDict=self.readXml_quary_dict(self._path,self._file,self._extension)
        return self._readDict

    def readPacks(self):
        self._readPack_dicts=self.readPack_quary_list(self._path,self._file,self._extension)
        return self._readPack_dicts

    def write(self):
        self.writeXml_create_func(self._path,self._file,self._extension,self._root_element)

    def writePacks(self):
        self.writePack_create_func(self._writePack_dicts,self._path,self._file,self._extension)

#Single Function
    def pathSetting_create_str(self,path,name,extension="xml",new_folder=None):
        if new_folder == None:
            xml_file=os.path.join(path,name+"."+extension)
            return xml_file
        else:
            xml_file=os.path.join(path,new_folder,name+"."+extension)
            return xml_file

    def readXml_quary_dict(self,path,file,extension):
        data_file=self.pathSetting_create_str(path,file,extension)
        return ET.parse(data_file).getroot()

    def readPack_quary_list(self,path,file,extension):
        self.thisPack_check_func(path,file,extension,"packFiles")
        pack_dict=self.readXml_quary_dict(path,file,extension+"Pack")
        data_dicts=[]
        for data_str in pack_dict["packFiles"]:
            data_dict=self.readXml_quary_dict(path,data_str,extension)
            data_dicts.append(data_dict)
        return data_dicts

    def thisPack_check_func(self,path,file,extension,checkDict):
        pack_dict=self.readXml_quary_dict(path,file,extension+"Pack")
        try:
            print(pack_dict[checkDict])
        except:
            pass

    def writeXml_create_func(self,path,file,extension,write_element):
        data_file=self.pathSetting_create_str(path,file,extension)
        with open(data_file, 'w') as f:
            write_element.write(f,encoding='utf-8',xml_declaration=True)

    def writePack_create_func(self,pack_dicts,path,file,extension):
        pack_file=self.pathSetting_create_str(path,file,extension+"Pack")
        packFiles=[]
        for pack_dict in pack_dicts:
            packFiles.append(pack_dict["fileName"])
            data_file = os.path.join(path,pack_dict["fileName"]+"."+extension)
            self.writeJson_create_func(data_file,pack_dict["dataDict"])
        write_dict={"packFiles":packFiles}
        self.writeJson_create_func(pack_file,write_dict)