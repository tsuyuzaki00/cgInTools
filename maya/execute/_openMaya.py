# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2
from cgInTools.maya.library import cClean as cc
import math

def mirrorAxis_query_tuple(self,mirrorX=True,mirrorY=False,mirrorZ=False):
        mirror_list=[1,1,1]
        if mirrorX:
            mirror_list[0]=-1
        if mirrorY:
            mirror_list[1]=-1
        if mirrorZ:
            mirror_list[2]=-1
        return tuple(mirror_list)

def pointMirror_edit_func(sourcePoint,targetPoint,mirrorX=True,mirrorY=False,mirrorZ=False):
    mirror=mirrorAxis_query_tuple(mirrorX,mirrorY,mirrorZ)
    values=cmds.getAttr(sourcePoint)[0]
    cmds.setAttr(targetPoint+".xValue",values[0]*mirror[0])
    cmds.setAttr(targetPoint+".yValue",values[1]*mirror[1])
    cmds.setAttr(targetPoint+".zValue",values[2]*mirror[2])

def getSurfacePoint_query_mPoint(node):
    node_mSelectionList=om2.MSelectionList().add(node)
    node_mObject=node_mSelectionList.getDependNode(0)

    attrFn = om2.MFnAttribute(node_mObject)
    node_mPlug=node_mSelectionList.getPlug(0)
    attrFn = om2.MFnAttribute(node_mPlug)
    print(attrFn.name)
    #node_mDagPath=node_mSelectionList.getDagPath(0)
    #surf_mFnNurbsSurface=om2.MFnNurbsSurface(node_mDagPath)
    #print(surf_mFnNurbsSurface)
    """
    node_mDagPath.extendToShape()# chenge shapes 
    shapes_mObject=node_mDagPath.node()
    shapes_mFnDependencyNode=om2.MFnDependencyNode(shapes_mObject)

    shape_mPlug = shapes_mFnDependencyNode.findPlug("outMesh", False)
    shape_mObject = shape_mPlug.asMObject()
    shape_mFnMesh = om2.MFnMesh(shape_mObject)
 
    print('num of polygons:',shape_mFnMesh.numPolygons)

    surf_mFnNurbsSurface.add
    """


def main():
    pass
    
main()