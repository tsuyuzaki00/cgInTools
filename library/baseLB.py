# -*- coding: iso-8859-15 -*-
import cgInTools as cit
from . import serializeLB as sLB
from . import jsonLB as jLB
cit.reloads([sLB,jLB])

class DataOrigin(object):
    def __init__(self,*dataTuple):
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._origin_DataPath=None
            self._dataChoice_strs=[]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataOrigin):
                self._origin_DataPath=dataTuple[0].getOriginDataPath()
                self._dataChoice_strs=dataTuple[0].getDataChoiceStrs()

    #Setting Function
    def setOriginDataPath(self,variable):
        self._origin_DataPath=variable
        return self._origin_DataPath
    def getOriginDataPath(self):
        return self._origin_DataPath
    
    def setDataChoiceStrs(self,variables):
        self._dataChoice_strs=variables
        return self._dataChoice_strs
    def addDataChoiceStrs(self,variables):
        self._dataChoice_strs+=variables
        return self._dataChoice_strs
    def getDataChoiceStrs(self):
        return self._dataChoice_strs
    
    #Public Function
    def writeDict(self,dataChoices=None):
        _dataChoice_strs=dataChoices or self._dataChoice_strs

        write_dict={}
        for _dataChoice_str in _dataChoice_strs:
            _dataChoice_str=_dataChoice_str[0].upper()+_dataChoice_str[1:]
            variable=eval('self.get'+_dataChoice_str+'()')
            if type(variable) in (bool,int,float,str) or variable is None:
                write_dict[_dataChoice_str]=variable
            elif type(variable) in (list,tuple):
                variables=[]
                for v in variable:
                    if type(v) in (bool,int,float,str) or v is None:
                        variables.append(v)
                    else:
                        variables.append(v.writeDict())
                write_dict[_dataChoice_str]=variables
            else:
                write_dict[_dataChoice_str]=variable.writeDict()
        return write_dict
    
    def writeJson(self,dataPath=None,dataChoices=None):
        _origin_DataPath=dataPath or self._origin_DataPath
        _dataChoice_strs=dataChoices or self._dataChoice_strs

        json_dict=self.writeDict(_dataChoice_strs)
        json_AppJson=jLB.AppJson()
        json_AppJson.setDataPath(_origin_DataPath)
        json_AppJson.setJsonDict(json_dict)
        json_AppJson.write()

class SelfOrigin(object):
    def __init__(self,selfObject=None):
        if selfObject is None:
            self._origin_DataPath=None
            self._doIt_strs=[]
        elif isinstance(selfObject,SelfOrigin):
            self._origin_DataPath=selfObject.getOriginDataPath()
            self._doIt_strs=selfObject.getDoItStrs()
    
    #Setting Function
    def setOriginDataPath(self,variable):
        self._origin_DataPath=variable
        return self._origin_DataPath
    def getOriginDataPath(self):
        return self._origin_DataPath

    def setDoItStrs(self,variables):
        self._doIt_strs=variables
        return self._doIt_strs
    def addDoItStrs(self,variables):
        self._doIt_strs+=variables
        return self._doIt_strs
    def getDoItStrs(self):
        return self._doIt_strs
    
    #Public Function
    def readData(self,dataPath=None):
        _origin_DataPath=dataPath or self._origin_DataPath

        selfpy_SelfSerialize=sLB.AppSerialize()
        selfpy_SelfSerialize.setDataPath(_origin_DataPath)
        selfpy_SelfObject=selfpy_SelfSerialize.read()
        self.__init__(selfpy_SelfObject)

    def writeData(self,dataPath=None):
        _origin_DataPath=dataPath or self._origin_DataPath

        selfpy_SelfSerialize=sLB.AppSerialize()
        selfpy_SelfSerialize.setDataPath(_origin_DataPath)
        selfpy_SelfSerialize.setWriteSelfObject(self)
        selfpy_SelfSerialize.write()

    def doIt(self,doIts=None):
        _doIt_strs=doIts or self._doIt_strs

        if _doIt_strs is None or _doIt_strs == []:
            return
        else:
            for _doIt_str in _doIt_strs:
                exec('self.'+_doIt_str+'()')