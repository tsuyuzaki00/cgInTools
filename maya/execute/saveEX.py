import cgInTools as cit
from ..library import filingLB as fLB
from ..library import jsonLB as jLB
cit.reloads([fLB,jLB])

def main():
    json_dict=jLB.getJson(cit.mayaData_dir,"save")
    share_dict=json_dict["share_dict"]
    for save_dict in json_dict.get("save_dicts"):
        save=fLB.File()
        save.setAbsoluteDirectory(share_dict.get("AbsoluteDirectory"))
        save.setRelativeDirectory(save_dict.get("RelativeDirectory"))
        save.setFile(save_dict.get("File"))
        save.save()