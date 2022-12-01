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