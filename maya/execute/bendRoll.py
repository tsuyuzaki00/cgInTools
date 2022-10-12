# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
from ..library import cBendRoll as cbr

def main():
    mirror=cbr.BendRollCtrl()
    mirror.setSource(cmds.ls(sl=True)[0])
    mirror.setTarget(cmds.ls(sl=True)[1])
    mirror.update()
    mirror.run()