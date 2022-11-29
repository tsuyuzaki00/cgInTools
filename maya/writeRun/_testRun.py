# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import cgInTools as cit
from cgInTools.maya.library import groupLB as gLB
cit.reloads([gLB])

def main():
    group=gLB.Group()
    group.setName()
main()