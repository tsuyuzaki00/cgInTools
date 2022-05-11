import maya.cmds as cmds

def grpNodeChoise_query_list(grpName,choisList,type="transform"):
    choiseNodes=[]
    grpName=objSence_check_string(objName=grpName)
    grpNodes=cmds.ls(grpName,dag=True,typ=type)
    grpNodes.remove(grpName)
    for node in grpNodes:
        for choisName in choisList:
            if choisName in node:
                choiseNodes.append(node)
    return choiseNodes

def geometryClean_create_obj(self,):
    pass

def objSence_check_string(objName):
    if cmds.objExists(objName):
        return objName
    else:
        cmds.error("There is no name for the group "+"'"+objName+"'")

def main():
    test=grpNodeChoise_query_list("Geo_Grp",["Geo"])
    print(test)