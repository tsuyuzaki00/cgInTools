import os
import maya.cmds as cmds

from mgear.shifter import io
from mgear.shifter import guide_manager

import cgInTools as cit
from ...library import jsonLB as jLB
from ...library import pathLB as pLB
from ...maya.library import projectLB as fLB
cit.reloads([pLB,jLB,fLB])

"""
{
    "buildPath_dicts":[
        {
            SavePath:{
                "AbsoluteDirectory":"directoryName",
                "RelativeDirectory":"projectName",
                "File":"fileName"
                "Extension":"ma"
            }
            GuidePath:{
                "AbsoluteDirectory":"directoryName",
                "RelativeDirectory":"projectName",
                "File":"fileName"
                "Extension":"sgt"
            },
        },
    ]
}
"""

def main():
    json_dict=jLB.readJson(cit.mayaData_dir,["guideBuild"])
    for buildPath_dict in json_dict.get("buildPath_dicts"):
        savePath_dict=buildPath_dict.get("SavePath")
        save_DataPath=pLB.DataPath()
        save_DataPath.setAbsoluteDirectory(savePath_dict.get("AbsoluteDirectory"))
        save_DataPath.setRelativeDirectory(savePath_dict.get("RelativeDirectory"))
        save_DataPath.setFile(savePath_dict.get("File"))
        save_DataPath.setExtension(savePath_dict.get("Extension"))
        
        guidePath_dict=buildPath_dict.get("GuidePath")
        guide_DataPath=pLB.DataPath()
        guide_DataPath.setAbsoluteDirectory(guidePath_dict.get("AbsoluteDirectory"))
        guide_DataPath.setRelativeDirectory(guidePath_dict.get("RelativeDirectory"))
        guide_DataPath.setFile(guidePath_dict.get("File"))
        guide_DataPath.setExtension(guidePath_dict.get("Extension"))

        project_SelfProject=fLB.SelfProject()
        project_SelfProject.setDataPath(save_DataPath)
        project_SelfProject.editProject()

        save_SelfFile=fLB.SelfFile()
        save_SelfFile.setDataPath(save_DataPath)
        save_SelfFile.save()

        mgearBuildDirectory=os.path.join(workDirectory,"mgear_build")
        
        guide_SelfPath=pLB.SelfPath()
        guide_SelfPath.setDataPath(guide_DataPath)
        mgearBulid_dir=guide_SelfPath.getAbsoluteDirectory()
        guide_path=guide_SelfPath.queryAbsolutePath()
        
        os.environ['MGEAR_SHIFTER_CUSTOMSTEP_PATH']=mgearBulid_dir
        io.import_guide_template(guide_path)

        cmds.select("guide")
        guide_manager.build_from_selection()

        save_SelfFile.save()
        