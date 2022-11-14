# -*- coding: iso-8859-15 -*-
import itertools
import maya.cmds as cmds

import cgInTools as cit
from . import setBaseLB as sbLB
from . import jsonLB as jLB
from . import attributeLB as ca

class Naming(sbLB.SetName):
    def __init__(self):
        self._object=""
        self._name=""
        self._title=""
        self._node=""
        self._side=""
        self._hierarchy=""
        self._number=00
        self._autoSwitch=True
        self._orders=["title","node","side","num"]

    def setLoading(self):
        self._num=str(self._number).zfill(2)
        self._titleNum=self._title+self._num
        self._nodeNum=self._node+self._num
        self._sideNum=self._side+self._num
        self._titleHie=self._title+self._hierarchy
        self._scene="scene"

#Public function
    def setOrders(self,variable):
        self._orders=variable
        return self._orders
    def getOrders(self):
        return self._orders

    def setAutoSwitch(self,variable):
        self._autoSwitch=variable
        return self._autoSwitch
    def getAutoSwitch(self):
        return self._autoSwitch

    def autoNamer(self):
        order_list=[]
        nullDel_list=[order for order in self._orders if order != ""]
        for chengeSelf in nullDel_list:
            add=eval("self._"+chengeSelf)
            order_list.append(add)
        self._auteName = "_".join(order_list)
        return self._auteName

    def rename(self):
        if self._autoSwitch:
            name=self.autoNamer()
        else:
            name=self._name
        rename=cmds.rename(self._object,name)
        return rename
        """
        self.node=self.node_query_str(self._object)
        if "num" in self.orders or "nameNum" in self.orders or "nodeNum" in self.orders or "posNum" in self.orders:
            self.num=self.number_query_str(self.obj,self.name,self.pos,self.node,self.number)
            self.nameNum=self.name+self.num
            self.nodeNum=self.node+self.num
            self.posNum=self.pos+self.num
        self.scene=self.scene_query_str()
        rename_str=self.getRename()
        """

    def markAttr(self):
        self.node=self.node_query_str(self.obj)
        #self.num=self.number_query_str(self.obj,self.name,self.pos,self.node,self.number)
        self.scene=self.scene_query_str()
        mark=ca.Attrebute()
        mark.setObj(self.obj)
        mark.setAttrType("string")
        self.addStringAttrs=[
            {"attrName":"ctitle","attrString":self._title},
            {"attrName":"cside","attrString":self._side},
            {"attrName":"cnode","attrString":self._node},
            {"attrName":"cnum","attrString":self._num},
        ]
        for addStringAttr in self.addStringAttrs:
            mark.setName(addStringAttr["attrName"])
            mark.setStringName(addStringAttr["attrString"])
            mark.addAttr()

    def setRename(self):
        self.addStringAttrs=[
            {"attrName":"cname","attrString":self._name},
            {"attrName":"cpos","attrString":self._pos},
            {"attrName":"cnode","attrString":self._node},
            {"attrName":"cnum","attrString":self._num},
        ]
        for addStringAttr in self.addStringAttrs:
            addStringAttr["attrString"]=cmds.getAttr(self.obj+"."+addStringAttr["attrName"])            
        rename_str=self.getRename()
        cmds.rename(self.obj,rename_str)

#Private function
    def node_query_str(self,obj):
        nodeType=jLB.Json()
        nodeType.setPath(cit.mayaSettings_path)
        nodeType.setFile("autoRename")
        nodeType_dict=nodeType.read()
        getNode_str=self.isNodeType_query_str(obj)
        nodeName_str=nodeType_dict["node_renames"][getNode_str]
        return nodeName_str

    def isNodeType_query_str(self,obj):
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

    def number_query_str(self,obj,name,pos,node,num):
        num_str=str(num).zfill(2)
        one_list = [(name),(pos),(node),(num_str)]
        two_list = list(itertools.product([name,pos,node,num_str],repeat=2))
        three_list = list(itertools.product([name,pos,node,num_str],repeat=3))
        four_list = list(itertools.product([name,pos,node,num_str],repeat=4))
        same_lists = one_list+two_list+three_list+four_list
    
        for same_list in same_lists:
            name_str="_".join(same_list)
            if cmds.objExists(name_str):
                num=self.count_edit_int(obj,name_str,num)
                num_str=str(num).zfill(2)
                return num_str
        num_str=str(num).zfill(2)    
        return num_str

    def count_edit_int(self,obj,same,num):
        nowNum=num
        oldNum=num
        while cmds.objExists(same):
            if obj == same:
                return nowNum
            nowNum=nowNum+1
            same=same.replace(str(oldNum).zfill(2),str(nowNum).zfill(2))
            oldNum=int(oldNum+1)
        return nowNum

    def scene_query_str(self):
        sceneName=cmds.file(q=True,sn=True).split("/")[-1]
        sceneName=sceneName.split(".")[0]
        sceneParent=cmds.workspace(q=True,sn=True).split("/")[-1]
        if sceneName == "":
            self.scene=sceneParent
        else:
            self.scene=sceneName
        return self.scene

    def sameName_check_str(self,check,sel):
        if sel is not check:
            if cmds.objExists(check):
                check = check + '_NG'
                return check
            else :
                return check
        return check
