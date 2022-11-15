import maya.cmds as cmds
from cgInTools.maya.library import namingLB as nLB;

def main():
    objs=cmds.ls(sl=True)
    model=nLB.Naming()
    model.setOrders(["title","node","side"])
    for obj in objs:
        model.setObject(obj)
        model.rename()
