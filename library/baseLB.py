# -*- coding: iso-8859-15 -*-

class SelfOrigin(object):
    def __init__(self):
        self._data_dict={}
        self._dataChoice_strs=["DoIts"]
        self._doIt_strs=[]
    
    #Setting Function
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
    def writeData(self,dataChoices=None):
        _dataChoice_strs=dataChoices or self._dataChoice_strs

        write_dict={}
        for _selfChoice in _dataChoice_strs:
            variable=eval('self.get'+_selfChoice+'()')
            write_dict[_selfChoice]=variable
        return write_dict

    def readData(self,settingData=None):
        _data_dict=settingData or self._data_dict

        setFunctions=list(_data_dict.keys())
        for setFunction in setFunctions:
            if _data_dict.get(setFunction) is None:
                continue
            elif isinstance(_data_dict[setFunction],str):
                variable='"'+_data_dict.get(setFunction)+'"'
            else:
                variable=str(_data_dict[setFunction])
            eval('self.set'+setFunction+'('+variable+')')

    def doIt(self,doIts=None):
        _doIt_strs=doIts or self._doIt_strs

        if _doIt_strs == None:
            return
        else:
            for _doIt in _doIt_strs:
                eval("self."+_doIt+"()")