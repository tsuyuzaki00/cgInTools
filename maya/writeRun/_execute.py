# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

import cgInTools as cit
#from cgInTools.maya.library import _testPath as TP
#from cgInTools.maya.manager import equipmentSettingsMN as MN
#from cgInTools.maya.option import autoRenameOP as OP
#from cgInTools.maya.library import objectLB as oLB
from cgInTools.maya.library import meshLB as mLB
from cgInTools.maya.library import pointLB as pLB
#from cgInTools.maya.execute import exportAnimPackEX as EX
cit.reloads([mLB,pLB])

def main():
    #OP.main()
    #MN.main()
    #EX.main()
    #TP.main()

    MPoint0=pLB.Point([-5,-5,-5])
    MPoint0.setID(0)
    MPoint1=pLB.Point([5,-5,-5])
    MPoint1.setID(1)
    MPoint2=pLB.Point([5,5,-5])
    MPoint2.setID(2)
    MPoint3=pLB.Point([-5,5,-5])
    MPoint3.setID(3)
    MPoint4=pLB.Point([-5,-5,5])
    MPoint4.setID(4)
    MPoint5=pLB.Point([5,-5,5])
    MPoint5.setID(5)
    MPoint6=pLB.Point([5,5,5])
    MPoint6.setID(6)
    MPoint7=pLB.Point([-5,5,5])
    MPoint7.setID(7)

    createPolygons=[
        [MPoint3,MPoint2,MPoint1,MPoint0],
        [MPoint2,MPoint6,MPoint5,MPoint1],
        [MPoint5,MPoint6,MPoint7,MPoint4],
        [MPoint7,MPoint3,MPoint0,MPoint4],
        #[MPoint0,MPoint1,MPoint5,MPoint4],
        #[MPoint2,MPoint3,MPoint7,MPoint6],
    ]

    cube=mLB.Polygon()
    cube.setName("pCube")
    cube.setPolygons(createPolygons)
    #print(cube.polygonCount_query_ints(createPolygons))
    #print(cube.pointID_query_ints(createPolygons))
    #print(cube.allVertex_query_MPoints(createPolygons))
    cube.create()

    cmds.select(cube.getName())
    cmds.hyperShade(a='standardSurface1')

main()