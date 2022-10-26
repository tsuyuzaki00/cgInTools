# -*- coding: iso-8859-15 -*-
import os,sys

def verReload(i):
    if sys.version.startswith("2"):
        reload(i)
    elif sys.version.startswith("3"):
        import importlib
        importlib.reload(i)

root_path = os.path.dirname(__file__) #.../cgInTools/
ui_path = os.path.join(root_path,"ui")

maya_path = os.path.join(root_path,"maya")
mayaSettings_path = os.path.join(maya_path,"_settings")
mayaDefSetProject_path = os.path.join(maya_path,"_defSetProject")
mayaData_path = os.path.join(maya_path,"data")
mayaExecute_path = os.path.join(maya_path,"execute")
mayaLibrary_path = os.path.join(maya_path,"library")
mayaManager_path = os.path.join(maya_path,"manager")
mayaSetup_path = os.path.join(maya_path,"setup")

mgear_path = os.path.join(root_path,"mgear")
mgearSettings_path = os.path.join(mgear_path,"_settings")
mgearData_path = os.path.join(mgear_path,"data")
mgearExecute_path = os.path.join(mgear_path,"execute")
mgearLibrary_path = os.path.join(mgear_path,"library")
mgearManager_path = os.path.join(mgear_path,"manager")
