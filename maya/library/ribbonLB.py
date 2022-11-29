# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.mel as mel

import cgInTools as cit
from cgInTools.maya.library import setBaseLB as sbLB
cit.reloads([sbLB])

class RibbonTwist():
    def __init__(self):
        self._twoObjects=["",""]
        self._name=""
        self._joint=5

    def __loading(self):
        self._value=""

#Public Function
    def public(self):
        print(self._value)
        pass

#Private Function
    def _private_mode_func(self):
        print(self._value)
        self.multi_mode_func()
        pass

#Multi Function
    def multi_mode_func(self):
        pass

#Single Function
    def nurbsPlane_create_func(self,joint,name,twoObjects=["",""]):
        width=5
        split=joint-1
        cmds.nurbsPlane(ax=[0,1,0],d=1,w=width,u=split,v=1,lr=0.1,ch=False,n=name+"_nurb")
        mel.eval('string $Ucount = "%s";' % 5)
        #createHair(name Ucount,Vcount,PointPerHair,CreateRestCurves,PassiveFill,EdgeBounded,Equalize,Length,Randomization,Output,Dynamic||Static,PlaceHairsInto)
        mel.eval('createHair $Ucount 1 10 0 0 1 0 5 0 2 1 1')
        hairGrp_obj=cmds.rename("hairSystem1Follicles",name+"_grp")
        cmds.delete("nucleus1","hairSystem1OutputCurves","hairSystem1")
        follicle_shapes=cmds.listRelatives(hairGrp_obj,ad=True,typ="follicle")
        follicles=cmds.ls(cmds.listRelatives(follicle_shapes,parent=True))
        for follicle in follicles:
            delTrs=cmds.listRelatives(follicle,typ="transform")
            cmds.delete(delTrs)
            joint=cmds.joint(r=True,rad=0.1,n=follicle+"_jnt")
            cmds.parent(joint,follicle)
            cmds.move(0,0,0,ls=True)
            cmds.select(cl=True)

class RibbonFollow():
    def __init__(self):
        self._objects=[]
        self._name=""

    def __loading(self):
        self._value=""

#Public Function
    def public(self):
        print(self._value)
        pass

#Private Function
    def _private_mode_func(self):
        print(self._value)
        self.multi_mode_func()
        self.single_mode_func()
        pass

#Multi Function
    def multi_mode_func(self):
        self.single_mode_func()
        pass

#Single Function
    def single_mode_func(self):
        pass