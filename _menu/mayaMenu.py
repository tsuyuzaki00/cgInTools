from maya import cmds
import json,os

#("labal=string or optionbox=True","path_import=string","run_function=string","icon=string")
#["label_name","from_name","import_name","executionFunction_name","imageFile_name"]

class Menu():
    def __init__(self):
        self._path=os.path.dirname(__file__)
        self._file="mayaMenu.json"

    #Single Function
    def setUpJson_quary_dict(self,path,file):
        json_file=os.path.join(path,file)
        with open(json_file, 'r') as f:
            json_dict=json.load(f)
            return json_dict

    def setItem_create_func(self,title,relative_path,fileName,function,image):
        if title == None:
            pass
        elif title == True or title == 1:
            cmds.menuItem(optionBox=title, c="from "+relative_path+" import "+fileName+" as ps; ps."+function)
        else:
            cmds.menuItem(label=title,c="from "+relative_path+" import "+fileName+" as ps; ps."+function,i=image)

    #Multi Function
    def _singleItem_create_func(self,titleName,singleList_lists):
        cmds.menuItem(divider=True,dividerLabel=titleName)
        for menuItem_string in singleList_lists:
            self.setItem_create_func(menuItem_string[0],menuItem_string[1],menuItem_string[2],menuItem_string[3],menuItem_string[4])

    def _multiItem_create_func(self,titleName,multiList_lists):
        cmds.menuItem(subMenu=True,to = True,label=titleName)
        for menuItem_string in multiList_lists:
            self.setItem_create_func(menuItem_string[0],menuItem_string[1],menuItem_string[2],menuItem_string[3],menuItem_string[4])
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

    def run(self):
        json_dict=self.setUpJson_quary_dict(self._path,self._file)
        self._settingsMenu_create_func(json_dict["menuTitle"],json_dict["orderMenu"],json_dict["menus"])
        
def setUp():
    menu=Menu()
    menu.run()