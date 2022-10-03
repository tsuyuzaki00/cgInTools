# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

createPlane=[]
point_lists=[(1,1,0,1),(-1,1,0,1),(1,-1,0,1),(-1,-1,0,1)]
for point in point_lists:
    append_MFloatPoint=om2.MFloatPoint(point[0],point[1],point[2],point[3])
    createPlane.append(append_MFloatPoint)


create=om2.MFloatPointArray()
create.append((-1,1,0,1))
create.append((1,1,0,1))
create.append((-1,-1,0,1))
create.append((1,-1,0,1))
nurbsSurface_MObject=om2.MFnNurbsSurface().create(create,[0.0,1.0],[0.0,1.0],1,1,1,1,False)
nurbPlane_MObject=om2.MFnDependencyNode().create("makeNurbPlane")

surface_MDagPath = om2.MDagPath()
surface_MDagPath.extendToShape()

source_MFnDependencyNode=om2.MFnDependencyNode(surface_MDagPath.node())
target_MFnDependencyNode=om2.MFnDependencyNode(nurbPlane_MObject)

source_MPlug=source_MFnDependencyNode.findPlug("outputSurface",False)
target_MPlug=target_MFnDependencyNode.findPlug("create",False)

#"outputSurface","create"
om2.MDGModifier.connect(source_MPlug,target_MPlug)
