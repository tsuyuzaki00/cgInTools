import maya.cmds as cmds
#import pymel.core as pm

import cgInTools as cit
from cgInTools import ui as UI
from cgInTools.maya import library as LB
from cgInTools.maya import execute as EX
from cgInTools.maya import manager as MN
from cgInTools.maya import option as OP
cit.reloads([UI,LB,EX,MN,OP])

obj=cmds.ls(sl=True)
test=LB.File()
print(test.setFileType("ma"))
