# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from ...library import baseLB as bLB
from ...library import jsonLB as jLB
from . import appLB as aLB
from . import dataLB as dLB
from . import setBaseLB as sbLB
cit.reloads([bLB,sbLB,jLB])

RULES_DICT=jLB.readJson(cit.mayaSettings_dir,"library")

class AppName(object):
    def __init__(self):
        self._name_DataName=None

    

class AppNodeName(aLB.AppOpenMayaBase):
    def __init__(self):
        super(AppNodeName,self).__init__()


class Naming(sbLB.BaseName):
    def __init__(self):
        super(Naming,self).__init__()
        self._nodeName_dict=RULES_DICT["nodeName_dict"]
        self._markNaming_dicts=RULES_DICT["markNaming_dicts"]

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
    
    def smashNumber_edit_str(self,name):
        if name == None:
            return None
        while name[-1].isdigit():
            name=name[:-1]
            if name=="":
                return None
        return name
    
    def smashAlphabet_edit_str(self,name):
        if name == None:
            return None
        while name[-1].isupper():
            name=name[:-1]
            if name=="":
                return None
        return name

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

class DataName(bLB.SelfOrigin):
    def __init__(self):
        self._titleName_str=None
        self._nodeTypeName_str=None
        self._sideName_str=None
        self._numberName_ints=[]
        self._hierarchyName_strs=[]
        self._customName_strs=[]
        self._orderName_enums=[]

    #Setting Function
    def setTitle(self,variable):
        self._titleName_str=variable
        return self._titleName_str
    def getTitle(self):
        return self._titleName_str
    
    def setNodeType(self,variable):
        self._nodeTypeName_str=variable
        return self._nodeTypeName_str
    def getNodeType(self):
        return self._nodeTypeName_str
    
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
        self._orderName_enums=variables
        return self._orderName_enums
    def addOrders(self,variables):
        self._orderName_enums+=variables
        return self._orderName_enums
    def getOrders(self):
        return self._orderName_enums

class SelfNodeName(bLB.SelfOrigin):
    def __init__(self):
        super(SelfNodeName,self).__init__()
        self._node_DataName=None
        self._node_DataNode=None

    #Private Function
    def __orderName_create_str(self,order_list):
        selfOrders=[eval("self._"+chengeSelf) for chengeSelf in order_list]
        orderName="_".join(selfOrders)
        return orderName

    #Setting Function
    def setDataName(self,variables):
        self._node_DataName=variables
        return self._node_DataName
    def getDataName(self):
        return self._node_DataName
    
    def setDataNode(self,variables):
        self._node_DataNode=variables
        return self._node_DataNode
    def getDataNode(self):
        return self._node_DataNode

    #Public Function
    def rename(self):
        name_str=""
        return name_str