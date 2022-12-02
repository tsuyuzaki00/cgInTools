# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
from ..library import cleanLB as cl

def main():
    objs=cmds.ls(sl=True,dag=True,tr=True)
    for obj in objs:
        cl.delFRHThree_edit_func(obj)