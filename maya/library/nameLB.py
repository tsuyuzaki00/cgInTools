# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

import cgInTools as cit
from ...library import baseLB as bLB
from ...library import jsonLB as jLB
from . import appLB as aLB
from . import dataLB as dLB
from . import setBaseLB as sbLB
cit.reloads([bLB,sbLB,jLB])

RULES_DICT=jLB.readJson(cit.mayaSettings_dir,"library")

class AppName(aLB.AppOpenMayaBase):
    def __init__(self):
        self._name_DataName=None

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

    #Setting Function
    def setDataName(self,variable):
        self._name_DataName=variable
        return self._name_DataName
    def getDataName(self):
        return self._name_DataName

    #Public Function
    def create(self,dataName=None):
        _name_DataName=dataName or self._name_DataName

        name_str=self.orderNames_create_str(_name_DataName)
        return name_str
    
    def nextIncrease(self,dataName=None):
        _name_DataName=dataName or self._name_DataName

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
            return None

class AppNodeName(AppName):
    def __init__(self):
        super(AppNodeName,self).__init__()
        self._node_DataNode=None
        self._nodeName_dict=RULES_DICT["nodeName_dict"]

    #Single Function
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

    def _nodeType_query_str(self,nodeName_str):
        node_MObject=self.node_query_MObject(nodeName_str)
        node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)
        if node_MFnDependencyNode.typeName == "transform":
            try:
                node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
                shape_MDagPath=node_MDagPath.extendToShape()
                shape_MFnDagNode=om2.MFnDagNode(shape_MDagPath)
                nodeType_str=shape_MFnDagNode.typeName
            except RuntimeError:
                return "none"
        else:
            nodeType_str=node_MFnDependencyNode.typeName
        return nodeType_str
        
    def _nodeRename_edit_str(self,nodeName_str,rename_str):
        node_MObject=self.node_query_MObject(nodeName_str)
        node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)
        node_MFnDependencyNode.setName(rename_str)
        return node_MFnDependencyNode.name()

    #Setting Function
    def setDataNode(self,variable):
        self._node_DataNode=variable
        return self._node_DataNode
    def getDataNode(self):
        return self._node_DataNode
    
    #Public Function
    def rename(self,dataName=None,dataNode=None):
        _name_DataName=dataName or self._name_DataName
        _node_DataNode=dataNode or self._node_DataNode

        name_str=self.orderNames_create_str(_name_DataName)
        while cmds.objExists(name_str):
            next_DataName=self.nextIncrease()
            if next_DataName is None:
                break
            else:
                name_str=self.orderNames_create_str(next_DataName)
        
        rename_str=self._nodeRename_edit_str(_node_DataNode.getName(),name_str)
        return rename_str

    def editRename(self,dataName=None,dataNode=None):
        _name_DataName=dataName or self._name_DataName
        _node_DataNode=dataNode or self._node_DataNode

        if _name_DataName.getTitle() is None:
            nameSplits=_node_DataNode.getName().split("_")
            smashNumber_str=self.smashNumber_edit_str(nameSplits[0])
            smashAlphabet_str=self.smashAlphabet_edit_str(smashNumber_str)
            _name_DataName.setTitle(smashAlphabet_str)

        if _name_DataName.getNodeType() is None:
            nodeType_str=self._nodeType_query_str(_node_DataNode.getName())
            typeName_str=self._nodeName_dict.get(nodeType_str)
            _name_DataName.setNodeType(typeName_str)

        if _name_DataName.getSide() is None:
            side_str=self._sideName_query_str(_node_DataNode.getName())
            _name_DataName.setSide(side_str)

        name_str=self.orderNames_create_str(_name_DataName)
        while cmds.objExists(name_str):
            next_DataName=self.nextIncrease()
            if next_DataName is None:
                break
            else:
                name_str=self.orderNames_create_str(next_DataName)
        
        rename_str=self._nodeRename_edit_str(_node_DataNode.getName(),name_str)
        return rename_str

    def autoRename(self,dataNode=None,order_strs=["Title","NodeType","Numbers_0"]):
        _node_DataNode=dataNode or self._node_DataNode

        _name_DataName=dLB.DataName()
        _name_DataName.setOrders(order_strs)

        nameSplits=_node_DataNode.getName().split("_")
        smashNumber_str=self.smashNumber_edit_str(nameSplits[0])
        smashAlphabet_str=self.smashAlphabet_edit_str(smashNumber_str)
        _name_DataName.setTitle(smashAlphabet_str)
        
        nodeType_str=self._nodeType_query_str(_node_DataNode.getName())
        typeName_str=self._nodeName_dict.get(nodeType_str)
        _name_DataName.setNodeType(typeName_str)
        
        side_str=self._sideName_query_str(_node_DataNode.getName())
        _name_DataName.setSide(side_str)

        name_str=self.orderNames_create_str(_name_DataName)
        while cmds.objExists(name_str):
            next_DataName=self.nextIncrease()
            if next_DataName is None:
                break
            else:
                name_str=self.orderNames_create_str(next_DataName)
        
        rename_str=self._nodeRename_edit_str(_node_DataNode.getName(),name_str)
        return rename_str

class Naming(sbLB.BaseName):
    def __init__(self):
        super(Naming,self).__init__()
        self._nodeName_dict=RULES_DICT["nodeName_dict"]

    #Single Function
    def nodeType_query_str(self,obj):
        objType_str=cmds.objectType(obj)
        if objType_str=="transform":
            shape_list = cmds.listRelatives(obj,s=True)
            if shape_list==None:
                return "none"
            else :
                shapeType_str=cmds.objectType(shape_list[0])
                return shapeType_str
        else :
            objType_str=cmds.objectType(obj)
            return objType_str

    def sideName_query_str(self,obj,dist=1):
        boundingBox=cmds.xform(obj,q=True,bb=True,ws=True)
        minX=boundingBox[0]
        maxX=boundingBox[3]
        if minX > dist and maxX > dist:
            return "L"
        elif minX < -dist and maxX < -dist:
            return "R"
        else:
            return "C"

    def noneDeleteOrder_edit_list(self,order_list):
        noneDel_list=[]
        for order in order_list:
            if not order == "none" and not order == "":
                noneDel_list.append(order)
        return noneDel_list

    def rangeNumber_query_str(self,name):
        for i in range(100):
            if i is None:
                cmds.error("Can't go over 99.")
            while name[-1].isdigit():
                name=name[:-1]
            same_list=cmds.ls("*"+name+str(i).zfill(2)+"*",dag=True)
            if same_list == []:
                return str(i).zfill(2)

    def rangeAlphabet_query_str(self,name):
        for i in range(65, 91):
            if i is None:
                cmds.error("Can't go over Z.")
            if name[-1].isupper():
                name=name[:-1]
            same_list=cmds.ls("*"+name+chr(i)+"*",dag=True)
            if same_list == []:
                return chr(i)

    def scene_query_str(self):
        sceneName=cmds.file(q=True,sn=True).split("/")[-1]
        sceneName=sceneName.split(".")[0]
        sceneParent=cmds.workspace(q=True,sn=True).split("/")[-1]
        if sceneName == "":
            self.scene=sceneParent
        else:
            self.scene=sceneName
        return self.scene
    
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

    def getAlphabet_query_str(self,obj):
        splitObjs=obj.split("_")
        for i in range(len(splitObjs)):
            if splitObjs[i][-1].isupper() and len(splitObjs[i])>1:
                return splitObjs[i][-1]
        
    def firstLowerCaseOnly_edit_str(str):
        str=str[0].lower()+str[1:]
        return str

    #Multi Function
    def _nodeName_query_str(self,obj):
        getNode_str=self.nodeType_query_str(obj)
        nodeName_str=self._nodeName_dict[getNode_str]
        return nodeName_str

    #Private Function
    def _titleName_query_str(self,obj,delAlph=True):
        splitObjs=obj.split("_")
        self._nodeName_query_str(obj)
        self.sideName_query_str(obj)
        for l in range(len(splitObjs)):
            if delAlph:
                smashName=self.smashAlphabet_edit_str(splitObjs[l])
            else:
                smashName=splitObjs[l]
            if not splitObjs[l].isdigit():
                name=self.smashNumber_edit_str(smashName)
                if not name==self._nodeName_query_str(obj) and\
                   not name==self.sideName_query_str(obj) and\
                   not name==None:
                    return name

    def _numberName_query_str(self,order_list):
        if "num" in order_list:
            noneDel_list=self.noneDeleteOrder_edit_list(order_list)
            orderName=self._orderName_create_str(noneDel_list)
            index=noneDel_list.index("num")
            for num in range(100):
                splitNum=orderName.split("_")[index]
                replaceName=orderName.replace(splitNum,str(num).zfill(2))
                if not cmds.objExists(replaceName):
                    return str(num).zfill(2)
        else:
            return str(0).zfill(2)

    def _orderName_create_str(self,order_list):
        selfOrder_list=[]
        for chengeSelf in order_list:
            addSelf=eval("self._"+chengeSelf)
            selfOrder_list.append(addSelf)
        orderName="_".join(selfOrder_list)
        return orderName

    #Public Function
    def __loading(self):
        order_list=self.noneDeleteOrder_edit_list(self._order_list)
        if self._custom == "":
            self._custom="custom"
        if self._title == "":
            self._title=self._titleName_query_str(self._object)
        if self._node == "":
            self._node=self._nodeName_query_str(self._object)
        if self._side == "":
            self._side=self.sideName_query_str(self._object)
        if "titleNum" in order_list:
            self._titleNum=self._title+self.rangeNumber_query_str(self._title)
        if "nodeNum" in order_list:
            self._nodeNum=self._node+self.rangeNumber_query_str(self._node)
        if "sideNum" in order_list:
            self._sideNum=self._side+self.rangeNumber_query_str(self._side)
        if "scene" in order_list:
            self._scene=self.scene_query_str()

    def __loadingPlus(self):
        order_list=self.noneDeleteOrder_edit_list(self._order_list)
        if "number" in order_list:
            self._number=self._numberName_query_str(order_list)
        if "titleHie" in order_list:
            self._hierarchy=self.rangeAlphabet_query_str(self._title)
            self._titleHie=self._title+self._hierarchy

    def getRename(self):
        if self._switch=="fullAuto":
            self._title=self._titleName_query_str(self._object)
            self._node=self._nodeName_query_str(self._object)
            self._side=self.sideName_query_str(self._object)
            self.__loading()
            self.__loadingPlus()
            noneDel_list=self.noneDeleteOrder_edit_list(self._order_list)
            name=self._orderName_create_str(noneDel_list)
            return name
        elif self._switch=="setAuto":
            self.__loading()
            self.__loadingPlus()
            noneDel_list=self.noneDeleteOrder_edit_list(self._order_list)
            name=self._orderName_create_str(noneDel_list)
            return name
        elif self._switch=="mark":
            self._title=cmds.getAttr(self._object+"."+"titleName")
            self._side=cmds.getAttr(self._object+"."+"nodeName")
            self._node=cmds.getAttr(self._object+"."+"sideName")
            self._number=cmds.getAttr(self._object+"."+"numberName")
            self._hierarchy=cmds.getAttr(self._object+"."+"hierarchyName")
            self.__loading()
            noneDel_list=self.noneDeleteOrder_edit_list(self._order_list)
            name=self._orderName_create_str(noneDel_list)
            return name

        elif self._switch=="replace":
            if not self._find == None and not self._replace == None:
                name=self._object
                name.replace(self._find,self._replace)
            else:
                name=self._name
                return name

        else:
            cmds.error("Unknown string in swicth value.")

    def rename(self):
        name=self.getRename()
        rename=cmds.rename(self._object,name)
        return rename

    def titleName(self):
        name=self._titleName_query_str(self._choise,delAlph=True)
        return name
    
    def titleHieName(self):
        name=self._titleName_query_str(self._choise,delAlph=False)
        return name
    
    def nodeName(self):
        name=self._nodeName_query_str(self._choise)
        return name
    
    def sideName(self):
        name=self.sideName_query_str(self._choise)
        return name

    def markAttr(self):
        if self._switch == "fullAuto":
            self._title=self._titleName_query_str(self._object)
            self._node=self._nodeName_query_str(self._object)
            self._side=self.sideName_query_str(self._object)
        self.__loading()
        self.__loadingPlus()
        mark=aLB.Attribute()
        mark.setObject(self._object)
        mark.setAttrType("string")
        for _markNaming_dict in self._markNaming_dicts:
            mark.setAttr(_markNaming_dict["attrName"])
            evalSelf=eval("self._"+_markNaming_dict["attrString"])
            mark.setStringName(evalSelf)
            mark.addAttr()
