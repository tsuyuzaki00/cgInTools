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


def createNurbsSurface(objs=[]):
    createPointArrays=om2.MFloatPointArray()
    for obj in objs:
        mVector=getPos_create_MVector(obj)
        mPoint=om2.MPoint(mVector)
        createPointArrays.append(mPoint)
    nurbsSurface_mFnNurbsSurface=om2.MFnNurbsSurface()
    nurbsSurface_mFnNurbsSurface.create(createPointArrays,[0.0,1.0],[0.0,1.0],1,1,1,1,True)
    cc.defaultMaterial_edit_func(nurbsSurface_mFnNurbsSurface.name())

def editNurbsSurface(surface,cvs=(0,0),pos=(0,0,0,0)):
    mPoint=om2.MPoint(pos)
    surface_mSelectionList=om2.MSelectionList().add(surface)
    surface_mDagPath=surface_mSelectionList.getDagPath(0)
    surface_mDagPath.extendToShape()
    surface_mObject=surface_mDagPath.node()
    nurbsSurface_mFnNurbsSurface=om2.MFnNurbsSurface()
    nurbsSurface_mFnNurbsSurface.setObject(surface_mObject)
    nurbsSurface_mFnNurbsSurface.setCVPosition(cvs[0],cvs[1],mPoint)

def main():
    cv00=getPos_create_MVector("locator1")
    cv04=getPos_create_MVector("locator2")
    cv40=getPos_create_MVector("locator3")
    cv44=getPos_create_MVector("locator4")
    cv22=(cv00+cv04+cv40+cv44)*0.5*0.5
    cv02=(cv00+cv04)*0.5
    cv20=(cv00+cv40)*0.5
    cv42=(cv40+cv44)*0.5
    cv24=(cv04+cv44)*0.5
    cv01=(cv00+cv02)*0.5
    cv03=(cv02+cv04)*0.5
    cv10=(cv00+cv20)*0.5
    cv30=(cv20+cv40)*0.5
    cv41=(cv40+cv42)*0.5
    cv43=(cv42+cv44)*0.5
    cv14=(cv04+cv24)*0.5
    cv34=(cv24+cv44)*0.5
    cv32=(cv42+cv22)*0.5
    cv12=(cv02+cv22)*0.5
    cv21=(cv20+cv22)*0.5
    cv23=(cv24+cv22)*0.5
    cv11=(cv00+cv22)*0.5
    cv13=(cv04+cv22)*0.5
    cv31=(cv40+cv22)*0.5
    cv33=(cv44+cv22)*0.5

    plane="nurbsPlane2"
    edits=[
        [plane,(0,0),cv00],
        [plane,(0,4),cv04],
        [plane,(4,0),cv40],
        [plane,(4,4),cv44],
        [plane,(2,2),cv22],
        [plane,(0,2),cv02],
        [plane,(2,0),cv20],
        [plane,(4,2),cv42],
        [plane,(2,4),cv24],
        [plane,(0,1),cv01],
        [plane,(0,3),cv03],
        [plane,(1,0),cv10],
        [plane,(3,0),cv30],
        [plane,(4,1),cv41],
        [plane,(4,3),cv43],
        [plane,(1,4),cv14],
        [plane,(3,4),cv34],
        [plane,(3,2),cv32],
        [plane,(1,2),cv12],
        [plane,(2,1),cv21],
        [plane,(2,3),cv23],
        [plane,(1,1),cv11],
        [plane,(1,3),cv13],
        [plane,(3,1),cv31],
        [plane,(3,3),cv33],
    ]
    for edit in edits:
        mPoint=om2.MPoint(edit[2])
        editNurbsSurface(edit[0],edit[1],mPoint)


    
main()