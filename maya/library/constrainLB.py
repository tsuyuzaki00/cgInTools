# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from cgInTools.maya.library import setBaseLB as sbLB
from cgInTools.maya.library import namingLB as nLB
cit.reloads([sbLB,nLB])

class Constrain(sbLB.BasePair):
    def __init__(self):
        self._sourceNode="" # string
        self._targetNode="" # string
        self._thirdNode="" # string

    def __loading(self):
        pass

#Public Function
    def parentConstraint(self):
        constraint=cmds.parentConstraint(self._sourceNode,self._targetNode,mo=True,w=1)
        cmds.rename(constraint,"test_constraint")
        print(constraint)

    def pointConstraint(self):
        constraint=cmds.pointConstraint(self._sourceNode,self._targetNode,mo=True,w=1)
        cmds.rename(constraint,"test_constraint")
        print(constraint)

    def orientConstraint(self):
        constraint=cmds.orientConstraint(self._sourceNode,self._targetNode,mo=True,w=1)
        cmds.rename(constraint,"test_constraint")
        print(constraint)

    def scaleConstraint(self):
        constraint=cmds.scaleConstraint(self._sourceNode,self._targetNode,mo=True,w=1)
        cmds.rename(constraint,"test_constraint")
        print(constraint)

    def aimConstraint(self):
        constraint=cmds.aimConstraint(self._sourceNode,self._targetNode,mo=True,w=1)
        cmds.rename(constraint,"test_constraint")
        print(constraint)

    def ikHandleConstraint(self):
        ikHandles=cmds.ikHandle(sj=self._sourceNode,ee=self._targetNode,p=2)
        ikHandle=cmds.rename(ikHandles[0],"test_handle")
        effector=cmds.rename(ikHandles[1],"test_effector")
        constraint=cmds.poleVectorConstraint(self._thirdNode,ikHandle,w=1)
        cmds.rename(constraint,"test_constraint")
        print(constraint)

    def aimConstraint(self):
        self.matrixConnect_create_func(self._sourceNode,self._targetNode)
    
    def aimConstraint(self):
        self.matrixParent_create_func(self._sourceNode,self._targetNode)

#Single Function
    def matrixConnect_create_func(self,sourceObj,targetObj):
        multMatrixName=sourceObj+"_mumx"
        decomposeMatrixName=sourceObj+"_demx"

        __createNode_dict={}
        __createNodes=[
            {"tag":"mumx","node":"multMatrix","name":multMatrixName},
            {"tag":"demx","node":"decomposeMatrix","name":decomposeMatrixName}
            ]
        for __createNode in __createNodes:
            node=cmds.createNode(__createNode["node"])
            rename=cmds.rename(node,__createNode["name"])
            __createNode_dict[__createNode["tag"]]=rename

        __connectNode_dicts=[
            {"sourceNode":sourceObj,"sourceAttr":"matrix","targetNode":__createNode_dict["mumx"],"targetAttr":"matrixIn[0]"},
            {"sourceNode":sourceObj,"sourceAttr":"parentMatrix","targetNode":__createNode_dict["mumx"],"targetAttr":"matrixIn[1]"},
            {"sourceNode":targetObj,"sourceAttr":"parentInverseMatrix","targetNode":__createNode_dict["mumx"],"targetAttr":"matrixIn[2]"},
            {"sourceNode":__createNode_dict["mumx"],"sourceAttr":"matrixSum","targetNode":__createNode_dict["demx"],"targetAttr":"inputMatrix"},
            {"sourceNode":__createNode_dict["demx"],"sourceAttr":"outputTranslate","targetNode":targetObj,"targetAttr":"translate"},
            {"sourceNode":__createNode_dict["demx"],"sourceAttr":"outputScale","targetNode":targetObj,"targetAttr":"scale"},
            {"sourceNode":__createNode_dict["demx"],"sourceAttr":"outputRotate","targetNode":targetObj,"targetAttr":"rotate"},
            {"sourceNode":__createNode_dict["demx"],"sourceAttr":"outputShear","targetNode":targetObj,"targetAttr":"shear"},
            ]
        for __connectNode_dict in __connectNode_dicts:
            cmds.connectAttr(__connectNode_dict["sourceNode"]+"."+__connectNode_dict["sourceAttr"],__connectNode_dict["targetNode"]+"."+__connectNode_dict["targetAttr"])
    
    def matrixParent_create_func(self,sourceObj,targetObj):
        multMatrixTrsName=sourceObj+"_mumxTrs"
        decomposeMatrixTrsName=sourceObj+"_demxTrs"
        multMatrixRotName=sourceObj+"_mumxRot"
        decomposeMatrixRotName=sourceObj+"_demxRot"

        __createNode_dict={}
        __createNodes=[
            {"tag":"mumxTrs","node":"multMatrix","name":multMatrixTrsName},
            {"tag":"mumxRot","node":"multMatrix","name":multMatrixRotName},
            {"tag":"demxTrs","node":"decomposeMatrix","name":decomposeMatrixTrsName},
            {"tag":"demxRot","node":"decomposeMatrix","name":decomposeMatrixRotName},
            ]
        for __createNode in __createNodes:
            node=cmds.createNode(__createNode["node"])
            rename=cmds.rename(node,__createNode["name"])
            __createNode_dict[__createNode["tag"]]=rename

        __setNode_dicts=[
            {"type":"matrix","getNode":targetObj,"getAttr":"inverseMatrix","setNode":__createNode_dict["mumxRot"],"setAttr":"matrixIn[1]"}
        ]
        for __setNode_dict in __setNode_dicts:
            value=cmds.getAttr(__setNode_dict["getNode"]+"."+__setNode_dict["getAttr"])
            cmds.setAttr(__setNode_dict["setNode"]+"."+__setNode_dict["setAttr"],value,type=__setNode_dict["type"])

        __connectNode_dicts=[
            {"sourceNode":sourceObj,"sourceAttr":"worldMatrix","targetNode":__createNode_dict["mumxTrs"],"targetAttr":"matrixIn[0]"},
            {"sourceNode":__createNode_dict["mumxTrs"],"sourceAttr":"matrixSum","targetNode":__createNode_dict["mumxRot"],"targetAttr":"matrixIn[0]"},
            {"sourceNode":targetObj,"sourceAttr":"parentInverseMatrix","targetNode":__createNode_dict["mumxTrs"],"targetAttr":"matrixIn[1]"},
            {"sourceNode":__createNode_dict["mumxTrs"],"sourceAttr":"matrixSum","targetNode":__createNode_dict["demxTrs"],"targetAttr":"inputMatrix"},
            {"sourceNode":__createNode_dict["mumxRot"],"sourceAttr":"matrixSum","targetNode":__createNode_dict["demxRot"],"targetAttr":"inputMatrix"},
            {"sourceNode":__createNode_dict["demxTrs"],"sourceAttr":"outputTranslate","targetNode":targetObj,"targetAttr":"translate"},
            {"sourceNode":__createNode_dict["demxTrs"],"sourceAttr":"outputScale","targetNode":targetObj,"targetAttr":"scale"},
            {"sourceNode":__createNode_dict["demxRot"],"sourceAttr":"outputRotate","targetNode":targetObj,"targetAttr":"rotate"},
            ]
        for __connectNode_dict in __connectNode_dicts:
            cmds.connectAttr(__connectNode_dict["sourceNode"]+"."+__connectNode_dict["sourceAttr"],__connectNode_dict["targetNode"]+"."+__connectNode_dict["targetAttr"])


    