# -*- coding: iso-8859-15 -*-
import cgInTools as cit
from . import dataLB as dLB
from . import jsonLB as jLB
from . import serializeLB as sLB
cit.reloads([dLB,jLB,sLB])

def readJson(absolute,relative=None,file="init",extension="json"):
    json_DataPath=dLB.DataPath()
    json_DataPath.setAbsoluteDirectory(absolute)
    json_DataPath.setRelativeDirectory(relative)
    json_DataPath.setFile(file)
    json_DataPath.setExtension(extension)

    json_AppJson=jLB.AppJson()
    json_AppJson.setDataPath(json_DataPath)
    json_dict=json_AppJson.read()
    return json_dict

def writeJson(absolute,relative=None,file="init",extension="json",write={}):
    json_DataPath=dLB.DataPath()
    json_DataPath.setAbsoluteDirectory(absolute)
    json_DataPath.setRelativeDirectory(relative)
    json_DataPath.setFile(file)
    json_DataPath.setExtension(extension)

    json_AppJson=jLB.AppJson()
    json_AppJson.setDataPath(json_DataPath)
    json_AppJson.setJsonDict(write)
    json_AppJson.write()

def readSelfObject(absolute,relative=None,file="init",extension="selfpy"):
    data_DataPath=dLB.DataPath()
    data_DataPath.setAbsoluteDirectory(absolute)
    data_DataPath.setRelativeDirectory(relative)
    data_DataPath.setFile(file)
    data_DataPath.setExtension(extension)

    data_SelfObject=sLB.AppSerialize()
    data_SelfObject.setDataPath(data_DataPath)
    selfpy_SelfObject=data_SelfObject.read()
    return selfpy_SelfObject

def writeSelfObject(absolute,relative=None,file="init",extension="selfpy",write=None):
    data_DataPath=dLB.DataPath()
    data_DataPath.setAbsoluteDirectory(absolute)
    data_DataPath.setRelativeDirectory(relative)
    data_DataPath.setFile(file)
    data_DataPath.setExtension(extension)
    
    data_SelfObject=sLB.AppSerialize()
    data_SelfObject.setDataPath(data_DataPath)
    data_SelfObject.setWriteSelfObject(write)
    data_SelfObject.write()
