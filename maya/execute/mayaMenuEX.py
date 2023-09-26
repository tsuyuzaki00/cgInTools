from maya import cmds
import json,os
import cgInTools as cit
from cgInTools.library import jsonLB as jLB

class AppMenu():
    def __init__(self):
        self._menu_SelfJson=jLB.SelfJson()

    #Single Function
    def setItem_create_func(self,title,fromFolder,importFile,function,icon):
        command="import cgInTools as cit; from "+fromFolder+" import "+importFile+" as ps; cit.reloads([ps]); ps."+function
        if title == True or title == 1:
            cmds.menuItem(optionBox=title,c=command)
        else:
            cmds.menuItem(label=title,c=command,i=icon)

    #Multi Function
    def _singleItem_create_func(self,titleName,singleItem_dicts):
        cmds.menuItem(divider=True,dividerLabel=titleName)
        for menuItem_dict in singleItem_dicts:
            self.setItem_create_func(menuItem_dict["label"],menuItem_dict["fromFolder"],menuItem_dict["importFile"],menuItem_dict["function"],menuItem_dict["icon"])

    def _multiItem_create_func(self,titleName,multiItem_dicts):
        cmds.menuItem(subMenu=True,to=True,label=titleName)
        for menuItem_dict in multiItem_dicts:
            self.setItem_create_func(menuItem_dict["label"],menuItem_dict["fromFolder"],menuItem_dict["importFile"],menuItem_dict["function"],menuItem_dict["icon"])
        cmds.setParent("..",menu=True)

    def _settingsMenu_create_func(self,menuTitle_str,orderMenu_dicts,menuItem_dict):
        cmds.menu(l=menuTitle_str,p="MayaWindow",to=True)
        for orderMenu_dict in orderMenu_dicts:
            if orderMenu_dict["type"] == "single":
                self._singleItem_create_func(orderMenu_dict["menu"],menuItem_dict[orderMenu_dict["menu"]])
            elif orderMenu_dict["type"] == "multi":
                self._multiItem_create_func(orderMenu_dict["menu"],menuItem_dict[orderMenu_dict["menu"]])
            else:
                pass
    
    #Setting Function
    def setDirectry(self,variable):
        menu_dir=self._menu_SelfJson.setAbsoluteDirectory(variable)
        return menu_dir
    def getDirectory(self):
        return self._menu_SelfJson.getAbsoluteDirectory()

    def setFile(self,variable):
        menu_str=self._menu_SelfJson.setFile(variable)
        return menu_str
    def getFile(self):
        return self._menu_SelfJson.getFile()

    def setSelfJson(self,variable):
        self._menu_SelfJson=variable
        self._menu_SelfJson.setExtension("json")
        return self._menu_SelfJson
    def getSelfJson(self):
        return self._menu_SelfJson
        
    #Public Function
    def doIt(self):
        json_dict=self._menu_SelfJson.read()
        self._settingsMenu_create_func(json_dict["menuTitle_str"],json_dict["orderMenu_dicts"],json_dict["menuItem_dict"])
        
def main():
    menu_AppMenu=AppMenu()
    menu_AppMenu.setDirectry(cit.mayaSettings_dir)
    menu_AppMenu.setFile("mayaMenu")
    menu_AppMenu.doIt()