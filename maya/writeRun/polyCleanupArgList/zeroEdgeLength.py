import maya.cmds as cmds
import maya.mel as mel

class KARI():
    def zeroEdgeLength_check_dict(self,node):
        evaluation_dict={"bool":False,"node":node,"zeroEdgeLength":[]}
        zeroEdgeLengths=mel.eval('polyCleanupArgList 4 { "0","2","0","0","0","0","0","0","0","1e-005","1","1e-005","0","1e-005","0","-1","0" };')
        if zeroEdgeLengths == []:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else:
            evaluation_dict["bool"]=False
            for zeroEdgeLength in zeroEdgeLengths:
                evaluation_dict["zeroEdgeLength"].append(zeroEdgeLength)
            return evaluation_dict
            
def main():
    objs=cmds.ls(sl=True)
    run=KARI()
    for obj in objs:
        print(run.zeroEdgeLength_check_dict(obj))

main()