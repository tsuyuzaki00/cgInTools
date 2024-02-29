# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import sys,math

import cgInTools as cit
from ...library import baseLB as bLB
from ..library import dataLB as dLB
cit.reloads([bLB,dLB])

class AppMatrix(bLB.SelfOrigin):
    def __init__(self):
        super(AppMatrix,self).__init__()
        self._matrix_DataMatrix=dLB.DataMatrix()
        self._pivot_DataMatrix=dLB.DataMatrix()
        self._subject_DataMatrix=dLB.DataMatrix()

        self._mirrorAxis_str="x"
        self._mirrorOrientVector_str="z"

    #Single Function
    @staticmethod
    def inverseAxis_create_DataMatrix(axis_str):
        inverseAxis_DataMatrix=dLB.DataMatrix()
        if "x" is axis_str or "X" is axis_str:
            axis_DataMatrix=inverseAxis_DataMatrix.inverseX
        elif "y" is axis_str or "Y" is axis_str:
            axis_DataMatrix=inverseAxis_DataMatrix.inverseY
        elif "z" is axis_str or "Z" is axis_str:
            axis_DataMatrix=inverseAxis_DataMatrix.inverseZ
        else:
            axis_DataMatrix=dLB.DataMatrix()
        return axis_DataMatrix

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
        _subject_DataMatrix=subjectDataMatrix or self._subject_DataMatrix#inverseParentMatrix

        matchMatrix_DataMatrix=_matrix_DataMatrix*_subject_DataMatrix
        return matchMatrix_DataMatrix

    def mirror(self,dataMatrix=None,subjectDataMatrix=None,pivotDataMatrix=None,mirrorAxis=None,mirrorOrientVector=None):
        _matrix_DataMatrix=dataMatrix or self._matrix_DataMatrix#worldMatrix
        _subject_DataMatrix=subjectDataMatrix or self._subject_DataMatrix#inverseParentMatrix
        _pivot_DataMatrix=pivotDataMatrix or self._pivot_DataMatrix
        _mirrorAxis_str=mirrorAxis or self._mirrorAxis_str
        _mirrorOrientVector_str=mirrorOrientVector or self._mirrorOrientVector_str

        mirrorAxis_DataMatrix=self.inverseAxis_create_DataMatrix(_mirrorAxis_str)
        mirrorOrientVector_DataMatrix=self.inverseAxis_create_DataMatrix(_mirrorOrientVector_str)
        
        mirrorMatrix_DataMatrix=mirrorOrientVector_DataMatrix*_matrix_DataMatrix*mirrorAxis_DataMatrix*_subject_DataMatrix
        return mirrorMatrix_DataMatrix