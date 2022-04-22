import maya.cmds as cmds

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

    def objsSkin_export_list(self,path,objs):
        pass

    def objsSkinPack_export_list(self,path,objs,file="skin"):
        pass

    def objSence_check_string(self,objName):
        if cmds.objExists(objName):
            return objName
        else:
            cmds.error("There is no name for the group "+"'"+objName+"'")

def main():
    _GE = GroupExport()
    test=_GE.grpNodeChoise_query_list("Geo_Grp",["Geo"])
    print(test)