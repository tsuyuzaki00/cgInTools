# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

import cgInTools as cit
from ...library import baseLB as bLB
from ...library import functionLB as fLB
from . import appLB as aLB
from . import dataLB as dLB
cit.reloads([bLB,fLB,aLB,dLB])

LIBRARYRULES_DICT=fLB.readJson(cit.mayaSettings_dir,"rules","library")

class AppNodeName(aLB.AppOpenMayaBase):
    def __init__(self):
        super(AppNodeName,self).__init__()
        self._name_DataName=None
        self._node_DataNode=None
        self._nodeName_dict=LIBRARYRULES_DICT["nodeName_dict"]

    #Single Function
    def orderNames_create_str(self,name_DataName):
        order_strs=name_DataName.getOrders()
        partsName_strs=[]
        for order_str in order_strs:
            if order_str is None:
                continue
            orderSplit_strs=order_str.split("_")
            if len(orderSplit_strs) is 1:
                partsName_value=eval('name_DataName.get'+orderSplit_strs[0]+'()')
            elif len(orderSplit_strs) is 2:
                partsName_value=eval('name_DataName.get'+orderSplit_strs[0]+'()['+orderSplit_strs[-1]+']')
            elif len(orderSplit_strs) is 3:
                partsName_value=eval('name_DataName.get'+orderSplit_strs[0]+'()')
                sequence_value=eval('name_DataName.get'+orderSplit_strs[1]+'()['+orderSplit_strs[-1]+']')
                if partsName_value is None:
                    partsName_value=sequence_value
                else:
                    partsName_value=partsName_value+str(sequence_value)
            partsName_strs.append(partsName_value)
        cleanName_strs=[str(partsName_str) for partsName_str in partsName_strs if partsName_str is not None]
        name_str="_".join(cleanName_strs)
        return name_str
    
    def nextAlphabet_edit_str(self,alphabet_str):
        if alphabet_str == "Z":
            return "A"
        elif alphabet_str == "z":
            return "a"
        else:
            return chr(ord(alphabet_str)+1)
    
    def smashNumber_edit_str(self,name_str):
        while name_str[-1].isdigit():
            name_str=name_str[:-1]
            if name_str == "":
                return None
        return name_str
    
    def smashAlphabet_edit_str(self,name_str):
        while name_str[-1].isupper():
            name_str=name_str[:-1]
            if name_str == "":
                return None
        return name_str

    #Multi Function
    def _sameName_check_str(self,name_str):
        while cmds.objExists(name_str):
            next_DataName=self.nextIncrease()
            if next_DataName is None:
                break
            else:
                name_str=self.orderNames_create_str(next_DataName)
        return name_str

    #Inheritance Function
    def _sideName_query_str(self,nodeName_str,dist=1):
        node_MObject=self.node_query_MObject(nodeName_str)
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        node_MFnTransform=om2.MFnTransform(node_MDagPath)
        node_MVector=node_MFnTransform.translation(om2.MSpace.kWorld)
        if node_MVector.x > dist and node_MVector.x > dist:
            return "L"
        elif node_MVector.x < -dist and node_MVector.x < -dist:
            return "R"
        else:
            return "C"

    def _tagType_query_str(self,nodeName_str):
        node_MObject=self.node_query_MObject(nodeName_str)
        node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)
        if node_MFnDependencyNode.typeName == "transform":
            try:
                node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
                shape_MDagPath=node_MDagPath.extendToShape()
                shape_MFnDagNode=om2.MFnDagNode(shape_MDagPath)
                tagType_str=shape_MFnDagNode.typeName
            except RuntimeError:
                return "none"
        else:
            tagType_str=node_MFnDependencyNode.typeName
        return tagType_str
        
    def _nodeRename_edit_str(self,nodeName_str,rename_str):
        node_MObject=self.node_query_MObject(nodeName_str)
        node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)
        node_MFnDependencyNode.setName(rename_str)
        return node_MFnDependencyNode.name()

    #Setting Function
    def setDataName(self,variable):
        self._name_DataName=variable
        return self._name_DataName
    def getDataName(self):
        return self._name_DataName

    def setDataNode(self,variable):
        self._node_DataNode=variable
        return self._node_DataNode
    def getDataNode(self):
        return self._node_DataNode
    
    #Public Function
    def create(self,dataName=None):
        _name_DataName=dataName or self._name_DataName

        name_str=self.orderNames_create_str(_name_DataName)
        checkName_str=self._sameName_check_str(name_str)
        return checkName_str
    
    def nextIncrease(self,dataName=None):
        _name_DataName=dataName or self._name_DataName

        if _name_DataName.getIncrease() is None:
            _name_DataName.addOrders(["Numbers_0"])
            return _name_DataName
        increase_strs=_name_DataName.getIncrease().split("_")
        if "Numbers" in increase_strs:
            number_ints=_name_DataName.getNumbers()
            number_int=number_ints[int(increase_strs[-1])]
            number_ints[int(increase_strs[-1])]=number_int+1
            _name_DataName.setNumbers(number_ints)
            return _name_DataName
        elif "Hierarchys" in increase_strs:
            increase_strs=_name_DataName.getIncrease().split("_")
            hierarchy_strs=_name_DataName.getHierarchys()
            hierarchy_str=hierarchy_strs[int(increase_strs[-1])]
            hierarchy_strs[int(increase_strs[-1])]=self.nextAlphabet_edit_str(hierarchy_str)
            _name_DataName.setHierarchys(hierarchy_strs)
            return _name_DataName
        else:
            _name_DataName.addOrders(["Numbers_0"])
            return _name_DataName
        
    def rename(self,dataName=None,dataNode=None):
        _name_DataName=dataName or self._name_DataName
        _node_DataNode=dataNode or self._node_DataNode

        name_str=self.orderNames_create_str(_name_DataName)
        checkName_str=self._sameName_check_str(name_str)
        rename_str=self._nodeRename_edit_str(_node_DataNode.getName(),checkName_str)
        return rename_str

    def editRename(self,dataName=None,dataNode=None):
        _name_DataName=dataName or self._name_DataName
        _node_DataNode=dataNode or self._node_DataNode

        if _name_DataName.getTitle() is None:
            nameSplits=_node_DataNode.getName().split("_")
            smashNumber_str=self.smashNumber_edit_str(nameSplits[0])
            smashAlphabet_str=self.smashAlphabet_edit_str(smashNumber_str)
            _name_DataName.setTitle(smashAlphabet_str)

        if _name_DataName.getTagType() is None:
            tagType_str=self._tagType_query_str(_node_DataNode.getName())
            typeName_str=self._nodeName_dict.get(tagType_str)
            _name_DataName.setTagType(typeName_str)

        if _name_DataName.getSide() is None:
            side_str=self._sideName_query_str(_node_DataNode.getName())
            _name_DataName.setSide(side_str)

        name_str=self.orderNames_create_str(_name_DataName)
        checkName_str=self._sameName_check_str(name_str)
        rename_str=self._nodeRename_edit_str(_node_DataNode.getName(),checkName_str)
        return rename_str

    def autoRename(self,dataNode=None,order_strs=["Title","TagType"]):
        _node_DataNode=dataNode or self._node_DataNode

        _name_DataName=dLB.DataName()
        _name_DataName.setOrders(order_strs)

        nameSplits=_node_DataNode.getName().split("_")
        smashNumber_str=self.smashNumber_edit_str(nameSplits[0])
        smashAlphabet_str=self.smashAlphabet_edit_str(smashNumber_str)
        _name_DataName.setTitle(smashAlphabet_str)
        
        tagType_str=self._tagType_query_str(_node_DataNode.getName())
        typeName_str=self._nodeName_dict.get(tagType_str)
        _name_DataName.setTagType(typeName_str)
        
        side_str=self._sideName_query_str(_node_DataNode.getName())
        _name_DataName.setSide(side_str)

        name_str=self.orderNames_create_str(_name_DataName)
        checkName_str=self._sameName_check_str(name_str)
        rename_str=self._nodeRename_edit_str(_node_DataNode.getName(),checkName_str)
        return rename_str
    