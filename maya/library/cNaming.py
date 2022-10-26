# -*- coding: iso-8859-15 -*-
import itertools
import maya.cmds as cmds

import cgInTools as cit
from . import cJson as cj
from . import cAttributes as ca

class Naming():
    def __init__(self):
        self.obj="null"
        self.name="name"
        self.node="node"
        self.pos="C"
        self.number=0
        self.num=str(self.number).zfill(2)
        self.nameNum=self.name+self.num
        self.nodeNum=self.node+self.num
        self.posNum=self.pos+self.num
        self.scene="scene"
        self.orders=["name","node","pos","num"]
        self.rename_str=""

#Public function
    def setObj(self,obj):
        self.obj=obj
        return self.obj

    def setName(self,name):
        self.name=name
        return self.name

    def setPos(self,pos):
        self.pos=pos
        return self.pos

    def setOrders(self,orders):
        self.orders=orders
        return self.orders

    def getRename(self):
        order_list=[]
        nullDel_list = [order for order in self.orders if order != ""]
        for chengeSelf in nullDel_list:
            add=eval("self."+chengeSelf)
            order_list.append(add)
        self.rename_str = "_".join(order_list)
        return self.rename_str

    def rename(self):
        self.node=self.node_query_str(self.obj)
        if "num" in self.orders or "nameNum" in self.orders or "nodeNum" in self.orders or "posNum" in self.orders:
            self.num=self.number_query_str(self.obj,self.name,self.pos,self.node,self.number)
            self.nameNum=self.name+self.num
            self.nodeNum=self.node+self.num
            self.posNum=self.pos+self.num
        self.scene=self.scene_query_str()
        rename_str=self.getRename()
        cmds.rename(self.obj,rename_str)

    def markAttr(self):
        self.node=self.node_query_str(self.obj)
        #self.num=self.number_query_str(self.obj,self.name,self.pos,self.node,self.number)
        self.scene=self.scene_query_str()
        mark=ca.Attrebute()
        mark.setObj(self.obj)
        mark.setAttrType("string")
        self.addStringAttrs=[
            {"attrName":"cname","attrString":self.name},
            {"attrName":"cpos","attrString":self.pos},
            {"attrName":"cnode","attrString":self.node},
            {"attrName":"cnum","attrString":self.num},
        ]
        for addStringAttr in self.addStringAttrs:
            mark.setName(addStringAttr["attrName"])
            mark.setStringName(addStringAttr["attrString"])
            mark.addAttr()

    def setRename(self):
        self.addStringAttrs=[
            {"attrName":"cname","attrString":self.name},
            {"attrName":"cpos","attrString":self.pos},
            {"attrName":"cnode","attrString":self.node},
            {"attrName":"cnum","attrString":self.num},
        ]
        for addStringAttr in self.addStringAttrs:
            addStringAttr["attrString"]=cmds.getAttr(self.obj+"."+addStringAttr["attrName"])            
        rename_str=self.getRename()
        cmds.rename(self.obj,rename_str)

#Private function
    def node_query_str(self,obj):
        setting_path=cj.pathSetting_create_str(cit.mayaSettings_path,"autoRename")
        readSettings_dict=cj.readJson_quary_dict(setting_path)
        getNode_str=self.isNodeType_query_str(obj)
        nodeName_str=readSettings_dict["node_renames"][getNode_str]
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
