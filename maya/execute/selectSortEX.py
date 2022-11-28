# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

def selectSortingOutliner_edit_func(objs):
    objSort_list=sorted(objs,key=str)
    for objSort in objSort_list:
        cmds.reorder(objSort,back=True)
        
def main():
    objs=cmds.ls(sl=True)
    selectSortingOutliner_edit_func(objs)