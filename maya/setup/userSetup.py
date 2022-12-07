import sys,os
import pymel.core as pm
import maya.cmds as cmds
from maya import utils

from cgInTools._menu import mayaMenu
utils.executeDeferred(mayaMenu.setUp)

"""
sys.path.append("D:/")
os.environ["OOMOZI"] = r"D:/"
"""

info=cmds.about(version=True)
if info == "2020":
    try:
        # Open new ports
        cmds.commandPort(name=":7001",sourceType="mel",echoOutput=True) 
        cmds.commandPort(name=":7002",sourceType="python",echoOutput=True)
    except RuntimeError:
        pass
elif info == "2022":
    try:
        # Open new ports
        cmds.commandPort(name=":7001",sourceType="mel") 
    except RuntimeError:
        pass