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

class NurbsToPoly():
    """
    ch bool constructionHistory
    n string name
    
    mrt bool matchRenderTessellation
    
    pt int
    0:"Triangles"
    1:"Quads"

    f int
    0:"Count"
    1:"Standard fit"
    2:"General"
    3:"Control point"

    ut int [General] U Type
    1:Per surf # of iso params in 3D
    2:Per surf # of iso params
    3:Per span # of iso params
    un int [General] Number U
    
    vt int [General] V Type
    1:Per surf # of iso params in 3D
    2:Per surf # of iso params
    3:Per span # of iso params
    vn int [General] Number V
    
    uch bool [General] Use chord height
    cht float [General] Chord height
    ucr bool [General] Use chord height ratio
    chr float [General][Standard fit] Chord height ratio
    es bool [General] Edge swap
    
    ft float [Standard fit] Fractional tolerance
    mel float [Standard fit] Minimal edge length
    d float [Standard fit] 3D delta
    
    pc int [Count] Count

    ? mnd bool
    ? ntr bool
    ? uss bool
    """
    def __init__(self):
        self.obj="nurbsPlane1"
        self.constructionHistory=False
        self.name=self.obj
        self.format=2
        self.polyType=1
        self.uType=1
        self.uNumber=5
        self.vType=1
        self.vNumber=5
        self.useChordHeigh=False
        self.chordHeight=0.2
        self.useChordHeighRatio=False
        self.chordHeighRatio=0.1
        self.edgeSwap=False
        self.fraction=0.01
        self.minEdgeLen=0.001
        self.delta3D=0.1
        self.count=200

    def run(self):
        cmds.nurbsToPoly(self.obj,
        ch=True,
        n=self.name,
        pt=self.polyType,
        f=self.format,
        ut=self.uType,
        un=self.uNumber,
        vt=self.vType,
        vn=self.vNumber,
        uch=self.useChordHeigh,
        cht=self.chordHeight,
        ucr=self.useChordHeighRatio,
        chr=self.chordHeighRatio,
        es=self.edgeSwap,
        ft=self.fraction,
        mel=self.minEdgeLen,
        d=self.delta3D,
        pc=self.count,
        mnd=True,
        mrt=False,
        ntr=False,
        uss=True)
