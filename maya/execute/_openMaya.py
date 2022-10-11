# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

def mirrorAxis_query_tuple(mirrorX=True,mirrorY=False,mirrorZ=False):
    mirror_list=[1,1,1]
    if mirrorX:
        mirror_list[0]=-1
    if mirrorY:
        mirror_list[1]=-1
    if mirrorZ:
        mirror_list[2]=-1
    return tuple(mirror_list)

def getNodeMatrix_query_mMatrix(node):
    node_mSelectionList=om2.MSelectionList().add(node)
    node_mDagPath=node_mSelectionList.getDagPath(0)
    node_mMatrix=node_mDagPath.inclusiveMatrix()
    return node_mMatrix

def translateMirror_edit_func(sourceNode,targetNode,mirrorX=True,mirrorY=False,mirrorZ=False):
    mirror=mirrorAxis_query_tuple(mirrorX,mirrorY,mirrorZ)
    sourceNode_mMatrix=getNodeMatrix_query_mMatrix(sourceNode)
    trans_mTransformationMatrix = om2.MTransformationMatrix(sourceNode_mMatrix)
    trans_mVector=trans_mTransformationMatrix.translation(om2.MSpace.kWorld)
    cmds.xform(targetNode,ws=True,t=(trans_mVector[0]*mirror[0],trans_mVector[1]*mirror[1],trans_mVector[2]*mirror[2]))
    
def rotateMirror_edit_func(sourceNode,targetNode,mirrorX=True,mirrorY=False,mirrorZ=False):
    mirror=mirrorAxis_query_tuple(mirrorX,mirrorY,mirrorZ)
    sourceNode_mMatrix=getNodeMatrix_query_mMatrix(sourceNode)
    mirror_mMatrix=om2.MMatrix((mirror[0],0,0,0, 0,mirror[1],0,0, 0,0,mirror[2],0, 0,0,0,1))
    mirror_mMatrix=sourceNode_mMatrix*mirror_mMatrix
    cmds.xform(targetNode,m=mirror_mMatrix)

def bendRollMirror_edit_func(sourceNode,targetNode,mirrorX=True,mirrorY=False,mirrorZ=False):
    mirror=mirrorAxis_query_tuple(mirrorX,mirrorY,mirrorZ)
    sourceNode_mMatrix=getNodeMatrix_query_mMatrix(sourceNode)
    aimVector_mMatrix=om2.MMatrix((1,0,0,0, 0,1,0,0, 0,0,1,0, 1,0,0,1))
    upVector_mMatrix=om2.MMatrix((1,0,0,0, 0,1,0,0, 0,0,1,0, 0,1,0,1))
    aimVector_mMatrix=sourceNode_mMatrix*aimVector_mMatrix
    upVector_mMatrix=sourceNode_mMatrix*upVector_mMatrix

    mirror_mMatrix=()
    cmds.xform(targetNode,m=mirror_mMatrix)


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

def pointMirror_edit_func(sourcePoint,targetPoint,mirrorX=True,mirrorY=False,mirrorZ=False):
    mirror=mirrorAxis_query_tuple(mirrorX,mirrorY,mirrorZ)
    values=cmds.getAttr(sourcePoint)[0]
    cmds.setAttr(targetPoint+".xValue",values[0]*mirror[0])
    cmds.setAttr(targetPoint+".yValue",values[1]*mirror[1])
    cmds.setAttr(targetPoint+".zValue",values[2]*mirror[2])

def main():
    source="C_model_geo_test_01"
    target="C_model_geo_test_03"
    #getSurfacePoint_query_mPoint(source)
    #print(getNodeMatrix_query_mMatrix(source))
    #print(getNodeMatrix_query_mMatrix(target))

    #rotateMirror_edit_func(source,target,mirrorX=False,mirrorY=False,mirrorZ=False)
    translateMirror_edit_func(source,target,mirrorX=True,mirrorY=False,mirrorZ=True)

main()