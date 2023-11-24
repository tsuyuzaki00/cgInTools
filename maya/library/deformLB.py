# -*- coding: iso-8859-15 -*-
import maya.api.OpenMaya as om2
import sys,math

import cgInTools as cit
from ...library import baseLB as bLB
from . import nodeAttrLB as naLB
cit.reloads([bLB,naLB])

class DataWeight(bLB.SelfOrigin):
    def __init__(self):
        super(DataWeight,self).__init__()
        self._weightIndex_int=None
        self._weightValue_float=None
    
    #Setting Function
    def setIndex(self,variable):
        self._weightIndex_int=variable
        return self._weightIndex_int
    def getIndex(self):
        return self._weightIndex_int
    
    def setValue(self,variable):
        self._weightValue_float=variable
        return self._weightValue_float
    def getValue(self):
        return self._weightValue_float

class DataDeformation(bLB.SelfOrigin):
    def __init__(self):
        super(DataDeformation,self).__init__()
        self._influenceIndex_int=None
        self._influenceNode_DataNode=None
        self._weight_DataWeights=[]
    
    #Setting Function
    def setIndex(self,variable):
        self._influenceIndex_int=variable
        return self._influenceIndex_int
    def getIndex(self):
        return self._influenceIndex_int

    def setNode(self,variable):
        self._influenceNode_DataNode=variable
        return self._influenceNode_DataNode
    def getNode(self):
        return self._influenceNode_DataNode
    
    def setDataWeights(self,variables):
        self._weight_DataWeights=variables
        return self._weight_DataWeights
    def addDataWeights(self,variables):
        self._weight_DataWeights+=variables
        return self._weight_DataWeights
    def getDataWeights(self):
        return self._weight_DataWeights

class SelfDeformation(bLB.SelfOrigin):
    def __init__(self):
        super(SelfDeformation,self).__init__()
        self._bindNode_DataNode=None
        self._deform_DataDeformations=[]

    #Single Function
    def node_query_MObject(self,node):
        if node == None:
            return None
        elif not isinstance(node,str):
            om2.MGlobal.displayError("Please insert one string in value")
            sys.exit()
        node_MSelectionList=om2.MGlobal.getSelectionListByName(node)
        node_MObject=node_MSelectionList.getDependNode(0)
        return node_MObject

    def convertMObject_query_MPlug(self,node_MObject,attr_str):
        node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)
        node_MPlug=node_MFnDependencyNode.findPlug(attr_str,False)
        return node_MPlug

    def weightListMPlug_query_DataDeformation(self,deform_MPlug):
        weightListCount_int=deform_MPlug.numElements()
        deform_DataDeformations=[]
        weightList_MPlugs=[deform_MPlug.elementByPhysicalIndex(count_int) for count_int in range(weightListCount_int)]

        for weightList_MPlug in weightList_MPlugs:
            deform_DataDeformation=DataDeformation()
            deform_DataDeformation.setIndex(weightList_MPlug.logicalIndex())
            
            weight_MPlug=weightList_MPlug.child(0)
            weightPointIndex_intArray=weight_MPlug.getExistingArrayAttributeIndices()
            weightPointIndex_ints=[weightPointIndex_int for weightPointIndex_int in weightPointIndex_intArray]
            
            weight_DataWeights=[]
            for weightPointIndex_int in weightPointIndex_ints:
                weight_DataWeight=DataWeight()
                weight_DataWeight.setIndex(weightPointIndex_int)
                weightValue_MPlug=weight_MPlug.elementByLogicalIndex(weightPointIndex_int)
                weight_DataWeight.setValue(weightValue_MPlug.asFloat())
                weight_DataWeights.append(weight_DataWeight)

            deform_DataDeformation.setDataWeights(weight_DataWeights)
            deform_DataDeformations.append(deform_DataDeformation)
        return deform_DataDeformations

    #Multi Function
    def weights_edit_func(self,ffdName_str,ffdWeight_dict):
        ffd_MObject=self.node_query_MObject(ffdName_str)
        ffd_MFnDependencyNode=om2.MFnDependencyNode(ffd_MObject)
        ffd_MPlug=ffd_MFnDependencyNode.findPlug("weightList",False)

        ffd_MPlug.setNumElements(ffdWeight_dict.get("weightListIndex"))
        weightList_MPlug=ffd_MPlug.elementByLogicalIndex(ffdWeight_dict.get("weightListIndex"))
        weight_MPlue=weightList_MPlug.child(0)

        for weightPoint_dict in ffdWeight_dict.get("weightPoint_dicts"):
            weightValue_MPlug=weight_MPlue.elementByLogicalIndex(weightPoint_dict.get("weightPointIndex"))
            weightValue_MPlug.setFloat(weightPoint_dict.get("weightPointValue"))
    
    #Setting Function
    def setNode(self,variable):
        self._bindNode_DataNode=variable
        return self._bindNode_DataNode
    def getNode(self):
        return self._bindNode_DataNode

    def setDataDeformations(self,variables):
        self._deform_DataDeformations=variables
        return self._deform_DataDeformations
    def addDataDeformations(self,variables):
        self._deform_DataDeformations+=variables
        return self._deform_DataDeformations
    def getDataDeformations(self):
        return self._deform_DataDeformations

    #Public Function
    def queryWeights(self):
        nodeName_str=self._bindNode_DataNode.getName()
        node_MObject=self.node_query_MObject(nodeName_str)
        node_MPlug=self.convertMObject_query_MPlug(node_MObject,"weightList")
        node_DataDeformation=self.weightListMPlug_query_DataDeformation(node_MPlug)
        return node_DataDeformation

    def editWeights(self):
        _bindNode_DataNode=self._bindNode_DataNode
        _deform_DataDeformations=self._deform_DataDeformations
        
        nodeName_str=_bindNode_DataNode.getName()
        node_MObject=self.node_query_MObject(nodeName_str)
        node_MPlug=self.convertMObject_query_MPlug(node_MObject,"weightList")
    