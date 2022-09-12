import os
import maya.cmds as cmds
import pymel.core as pm

import cJson as cj

class Naming():
    def __init__(self):
        self.obj="obj"
        self.name="name"
        self.pos="C"
        self.node="node"
        self.num='0'.zfill(2)
        sceneName=cmds.workspace(q=True,sn=True).split("/")[-1]
        self.scene=sceneName
        self.orders=["name","node","pos","num"]

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

    def rename(self):
        self.node=self.node_query_str(self.obj)
        orders=[]
        for order in self.orders:
            add=eval("self."+order)
            orders.append(add)
        rename_list = [order for order in orders if order != ""]
        autoRename = "_".join(rename_list)
        cmds.rename(self.obj, autoRename)

#Private function
    def node_query_str(self,obj):
        root_path = os.path.dirname(__file__) #.../cgInTools/maya/library
        maya_path = os.path.abspath(os.path.join(root_path,".."))
        maya_settings_path = os.path.join(maya_path,"_settings")
        setting_path=cj.pathSetting_create_str(maya_settings_path,"autoRename")
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
