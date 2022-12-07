import maya.cmds as cmds
import maya.mel as mel

class KARI():
    def nonConcave_check_dict(self,node):
        evaluation_dict={"bool":False,"node":node,"concave":[]}
        concaves=mel.eval('polyCleanupArgList 4 { "0","2","1","0","1","1","0","0","0","1e-05","0","1e-05","0","1e-05","0","-1","0","0" };')
        if concaves == []:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else:
            evaluation_dict["bool"]=False
            for concave in concaves:
                evaluation_dict["concave"].append(concave)
            return evaluation_dict
 
def main():
    objs=cmds.ls(sl=True)
    run=KARI()
    for obj in objs:
        print(run.concaveCheck(obj))

main()