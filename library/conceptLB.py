# -*- coding: iso-8859-15 -*-
import cgInTools as cit
from ..library import jsonLB as jLB
cit.reloads([jLB])

class SelfOrigin(object):
    def __init__(self):
        self._read_dict={}
        self._dataChoices=["DoIts"]
        self._doIts=[]
    
    #Setting Function
    def setReadDict(self,variable):
        self._read_dict=variable
    def getReadDict(self):
        return self._read_dict
    
    def setDataChoices(self,variables):
        self._dataChoices=variables
    def addDataChoices(self,variables):
        self._dataChoices+=variables
    def getDataChoices(self):
        return self._dataChoices
    
    def setDoIts(self,variables):
        self._doIts=variables
    def addDoIts(self,variables):
        self._doIts+=variables
    def getDoIts(self):
        return self._doIts
    
    #Public Function
    def writeDict(self,setChoices=None):
        _dataChoices=setChoices or self._dataChoices

        write_dict={}
        for _selfChoice in _dataChoices:
            variable=eval('self.get'+_selfChoice+'()')
            write_dict[_selfChoice]=variable
        return write_dict

    def readDict(self,read_dict=None):
        _read_dict=read_dict or self._read_dict

        setFunctions=list(_read_dict.keys())
        for setFunction in setFunctions:
            if _read_dict.get(setFunction) is None:
                continue
            elif isinstance(_read_dict[setFunction],str):
                variable='"'+_read_dict.get(setFunction)+'"'
            else:
                variable=str(_read_dict[setFunction])
            eval('self.set'+setFunction+'('+variable+')')

    def doIt(self,doIts=None):
        _doIts=doIts or self._doIts

        if _doIts == None:
            return
        else:
            for _doIt in _doIts:
                eval("self."+_doIt+"()")