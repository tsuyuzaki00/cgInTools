# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
from ..library import cClean as cl

def main():
    objs = cmds.ls(sl=True)
    for obj in objs:
        cl.defaultMaterial_edit_func(obj)