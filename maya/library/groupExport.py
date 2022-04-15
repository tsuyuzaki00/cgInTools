import maya.cmds as cmds

class GroupExport():
    def grpNodeChoise_query_list(self,name):
        choiseNodes=[]
        grpNodes=cmds.ls(name,dag=True,typ="transform")
        grpNodes.remove(name)
        nodeOnly_name=name.replace("_grp","")
        for node in grpNodes:
            if nodeOnly_name in node:
                choiseNodes.append(node)
        return choiseNodes

    def geometryClean_create_obj(self,):
        pass

    def selectModelExport_export_list(self,path,objs,file="model"):
        pass

    def selectSkinExport_export_list(self,path,objs,file="skin"):
        pass

def main():
    _GE = GroupExport()
    _GE.grpNodeChoise_query_list("cage_grp")