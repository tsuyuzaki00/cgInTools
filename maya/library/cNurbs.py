# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2
from cgInTools.maya.library import cleanLB as cc

class QuadPosSurface():
    def __init__(self):
        self.locatorsFour=["","","",""]
        self.name=""

    def setName(self,variable):
        self.name=variable
        return self.name

    def setLoctorsFour(self,variable):
        self.locatorsFour=variable
        self.loctorPos_update()
        return self.locatorsFour

    def create(self):
        plane=cmds.nurbsPlane(n=self.name,u=2,v=2)[0]
        cmds.delete(plane,ch=True)
        self.name=plane
        for edit in self.edits:
            surf=self.editNurbsSurface_edit_mFnNurbsSurface(plane,edit["cv"],edit["mVector"])
        return surf

    def update(self):
        self.loctorPos_update()
        for edit in self.edits:
            surf=self.editNurbsSurface_edit_mFnNurbsSurface(self.name,edit["cv"],edit["mVector"])
        return surf

    def loctorPos_update(self):
        cv00=self.getPos_create_MVector(self.locatorsFour[0])
        cv04=self.getPos_create_MVector(self.locatorsFour[1])
        cv44=self.getPos_create_MVector(self.locatorsFour[2])
        cv40=self.getPos_create_MVector(self.locatorsFour[3])
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

        self.edits=[
            {"cv":(0,0),"mVector":cv00},
            {"cv":(0,4),"mVector":cv04},
            {"cv":(4,0),"mVector":cv40},
            {"cv":(4,4),"mVector":cv44},
            {"cv":(2,2),"mVector":cv22},
            {"cv":(0,2),"mVector":cv02},
            {"cv":(2,0),"mVector":cv20},
            {"cv":(4,2),"mVector":cv42},
            {"cv":(2,4),"mVector":cv24},
            {"cv":(0,1),"mVector":cv01},
            {"cv":(0,3),"mVector":cv03},
            {"cv":(1,0),"mVector":cv10},
            {"cv":(3,0),"mVector":cv30},
            {"cv":(4,1),"mVector":cv41},
            {"cv":(4,3),"mVector":cv43},
            {"cv":(1,4),"mVector":cv14},
            {"cv":(3,4),"mVector":cv34},
            {"cv":(3,2),"mVector":cv32},
            {"cv":(1,2),"mVector":cv12},
            {"cv":(2,1),"mVector":cv21},
            {"cv":(2,3),"mVector":cv23},
            {"cv":(1,1),"mVector":cv11},
            {"cv":(1,3),"mVector":cv13},
            {"cv":(3,1),"mVector":cv31},
            {"cv":(3,3),"mVector":cv33},
        ]

    def getPos_create_MVector(self,obj):
        pointNode_mSelectionList=om2.MSelectionList().add(obj)
        pointNode_mDagPath=pointNode_mSelectionList.getDagPath(0)
        point_mVector=om2.MFnTransform(pointNode_mDagPath).translation(om2.MSpace.kWorld)
        return point_mVector

    def objsInSurface_create_mFnNurbsSurface(self,objs=[]):
        createPointArrays=om2.MFloatPointArray()
        for obj in objs:
            mVector=self.getPos_create_MVector(obj)
            mPoint=om2.MPoint(mVector)
            createPointArrays.append(mPoint)
        nurbsSurface_mFnNurbsSurface=om2.MFnNurbsSurface()
        nurbsSurface_mFnNurbsSurface.create(createPointArrays,[0.0,1.0],[0.0,1.0],1,1,1,1,True)
        cc.defaultMaterial_edit_func(nurbsSurface_mFnNurbsSurface.name())

    def editNurbsSurface_edit_mFnNurbsSurface(self,surface,cvs=(0,0),pos=(0,0,0,0)):
        mPoint=om2.MPoint(pos)
        surface_mSelectionList=om2.MSelectionList().add(surface)
        surface_mDagPath=surface_mSelectionList.getDagPath(0)
        surface_mDagPath.extendToShape()
        surface_mObject=surface_mDagPath.node()
        nurbsSurface_mFnNurbsSurface=om2.MFnNurbsSurface()
        nurbsSurface_mFnNurbsSurface.setObject(surface_mObject)
        nurbsSurface_mFnNurbsSurface.setCVPosition(cvs[0],cvs[1],mPoint)
        nurbsSurface_mFnNurbsSurface.updateSurface()
        return nurbsSurface_mFnNurbsSurface
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

    def create(self):
        if self.format is 0:
            polygon=cmds.nurbsToPoly(self.obj,
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
            polygon=cmds.nurbsToPoly(self.obj,
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
            polygon=cmds.nurbsToPoly(self.obj,
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
            polygon=cmds.nurbsToPoly(self.obj,
                ch=self.constructionHistory,
                n=self.name,
                mrt=self.matchRender,
                f=self.format,
                pt=self.polyType,
                mnd=self.matchNormalDir,
                ntr=self.normalizeTrimmedUVRange,
                uss=True)
        return polygon[0]
class NurbsMirror():
    def __init__(self):
        self.surfaceLeft=""
        self.surfaceRight=""
        self.surfaceCecter=""
        self.nameJadges=[]

    def setNameJadges(self,):
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
