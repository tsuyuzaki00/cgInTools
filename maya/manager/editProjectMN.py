# -*- coding: iso-8859-15 -*-
import cgInTools as cit
from ...library import pathLB as pLB
from ..library import projectLB as pjLB
from ..library import windowLB as wLB
cit.reloads([pLB,pjLB,wLB])

def main():
    project_dict=wLB.mayaDirDialog_query_dict("Edit",upRoot=True)
    if project_dict is None:
        return

    project_DataPath=pLB.DataPath()
    project_DataPath.setAbsoluteDirectory(project_dict["directory"])
    project_DataPath.setRelativeDirectory(project_dict["folder"])

    project_SelfProject=pjLB.SelfProject()
    project_SelfProject.setDataPath(project_DataPath)
    project_SelfProject.editProject()