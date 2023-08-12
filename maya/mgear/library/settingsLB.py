import os
import maya.cmds as cmds

def setMgearBuild_edit_func(wrk_path="",folder_str=""):
    wrk_path=wrk_path or cmds.workspace(q=True,rd=True)
    folder_str=folder_str or 'mgear_build'
    os.environ['MGEAR_SHIFTER_CUSTOMSTEP_PATH']=os.path.join(wrk_path,folder_str)
    