import sys,os
import maya.cmds as cmds
from maya import utils

from cgInTools.maya.execute import mayaMenuEX
utils.executeDeferred(mayaMenuEX.main)

"""
sys.path.append("D:/")
os.environ["OOMOZI"] = r"D:/"
"""

wrk_path=cmds.workspace(q=True,rd=True)
folder_str="cgInToolsData"
cgInToolsData_dir=os.path.join(wrk_path,"scripts",folder_str)
os.environ['MAYACGINTOOLSDATA_DIRECTORY']=cgInToolsData_dir

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