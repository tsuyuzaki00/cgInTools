import maya.cmds as cmds
import maya.mel as mel

class KARI():
    def holes_check_dict(self,node):
        evaluation_dict={"bool":False,"node":node,"hole":[]}
        holes=mel.eval('polyCleanupArgList 4 { "0","2","1","0","0","0","1","0","0","1e-05","0","1e-05","0","1e-05","0","-1","0","0" };')
        if holes == []:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else:
            evaluation_dict["bool"]=False
            for hole in holes:
                evaluation_dict["hole"].append(hole)
            return evaluation_dict

def main():
    objs=cmds.ls(sl=True)
    run=KARI()
    for obj in objs:
        print(run.holes_check_dict(obj))

main()