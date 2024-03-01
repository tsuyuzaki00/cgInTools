# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import maya.api.OpenMayaAnim as oma2

import cgInTools as cit
from ...library import baseLB as bLB
cit.reloads([bLB])

from ...library.dataLB import *

#Definition Data
class DataMenuParam(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataMenuParam,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._label_str=None
            self._fromFolder_str=None
            self._importFile_str=None
            self._function_str=None
            self._iconFileExt_str=None
            self._dataChoice_strs=[
                "Label",
                "FromFolder",
                "ImportFile",
                "Function",
                "Icon"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataMenuParam):
                self._label_str=dataTuple[0].getLabel()
                self._fromFolder_str=dataTuple[0].getFromFolder()
                self._importFile_str=dataTuple[0].getImportFile()
                self._function_str=dataTuple[0].getFunction()
                self._iconFileExt_str=dataTuple[0].getIcon()

    #Setting Function
    def setLabel(self,variable):
        self._label_str=variable
        return self._label_str
    def getLabel(self):
        return self._label_str
    
    def setFromFolder(self,variable):
        self._fromFolder_str=variable
        return self._fromFolder_str
    def getFromFolder(self):
        return self._fromFolder_str
    
    def setImportFile(self,variable):
        self._importFile_str=variable
        return self._importFile_str
    def getImportFile(self):
        return self._importFile_str
    
    def setFunction(self,variable):
        self._function_str=variable
        return self._function_str
    def getFunction(self):
        return self._function_str
    
    def setIcon(self,variable):
        self._iconFileExt_str=variable
        return self._iconFileExt_str
    def getIcon(self):
        return self._iconFileExt_str

class DataAttribute(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataAttribute,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._longName_str=None
            self._shortName_str=None
            self._dataChoice_strs=[
                "Name",
                "ShortName"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataAttribute):
                self._longName_str=dataTuple[0].getName()
                self._shortName_str=dataTuple[0].getShortName()
            elif isinstance(dataTuple[0],om2.MObject):
                attr_MFnAttribute=om2.MFnAttribute(dataTuple[0])
                self._longName_str=attr_MFnAttribute.name
                self._shortName_str=attr_MFnAttribute.shortName
                self._dataChoice_strs=[
                    "Name",
                    "ShortName"
                ]
    
    def __str__(self):
        return str(self._longName_str)

    #Setting Function
    def setName(self,variable):
        self._longName_str=variable
        return self._longName_str
    def getName(self):
        return self._longName_str
    
    def setShortName(self,variable):
        self._shortName_str=variable
        return self._shortName_str
    def getShortName(self):
        return self._shortName_str

class DataAttributeBoolean(DataAttribute):
    def __init__(self,*dataTuple):
        super(DataAttributeBoolean,self).__init__(*dataTuple)
        self.__valueType_int=om2.MFnNumericData().kBoolean #1
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._value_bool=None
            self._dataChoice_strs=[
                "Value"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataAttributeBoolean):
                self._value_bool=dataTuple[0].getValue()

    #Setting Function
    def setValue(self,variable):
        self._value_bool=variable
        return self._value_bool
    def getValue(self):
        return self._value_bool

    def getValueType(self):
        return self.__valueType_int

class DataAttributeInt(DataAttribute):
    def __init__(self,*dataTuple):
        super(DataAttributeInt,self).__init__(*dataTuple)
        self.__valueType_int=om2.MFnNumericData().kInt #7
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._value_int=None
            self._limitMax_int=None
            self._limitMin_int=None
            self._dataChoice_strs=[
                "Value",
                "Max",
                "Min"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataAttributeInt):
                self._value_int=dataTuple[0].getValue()
                self._limitMax_int=dataTuple[0].getMax()
                self._limitMin_int=dataTuple[0].getMin()

    #Setting Function
    def setValue(self,variable):
        self._value_int=variable
        return self._value_int
    def getValue(self):
        return self._value_int
    
    def setMax(self,variable):
        self._limitMax_int=variable
        return self._limitMax_int
    def getMax(self):
        return self._limitMax_int
    
    def setMin(self,variable):
        self._limitMin_int=variable
        return self._limitMin_int
    def getMin(self):
        return self._limitMin_int
    
    def getValueType(self):
        return self.__valueType_int

class DataAttributeFloat(DataAttribute):
    def __init__(self,*dataTuple):
        super(DataAttributeFloat,self).__init__(*dataTuple)
        self.__valueType_int=om2.MFnNumericData().kFloat #11
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._value_float=None
            self._limitMax_float=None
            self._limitMin_float=None
            self._dataChoice_strs=[
                "Value",
                "Max",
                "Min"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataAttributeFloat):
                self._value_float=dataTuple[0].getValue()
                self._limitMax_float=dataTuple[0].getMax()
                self._limitMin_float=dataTuple[0].getMin()

    #Setting Function
    def setValue(self,variable):
        self._value_float=variable
        return self._value_float
    def getValue(self):
        return self._value_float

    def setMax(self,variable):
        self._limitMax_float=variable
        return self._limitMax_float
    def getMax(self):
        return self._limitMax_float
    
    def setMin(self,variable):
        self._limitMin_float=variable
        return self._limitMin_float
    def getMin(self):
        return self._limitMin_float
    
    def getValueType(self):
        return self.__valueType_int

class DataAttributeVector(DataAttribute):
    def __init__(self,*dataTuple):
        super(DataAttributeVector,self).__init__(*dataTuple)
        self.__valueType_int=om2.MFnNumericData().k3Float  #13
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._valueVector_tuple3=[0.0,0.0,0.0]
            self._limitMax_floats=[]
            self._limitMin_floats=[]
            self._dataChoice_strs=[
                "ValueX",
                "ValueY",
                "ValueZ",
                "Maxs",
                "Mins"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataAttributeVector):
                self._valueVector_tuple3=dataTuple[0].getValues()
                self._limitMax_float=dataTuple[0].getMaxs()
                self._limitMin_float=dataTuple[0].getMins()

    @property
    def vector(self):
        pass

    #Setting Function
    def setValues(self,variables):
        self._valueVector_tuple3=variables
        return self._valueVector_tuple3
    def getValues(self):
        return self._valueVector_tuple3
    
    def setMaxs(self,variables):
        self._limitMax_floats=variables
        return self._limitMax_floats
    def getMaxs(self):
        return self._limitMax_floats
    
    def setMins(self,variables):
        self._limitMin_floats=variables
        return self._limitMin_floats
    def getMins(self):
        return self._limitMin_floats
    
    def setVectorX(self,variable):
        self._valueVector_tuple3[0]=variable
        return self._valueVector_tuple3[0]
    def getVectorX(self):
        return self._valueVector_tuple3[0]
    
    def setVectorY(self,variable):
        self._valueVector_tuple3[1]=variable
        return self._valueVector_tuple3[1]
    def getVectorY(self):
        return self._valueVector_tuple3[1]
    
    def setVectorZ(self,variable):
        self._valueVector_tuple3[2]=variable
        return self._valueVector_tuple3[2]
    def getVectorZ(self):
        return self._valueVector_tuple3[2]
    
    def getValueType(self):
        return self.__valueType_int

class DataAttributeString(DataAttribute):
    def __init__(self,*dataTuple):
        super(DataAttributeString,self).__init__(*dataTuple)
        self.__valueType_int=om2.MFnData().kString #4
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._valueString_str=None
            self._dataChoice_strs=[
                "Value"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple,DataAttributeString):
                self._valueString_str=dataTuple.getValue()
    
    def setValue(self,variable):
        self._valueString_str=variable
        return self._valueString_str
    def getValue(self):
        return self._valueString_str
    
    def getValueType(self):
        return self.__valueType_int

class DataAttributeEnum(DataAttribute):
    def __init__(self,*dataTuple):
        super(DataAttributeEnum,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._fieldEnum_strs=[]
            self._valueEnum_str=None
            self._dataChoice_strs=[
                "FieldStrs",
                "Enum"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple,DataAttributeEnum):
                self._fieldEnum_strs=dataTuple.getFieldStrs()
                self._valueEnum_str=dataTuple.getEnum()

    #Setting Function
    def setFieldStrs(self,variables):
        self._fieldEnum_strs=variables
        return self._fieldEnum_strs
    def addFieldStrs(self,variables):
        self._fieldEnum_strs+=variables
        return self._fieldEnum_strs
    def getFieldStrs(self):
        return self._fieldEnum_strs

    def setEnum(self,variable):
        self._valueEnum_str=variable
        return self._valueEnum_str
    def getEnum(self):
        return self._valueEnum_str

class DataAttributeWeight(DataAttribute):
    def __init__(self,*dataTuple):
        super(DataAttributeWeight,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._valueWeight_float=None
            self._indexWeight_int=None
            self._dataChoice_strs=[
                "ValueWeight",
                "IndexWeight"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple,DataAttributeWeight):
                self._valueWeight_float=dataTuple.getValueWeight()
                self._indexWeight_int=dataTuple.getIndexWeight()

    #Setting Function
    def setValueWeight(self,variable):
        self._valueWeight_float=variable
        return self._valueWeight_float
    def getValueWeight(self):
        return self._valueWeight_float
    
    def setIndexWeight(self,variable):
        self._indexWeight_int=variable
        return self._indexWeight_int
    def getIndexWeight(self):
        return self._indexWeight_int

class DataName(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataName,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._titleName_str=None
            self._tagTypeName_str=None
            self._sideName_str=None
            self._numberName_ints=[0]
            self._hierarchyName_strs=["A"]
            self._customName_strs=[]
            #["Title","TagType","Side","Numbers_0","Hierarchys_1","Customs_10","Title_Numbers_0","Title_Hierarchys_2","Side_Numbers_0","Side_Hierarchys_2"]
            self._orderName_strs=["Title","TagType"]
            #None,"Numbers_0","Hierarchys_10"
            self._increaseName_str=None
            self._dataChoice_strs=[
                "Title",
                "TagType",
                "Side",
                "Numbers",
                "Hierarchys",
                "Customs",
                "Orders",
                "Increase"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataName):
                self._titleName_str=dataTuple[0].getTitle()
                self._tagTypeName_str=dataTuple[0].getTagType()
                self._sideName_str=dataTuple[0].getSide()
                self._numberName_ints=dataTuple[0].getNumbers()
                self._hierarchyName_strs=dataTuple[0].getHierarchys()
                self._customName_strs=dataTuple[0].getCustoms()
                self._orderName_strs=dataTuple[0].getOrders()
                self._increaseName_str=dataTuple[0].getIncrease()

    #Setting Function
    def setTitle(self,variable):
        self._titleName_str=variable
        return self._titleName_str
    def getTitle(self):
        return self._titleName_str
    
    def setTagType(self,variable):
        self._tagTypeName_str=variable
        return self._tagTypeName_str
    def getTagType(self):
        return self._tagTypeName_str
    
    def setSide(self,variable):
        self._sideName_str=variable
        return self._sideName_str
    def getSide(self):
        return self._sideName_str
    
    def setNumbers(self,variables):
        self._numberName_ints=variables
        return self._numberName_ints
    def addNumbers(self,variables):
        self._numberName_ints+=variables
        return self._numberName_ints
    def getNumbers(self):
        return self._numberName_ints
    
    def setHierarchys(self,variables):
        self._hierarchyName_strs=variables
        return self._hierarchyName_strs
    def addHierarchys(self,variables):
        self._hierarchyName_strs+=variables
        return self._hierarchyName_strs
    def getHierarchys(self):
        return self._hierarchyName_strs
    
    def setCustoms(self,variables):
        self._customName_strs=variables
        return self._customName_strs
    def addCustoms(self,variables):
        self._customName_strs+=variables
        return self._customName_strs
    def getCustoms(self):
        return self._customName_strs
    
    def setOrders(self,variables):
        self._orderName_strs=variables
        return self._orderName_strs
    def addOrders(self,variables):
        self._orderName_strs+=variables
        return self._orderName_strs
    def getOrders(self):
        return self._orderName_strs

    def setIncrease(self,variable):
        self._increaseName_str=variable
        return self._increaseName_str
    def getIncrease(self):
        return self._increaseName_str

class DataMatrix(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataMatrix,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._matrix_MMatrix=om2.MMatrix()
            self._MSpace=om2.MSpace.kTransform #1
            self._rotateOrder=om2.MEulerRotation.kXYZ #0
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataMatrix):
                self._matrix_MMatrix=dataTuple[0].getMatrix()
                self._MSpace=dataTuple[0].getMSpace()
                self._rotateOrder=dataTuple[0].getRotateOrder()
            elif isinstance(dataTuple[0],om2.MMatrix):
                self._matrix_MMatrix=om2.MMatrix(dataTuple[0])
                self._MSpace=om2.MSpace.kTransform #1
                self._rotateOrder=om2.MEulerRotation.kXYZ #0
            elif isinstance(dataTuple[0],(list,tuple)):
                self._matrix_MMatrix=om2.MMatrix(dataTuple[0])
                self._MSpace=om2.MSpace.kTransform #1
                self._rotateOrder=om2.MEulerRotation.kXYZ #0

    def __repr__(self):
        matrix=list(self._matrix_MMatrix)
        return matrix

    def __str__(self):
        matrix=list(self._matrix_MMatrix)
        return matrix
    
    def __eq__(self,variable):
        return self._matrix_MMatrix == variable

    def __ne__(self,variable):
        return self._matrix_MMatrix != variable
    
    def __lt__(self,variable):
        return self._matrix_MMatrix < variable

    def __le__(self,variable):
        return self._matrix_MMatrix <= variable
    
    def __gt__(self,variable):
        return self._matrix_MMatrix > variable

    def __ge__(self,variable):
        return self._matrix_MMatrix >= variable

    def __add__(self,variable):
        if isinstance(variable,DataMatrix):
            add_MMatrix=self._matrix_MMatrix+variable.getMMatrix()   
            add_DataMatrix=DataMatrix(add_MMatrix)
        elif isinstance(variable,om2.MMatrix):
            add_MMatrix=self._matrix_MMatrix+variable   
            add_DataMatrix=DataMatrix(add_MMatrix)
        elif isinstance(variable,(list,tuple)):
            add_MMatrix=self._matrix_MMatrix+om2.MMatrix(variable)
            add_DataMatrix=DataMatrix(add_MMatrix)
        return add_DataMatrix

    def __radd__(self,variable):
        if isinstance(variable,DataMatrix):
            add_MMatrix=self._matrix_MMatrix+variable.getMMatrix()   
            add_DataMatrix=DataMatrix(add_MMatrix)
        elif isinstance(variable,om2.MMatrix):
            add_MMatrix=self._matrix_MMatrix+variable   
            add_DataMatrix=DataMatrix(add_MMatrix)
        elif isinstance(variable,(list,tuple)):
            add_MMatrix=self._matrix_MMatrix+om2.MMatrix(variable)
            add_DataMatrix=DataMatrix(add_MMatrix)
        return add_DataMatrix

    def __iadd__(self,variable):
        if isinstance(variable,DataMatrix):
            self._matrix_MMatrix+=variable.getMMatrix()
        elif isinstance(variable,om2.MMatrix):
            self._matrix_MMatrix+=variable
        elif isinstance(variable,(list,tuple)):
            self._matrix_MMatrix+=om2.MMatrix(variable)
        return self._matrix_MMatrix

    def __sub__(self,variable):
        if isinstance(variable,DataMatrix):
            sub_MMatrix=self._matrix_MMatrix-variable.getMMatrix()   
            sub_DataMatrix=DataMatrix(sub_MMatrix)
        elif isinstance(variable,om2.MMatrix):
            sub_MMatrix=self._matrix_MMatrix-variable   
            sub_DataMatrix=DataMatrix(sub_MMatrix)
        elif isinstance(variable,(list,tuple)):
            sub_MMatrix=self._matrix_MMatrix-om2.MMatrix(variable)
            sub_DataMatrix=DataMatrix(sub_MMatrix)
        return sub_DataMatrix

    def __rsub__(self,variable):
        if isinstance(variable,DataMatrix):
            sub_MMatrix=self._matrix_MMatrix-variable.getMMatrix()   
            sub_DataMatrix=DataMatrix(sub_MMatrix)
        elif isinstance(variable,om2.MMatrix):
            sub_MMatrix=self._matrix_MMatrix-variable   
            sub_DataMatrix=DataMatrix(sub_MMatrix)
        elif isinstance(variable,(list,tuple)):
            sub_MMatrix=self._matrix_MMatrix-om2.MMatrix(variable)
            sub_DataMatrix=DataMatrix(sub_MMatrix)
        return sub_DataMatrix

    def __isub__(self,variable):
        if isinstance(variable,DataMatrix):
            self._matrix_MMatrix-=variable.getMMatrix()   
        elif isinstance(variable,om2.MMatrix):
            self._matrix_MMatrix-=variable   
        elif isinstance(variable,(list,tuple)):
            self._matrix_MMatrix-=om2.MMatrix(variable)
        return self._matrix_MMatrix

    def __mul__(self,variable):
        if isinstance(variable,DataMatrix):
            mul_MMatrix=self._matrix_MMatrix*variable.getMMatrix()   
            mul_DataMatrix=DataMatrix(mul_MMatrix)
        elif isinstance(variable,om2.MMatrix):
            mul_MMatrix=self._matrix_MMatrix*variable   
            mul_DataMatrix=DataMatrix(mul_MMatrix)
        elif isinstance(variable,(list,tuple)):
            mul_MMatrix=self._matrix_MMatrix*om2.MMatrix(variable)
            mul_DataMatrix=DataMatrix(mul_MMatrix)
        return mul_DataMatrix

    def __rmul__(self,variable):
        if isinstance(variable,DataMatrix):
            mul_MMatrix=self._matrix_MMatrix*variable.getMMatrix()   
            mul_DataMatrix=DataMatrix(mul_MMatrix)
        elif isinstance(variable,om2.MMatrix):
            mul_MMatrix=self._matrix_MMatrix*variable   
            mul_DataMatrix=DataMatrix(mul_MMatrix)
        elif isinstance(variable,(list,tuple)):
            mul_MMatrix=self._matrix_MMatrix*om2.MMatrix(variable)
            mul_DataMatrix=DataMatrix(mul_MMatrix)
        return mul_DataMatrix
    
    def __imul__(self,variable):
        if isinstance(variable,DataMatrix):
            self._matrix_MMatrix*=variable.getMMatrix()
        elif isinstance(variable,om2.MMatrix):
            self._matrix_MMatrix*=variable
        elif isinstance(variable,(list,tuple)):
            self._matrix_MMatrix*=om2.MMatrix(variable)
        return self._matrix_MMatrix

    def __len__(self):
        return len(self._matrix_MMatrix)

    def __setitem__(self,key,variable):
        self._matrix_MMatrix[key]=variable
    
    def __getitem__(self,variable):
        return self._matrix_MMatrix[variable]
    
    def __delitem__(self,variable):
        return self._matrix_MMatrix[variable]

    #Setting Function
    def setMatrix(self,variable):
        self._matrix_MMatrix=om2.MMatrix(variable)
        return self._matrix_MMatrix
    def getMatrix(self):
        matrix=list(self._matrix_MMatrix)
        return matrix
    def getMMatrix(self):
        return self._matrix_MMatrix
    
    def setMSpace(self,variable):
        self._MSpace=variable
    def getMSpace(self):
        return self._MSpace

    def setRotateOrder(self,variable):
        self._rotateOrder=variable
    def getRotateOrder(self):
        return self._rotateOrder

    @property
    def inverseX(self):
        inverse_DataMatrix=DataMatrix([
            -1.0,0.0,0.0,0.0, 
            0.0,1.0,0.0,0.0, 
            0.0,0.0,1.0,0.0, 
            0.0,0.0,0.0,1.0 
        ])
        return inverse_DataMatrix
    
    @property
    def inverseY(self):
        inverse_DataMatrix=DataMatrix([
            1.0,0.0,0.0,0.0, 
            0.0,-1.0,0.0,0.0, 
            0.0,0.0,1.0,0.0, 
            0.0,0.0,0.0,1.0 
        ])
        return inverse_DataMatrix
    
    @property
    def inverseZ(self):
        inverse_DataMatrix=DataMatrix([
            1.0,0.0,0.0,0.0, 
            0.0,1.0,0.0,0.0, 
            0.0,0.0,-1.0,0.0, 
            0.0,0.0,0.0,1.0 
        ])
        return inverse_DataMatrix

class DataMatrixMix(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataMatrixMix,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._world_DataMatrix=None
            self._local_DataMatrix=None
            self._parent_DataMatrix=None
            self._dataChoice_strs=[
                "WorldDataMatrix",
                "LocalDataMatrix",
                "ParentDataMatrix"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataMatrixMix):
                self._world_DataMatrix=dataTuple[0].getWorldDataMatrix()
                self._local_DataMatrix=dataTuple[0].getLocalDataMatrix()
                self._parent_DataMatrix=dataTuple[0].getParentDataMatrix()

    #Setting Function
    def setWorldDataMatrix(self,variable):
        self._world_DataMatrix=variable
        return self._world_DataMatrix
    def getWorldDataMatrix(self):
        return self._world_DataMatrix
    
    def setLocalDataMatrix(self,variable):
        self._local_DataMatrix=variable
        return self._local_DataMatrix
    def getLocalDataMatrix(self):
        return self._local_DataMatrix
    
    def setParentDataMatrix(self,variable):
        self._parent_DataMatrix=variable
        return self._parent_DataMatrix
    def getParentDataMatrix(self):
        return self._parent_DataMatrix

class DataTime(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataTime,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._unit_int=None
            self._time_float=None
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataTime):
                self._unit_int=dataTuple[0].getUnitType()
                self._time_float=dataTuple[0].getTime()
        
    def setUnitType(self,variable):
        self._unit_int=variable
        return self._unit_int
    def currentUnitType(self):
        self._unit_int=om2.MTime.uiUnit
        return self._unit_int
    def getUnitType(self):
        return self._unit_int
    
    def setTime(self,variable):
        self._time_float=variable
        return self._time_float
    def currentTime(self):
        current_MTime=oma2.MAnimControl.currentTime()
        self._time_float=current_MTime.value
        return self._time_float
    def getTime(self):
        return self._time_float

class DataVector(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataVector,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 == len(dataTuple) or 
            4 <= len(dataTuple)):
            self._x_float=None
            self._y_float=None
            self._z_float=None
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataVector):
                self._x_float=dataTuple[0].getVectorX()
                self._y_float=dataTuple[0].getVectorY()
                self._z_float=dataTuple[0].getVectorZ()
            elif isinstance(dataTuple[0],
                (om2.MVector,
                 om2.MFloatVector,
                 om2.MPoint,
                 om2.MFloatPoint)):
                self._x_float=dataTuple[0].x
                self._y_float=dataTuple[0].y
                self._z_float=dataTuple[0].z
        elif 3 == len(dataTuple):
            self._x_float=dataTuple[0]
            self._y_float=dataTuple[1]
            self._z_float=dataTuple[2]

    @property
    def vector(self):
        vector_tuple3=(self._x_float,self._y_float,self._z_float)
        return vector_tuple3

    #Setting Function
    def setVector(self,variables):
        vector_MVector=om2.MVector(variables)
        self._x_float=vector_MVector.x
        self._y_float=vector_MVector.y
        self._z_float=vector_MVector.z
        return self.vector
    def getVector(self):
        return self.vector
    def getMVector(self):
        vector_MVector=om2.MVector(self._x_float,self._y_float,self._z_float)
        return vector_MVector
    
    def setVectorX(self,variable):
        self._x_float=variable
        return self._x_float
    def getVectorX(self):
        return self._x_float
    
    def setVectorY(self,variable):
        self._y_float=variable
        return self._y_float
    def getVectorY(self):
        return self._y_float
    
    def setVectorZ(self,variable):
        self._z_float=variable
        return self._z_float
    def getVectorZ(self):
        return self._z_float

class DataTranslate(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataTranslate,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 == len(dataTuple) or 
            4 <= len(dataTuple)):
            self._x_float=None
            self._y_float=None
            self._z_float=None
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataVector):
                self._x_float=dataTuple[0].getVectorX()
                self._y_float=dataTuple[0].getVectorY()
                self._z_float=dataTuple[0].getVectorZ()
            elif isinstance(dataTuple[0],
                (om2.MVector,
                 om2.MFloatVector,
                 om2.MPoint,
                 om2.MFloatPoint)):
                self._x_float=dataTuple[0].x
                self._y_float=dataTuple[0].y
                self._z_float=dataTuple[0].z
        elif 3 == len(dataTuple):
            self._x_float=dataTuple[0]
            self._y_float=dataTuple[1]
            self._z_float=dataTuple[2]

    #Setting Function
    @property
    def vector(self):
        vector_tuple3=(self._x_float,self._y_float,self._z_float)
        return vector_tuple3
    
    def setTranslate(self,variables):
        translate_MVector=om2.MVector(variables)
        self._x_float=translate_MVector.x
        self._y_float=translate_MVector.y
        self._z_float=translate_MVector.z
        return self.vector
    def getTranslate(self):
        return self.vector
    def getMVector(self):
        vector_MVector=om2.MVector(self._x_float,self._y_float,self._z_float)
        return vector_MVector
    
    def setTranslateX(self,variable):
        self.x=variable
        return self.x
    def getTranslateX(self):
        return self.x
    
    def setTranslateY(self,variable):
        self.y=variable
        return self.y
    def getTranslateY(self):
        return self.y
    
    def setTranslateZ(self,variable):
        self.z=variable
        return self.z
    def getTranslateZ(self):
        return self.z

class DataRotation(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataRotation,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or  
            5 <= len(dataTuple)):
            self._x_float=None
            self._y_float=None
            self._z_float=None
            self._order_int=None
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataRotation):
                self._x_float=dataTuple[0].getRotateX()
                self._y_float=dataTuple[0].getRotateY()
                self._z_float=dataTuple[0].getRotateZ()
                self._order_int=dataTuple[0].getRotateOrder()
            elif isinstance(dataTuple[0],om2.MEulerRotation):
                self._x_float=dataTuple[0].x
                self._y_float=dataTuple[0].y
                self._z_float=dataTuple[0].z
                self._order_int=dataTuple[0].order
            elif isinstance(dataTuple[0],om2.MVector):
                self._x_float=dataTuple[0].x
                self._y_float=dataTuple[0].y
                self._z_float=dataTuple[0].z
                self._order_int=om2.MEulerRotation.kXYZ #0
            elif isinstance(dataTuple[0],(list,tuple)):
                self._x_float=dataTuple[0][0]
                self._y_float=dataTuple[0][1]
                self._z_float=dataTuple[0][2]
                self._order_int=om2.MEulerRotation.kXYZ #0
        elif 2 == len(dataTuple):
            if (isinstance(dataTuple[0],(list,tuple)) and 
                isinstance(dataTuple[1],int)):
                self._x_float=dataTuple[0][0]
                self._y_float=dataTuple[0][1]
                self._z_float=dataTuple[0][2]
                self._order_int=dataTuple[1]
        elif 3 == len(dataTuple):
            self._x_float=dataTuple[0]
            self._y_float=dataTuple[1]
            self._z_float=dataTuple[2]
            self._order_int=om2.MEulerRotation.kXYZ #0
        elif 4 == len(dataTuple):
            self._x_float=dataTuple[0]
            self._y_float=dataTuple[1]
            self._z_float=dataTuple[2]
            self._order_int=dataTuple[3]

    @property
    def euler(self):
        euler_tuple3=(self._x_float,self._y_float,self._z_float)
        return euler_tuple3

    #Setting Function
    def setRotate(self,variables):
        rotate_MEulerRotation=om2.MEulerRotation(variables)
        self._x_float=rotate_MEulerRotation.x
        self._y_float=rotate_MEulerRotation.y
        self._z_float=rotate_MEulerRotation.z
        self._order_int=rotate_MEulerRotation.order
        return self.euler
    def getRotate(self):
        return self.euler
    
    def setRotateX(self,variable):
        self._x_float=variable
        return self._x_float
    def getRotateX(self):
        return self._x_float
    
    def setRotateY(self,variable):
        self._y_float=variable
        return self._y_float
    def getRotateY(self):
        return self._y_float
    
    def setRotateZ(self,variable):
        self._z_float=variable
        return self._z_float
    def getRotateZ(self):
        return self._z_float

    def setRotateOrder(self,variable):
        self._order_int=variable
        return self._order_int
    def getRotateOrder(self):
        return self._order_int

class DataQuaternion(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataQuaternion,self).__init__(*dataTuple)
        #self.x=float
        #self.y=float
        #self.z=float
        #self.w=float
        if (0 == len(dataTuple) or  
            5 <= len(dataTuple)):
            self._x_float=None
            self._y_float=None
            self._z_float=None
            self._order_int=None
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataQuaternion):
                self._x_float=dataTuple[0].getQuaternionX()
                self._y_float=dataTuple[0].getQuaternionY()
                self._z_float=dataTuple[0].getQuaternionZ()
                self._w_float=dataTuple[0].getQuaternionW()
            elif isinstance(dataTuple[0],om2.MQuaternion):
                self._x_float=dataTuple[0].x
                self._y_float=dataTuple[0].y
                self._z_float=dataTuple[0].z
                self._order_int=dataTuple[0].w
            elif isinstance(dataTuple[0],(list,tuple)):
                self._x_float=dataTuple[0][0]
                self._y_float=dataTuple[0][1]
                self._z_float=dataTuple[0][2]
                self._w_float=dataTuple[0][3]
        elif 2 == len(dataTuple):
            if (isinstance(dataTuple[0],om2.MVector) and 
                isinstance(dataTuple[1],float) or 
                isinstance(dataTuple[0],float) and 
                isinstance(dataTuple[1],om2.MVector)):
                pass
        elif 3 == len(dataTuple):
            if (isinstance(dataTuple[0],om2.MVector) and 
                isinstance(dataTuple[1],om2.MVector) and 
                isinstance(dataTuple[2],float)):
                pass
        elif 4 == len(dataTuple):
            self._x_float=dataTuple[0]
            self._y_float=dataTuple[1]
            self._z_float=dataTuple[2]
            self._w_float=dataTuple[3]

    @property
    def quaternion(self):
        quaternion_tuple4=(self._x_float,self._y_float,self._z_float,self._w_float)
        return quaternion_tuple4

    #Setting Function
    def setQuaternion(self,variables):
        quat_MQuaternion=om2.MQuaternion(variables)
        self.x=quat_MQuaternion.x
        self.y=quat_MQuaternion.y
        self.z=quat_MQuaternion.z
        self.w=quat_MQuaternion.w
        return self.quaternion
    def getQuaternion(self):
        return self.quaternion

    def setQuaternionX(self,variable):
        self._x_float=variable
        return self._x_float
    def getQuaternionX(self):
        return self._x_float
    
    def setQuaternionY(self,variable):
        self._y_float=variable
        return self._y_float
    def getQuaternionY(self):
        return self._y_float
    
    def setQuaternionZ(self,variable):
        self._z_float=variable
        return self._z_float
    def getQuaternionZ(self):
        return self._z_float
    
    def setQuaternionW(self,variable):
        self._w_float=variable
        return self._w_float
    def getQuaternionW(self):
        return self._w_float

class DataScale(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataScale,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 == len(dataTuple) or 
            4 <= len(dataTuple)):
            self._x_float=None
            self._y_float=None
            self._z_float=None
            self._dataChoice_strs=[
                "Scale"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataScale):
                self._x_float=dataTuple[0].getScaleX()
                self._y_float=dataTuple[0].getScaleY()
                self._z_float=dataTuple[0].getScaleZ()
            elif isinstance(dataTuple[0],om2.MVector):
                self._x_float=dataTuple[0].x
                self._y_float=dataTuple[0].y
                self._z_float=dataTuple[0].z
                self._dataChoice_strs=[
                    "Scale"
                ]
            elif isinstance(dataTuple[0],(list,tuple)):
                self._x_float=dataTuple[0][0]
                self._y_float=dataTuple[0][1]
                self._z_float=dataTuple[0][2]
                self._dataChoice_strs=[
                    "Scale"
                ]
        elif 3 == len(dataTuple):
            self._x_float=dataTuple[0]
            self._y_float=dataTuple[1]
            self._z_float=dataTuple[2]
            self._dataChoice_strs=[
                "Scale"
            ]

    @property
    def vector(self):
        scale_tuple3=(self._x_float,self._y_float,self._z_float)
        return scale_tuple3

    #Setting Function
    def setScale(self,variables):
        scale_DataScale=DataScale(variables)
        self._x_float=scale_DataScale.getScaleX()
        self._y_float=scale_DataScale.getScaleY()
        self._z_float=scale_DataScale.getScaleZ()
        return self.vector
    def getScale(self):
        return self.vector
    
    def setScaleX(self,variable):
        self._x_float=variable
        return self._x_float
    def getScaleX(self):
        return self._x_float
    
    def setScaleY(self,variable):
        self._y_float=variable
        return self._y_float
    def getScaleY(self):
        return self._y_float
    
    def setScaleZ(self,variable):
        self._z_float=variable
        return self._z_float
    def getScaleZ(self):
        return self._z_float

class DataKey(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataKey,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or
            2 <= len(dataTuple)):
            self._input_value=None
            self._output_value=None
            self._inTanType_str=None
            self._outTanType_str=None
            self._dataChoice_strs=[
                "InputValue",
                "OutputValue",
                "InputTanType",
                "OutputTanType"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataKey):
                self._input_value=dataTuple[0].getInputValue()
                self._output_value=dataTuple[0].getOutputValue()
                self._inTanType_str=dataTuple[0].getInputTanType()
                self._outTanType_str=dataTuple[0].getOutputTanType()

    #Setting Function
    def setInputValue(self,variable):
        self._input_value=variable
        return self._input_value
    def getInputValue(self):
        return self._input_value
    
    def setOutputValue(self,variable):
        self._output_value=variable
        return self._output_value
    def getOutputValue(self):
        return self._output_value
    
    def setInputTanType(self,variable):
        self._inputTanType_str=variable
        return self._inputTanType_str
    def getInputTanType(self):
        return self._inputTanType_str
    
    def setOutputTanType(self,variable):
        self._outputTanType_str=variable
        return self._outputTanType_str
    def getOutputTanType(self):
        return self._outputTanType_str

class DataPoint(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataPoint,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 == len(dataTuple) or 
            3 == len(dataTuple) or 
            6 <= len(dataTuple)):
            self._x_float=None
            self._y_float=None
            self._z_float=None
            self._index_int=None
            self._dataChoice_strs=[
                "PointX",
                "PointY",
                "PointZ",
                "PointW",
                "ID"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataPoint):
                self._x_float=dataTuple[0].getPointX()
                self._y_float=dataTuple[0].getPointY()
                self._z_float=dataTuple[0].getPointZ()
                self._w_float=dataTuple[0].getPointW()
                self._index_int=dataTuple[0].getID()
            elif isinstance(dataTuple[0],om2.MPoint):
                self._x_float=dataTuple[0].x
                self._y_float=dataTuple[0].y
                self._z_float=dataTuple[0].z
                self._w_float=dataTuple[0].w
                self._index_int=None
                self._dataChoice_strs=[
                    "PointX",
                    "PointY",
                    "PointZ",
                    "PointW",
                    "ID"
                ]
        elif 4 == len(dataTuple):
            self._x_float=dataTuple[0]
            self._y_float=dataTuple[1]
            self._z_float=dataTuple[2]
            self._index_int=dataTuple[3]
            self._dataChoice_strs=[
                "PointX",
                "PointY",
                "PointZ",
                "PointW",
                "ID"
            ]
        elif 5 == len(dataTuple):
            self._x_float=dataTuple[0]
            self._y_float=dataTuple[1]
            self._z_float=dataTuple[2]
            self._w_float=dataTuple[3]
            self._index_int=[4]
            self._dataChoice_strs=[
                "PointX",
                "PointY",
                "PointZ",
                "PointW",
                "ID"
            ]
                
    @property
    def point(self):
        point_tuple4=(self._x_float,self._y_float,self._z_float,self._w_float)
        return point_tuple4

    def setPoint(self,variables):
        self.point=DataPoint(variables)
        return self.point
    def getPoint(self):
        return self.point
    def getMPoint(self):
        point_MPoint=om2.MPoint(self._x_float,self._y_float,self._z_float,self._w_float)
        return point_MPoint
    
    def setPointX(self,variable):
        self._x_float=variable
        return self._x_float
    def getPointX(self):
        return self._x_float
    
    def setPointY(self,variable):
        self._y_float=variable
        return self._y_float
    def getPointY(self):
        return self._y_float
    
    def setPointZ(self,variable):
        self._z_float=variable
        return self._z_float
    def getPointZ(self):
        return self._z_float
    
    def setPointW(self,variable):
        self._w_float=variable
        return self._w_float
    def getPointW(self):
        return self._w_float

    def setID(self,variable):
        self._index_int=variable
        return self._index_int
    def getID(self):
        return self._index_int

class DataVertex(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataVertex,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._vertex_DataPoint=None
            self._vector_DataVector=None
            self._index_int=None
            self._dataChoice_strs=[
                "DataPoint",
                "DataVector",
                "ID"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataVertex):
                self._vertex_DataPoint=dataTuple[0].getDataPoint()
                self._vector_DataVector=dataTuple[0].getDataVector()
                self._index_int=dataTuple[0].getID()

    def setDataPoint(self,variable):
        self._vertex_DataPoint=variable
        return self._vertex_DataPoint
    def getDataPoint(self):
        return self._vertex_DataPoint

    def setDataVector(self,variable):
        self._vector_DataVector=variable
        return self._vector_DataVector
    def getDataVector(self):
        return self._vector_DataVector

    def setID(self,variable):
        self._index_int=variable
        return self._index_int
    def getID(self):
        return self._index_int

class DataEdge(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataEdge,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._edge_DataVertex2=[]
            self._index_int=None
            self._dataChoice_strs=[
                "DataVertex2",
                "ID"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataEdge):
                self._edge_DataVertex2=dataTuple[0].getDataVertex2()
                self._index_int=dataTuple[0].getID()

    def setDataVertex2(self,variable2):
        self._edge_DataVertex2=variable2
        return self._edge_DataVertex2
    def getDataVertex2(self):
        return self._edge_DataVertex2

    def setID(self,variable):
        self._index_int=variable
        return self._index_int
    def getID(self):
        return self._index_int

class DataFace(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataFace,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._vertexFace_DataVertexs=[]
            self._edgeFace_DataEdges=[]
            self._index_int=None
            self._dataChoice_strs=[
                "DataVertexs",
                "DataEdges",
                "ID"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataFace):
                self._vertexFace_DataVertexs=dataTuple[0].getDataVertexs()
                self._edgeFace_DataEdges=dataTuple[0].getDataEdges()
                self._index_int=dataTuple[0].getID()

    def setDataVertexs(self,variables):
        self._vertexFace_DataVertexs=variables
        return self._vertexFace_DataVertexs
    def getDataVertexs(self):
        return self._vertexFace_DataVertexs
    
    def setDataEdges(self,variables):
        self._edgeFace_DataEdges=variables
        return self._edgeFace_DataEdges
    def getDataEdges(self):
        return self._edgeFace_DataEdges

    def setID(self,variable):
        self._index_int=variable
        return self._index_int
    def getID(self):
        return self._index_int

#DefinitionArray Data
class DataMenuParamArray(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataMenuParamArray,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._menuName_str=None
            self._menuType_str=None #"single" or "multi"
            self._menu_DataMenuParams=[]
            self._dataChoice_strs=[
                "Name",
                "Type",
                "DataMenuParams"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataMenuParamArray):
                self._menuName_str=dataTuple[0].getName()
                self._menuType_str=dataTuple[0].getType()
                self._menu_DataMenuParams=dataTuple[0].getDataMenuParams()

    def __len__(self):
        return len(self._menu_DataMenuParams)

    def __getitem__(self,index):
        return self._menu_DataMenuParams[index]

    def __setitem__(self,index,value):
        self._menu_DataMenuParams[index]=value

    def __delitem__(self,index):
        del self._menu_DataMenuParams[index]

    def __iter__(self):
        return iter(self._menu_DataMenuParams)

    #Setting Function
    def setName(self,variable):
        self._menuName_str=variable
        return self._menuName_str
    def getName(self):
        return self._menuName_str
    
    def setType(self,variable):
        self._menuType_str=variable
        return self._menuType_str
    def getType(self):
        return self._menuType_str
    
    def setDataMenuParams(self,variable):
        self._menu_DataMenuParams=variable
        return self._menu_DataMenuParams
    def addDataMenuParams(self,variable):
        self._menu_DataMenuParams+=variable
        return self._menu_DataMenuParams
    def getDataMenuParams(self):
        return self._menu_DataMenuParams
    
class DataAttributeWeightArray(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataAttributeWeightArray,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._attrWeight_DataAttributeWeights=[]
            self._indexWeightArray_int=None
            self._dataChoice_strs=[
                "IndexWeidghts",
                "DataAttributeWeights"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataAttributeWeightArray):
                self._attrWeight_DataAttributeWeights=dataTuple[0].getDataAttributeWeights()
                self._indexWeightArray_int=dataTuple[0].getIndexWeightArray()

    def __len__(self):
        return len(self._attrWeight_DataAttributeWeights)

    def __getitem__(self,index):
        return self._attrWeight_DataAttributeWeights[index]

    def __setitem__(self,index,value):
        self._attrWeight_DataAttributeWeights[index]=value

    def __delitem__(self,index):
        del self._attrWeight_DataAttributeWeights[index]

    def __iter__(self):
        return iter(self._attrWeight_DataAttributeWeights)

    #Setting Function
    def setIndexWeightArray(self,variable):
        self._indexWeightArray_int=variable
        return self._indexWeightArray_int
    def getIndexWeightArray(self):
        return self._indexWeightArray_int

    def setDataAttributeWeights(self,variables):
        self._attrWeight_DataAttributeWeights=variables
        return self._attrWeight_DataAttributeWeights
    def addDataAttributeWeights(self,variables):
        self._attrWeight_DataAttributeWeights+=variables
        return self._attrWeight_DataAttributeWeights
    def getDataAttributeWeights(self):
        return self._attrWeight_DataAttributeWeights

class DataPointArray(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataPointArray,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._point_DataPoints=[]
            self._dataChoice_strs=[
                "DataPoints"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataPointArray):
                self._point_DataPoints=dataTuple[0].getDataPoints()
    
    def __len__(self):
        return len(self._point_DataPoints)

    def __getitem__(self,index):
        return self._point_DataPoints[index]

    def __setitem__(self,index,value):
        self._point_DataPoints[index]=value

    def __delitem__(self,index):
        del self._point_DataPoints[index]

    def __iter__(self):
        return iter(self._point_DataPoints)

    def setDataPoints(self,variables):
        self._point_DataPoints=variables
        return self._point_DataPoints
    def addDataPoints(self,variables):
        self._point_DataPoints+=variables
        return self._point_DataPoints
    def getDataPoints(self):
        return self._point_DataPoints

#Object Data
class DataMenu(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataMenu,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._menuName_str=None
            self._menu_DataMenuParamArrays=[]
            self._dataChoice_strs=[
                "Name",
                "DataMenuParamArrays"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataMenu):
                self._menuName_str=dataTuple[0].getName()
                self._menu_DataMenuParamArrays=dataTuple[0].getDataMenuParamArrays()

    def setName(self,variable):
        self._menuName_str=variable
        return self._menuName_str
    def getName(self):
        return self._menuName_str
    
    def setDataMenuParamArrays(self,variables):
        self._menu_DataMenuParamArrays=variables
        return self._menu_DataMenuParamArrays
    def addDataMenuParamArrays(self,variables):
        self._menu_DataMenuParamArrays+=variables
        return self._menu_DataMenuParamArrays
    def getDataMenuParamArrays(self):
        return self._menu_DataMenuParamArrays

class DataNode(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataNode,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._nodeName_str=None
            self._nodeType_str=None
            self._dataChoice_strs=[
                "Name",
                "Type"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataNode):
                self._nodeName_str=dataTuple[0].getName()
                self._nodeType_str=dataTuple[0].getType()
            elif isinstance(dataTuple[0],om2.MObject):
                node_MFnDependencyNode=om2.MFnDependencyNode(dataTuple[0])
                self._nodeName_str=node_MFnDependencyNode.name()
                self._nodeType_str=node_MFnDependencyNode.typeName
                self._dataChoice_strs=[
                    "Name",
                    "Type"
                ]

    def __str__(self):
        return str(self._nodeName_str)
    
    #Setting Function
    def setName(self,variable):
        self._nodeName_str=variable
        return self._nodeName_str
    def getName(self):
        return self._nodeName_str
    
    def setType(self,variable):
        self._nodeType_str=variable
        return self._nodeType_str
    def getType(self):
        return self._nodeType_str

class DataPlug(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataPlug,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._node_DataNode=None
            self._attr_DataAttribute=None
            self._keyLock_bool=False
            self._valueLock_bool=False
            self._channelHide_bool=False
            self._dataChoice_strs=[
                "DataNode",
                "DataAttribute",
                "KeyLockState",
                "ValueLockState",
                "HideState"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataPlug):
                self._node_DataNode=dataTuple[0].getDataNode()
                self._attr_DataAttribute=dataTuple[0].getDataAttribute()
                self._keyLock_bool=dataTuple[0].getKeyLockState()
                self._valueLock_bool=dataTuple[0].getValueLockState()
                self._channelHide_bool=dataTuple[0].getHideState()
            elif isinstance(dataTuple[0],om2.MPlug):
                self._node_DataNode=DataNode(dataTuple[0].node())
                self._attr_DataAttribute=DataAttribute(dataTuple[0].attribute())
                self._keyLock_bool=not dataTuple[0].isKeyable
                self._valueLock_bool=dataTuple[0].isLocked
                self._channelHide_bool=not dataTuple[0].isChannelBox
                self._dataChoice_strs=[
                    "DataNode",
                    "DataAttribute",
                    "KeyLockState",
                    "ValueLockState",
                    "HideState"
                ]

    #Setting Function
    def setDataNode(self,variable):
        self._node_DataNode=variable
        return self._node_DataNode
    def getDataNode(self):
        return self._node_DataNode
    
    def setDataAttribute(self,variable):
        self._attr_DataAttribute=variable
        return self._attr_DataAttribute
    def getDataAttribute(self):
        return self._attr_DataAttribute

    def setKeyLockState(self,variable):
        self._keyLock_bool=variable
        return self._keyLock_bool
    def getKeyLockState(self):
        return self._keyLock_bool
    
    def setValueLockState(self,variable):
        self._valueLock_bool=variable
        return self._valueLock_bool
    def getValueLockState(self):
        return self._valueLock_bool
    
    def setHideState(self,variable):
        self._channelHide_bool=variable
        return self._channelHide_bool
    def getHideState(self):
        return self._channelHide_bool

class DataConnectPlug(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataConnectPlug,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._source_DataPlug=None
            self._target_DataPlugs=[]
            self._dataChoice_strs=[
                "SourceDataPlug",
                "TargetDataPlugs"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataConnectPlug):
                self._source_DataPlug=dataTuple[0].getSourceDataPlug()
                self._target_DataPlugs=dataTuple[0].getTargetDataPlugs()

    #Setting Function
    def setSourceDataPlug(self,variable):
        self._source_DataPlug=variable
        return self._source_DataPlug
    def getSourceDataPlug(self):
        return self._source_DataPlug
    
    def setTargetDataPlugs(self,variables):
        self._target_DataPlugs=variables
        return self._target_DataPlugs
    def addTargetDataPlugs(self,variables):
        self._target_DataPlugs+=variables
        return self._target_DataPlugs
    def getTargetDataPlugs(self):
        return self._target_DataPlugs

class DataMesh(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataMesh,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._polygon_DataFaces=[]
            self._dataChoice_strs=[
                "DataFaces"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataMesh):
                self._polygon_DataFaces=dataTuple[0].getDataFaces()

    def setDataFaces(self,variables):
        self._polygon_DataFaces=variables
        return self._polygon_DataFaces
    def getDataFaces(self):
        return self._polygon_DataFaces

class DataNurbsSurface(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataNurbsSurface,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            pass
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataNurbsSurface):
                pass

class DataNurbsCurve(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataNurbsCurve,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            pass
        elif 1 == len(dataTuple):
            if isinstance(dataTuple,DataNurbsCurve):
                pass

class DataAnimCurve(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataAnimCurve,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._key_DataKeys=[]
            self._input_DataPlug=None
            self._output_DataPlug=None
            self._dataChoice_strs=[
                "DataKeys",
                "InputDataPlug",
                "OutputDataPlug"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataAnimCurve):
                self._key_DataKeys=dataTuple[0].getDataKeys()
                self._input_DataPlug=dataTuple[0].getInputDataPlug()
                self._output_DataPlug=dataTuple[0].getOutputDataPlug()

    #Setting Function
    def setDataKeys(self,variables):
        self._key_DataKeys=variables
        return self._key_DataKeys
    def addDataKeys(self,variables):
        self._key_DataKeys+=variables
        return self._key_DataKeys
    def getDataKeys(self):
        return self._key_DataKeys
    
    def setInputDataPlug(self,variable):
        self._input_DataPlug=variable
        return self._input_DataPlug
    def getInputDataPlug(self):
        return self._input_DataPlug
    
    def setOutputDataPlug(self,variable):
        self._output_DataPlug=variable
        return self._output_DataPlug
    def getOutputDataPlug(self):
        return self._output_DataPlug

#Action Data
class DataBind(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataBind,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._shape_DataNode=None
            self._joint_DataNodes=[]
            self._skicWeight_DataAttributeWeightArrays=[]
            self._dataChoice_strs=[
                "ShapeDataNode",
                "JointDataNodes",
                "DataAttributeWeightArrays"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataBind):
                self._shape_DataNode=dataTuple[0].getShapeDataNode()
                self._joint_DataNodes=dataTuple[0].getJointDataNodes()
                self._skicWeight_DataAttributeWeightArrays=dataTuple[0].getDataAttributeWeightArrays()
    
    #Setting Function
    def setShapeDataNode(self,variable):
        self._shape_DataNode=variable
        return self._shape_DataNode
    def getShapeDataNode(self):
        return self._shape_DataNode

    def setJointDataNodes(self,variables):
        self._joint_DataNodes=variables
        return self._joint_DataNodes
    def addJointDataNodes(self,variables):
        self._joint_DataNodes+=variables
        return self._joint_DataNodes
    def getJointDataNodes(self):
        return self._joint_DataNodes
    
    def setDataAttributeWeightArrays(self,variables):
        self._skicWeight_DataAttributeWeightArrays=variables
        return self._skicWeight_DataAttributeWeightArrays
    def addDataAttributeWeightArrays(self,variables):
        self._skicWeight_DataAttributeWeightArrays+=variables
        return self._skicWeight_DataAttributeWeightArrays
    def getDataAttributeWeightArrays(self):
        return self._skicWeight_DataAttributeWeightArrays

class DataKeyable(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataKeyable,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._node_DataNode=None
            self._keyable_DataAnimCurves=[]
            self._dataChoice_strs=[
                "DataNode",
                "DataAnimCurves"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataKeyable):
                self._node_DataNode=dataTuple[0].getDataNode()
                self._keyable_DataAnimCurves=dataTuple[0].getDataAnimCurves()

    #Setting Function
    def setDataNode(self,variable):
        self._node_DataNode=variable
        return self._node_DataNode
    def getDataNode(self):
        return self._node_DataNode

    def setDataAnimCurves(self,variables):
        self._keyable_DataAnimCurves=variables
        return self._keyable_DataAnimCurves
    def addDataAnimCurves(self,variables):
        self._keyable_DataAnimCurves+=variables
        return self._keyable_DataAnimCurves
    def getDataAnimCurves(self):
        return self._keyable_DataAnimCurves

class DataMatch(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataMatch,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._node_DataNode=None
            self._match_DataNode=None
            self._match_DataMatrix=None
            self._dataChoice_strs=[
                "DataNode",
                "MatchDataNode",
                "MatchDataMatrix"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataMatch):
                self._node_DataNode=dataTuple[0].getDataNode()
                self._match_DataNode=dataTuple[0].getMatchDataNode()
                self._match_DataMatrix=dataTuple[0].getMatchDataMatrix()

    #Setting Function
    def setDataNode(self,variable):
        self._node_DataNode=variable
        return self._node_DataNode
    def getDataNode(self):
        return self._node_DataNode

    def setMatchDataNode(self,variable):
        self._match_DataNode=variable
        return self._match_DataNode
    def getMatchDataNode(self):
        return self._match_DataNode
    
    def setMatchDataMatrix(self,variable):
        self._match_DataMatrix=variable
        return self._match_DataMatrix
    def getMatchDataMatrix(self):
        return self._match_DataMatrix

class DataMirror(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataMirror,self).__init__(*dataTuple)
        if dataTuple is None:
            self._node_DataNode=None
            self._pivot_DataNode=None
            self._pivot_DataMatrix=None
            self._mirrorAxis_str="x"
            self._mirrorOrientVector_str="z"
            self._dataChoice_strs=[
                "DataNode",
                "PivotDataNode",
                "PivotDataMatrix",
                "MirrorAxis",
                "MirrorOrientVector"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataMirror):
                self._node_DataNode=dataTuple[0].getDataNode()
                self._pivot_DataNode=dataTuple[0].getPivotDataNode()
                self._pivot_DataMatrix=dataTuple[0].getPivotDataMatrix()
                self._mirrorAxis_str=dataTuple[0].getMirrorAxis()
                self._mirrorOrientVector_str=dataTuple[0].getMirrorOrientVector()

    #Setting Function
    def setDataNode(self,variable):
        self._node_DataNode=variable
        return self._node_DataNode
    def getDataNode(self):
        return self._node_DataNode
    
    def setPivotDataNode(self,variable):
        self._pivot_DataNode=variable
        return self._pivot_DataNode
    def getPivotDataNode(self):
        return self._pivot_DataNode
    
    def setPivotDataMatrix(self,variable):
        self._pivot_DataMatrix=variable
        return self._pivot_DataMatrix
    def getPivotDataMatrix(self):
        return self._pivot_DataMatrix
    
    def setMirrorAxis(self,variable):
        self._mirrorAxis_str=variable
        return self._mirrorAxis_str
    def getMirrorAxis(self):
        return self._mirrorAxis_str

    def setMirrorOrientVector(self,variable):
        self._mirrorOrientVector_str=variable
        return self._mirrorOrientVector_str
    def getMirrorOrientVector(self):
        return self._mirrorOrientVector_str
