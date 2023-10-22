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
        return self.kIdentity
    
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
        self._mirrorDirectionAxis_str="x"
        self._mirrorPrimaryAxis_str="+x"
        self._mirrorSecondaryAxis_str="+y"
        
        self._pivot_DataMatrix=DataMatrix()
        self._target_DataMatrix=DataMatrix()
        self._source_DataMatrix=DataMatrix()

    #Single Function
    def matchMatrix_edit_DataMatrix(self,source_DataMatrix,target_DataMatrix):
        transform_DataMatrix=source_DataMatrix*target_DataMatrix
        return transform_DataMatrix

    #Setting Function
    def setDataMatrix(self,variable):
        self._matrix_DataMatrix=variable
        return self._matrix_DataMatrix
    def getDataMatrix(self):
        return self._matrix_DataMatrix
    
    def setMirrorDirectionAxis(self,variable):
        self._mirrorDirectionAxis_str=variable
        return self._mirrorDirectionAxis_str
    def getMirrorDirectionAxis(self):
        return self._mirrorDirectionAxis_str
    
    def setMirrorPrimaryAxis(self,variable):
        self._mirrorPrimaryAxis_str=variable
        return self._mirrorPrimaryAxis_str
    def getMirrorPrimaryAxis(self):
        return self._mirrorPrimaryAxis_str
    
    def setMirrorSecondaryAxis(self,variable):
        self._mirrorSecondaryAxis_str=variable
        return self._mirrorSecondaryAxis_str
    def getMirrorSecondaryAxis(self):
        return self._mirrorSecondaryAxis_str

    def setPivotDataMatrix(self,variable):
        self._pivot_DataMatrix=variable
        return self._pivot_DataMatrix
    def getPivotDataMatrix(self):
        return self._pivot_DataMatrix

    def setTargetDataMatrix(self,variable):
        self._target_DataMatrix=variable
        return self._target_DataMatrix
    def getTargetDataMatrix(self):
        return self._target_DataMatrix

    def setSourceDataMatrix(self,variable):
        self._source_DataMatrix=variable
        return self._source_DataMatrix
    def getSourceDataMatrix(self):
        return self._source_DataMatrix

    #Public Function
    def matchTargetTransform(self,dataMatrix=None,targetDataMatrix=None):
        _matrix_DataMatrix=dataMatrix or self._matrix_DataMatrix
        _target_DataMatrix=targetDataMatrix or self._target_DataMatrix



    def matchSourceTransform(self,dataMatrix=None,sourceDataMatrix=None):
        _matrix_DataMatrix=dataMatrix or self._matrix_DataMatrix
        _source_DataMatrix=sourceDataMatrix or self._source_DataMatrix



    def mirror(self,dataMatrix=None,direction=None,primary=None,secondary=None,pivotDataMatrix=None):
        _matrix_DataMatrix=dataMatrix or self._matrix_DataMatrix
        _mirrorDirectionAxis_str=direction or self._mirrorDirectionAxis_str
        _mirrorPrimaryAxis_str=primary or self._mirrorPrimaryAxis_str
        _mirrorSecondaryAxis_str=secondary or self._mirrorSecondaryAxis_str
        _pivot_DataMatrix=pivotDataMatrix or self._pivot_DataMatrix



class SelfMatrixNode(om2.MMatrix):
    def __init__(self,*matrix):
        super(SelfMatrixNode,self).__init__(*matrix)
        #self.kIdentity=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
        self._node_MObject=None
        self._MSpace=om2.MSpace.kTransform #1
        self._rotateOrder=om2.MEulerRotation.kXYZ #0
        
        self._targetNode_MObject=None
        self._mirrorAxis_str=None
        self._mirrorOrientation_str=None

    #Single Function
    def selectNode_create_MObject(self,node):
        if node == None:
            return None
        elif not isinstance(node,str):
            om2.MGlobal.displayError("Please insert one string in value")
            sys.exit()
        node_MSelectionList=om2.MGlobal.getSelectionListByName(node)
        node_MObject=node_MSelectionList.getDependNode(0)
        return node_MObject

    def convertMObject_create_MDagPath(self,node_MObject):
        node_MDagPath=om2.MDagPath().getAPathTo(node_MObject)
        return node_MDagPath
    
    def vector3_check_vector3(self,variable):
        if isinstance(variable,tuple) and len(variable) == 3 or isinstance(variable,list) and len(variable) == 3:
            return variable
        else:
            return None
        
    def initialNoneMMatrix_check_MMatrix(self,MMatrix):
        if isinstance(MMatrix,om2.MMatrix):
            return MMatrix
        elif MMatrix == None:
            MMatrix=om2.MMatrix([1,0,0,0, 0,1,0,0, 0,0,1,0, 0,0,0,1])
            return MMatrix
        else:
            MMatrix = None
            return MMatrix

    def mirrorMatrix_create_MMatrix(self,matrix_MMatrix,axis_str,orient_str):
        if axis_str is "x":
            matrix_MMatrix[12]=matrix_MMatrix[12]*(-1)
        if axis_str is "y":
            matrix_MMatrix[13]=matrix_MMatrix[13]*(-1)
        if axis_str is "z":
            matrix_MMatrix[14]=matrix_MMatrix[14]*(-1)

        if orient_str is "x":
            matrix_MMatrix[5]=matrix_MMatrix[5]*(-1)
            matrix_MMatrix[10]=matrix_MMatrix[10]*(-1)
        if orient_str is "y":
            matrix_MMatrix[0]=matrix_MMatrix[0]*(-1)
            matrix_MMatrix[10]=matrix_MMatrix[10]*(-1)
        if orient_str is "z":
            matrix_MMatrix[0]=matrix_MMatrix[0]*(-1)
            matrix_MMatrix[5]=matrix_MMatrix[5]*(-1)

        return matrix_MMatrix

    #Multi Function
    def _nodeToNormalMMatrix_query_MMatrix(self,node_MObject):
        node_MDagPath=self.convertMObject_create_MDagPath(node_MObject)
        node_MFnDagNode=om2.MFnDagNode(node_MDagPath)
        node_MMatrix=node_MFnDagNode.transformationMatrix()
        return node_MMatrix
    
    def _nodeToWorldMMatrix_query_MMatrix(self,node_MObject):
        node_MDagPath=self.convertMObject_create_MDagPath(node_MObject)
        node_MMatrix=node_MDagPath.inclusiveMatrix()
        return node_MMatrix
    
    def _nodeToParentMMatrix_query_MMatrix(self,node_MObject):
        node_MDagPath=self.convertMObject_create_MDagPath(node_MObject)
        node_MMatrix=node_MDagPath.exclusiveMatrix()
        return node_MMatrix
    
    def _nodeToInverseNormalMMatrix_query_MMatrix(self,node_MObject):
        node_MDagPath=self.convertMObject_create_MDagPath(node_MObject)
        node_MFnDagNode=om2.MFnDagNode(node_MDagPath)
        normal_MMatrix=node_MFnDagNode.transformationMatrix()
        normal_MTransformationMatrix=om2.MTransformationMatrix(normal_MMatrix)
        node_MMatrix=normal_MTransformationMatrix.asMatrixInverse()
        return node_MMatrix
    
    def _nodeToInverseWorldMMatrix_query_MMatrix(self,node_MObject):
        node_MDagPath=self.convertMObject_create_MDagPath(node_MObject)
        world_MMatrix=node_MDagPath.inclusiveMatrix()
        world_MTransformationMatrix=om2.MTransformationMatrix(world_MMatrix)
        node_MMatrix=world_MTransformationMatrix.asMatrixInverse()
        return node_MMatrix
    
    def _nodeToInverseParentMMatrix_query_MMatrix(self,node_MObject):
        node_MDagPath=self.convertMObject_create_MDagPath(node_MObject)
        parent_MMatrix=node_MDagPath.exclusiveMatrix()
        parent_MTransformationMatrix=om2.MTransformationMatrix(parent_MMatrix)
        node_MMatrix=parent_MTransformationMatrix.asMatrixInverse()
        return node_MMatrix

    #Setting Function
    def setNode(self,variable):
        self._node_MObject=self.selectNode_create_MObject(variable)
        self.kIdentity=self._nodeToNormalMMatrix_query_MMatrix(self._node_MObject)
    def getNode(self):
        node_MFnDependencyNode=om2.MFnDependencyNode(self._node_MObject)
        name_str=node_MFnDependencyNode.name()
        return name_str
    
    def setTargetNode(self,variable):
        self._targetNode_MObject=self.selectNode_create_MObject(variable)
        return self._targetNode_MObject
    def getTargetNode(self):
        targetNode_MFnDependencyNode=om2.MFnDependencyNode(self._targetNode_MObject)
        name_str=targetNode_MFnDependencyNode.name()
        return name_str

    def setMatrix(self,variable):
        self.kIdentity=om2.MMatrix(variable)
        return self.kIdentity
    def getMatrix(self):
        matrix=list(self.kIdentity)
        return matrix
    
    def setMSpace(self,variable):
        self._MSpace=variable
    def getMSpace(self):
        return self._MSpace

    def setRotateOrder(self,variable):
        self._rotateOrder=variable
    def getRotateOrder(self):
        return self._rotateOrder

    def setMirrorAxis(self,variable):
        self._mirrorAxis_str=variable
        return self._mirrorAxis_str
    def getMirrorAxis(self):
        return self._mirrorAxis_str
    
    def setMirrorOrient(self,variable):
        self._mirrorOrientation_str=variable
        return self._mirrorOrientation_str
    def getMirrorOrient(self):
        return self._mirrorOrientation_str

    def currentNormalMMatrix(self):
        self.kIdentity=self._nodeToNormalMMatrix_query_MMatrix(self._node_MObject)
        return self.kIdentity
    def currentWorldMMatrix(self):
        self.kIdentity=self._nodeToWorldMMatrix_query_MMatrix(self._node_MObject)
        return self.kIdentity
    def currentParentMMatrix(self):
        self.kIdentity=self._nodeToParentMMatrix_query_MMatrix(self._node_MObject)
        return self.kIdentity
    def currentInverseNormalMMatrix(self):
        self.kIdentity=self._nodeToInverseNormalMMatrix_query_MMatrix(self._node_MObject)
        return self.kIdentity
    def currentInverseWorldMMatrix(self):
        self.kIdentity=self._nodeToInverseWorldMMatrix_query_MMatrix(self._node_MObject)
        return self.kIdentity
    def currentInverseParentMMatrix(self):
        self.kIdentity=self._nodeToInverseParentMMatrix_query_MMatrix(self._node_MObject)
        return self.kIdentity

    def setTranslateMMatrix(self,variable):
        trans_MVector=om2.MVector(variable)
        self.kIdentity=om2.MMatrix()
        self.kIdentity.setElement(3,0,trans_MVector.x)
        self.kIdentity.setElement(3,1,trans_MVector.y)
        self.kIdentity.setElement(3,2,trans_MVector.z)
        return self.kIdentity
    def addTranslateMMatrix(self,variable):
        MVector=om2.MVector(variable)
        add_MMatrix=om2.MMatrix()
        add_MMatrix.setElement(3,0,MVector.x)
        add_MMatrix.setElement(3,1,MVector.y)
        add_MMatrix.setElement(3,2,MVector.z)
        have_MMatrix=self.initialNoneMMatrix_check_MMatrix(self.kIdentity)  or self.kIdentity
        self.kIdentity=have_MMatrix*add_MMatrix
        return self.kIdentity
    def getTranslateMMatrix(self):
        MTransformationMatrix=om2.MTransformationMatrix(self.kIdentity)
        MVector=MTransformationMatrix.translation(self._MSpace)
        return MVector

    def setRotateMMatrix(self,variable):
        radian=[math.radians(variable[0]),math.radians(variable[1]),math.radians(variable[2])]
        MEulerRotation=om2.MEulerRotation(radian,self._rotateOrder)
        self.kIdentity=MEulerRotation.asMatrix()
        return self.kIdentity
    def addRotateMMatrix(self,variable):
        radian=[math.radians(variable[0]),math.radians(variable[1]),math.radians(variable[2])]
        MEulerRotation=om2.MEulerRotation(radian,self._rotateOrder)
        add_MMatrix=MEulerRotation.asMatrix()
        have_MMatrix=self.initialNoneMMatrix_check_MMatrix(self.kIdentity)  or self.kIdentity
        self.kIdentity=have_MMatrix*add_MMatrix
        return self.kIdentity
    def getRotateMMatrix(self,radian=True):
        MTransformationMatrix=om2.MTransformationMatrix(self.kIdentity)
        MEulerRotation=MTransformationMatrix.rotation(asQuaternion=False)
        if not radian:
            MEulerRotation.x=math.degrees(MEulerRotation.x)
            MEulerRotation.y=math.degrees(MEulerRotation.y)
            MEulerRotation.z=math.degrees(MEulerRotation.z)
        return MEulerRotation
    
    def setQuaternionMMatrix(self,variable):
        MQuaternion=om2.MQuaternion(variable)
        self.kIdentity=MQuaternion.asMatrix()
        return self.kIdentity
    def addQuaternionMMatrix(self,variable):
        MQuaternion=om2.MQuaternion(variable)
        add_MMatrix=MQuaternion.asMatrix()
        have_MMatrix=self.initialNoneMMatrix_check_MMatrix(self.kIdentity) or self.kIdentity
        self.kIdentity=have_MMatrix*add_MMatrix
        return self.kIdentity
    def getQuaternionMMatrix(self):
        MTransformationMatrix=om2.MTransformationMatrix(self.kIdentity)
        MQuaternion=MTransformationMatrix.rotation(asQuaternion=True)
        return MQuaternion

    def setAxisAngleMMartix(self,bend=(1,0,0),twist=0):
        bend_MVector=om2.MVector(bend)
        MQuaternion=om2.MQuaternion(twist,bend)
        add_MMatrix=MQuaternion.asMatrix()
        have_MMatrix=self.initialNoneMMatrix_check_MMatrix(self.kIdentity)
        self.kIdentity=have_MMatrix*add_MMatrix
        return self.kIdentity
    def addAxisAngleMMatrix(self,bend=(1,0,0),twist=0):
        bend_MVector=om2.MVector(bend)
        MQuaternion=om2.MQuaternion(twist,bend)
        self.kIdentity=MQuaternion.asMatrix()
        return self.kIdentity
    def getAxisAngleMMatrix(self,radian=True):
        MTransformationMatrix=om2.MTransformationMatrix(self.kIdentity)
        MQuaternion=MTransformationMatrix.rotation(asQuaternion=True)
        bend_MVector,twist_float,=MQuaternion.asAxisAngle()
        if not radian:
            twist_float=math.degrees(twist_float)
        return bend_MVector,twist_float

    def setScaleMMatrix(self,variable):
        scale_list3=self.vector3_check_vector3(variable)
        MTransformationMatrix=om2.MTransformationMatrix()
        MTransformationMatrix.setScale(scale_list3,self._MSpace)
        self.kIdentity=MTransformationMatrix.asMatrix()
        return self.kIdentity
    def addScaleMMatrix(self,variable):
        scale_list3=self.vector3_check_vector3(variable)
        MTransformationMatrix=om2.MTransformationMatrix()
        MTransformationMatrix.setScale(scale_list3,self._MSpace)
        add_MMatrix=MTransformationMatrix.asMatrix()
        have_MMatrix=self.initialNoneMMatrix_check_MMatrix(self.kIdentity) or self.kIdentity
        self.kIdentity=have_MMatrix*add_MMatrix
        return self.kIdentity
    def getScaleMMatrix(self):
        MTransformationMatrix=om2.MTransformationMatrix(self.kIdentity)
        scale_list=MTransformationMatrix.scale(self._MSpace)
        return scale_list

    #Public Function
    def queryDirectionX(self):
        MVectorX=om2.MVector(self.kIdentity[0],self.kIdentity[1],self.kIdentity[2])
        return MVectorX
    
    def queryDirectionY(self):
        MVectorY=om2.MVector(self.kIdentity[4],self.kIdentity[5],self.kIdentity[6])
        return MVectorY
    
    def queryDirectionZ(self):
        MVectorZ=om2.MVector(self.kIdentity[8],self.kIdentity[9],self.kIdentity[10])
        return MVectorZ

    def mirror(self,node=None,targetNode=None,axis=None,orient=None):
        _node_MObject=self.selectNode_create_MObject(node) or self._node_MObject
        _mirrorAxis_str=axis or self._mirrorAxis_str or "x"
        _mirrorOrientation_str=orient or self._mirrorOrientation_str or "x"
        _targetNode_MObject=self.selectNode_create_MObject(targetNode) or self._targetNode_MObject

        InverseParentTargetNode_MMatrix=self._nodeToInverseParentMMatrix_query_MMatrix(_targetNode_MObject)
        worldNode_MMatrix=self._nodeToWorldMMatrix_query_MMatrix(_node_MObject)

        transform_MMatrix=worldNode_MMatrix*InverseParentTargetNode_MMatrix

        mirrorNode_MMatrix=self.mirrorMatrix_create_MMatrix(transform_MMatrix,_mirrorAxis_str,_mirrorOrientation_str)

        mirrorNode_MTransformationMatrix=om2.MTransformationMatrix(mirrorNode_MMatrix)
        translateNode_MVector=mirrorNode_MTransformationMatrix.translation(self._MSpace)
        rotationNode_MQuaternion=mirrorNode_MTransformationMatrix.rotation(True)

        targetNode_MFnTransform=om2.MFnTransform(_targetNode_MObject)
        targetNode_MFnTransform.setTranslation(translateNode_MVector,self._MSpace)
        targetNode_MFnTransform.setRotation(rotationNode_MQuaternion,self._MSpace)