import cgInTools as cit
from ...library import dataLB as dLB
from ...library import jsonLB as jLB
from ..library import selfLB as sLB
from ..library import dataLB as mdLB
cit.reloads([dLB,jLB,sLB,mdLB])

def main(readFile_str="init",writeFile_str="init"):
    read_DataPath=dLB.DataPath()
    read_DataPath.setAbsoluteDirectory(cit.mayaSettings_dir)
    read_DataPath.setRelativeDirectory("mayaMenu")
    read_DataPath.setFile(readFile_str)
    read_DataPath.setExtension("json")

    write_DataPath=dLB.DataPath()
    write_DataPath.setAbsoluteDirectory(cit.mayaSettings_dir)
    write_DataPath.setRelativeDirectory("mayaMenu")
    write_DataPath.setFile(writeFile_str)
    write_DataPath.setExtension("mayaMenu")

    menu_AppJson=jLB.AppJson()
    menu_AppJson.setDataPath(read_DataPath)
    menu_dict=menu_AppJson.read()

    menu_DataMenuParamArrays=[]
    for menuItem_dict in menu_dict.get("DataMenuParamArrays"):
        menu_DataMenuParamArray=mdLB.DataMenuParamArray()
        menu_DataMenuParamArray.setName(menuItem_dict.get("Name"))
        menu_DataMenuParamArray.setType(menuItem_dict.get("Type"))
        for item_dict in menuItem_dict.get("DataMenuParamArray"):
            menu_DataMenuParam=mdLB.DataMenuParam()
            menu_DataMenuParam.setLabel(item_dict.get("Label"))
            menu_DataMenuParam.setFromFolder(item_dict.get("FromFolder"))
            menu_DataMenuParam.setImportFile(item_dict.get("ImportFile"))
            menu_DataMenuParam.setFunction(item_dict.get("Function"))
            menu_DataMenuParam.setIcon(item_dict.get("Icon"))
            menu_DataMenuParamArray.addDataMenuParams([menu_DataMenuParam])
        menu_DataMenuParamArrays.append(menu_DataMenuParamArray)

    menu_DataMenu=mdLB.DataMenu()
    menu_DataMenu.setName(menu_dict.get("Name"))
    menu_DataMenu.setDataMenuParamArrays(menu_DataMenuParamArrays)

    menu_SelfMenu=sLB.SelfMenu()
    menu_SelfMenu.setOriginDataPath(write_DataPath)
    menu_SelfMenu.setDataMenu(menu_DataMenu)
    menu_SelfMenu.writeData()
    