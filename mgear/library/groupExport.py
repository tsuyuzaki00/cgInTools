import maya.cmds as cmds
import pymel.core as pm
from mgear.core import skin
import os

class GroupExport():
    def grpNodeChoise_query_list(self,grpName,choisList,type="transform"):
        choiseNodes=[]
        grpName=self.objSence_check_string(objName=grpName)
        grpNodes=cmds.ls(grpName,dag=True,typ=type)
        grpNodes.remove(grpName)
        for node in grpNodes:
            for choisName in choisList:
                if choisName in node:
                    choiseNodes.append(node)
        return choiseNodes

    def geometryClean_create_obj(self,):
        pass

    def model_export_list(self,path,objs,file="model"):
        pass

    def objsSkin_export_func(self,path,objs):
        objs=pm.ls(objs)
        filePath=path
        for obj in objs:
            filePath=os.path.join(path,obj+".jSkin")
            skin.exportSkin(filePath=filePath,objs=[obj])

    def objsSkinPack_export_func(self,path,objs,file="skin"):
        objs=pm.ls(objs)
        packPath=os.path.join(path,file+".gSkinPack")
        skin.exportJsonSkinPack(packPath=packPath,objs=objs)

    def objSence_check_string(self,objName):
        if cmds.objExists(objName):
            return objName
        else:
            cmds.error("There is no name for the group "+"'"+objName+"'")

def main():
    _GE = GroupExport()
    test=_GE.grpNodeChoise_query_list("Geo_Grp",["Geo"])
    print(test)