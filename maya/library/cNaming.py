# -*- coding: iso-8859-15 -*-
import itertools
import maya.cmds as cmds
import pymel.core as pm

import cgInTools as cit
import cJson as cj
import cAttributes as ca; reload(ca);

class Naming():
    def __init__(self):
        self.obj="null"
        self.name="name"
        self.pos="C"
        self.node="node"
        self.number=0
        self.num=str(self.number).zfill(2)
        sceneName=cmds.workspace(q=True,sn=True).split("/")[-1]
        self.scene=sceneName
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

    def markAttr(self):
        self.node=self.node_query_str(self.obj)
        self.num=self.number_query_str(self.obj,self.name,self.pos,self.node,self.number)
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

    def rename(self):
        self.node=self.node_query_str(self.obj)
        self.num=self.number_query_str(self.obj,self.name,self.pos,self.node,self.number)
        rename_str=self.getRename()
        cmds.rename(self.obj,rename_str)

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
        setting_path=cj.pathSetting_create_str(cit.maya_settings_path,"autoRename")
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
        sceneName = pm.sceneName().basename()
        part = sceneName.split("_")
        if part[0].endswith('.ma') or part[0].endswith('.mb'):
            scene = part[0][:-3]
        elif part[0] == '':
            scene = 'scene'
        else:
            scene = part[0]
        return scene


class NamingSplits():
    def __init__(self):
        pass
        #setting = sj.pathSetting_create_str(sf.maya_settings_path,"autoRename")
        #self.read_setting = sj.readJson_quary_dict(setting)

    def scene(self):
        sceneName = pm.sceneName().basename()
        part = sceneName.split("_")
        if part[0].endswith('.ma') or part[0].endswith('.mb'):
            scene = part[0][:-3]
        elif part[0] == '':
            scene = 'scene'
        else:
            scene = part[0]
        return scene

    def obj(self, sel):
        part = sel.split("_")

        if part[0] == self.pos(sel):
            if part[1] == self.scene():
                obj = part[2]
                return obj
            else :
                obj = part[1]
                return obj
        elif part[0] == self.node(sel):
            obj = part[1]
            return obj
        elif part[0] == self.scene():
            obj = part[1]
            return obj     
        else :
            obj = part[0]
            return obj

    def pos(self, sel):
        pos = 'C'
        if 'joint' == self.node(sel):
            if pm.listRelatives(sel, c = True) == []:
                pos = 'CT'

        elif sel.endswith('_C') or sel.startswith('C_'):
            pos = 'C'
        elif sel.endswith('_CT') or sel.startswith('CT_'):
            pos = 'CT'
        elif sel.endswith('_L') or sel.startswith('L_'):
            pos = 'L'
        elif sel.endswith('_LT') or sel.startswith('LT_'):
            pos = 'LT'
        elif sel.endswith('_R') or sel.startswith('R_'):
            pos = 'R'
        elif sel.endswith('_RT') or sel.startswith('RT_'):
            pos = 'RT'
        elif sel.endswith('_U') or sel.startswith('U_'):
            pos = 'U'
        elif sel.endswith('_D') or sel.startswith('D_'):
            pos = 'D'
        else :
            pos = 'C'

        return pos

    def num(self, sel):
        part = sel.split("_")
        try:
            part[-1]
            part[-2]
        except IndexError:
            num = '0'.zfill(2)
            return num
        else :
            if (part[-1].startswith('0') 
                or part[-1].startswith('1')
                or part[-1].startswith('2')
                or part[-1].startswith('3')
                or part[-1].startswith('4')
                or part[-1].startswith('5')
                or part[-1].startswith('6')
                or part[-1].startswith('7')
                or part[-1].startswith('8')
                or part[-1].startswith('9')) :
                num = part[-1]
                return num   
            elif (part[-2].startswith('0') 
                or part[-2].startswith('1')
                or part[-2].startswith('2')
                or part[-2].startswith('3')
                or part[-2].startswith('4')
                or part[-2].startswith('5')
                or part[-2].startswith('6')
                or part[-2].startswith('7')
                or part[-2].startswith('8')
                or part[-2].startswith('9')) :
                num = part[-2]
                return num
            else :
                num = '0'.zfill(2)
                return num

    def same_name_check(self, check):
        print (check)
        if pm.objExists(check):
            check = check + '_NG'
            return check
        else :
            return check

def main():
    sel = cmds.ls(sl=True)
    gns = NamingSplits()
    print(gns.test_node(sel))
