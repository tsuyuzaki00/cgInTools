# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

# 複数選択をしていてもジョイントを作成出来る用にしている
def jointOnly(**kwargs):
    cmds.select(cl=True)
    joint=cmds.joint(**kwargs)
    return joint

def transferOrient(node):
    if cmds.nodeType(node) == "joint":
        jointOrient_tuple=cmds.getAttr(node+".jointOrient")[0]
        cmds.setAttr(node+".rotate",jointOrient_tuple[0],jointOrient_tuple[1],jointOrient_tuple[2],type="double3")
        cmds.setAttr(node+".jointOrient",0,0,0,type="double3")

def setLabelling(obj,side=0,type=18,other=""):
    cmds.setAttr(obj+'.side',side) # 0=Center 1=Left 2=Right 3=None
    cmds.setAttr(obj+'.type',type) # 18=Other
    cmds.setAttr(obj+'.otherType',other,type='string')