import cgInTools as cit
from ...library import jsonLB as jLB
from ...library import dataLB as dLB
from ..library import dataLB as mdLB
from ..library import selfLB as sLB
cit.reloads([jLB,dLB,mdLB,sLB])
        
def main():
    loadFile_str="init"

    menu_DataJson=dLB.DataJson()
    menu_DataJson.setAbsoluteDirectory(cit.mayaSettings_dir)
    menu_DataJson.setRelativeDirectory("mayaMenu")
    menu_DataJson.setFile(loadFile_str)
    menu_DataJson.setExtension("json")

    menu_AppMenu=jLB.AppJson()
    menu_AppMenu.setDataJson(menu_DataJson)
    menu_dict=menu_AppMenu.read()

    menu_DataMeunParamArrays=[]
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
        menu_DataMeunParamArrays.append(menu_DataMenuParamArray)

    menu_DataMenu=mdLB.DataMenu()
    menu_DataMenu.setName(menu_dict.get("Name"))
    menu_DataMenu.setDataMeunParamArrays(menu_DataMeunParamArrays)

    menu_AppMenu=sLB.SelfMenu()
    menu_AppMenu.setDataMenu(menu_DataMenu)
    menu_AppMenu.create()