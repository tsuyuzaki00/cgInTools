from maya import cmds
import json,os
import cgInTools as cit

#("labal=string or optionbox=True","relativePath=string","fileName=string","run_function=string","icon=string")
#["title","relativePath","fileName","function","icon"]

class Menu():
    def __init__(self):
        self._path=os.path.dirname(__file__)
        self._file="mayaMenu"

    #Single Function
    def setUpJson_quary_dict(self,path,file,extension="json"):
        json_file=os.path.join(path,file+"."+extension)
        with open(json_file, 'r') as f:
            json_dict=json.load(f)
            return json_dict

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

    def _settingsMenu_create_func(self,menuTitle_str,orderMenu_lists,menus_dict):
        cmds.menu(l=menuTitle_str,p="MayaWindow",to=True)
        for orderMenu_list in orderMenu_lists:
            if orderMenu_list[0] == "single":
                self._singleItem_create_func(orderMenu_list[1],menus_dict[orderMenu_list[1]])
            elif orderMenu_list[0] == "multi":
                self._multiItem_create_func(orderMenu_list[1],menus_dict[orderMenu_list[1]])
            else:
                pass
    
    #Public Function
    def run(self):
        json_dict=self.setUpJson_quary_dict(self._path,self._file)
        self._settingsMenu_create_func(json_dict["menuTitle"],json_dict["orderMenu"],json_dict["menus"])
        
def setUp():
    menu=Menu()
    menu.run()