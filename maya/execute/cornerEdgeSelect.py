import pymel.core as pm
import maya.cmds as cmds

def cornerEdge_select_func(lowAngle=30,highAngle=150):
    sels = cmds.ls(sl=True)
    for sel in sels:
        selEdge_int = cmds.polyEvaluate(e=True)
        edgeNum_int = selEdge_int-1
        cmds.select(sel+".e[0:"+str(edgeNum_int)+"]",add=True)
        cmds.polySelectConstraint(a=1,m=3,t=0x8000,ab=(lowAngle,highAngle))
        cmds.polySelectConstraint(m=0)


def main():
    cornerEdge_select_func()