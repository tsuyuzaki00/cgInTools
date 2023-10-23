# -*- coding: iso-8859-15 -*-
import os,sys,inspect

def reloads(ps=[]):
    if ps == [] or ps == None:
        return None
    for p in ps:
        if sys.version.startswith("2"):
            reload(p)
        elif sys.version.startswith("3"):
            import importlib
            importlib.reload(p)

root_dir=os.path.dirname(__file__) #.../cgInTools/
ui_dir=os.path.join(root_dir,"ui")
settings_dir=os.path.join(root_dir,"_settings")
library_dir=os.path.join(root_dir,"library")
execute_dir=os.path.join(root_dir,"execute")

maya_dir=os.path.join(root_dir,"maya")
mayaDefSetProject_dir=os.path.join(maya_dir,"__defSetProject")
mayaSettings_dir=os.path.join(maya_dir,"_settings")
mayaExecute_dir=os.path.join(maya_dir,"execute")
mayaLibrary_dir=os.path.join(maya_dir,"library")
mayaManager_dir=os.path.join(maya_dir,"manager")
mayaOption_dir=os.path.join(maya_dir,"option")
mayaSetup_dir=os.path.join(maya_dir,"setup")
#mayaData_dir=os.environ['MAYACGINTOOLSDATA_DIRECTORY']

mgear_dir=os.path.join(maya_dir,"mgear")
mgearSettings_dir=os.path.join(mgear_dir,"_settings")
mgearExecute_dir=os.path.join(mgear_dir,"execute")
mgearLibrary_dir=os.path.join(mgear_dir,"library")
mgearManager_dir=os.path.join(mgear_dir,"manager")
mgearOption_dir=os.path.join(mgear_dir,"option")
mgearSetup_dir=os.path.join(mgear_dir,"setup")
#mgearData_dir=os.environ['MGEARCGINTOOLSDATA_DIRECTORY']

blender_dir=os.path.join(root_dir,"blender")
blenderSettings_dir=os.path.join(blender_dir,"_settings")
blenderExecute_dir=os.path.join(blender_dir,"execute")
blenderLibrary_dir=os.path.join(blender_dir,"library")
blenderManager_dir=os.path.join(blender_dir,"manager")
blenderOption_dir=os.path.join(blender_dir,"option")
blenderSetup_dir=os.path.join(blender_dir,"setup")
#blenderData_dir=os.environ['BLENDERCGINTOOLSDATA_DIRECTORY']