import os
import maya.cmds as cmds

from mgear.shifter import io
from mgear.shifter import guide_manager

import cgInTools as cit
from ...library import pathLB as pLB
from ...library import jsonLB as jLB
from ...maya.library import filingLB as fLB
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
        guidePath_dict=buildPath_dict.get("SavePath")
        
        project=fLB.SelfProject()
        project.setAbsoluteDirectory(guidePath_dict.get("AbsoluteDirectory"))
        project.setProjectName(guidePath_dict.get("RelativeDirectory"))
        workDirectory=project.editProject()

        save=fLB.SelfFile()
        save.setAbsoluteDirectory(workDirectory)
        save.setRelativeDirectory("scenes")
        save.addRelativeDirectory("scenes")
        save.setFile(buildPath_dict.get("File"))
        save.save()

        mgearBuildDirectory=os.path.join(workDirectory,"mgear_build")
        os.environ['MGEAR_SHIFTER_CUSTOMSTEP_PATH']=mgearBuildDirectory
        
        guidePath=os.path.join(mgearBuildDirectory,"guide",share_dict.get("guideFile"))
        guidePath=os.path.normpath(guidePath)
        io.import_guide_template(guidePath)

        cmds.select("guide")
        guide_manager.build_from_selection()

        save.save()
        