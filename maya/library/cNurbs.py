# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

class CreateNurbs():
    def __init__():
        pass

def main():
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
    
    mrt bool Match render tessellation
    
    pt int
    0:"Triangles"
    1:"Quads"

    f int
    0:"Count"
    1:"Standard fit"
    2:"General"
    3:"Control point"
    
    mnd bool Match Normal Dir
    ntr bool Normalize Trimmed UVRange

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

    ? uss bool
    --example--
    cmds.nurbsToPoly(self.obj,
        ch=self.constructionHistory,
        n=self.name,
        mrt=self.matchRender,
        f=self.format,
        pt=self.polyType,
        mnd=self.matchNormalDir,
        ntr=self.normalizeTrimmedUVRange,
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
        uss=True)
    """
    def __init__(self):
        self.obj="nurbsPlane1"
        self.constructionHistory=False
        self.name=self.obj+"_geo"
        self.matchRender=False
        self.polyType=1
        self.format=2
        self.matchNormalDir=True
        self.normalizeTrimmedUVRange=False
        self.uType=1
        self.uNumber=5
        self.vType=1
        self.vNumber=5
        self.useChordHeight=False
        self.chordHeight=0.2
        self.useChordHeightRatio=False
        self.chordHeightRatio=0.1
        self.edgeSwap=False
        self.fraction=0.01
        self.minEdgeLen=0.001
        self.delta3D=0.1
        self.count=200

    def setObj(self,variable):
        self.obj=variable
        return self.obj
    def setHistory(self,variable):
        self.constructionHistory=variable
        return self.constructionHistory
    def setName(self,variable):
        self.name=variable
        return self.name
    def setMR(self,variable):
        self.matchRender=variable
        return self.matchRender
    def setPolyType(self,variable):
        if variable is 0 or variable is "triangles":
            self.polyType=0
            return self.polyType
        elif variable is 1 or variable is "quads":
            self.polyType=1
            return self.polyType
    def setFormat(self,variable):
        if variable is 0 or variable is "count":
            self.format=0
            return self.format
        elif variable is 1 or variable is "standardFit":
            self.format=1
            return self.format
        elif variable is 2 or variable is "general":
            self.format=2
            return self.format
        elif variable is 3 or variable is "controlPoint":
            self.format=3
            return self.format
        else:
            cmds.error("setFormat to a number between 0~3")
    def setMND(self,variable):
        self.matchNormalDir=variable
        return self.matchNormalDir
    def setNTR(self,variable):
        self.normalizeTrimmedUVRange=variable
        return self.normalizeTrimmedUVRange
    def setUType(self,variable):
        self.uType=variable
        return self.uType
    def setUNumber(self,variable):
        self.uNumber=variable
        return self.uNumber
    def setVType(self,variable):
        self.vType=variable
        return self.vType
    def setVNumber(self,variable):
        self.vNumber=variable
        return self.vNumber
    def setUCH(self,variable):
        self.useChordHeight=variable
        return self.useChordHeight
    def setCH(self,variable):
        self.chordHeight=variable
        return self.chordHeight
    def setUCHR(self,variable):
        self.useChordHeightRatio=variable
        return self.useChordHeightRatio
    def setCHR(self,variable):
        self.chordHeightRatio=variable
        return self.chordHeightRatio
    def setES(self,variable):
        self.edgeSwap=variable
        return self.edgeSwap
    def setF(self,variable):
        self.fraction=variable
        return self.fraction
    def setMEL(self,variable):
        self.minEdgeLen=variable
        return self.minEdgeLen
    def setD3D(self,variable):
        self.delta3D=variable
        return self.delta3D
    def setC(self,variable):
        self.count=variable
        return self.count

    def run(self):
        if self.format is 0:
            cmds.nurbsToPoly(self.obj,
                ch=self.constructionHistory,
                n=self.name,
                mrt=self.matchRender,
                f=self.format,
                pt=self.polyType,
                mnd=self.matchNormalDir,
                ntr=self.normalizeTrimmedUVRange,
                pc=self.count,
                uss=True)
        elif self.format is 1:
            cmds.nurbsToPoly(self.obj,
                ch=self.constructionHistory,
                n=self.name,
                mrt=self.matchRender,
                f=self.format,
                pt=self.polyType,
                mnd=self.matchNormalDir,
                ntr=self.normalizeTrimmedUVRange,
                ft=self.fraction,
                chr=self.chordHeightRatio,
                mel=self.minEdgeLen,
                d=self.delta3D,
                uss=True)
        elif self.format is 2:
            cmds.nurbsToPoly(self.obj,
                ch=self.constructionHistory,
                n=self.name,
                mrt=self.matchRender,
                f=self.format,
                pt=self.polyType,
                mnd=self.matchNormalDir,
                ntr=self.normalizeTrimmedUVRange,
                ut=self.uType,
                un=self.uNumber,
                vt=self.vType,
                vn=self.vNumber,
                uch=self.useChordHeight,
                cht=self.chordHeight,
                ucr=self.useChordHeightRatio,
                chr=self.chordHeightRatio,
                es=self.edgeSwap,
                uss=True)
        elif self.format is 3:
            cmds.nurbsToPoly(self.obj,
                ch=self.constructionHistory,
                n=self.name,
                mrt=self.matchRender,
                f=self.format,
                pt=self.polyType,
                mnd=self.matchNormalDir,
                ntr=self.normalizeTrimmedUVRange,
                uss=True)

class NurbsMirror():
    def __init__(self):
        self.surfaceLeft=""
        self.surfaceRight=""
        self.surfaceCecter=""
        self.nameJadges=[]

    def setNameJadges(self,):
        pass