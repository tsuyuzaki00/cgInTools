# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
from ..library import cleanLB as cl

def main():
    objs = cmds.ls(sl=True,dag=True,tr=True)
    cl.delFRHThree_edit_func(objs)