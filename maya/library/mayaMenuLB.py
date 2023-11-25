import maya.cmds as cmds
import cgInTools as cit
from ...library import jsonLB as jLB
from ...library import dataLB as dLB
from . import dataLB as mdLB
cit.reloads([jLB,dLB,mdLB])

class AppMenu():
    def __init__(self):
        self._menu_DataMenu=None

    #Single Function
    def setItem_create_func(self,title,fromFolder,importFile,function,icon):
        command="import cgInTools as cit; from "+fromFolder+" import "+importFile+" as ps; cit.reloads([ps]); ps."+function
        if title == True or title == 1:
            cmds.menuItem(optionBox=title,c=command)
        else:
            cmds.menuItem(label=title,c=command,i=icon)

    #Multi Function
    def _singleItem_create_func(self,itemName_str,menu_DataMenuParams):
        cmds.menuItem(divider=True,dividerLabel=itemName_str)
        for menu_DataMenuParam in menu_DataMenuParams:
            label_str=menu_DataMenuParam.getLabel()
            from_str=menu_DataMenuParam.getFromFolder()
            import_str=menu_DataMenuParam.getImportFile()
            function_str=menu_DataMenuParam.getFunction()
            icon_str=menu_DataMenuParam.getIcon()
            self.setItem_create_func(label_str,from_str,import_str,function_str,icon_str)

    def _multiItem_create_func(self,itemName_str,menu_DataMenuParams):
        cmds.menuItem(subMenu=True,to=True,label=itemName_str)
        for menu_DataMenuParam in menu_DataMenuParams:
            label_str=menu_DataMenuParam.getLabel()
            from_str=menu_DataMenuParam.getFromFolder()
            import_str=menu_DataMenuParam.getImportFile()
            function_str=menu_DataMenuParam.getFunction()
            icon_str=menu_DataMenuParam.getIcon()
            self.setItem_create_func(label_str,from_str,import_str,function_str,icon_str)
        cmds.setParent("..",menu=True)

    def _settingsMenu_create_func(self,menuName_str,menu_DataMenuParamArrays):
        cmds.menu(l=menuName_str,p="MayaWindow",to=True)
        for menu_DataMenuParamArray in menu_DataMenuParamArrays:
            if menu_DataMenuParamArray.getType() == "single":
                self._singleItem_create_func(menu_DataMenuParamArray.getName(),menu_DataMenuParamArray.getDataMenuParams())
            elif menu_DataMenuParamArray.getType() == "multi":
                self._multiItem_create_func(menu_DataMenuParamArray.getName(),menu_DataMenuParamArray.getDataMenuParams())
            else:
                pass
    
    #Setting Function
    def setDataMenu(self,variable):
        self._menu_DataMenu=variable
        return self._menu_DataMenu
    def getDataPath(self):
        return self._menu_DataMenu
        
    #Public Function
    def create(self):
        menuName_str=self._menu_DataMenu.getName()
        menu_DataMenuParamArrays=self._menu_DataMenu.getDataMeunParamArrays()
        self._settingsMenu_create_func(menuName_str,menu_DataMenuParamArrays)