# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import importlib
from cgInTools.maya.library import cJson as cj
from cgInTools.maya.library import cFiling as cf
importlib.reload(cf)

setProject=cf.Path()
setProject.upCreateProject("L")
"""
setProject.setDefPath("D:\DTN")
names=["FRA_Calw","HER_Cal","HER_Calw","HorseHera","HorseLIE","HorseOLW"]
for name in names:
    setProject.setProjectName(name)
    setProject.createProject()
"""