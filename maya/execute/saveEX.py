import cgInTools as cit
from ..library import filingLB as fLB
from ...library import jsonLB as jLB
cit.reloads([fLB,jLB])

def main():
    json_dict=jLB.readJson(cit.mayaData_dir,"save")
    share_dict=json_dict["share_dict"]
    for saveName in json_dict.get("saves"):
        project=fLB.Project()
        project.setAbsoluteDirectory(share_dict.get("AbsoluteDirectory"))
        project.setProjectName(saveName)
        workDirectory=project.editProject()

        save=fLB.File()
        save.setAbsoluteDirectory(workDirectory)
        save.setRelativeDirectory("scenes")
        save.setFile(share_dict.get("firstFile")+saveName+share_dict.get("lastFile"))
        save.save()