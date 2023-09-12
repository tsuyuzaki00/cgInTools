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

wrk_path=cmds.workspace(q=True,rd=True)
folder_str="cgInToolsData"
os.environ['CGINTOOLSDATA_DIRECTORY']=os.path.join(wrk_path,"scripts",folder_str)

if int(sys.version[0]) == 2:
    try:
        # Open new ports
        cmds.commandPort(name=":7001",sourceType="mel",echoOutput=True) 
        cmds.commandPort(name=":7002",sourceType="python",echoOutput=True)
    except RuntimeError:
        pass
elif int(sys.version[0]) == 3:
    try:
        # Open new ports
        cmds.commandPort(name=":7001",sourceType="mel") 
    except RuntimeError:
        pass
else:
    pass