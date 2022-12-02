# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import cgInTools as cit
from ..library import jsonLB as cj

def cornerEdge_query_func(obj,lowAngle=30,highAngle=165):
    selEdge_int=cmds.polyEvaluate(e=True)
    edgeNum_int=selEdge_int-1
    cmds.select(obj+".e[0:"+str(edgeNum_int)+"]",add=True)
    cmds.polySelectConstraint(a=1,m=3,t=0x8000,ab=(lowAngle,highAngle))
    cmds.polySelectConstraint(m=0)
    edges=cmds.ls(sl=True,fl=True)
    return edges

def main():
    setting=cj.Json()
    setting.setPath(cit.mayaData_path)
    setting.setFile("geometryCornerEdge")
    data_dict=setting.read()
    
    objs = cmds.ls(sl=True,o=True)
    for obj in objs:
        cornerEdge_query_func(obj,data_dict["lowAngle"],data_dict["highAngle"])