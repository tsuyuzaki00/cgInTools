# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import maya.api.OpenMayaAnim as oma2
from cgInTools.maya.library import cleanLB as cLB
import math

def test():
    name="surface"
    control_vertices = [(-0.5,0.0,-0.5),(0.5,0.0,-0.5),(-0.5,0.0,0.5),(0.5,0.0,0.5)]
    surface_MObject=om2.MFnDagNode().create("transform",name)
    surface_MFnNurbsSurface=om2.MFnNurbsSurface()
    surface_MFnNurbsSurface.create(control_vertices,[0.0,1.0],[0.0,1.0],1,1,1,1,False,surface_MObject)
    surface_MFnDependencyNode=om2.MFnDependencyNode(surface_MObject)
    object_str=surface_MFnDependencyNode.name()
    cLB.defaultMaterial_edit_func(object_str)

    surface_MFnDagNode=om2.MFnDagNode(surface_MObject)
    surface_MDagPath=surface_MFnDagNode.getPath()
    surface_MDagPath.extendToShape()
    surface_MFnDagNode=om2.MFnDagNode(surface_MDagPath)
    surface_MPlug=surface_MFnDagNode.findPlug("create",False)

    makeNurb_MDGModifier=om2.MDGModifier()
    makeNurb_MObject=makeNurb_MDGModifier.createNode("makeNurbPlane")
    makeNurb_MDGModifier.doIt()

    makeNurb_MFnDependencyNode=om2.MFnDependencyNode(makeNurb_MObject)
    makeNurb_MPlug=makeNurb_MFnDependencyNode.findPlug("outputSurface",False)
    
    connect_MDGModifier=om2.MDGModifier()
    connect_MDGModifier.connect(makeNurb_MPlug,surface_MPlug)
    connect_MDGModifier.doIt()

def main():
    test()
main()