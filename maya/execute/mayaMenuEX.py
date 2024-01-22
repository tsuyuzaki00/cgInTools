import cgInTools as cit
from ...library import dataLB as dLB
from ..library import selfLB as sLB
cit.reloads([dLB,sLB])
        
def main(readFile_str="init"):
    menu_DataPath=dLB.DataPath()
    menu_DataPath.setAbsoluteDirectory(cit.mayaSettings_dir)
    menu_DataPath.setRelativeDirectory("mayaMenu")
    menu_DataPath.setFile(readFile_str)
    menu_DataPath.setExtension("mayaMenu")

    menu_SelfMenu=sLB.SelfMenu()
    menu_SelfMenu.setOriginDataPath(menu_DataPath)
    menu_SelfMenu.readData()
    menu_SelfMenu.create()