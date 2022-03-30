import sys,os
import pymel.core as pm
import maya.cmds as cmds
from maya import utils

from scriptsInTools._Menu import mayaMenu
utils.executeDeferred(mayaMenu.main)

"""
sys.path.append("D:/")
os.environ["OOMOZI"] = r"D:/"
"""

try:
    # Open new ports
    cmds.commandPort(name=":7001", sourceType="mel", echoOutput=True)
    cmds.commandPort(name=":7002", sourceType="python", echoOutput=True)
except RuntimeError:
    pass