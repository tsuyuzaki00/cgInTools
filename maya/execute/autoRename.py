import maya.cmds as cmds
from cgInTools.maya.library import cNaming as cn; reload(cn);

def main():
    objs=cmds.ls(sl=True)
    for obj in objs:
        model=cn.Naming()
        model.setObj(obj)
        objName_list=obj.split("_")
        model.setName(objName_list[0])
        model.setPos("C")
        model.setOrders(["name","node","pos","num"])
        model.rename()
