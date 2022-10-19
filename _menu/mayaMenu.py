from maya import cmds
import json,os

#("labal=string or optionbox=True","path_import=string","run_function=string","icon=string")
#["label_name","from_name","import_name","executionFunction_name","imageFile_name"]

def importJson_quary_dicts(json_name,path_name):
    json_file = os.path.join(path_name,json_name)
    with open(json_file, 'r') as f:
        connect_list = json.load(f)
        return connect_list

class Menu():
    def settingMenu_create_func(self,menuJson_query_dicts):
        self.titleMenu_create_func(menuJson_query_dicts["menu_title"])
        menu_dicts = menuJson_query_dicts["menus"]
        order_dicts = menuJson_query_dicts["order_menu"]
        self.organizeMenu_create_func(menu_dicts,order_dicts)

    def organizeMenu_create_func(self,menu_dicts,order_dicts):
        for order_name in order_dicts:
            if order_name[0] == "single":
                self.singleItem_create_func(order_name[1],menu_dicts[order_name[1]])
            elif order_name[0] == "multi":
                self.multiItem_create_func(order_name[1],menu_dicts[order_name[1]])
            else:
                pass

    def titleMenu_create_func(self,menu_title):
        cmds.menu(l = menu_title, p ="MayaWindow", to = True)

    def singleItem_create_func(self,titleName,singleList_list5):
        cmds.menuItem(divider=True,dividerLabel=titleName)
        for menuItem_string in singleList_list5:
            self.setItem_create_func(menuItem_string)

    def multiItem_create_func(self,titleName,multiList_list5):
        cmds.menuItem(subMenu=True,to = True,label=titleName)
        for menuItem_string in multiList_list5:
            self.setItem_create_func(menuItem_string)
        cmds.setParent("..",menu=True)

    def setItem_create_func(self,menuItem_string):
        if menuItem_string[0] == None:
            pass
        elif menuItem_string[0] == True or menuItem_string[0] == 1:
            cmds.menuItem(optionBox=menuItem_string[0], c="from "+menuItem_string[1]+" import "+menuItem_string[2]+" as ps; ps."+menuItem_string[3])
        else:
            cmds.menuItem(label=menuItem_string[0],c="from "+menuItem_string[1]+" import "+menuItem_string[2]+" as ps; ps."+menuItem_string[3],i=menuItem_string[4])

def main():
    menuJson_query_dicts = importJson_quary_dicts("mayaMenu.json",os.path.dirname(__file__))
    _Menu = Menu()
    _Menu.settingMenu_create_func(menuJson_query_dicts)