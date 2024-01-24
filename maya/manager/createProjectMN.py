# -*- coding: iso-8859-15 -*-
import cgInTools as cit
from ...library import dataLB as dLB
#from ..library import projectLB as pjLB
from ..library import selfLB as sLB
from ..library import windowLB as wLB
cit.reloads([dLB,sLB,wLB])

def main():
    project_dict=wLB.mayaDirDialog_query_dict("Create",upRoot=True)
    if project_dict is None:
        return

    project_DataPath=dLB.DataPath()
    project_DataPath.setAbsoluteDirectory(project_dict["directory"])
    project_DataPath.setRelativeDirectory(project_dict["folder"])

    project_SelfProject=sLB.SelfProject()
    project_SelfProject.setProjectDataPath(project_DataPath)
    project_SelfProject.createProject()