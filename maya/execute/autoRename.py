import maya.cmds as cmds
from cgInTools.maya.library import cNaming as cn;

def main():
    objs=cmds.ls(sl=True)
    index=0
    for obj in objs:
        model=cn.Naming()
        model.setObj(obj)
        objName_list=obj.split("_")[0]
        if any(chr.isdigit() for chr in objName_list):
            objName_list=''.join([i for i in objName_list if not i.isdigit()])
        model.setName(objName_list)
        model.setPos("C")
        model.setOrders(["nameNum","node","pos"])
        model.number=index
        model.rename()
        index=index+1
