# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import cgInTools as cit
from cgInTools.maya.library import filingLB as fLB
cit.reloads([fLB])

def main():
    check=fLB.Project()
    print(check.getName())
main()