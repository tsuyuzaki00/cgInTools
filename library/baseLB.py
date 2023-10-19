# -*- coding: iso-8859-15 -*-

import cgInTools as cit
from . import pathLB as pLB
from . import jsonLB as jLB
from . import serializeLB as sLB
cit.reloads([pLB,jLB,sLB])

class SelfOrigin(object):
    def __init__(self):
        self._origin_DataPath=pLB.DataPath()
        self._data_dict={}
        self._dataChoice_strs=["DoIts"]
        self._doIt_strs=[]
    
    #Setting Function
    def setDataPath(self,variable):
        self._origin_DataPath=variable
        return self._origin_DataPath
    def getDataPath(self):
        return self._origin_DataPath
    
    def setDataDict(self,variable):
        self._data_dict=variable
        return self._data_dict
    def getDataDict(self):
        return self._data_dict
    
    def setDataChoices(self,variables):
        self._dataChoice_strs=variables
        return self._dataChoice_strs
    def addDataChoices(self,variables):
        self._dataChoice_strs+=variables
        return self._dataChoice_strs
    def getDataChoices(self):
        return self._dataChoice_strs
    
    def setDoIts(self,variables):
        self._doIt_strs=variables
        return self._doIt_strs
    def addDoIts(self,variables):
        self._doIt_strs+=variables
        return self._doIt_strs
    def getDoIts(self):
        return self._doIt_strs
    
    #Public Function
    def readDict(self,settingData=None):
        _data_dict=settingData or self._data_dict
        setFunctions=list(_data_dict.keys())
        for setFunction in setFunctions:
            if _data_dict.get(setFunction) is None:
                continue
            elif type(_data_dict[setFunction]) is str:
                variable='"'+_data_dict.get(setFunction)+'"'
            else:
                variable=str(_data_dict[setFunction])
            eval('self.set'+setFunction+'('+variable+')')

    def writeDict(self,dataChoices=None):
        _dataChoice_strs=dataChoices or self._dataChoice_strs

        write_dict={}
        for _dataChoice_str in _dataChoice_strs:
            _dataChoice_str=_dataChoice_str[0].upper()+_dataChoice_str[1:]
            variable=eval('self.get'+_dataChoice_str+'()')
            if type(variable) in (bool,int,float,str,list,tuple,dict) or variable is None:
                write_dict[_dataChoice_str]=variable
            else:
                write_dict[_dataChoice_str]=variable.writeData()
        return write_dict
    
    def readData(self,dataPath=None):
        _origin_DataPath=dataPath or self._origin_DataPath

        read_SelfSerialize=sLB.SelfSerialize()
        read_SelfSerialize.setDataPath(_origin_DataPath)
        read_SelfObject=read_SelfSerialize.read()
        return read_SelfObject

    def writeData(self,dataPath=None):
        _origin_DataPath=dataPath or self._origin_DataPath

        write_SelfSerialize=sLB.SelfSerialize()
        write_SelfSerialize.setDataPath(_origin_DataPath)
        write_SelfSerialize.setWriteSelfObject(self)
        write_SelfSerialize.write()

    def readJson(self,dataPath=None):
        _origin_DataPath=dataPath or self._origin_DataPath

        write_SelfJson=jLB.SelfJson()
        write_SelfJson.setDataPath(_origin_DataPath)
        read_dict=write_SelfJson.read()
        return read_dict
    
    def writeJson(self,dataPath=None,dataChoices=None):
        _dataChoice_strs=dataChoices or self._dataChoice_strs
        _origin_DataPath=dataPath or self._origin_DataPath

        write_dict=self.writeDict(_dataChoice_strs)
        
        write_SelfJson=jLB.SelfJson()
        write_SelfJson.setDataPath(_origin_DataPath)
        write_SelfJson.setWriteDict(write_dict)
        write_SelfJson.write()

    def doIt(self,doIts=None):
        _doIt_strs=doIts or self._doIt_strs

        if _doIt_strs == None:
            return
        else:
            for _doIt in _doIt_strs:
                eval("self."+_doIt+"()")