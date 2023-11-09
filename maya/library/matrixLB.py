# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import sys,math

import cgInTools as cit
from ...library import baseLB as bLB
cit.reloads([bLB])

class DataMatrix(om2.MMatrix):
    def __init__(self,*matrix):
        super(DataMatrix,self).__init__(*matrix)
        #self.kIdentity=om2.MMatrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
        self._MSpace=om2.MSpace.kTransform #1
        self._rotateOrder=om2.MEulerRotation.kXYZ #0

    def setMatrix(self,variable):
        self.kIdentity=om2.MMatrix(variable)
        return self.kIdentity
    def getMatrix(self):
        matrix=list(self.kIdentity)
        return matrix
    def getMMatrix(self):
        return self.self.kIdentity
    
    def setMSpace(self,variable):
        self._MSpace=variable
    def getMSpace(self):
        return self._MSpace

    def setRotateOrder(self,variable):
        self._rotateOrder=variable
    def getRotateOrder(self):
        return self._rotateOrder

class SelfMatrix(bLB.SelfOrigin):
    def __init__(self):
        super(SelfMatrix,self).__init__()
        self._matrix_DataMatrix=DataMatrix()
        self._pivot_DataMatrix=DataMatrix()
        self._subject_DataMatrix=DataMatrix()

        self._mirrorAxis_str="x"
        self._mirrorOrientVector_str="z"
        self._mirrorData_dict={
            "x":[
                -1.0,0.0,0.0,0.0, 
                0.0,1.0,0.0,0.0, 
                0.0,0.0,1.0,0.0, 
                0.0,0.0,0.0,1.0 
            ],
            "X":[
                -1.0,0.0,0.0,0.0, 
                0.0,1.0,0.0,0.0, 
                0.0,0.0,1.0,0.0, 
                0.0,0.0,0.0,1.0 
            ],
            "y":[
                1.0,0.0,0.0,0.0, 
                0.0,-1.0,0.0,0.0, 
                0.0,0.0,1.0,0.0, 
                0.0,0.0,0.0,1.0 
            ],
            "Y":[
                1.0,0.0,0.0,0.0, 
                0.0,-1.0,0.0,0.0, 
                0.0,0.0,1.0,0.0, 
                0.0,0.0,0.0,1.0 
            ],
            "z":[
                1.0,0.0,0.0,0.0, 
                0.0,1.0,0.0,0.0, 
                0.0,0.0,-1.0,0.0, 
                0.0,0.0,0.0,1.0 
            ],
            "Z":[
                1.0,0.0,0.0,0.0, 
                0.0,1.0,0.0,0.0, 
                0.0,0.0,-1.0,0.0, 
                0.0,0.0,0.0,1.0 
            ],
        }

    #Single Function
    def mirrorAxis_create_DataMatrix(self,mirrorAxis_str):
        mirrorAxis_MMatrix=om2.MMatrix(self._mirrorData_dict.get(mirrorAxis_str))
        mirrorAxis_DataMatrix=DataMatrix(mirrorAxis_MMatrix)
        return mirrorAxis_DataMatrix

    def mirrorOrientVector_create_DataMatrix(self,mirrorOrientVector_str):
        mirrorOrientVector_MMatrix=om2.MMatrix(self._mirrorData_dict.get(mirrorOrientVector_str))
        mirrorOrientVector_DataMatrix=DataMatrix(mirrorOrientVector_MMatrix)
        return mirrorOrientVector_DataMatrix

    #Setting Function
    def setDataMatrix(self,variable):
        self._matrix_DataMatrix=variable
        return self._matrix_DataMatrix
    def getDataMatrix(self):
        return self._matrix_DataMatrix
    
    def setPivotDataMatrix(self,variable):
        self._pivot_DataMatrix=variable
        return self._pivot_DataMatrix
    def getPivotDataMatrix(self):
        return self._pivot_DataMatrix

    def setSubjectDataMatrix(self,variable):
        self._subject_DataMatrix=variable
        return self._subject_DataMatrix
    def getSubjectDataMatrix(self):
        return self._subject_DataMatrix

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

    #Public Function
    def match(self,dataMatrix=None,subjectDataMatrix=None):
        _matrix_DataMatrix=dataMatrix or self._matrix_DataMatrix#worldMatrix
        _subject_DataMatrix=targetDataMatrix or self._subject_DataMatrix#inverseParentMatrix

        matchMatrix_MMatrix=_matrix_DataMatrix*_subject_DataMatrix
        matchMatrix_DataMatrix=DataMatrix(matchMatrix_MMatrix)
        return matchMatrix_DataMatrix

    def mirror(self,dataMatrix=None,subjectDataMatrix=None,pivotDataMatrix=None,mirrorAxis=None,mirrorOrientVector=None):
        _matrix_DataMatrix=dataMatrix or self._matrix_DataMatrix#worldMatrix
        _subject_DataMatrix=subjectDataMatrix or self._subject_DataMatrix#inverseParentMatrix
        _pivot_DataMatrix=pivotDataMatrix or self._pivot_DataMatrix
        _mirrorAxis_str=mirrorAxis or self._mirrorAxis_str
        _mirrorOrientVector_str=mirrorOrientVector or self._mirrorOrientVector_str

        mirrorAxis_DataMatrix=self.mirrorAxis_create_DataMatrix(_mirrorAxis_str)
        mirrorOrientVector_DataMatrix=self.mirrorOrientVector_create_DataMatrix(_mirrorOrientVector_str)
        mirrorMatrix_MMatrix=mirrorOrientVector_DataMatrix*_matrix_DataMatrix*mirrorAxis_DataMatrix*_subject_DataMatrix
        mirrorMatrix_DataMatrix=DataMatrix(mirrorMatrix_MMatrix)
        return mirrorMatrix_DataMatrix