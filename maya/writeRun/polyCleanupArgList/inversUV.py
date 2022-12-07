import maya.cmds as cmds
import maya.mel as mel

class KARI():
    def inversUV_check_dict(self,node):
        evaluation_dict={"bool":False,"node":node,"invers":[]}
        cmds.hilite(node)
        invers=mel.eval('selectUVFaceOrientationComponents {} 1 2 1')
        if invers_list == []:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else:
            evaluation_dict["bool"]=False
            for invers in invers_list:
                evaluation_dict["invers"].append(invers)
            return evaluation_dict
            
def main():
    objs=cmds.ls(sl=True)
    run=KARI()
    for obj in objs:
        print(run.inversUV_check_dict(obj))

main()