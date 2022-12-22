# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from ..library import cleanLB as cLB
cit.reloads([cLB])

def main():
    objs=cmds.ls(sl=True,dag=True,tr=True)
    for obj in objs:
        cLB.delFRHThree_edit_func(obj)