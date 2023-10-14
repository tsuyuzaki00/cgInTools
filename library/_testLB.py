# -*- coding: iso-8859-15 -*-
import cgInTools as cit
from . import baseLB as bLB
cit.reloads([bLB])

class DataTest(bLB.SelfOrigin):
    def __init__(self):
        super(DataTest,self).__init__()
        self._value=None
        self._dataChoice_strs=["Variable"]

    def setVariable(self,variable):
        self._value=variable
        return self._value
    def getVariable(self):
        return self._value

class SelfTest(bLB.SelfOrigin):
    def __init__(self):
        super(SelfTest,self).__init__()
        self._dataChoice_strs+=[
            "Boolean",
            "Int",
            "Float",
            "String",
            "List",
            "Tuple",
            "Dict",
            "None",
            "DataTest"
            "DataTests"
        ]
        
        self._boolean_bool=True
        self._int_int=1
        self._float_float=3.14
        self._string_str="string"
        self._dict_dict={"bool":True,"int":1,"float":3.14,"str":"string"}
        self._none_none=None
        self._list_list=[True,1,3.14,"string"]
        self._tuple_tuple=(True,1,3.14,"string")
        self._dataTest_DataTest=None
        self._dataTest_DataTests=[]

    def setBoolean(self,variable):
        self._boolean_bool=variable
        return self._boolean_bool
    def getBoolean(self):
        return self._boolean_bool
    
    def setInt(self,variable):
        self._int_int=variable
        return self._int_int
    def getInt(self):
        return self._int_int
    
    def setFloat(self,variable):
        self._float_float=variable
        return self._float_float
    def getFloat(self):
        return self._float_float
    
    def setString(self,variable):
        self._string_str=variable
        return self._string_str
    def getString(self):
        return self._string_str
    
    def setDict(self,variable):
        self._dict_dict=variable
        return self._dict_dict
    def getDict(self):
        return self._dict_dict
    
    def setNone(self,variable):
        self._none_none=variable
        return self._none_none
    def getNone(self):
        return self._none_none
    
    def setList(self,variables):
        self._list_list=variables
        return self._list_list
    def getList(self):
        return self._list_list
    
    def setTuple(self,variables):
        self._tuple_tuple=variables
        return self._tuple_tuple
    def getTuple(self):
        return self._tuple_tuple

    def setDataTest(self,variable):
        self._dataTest_DataTest=variable
        return self._dataTest_DataTest
    def getDataTest(self):
        return self._dataTest_DataTest
    
    def setDataTests(self,variables):
        self._dataTest_DataTests=variables
        return self._dataTest_DataTests
    def getDataTests(self):
        return self._dataTest_DataTests