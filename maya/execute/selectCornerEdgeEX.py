# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import cgInTools as cit
from cgInTools.maya.library import cJson as cj

def cornerEdge_query_func(obj,lowAngle=30,highAngle=150):
    selEdge_int=cmds.polyEvaluate(e=True)
    edgeNum_int=selEdge_int-1
    cmds.select(obj+".e[0:"+str(edgeNum_int)+"]",add=True)
    cmds.polySelectConstraint(a=1,m=3,t=0x8000,ab=(lowAngle,highAngle))
    cmds.polySelectConstraint(m=0)
    edges=cmds.ls(sl=True)
    return edges

def main():
    data_file=cj.pathSetting_create_str(cit.mayaData_path,"selectCornerEdge")
    data_dict=cj.readJson_quary_dict(data_file)
    
    objs = cmds.ls(sl=True)
    for obj in objs:
        cornerEdge_query_func(obj,data_dict["lowAngle"],data_dict["highAngle"])

main()