# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from . import setBaseLB as sbLB
from . import jsonLB as jLB
from . import namingLB as nLB
from . import hierarchyLB as hLB
cit.reloads([sbLB,jLB,nLB,hLB])

RULES_DICT=jLB.getJson(cit.mayaData_dir,"autoRename")
class Constrain(sbLB.BasePair):
    def __init__(self):
        super(Constrain,self).__init__()
        self._rename=nLB.Naming()
        self._rename.setOrderList(RULES_DICT["nameOrderList"])
        self._rename.setSwitch(RULES_DICT["modeSwitch"])

    #Single Function   
    def bindShape_check_geo(self,geo):
        child_check=cmds.listRelatives(geo,c=True)
        if len(child_check) == 2:
            return geo
        else:
            cmds.error("Bind to the "+geo+".")

    #Private Function
    def _matrixConnect_create_func(self,sourceObj,targetObj,trs=True,rot=True,scl=True,shr=True):
        self._rename.setChoise(targetObj)
        titleOnly_str=self._rename.titleHieName()
        
        node_dict={}
        __createNode_dicts=[
            {"node":"multMatrix","tag":"mumx"},
            {"node":"decomposeMatrix","tag":"demx"},
            ]
        for __createNode_dict in __createNode_dicts:
            node=cmds.createNode(__createNode_dict["node"])

            self._rename.setSwitch("setAuto")
            self._rename.setOrderList(["title","node"])
            self._rename.setObject(node)
            self._rename.setTitle(titleOnly_str)
            self._rename.setNode("")
            self._rename.setSide("C")
            renameMatrix=self._rename.rename()
            node_dict[__createNode_dict["tag"]]=renameMatrix

        __connectNode_dicts=[
            {"sourceNode":sourceObj,"sourceAttr":"matrix","targetNode":node_dict["mumx"],"targetAttr":"matrixIn[0]"},
            {"sourceNode":sourceObj,"sourceAttr":"parentMatrix","targetNode":node_dict["mumx"],"targetAttr":"matrixIn[1]"},
            {"sourceNode":targetObj,"sourceAttr":"parentInverseMatrix","targetNode":node_dict["mumx"],"targetAttr":"matrixIn[2]"},
            {"sourceNode":node_dict["mumx"],"sourceAttr":"matrixSum","targetNode":node_dict["demx"],"targetAttr":"inputMatrix"},
            ]
        if trs:
            __connectNode_dicts.append({"sourceNode":node_dict["demx"],"sourceAttr":"outputTranslate","targetNode":targetObj,"targetAttr":"translate"})
        if rot:
            __connectNode_dicts.append({"sourceNode":node_dict["demx"],"sourceAttr":"outputRotate","targetNode":targetObj,"targetAttr":"rotate"})
        if scl:
            __connectNode_dicts.append({"sourceNode":node_dict["demx"],"sourceAttr":"outputScale","targetNode":targetObj,"targetAttr":"scale"})
        if shr:
            __connectNode_dicts.append({"sourceNode":node_dict["demx"],"sourceAttr":"outputShear","targetNode":targetObj,"targetAttr":"shear"})
        for __connectNode_dict in __connectNode_dicts:
            cmds.connectAttr(__connectNode_dict["sourceNode"]+"."+__connectNode_dict["sourceAttr"],__connectNode_dict["targetNode"]+"."+__connectNode_dict["targetAttr"])

    def _matrixParent_create_func(self,sourceObj,targetObj):
        self._rename.setChoise(targetObj)
        titleOnly_str=self._rename.titleHieName()

        node_dict={}
        __createNode_dicts=[
            {"node":"multMatrix","tag":"mumxTrs","plus":"Trs"},
            {"node":"decomposeMatrix","tag":"demxTrs","plus":"Trs"},
            {"node":"multMatrix","tag":"mumxRot","plus":"Rot"},
            {"node":"decomposeMatrix","tag":"demxRot","plus":"Rot"},
            ]
        for __createNode_dict in __createNode_dicts:
            node=cmds.createNode(__createNode_dict["node"])

            self._rename.setSwitch("setAuto")
            self._rename.setOrderList(["title","node"])
            self._rename.setObject(node)
            self._rename.setTitle(titleOnly_str+__createNode_dict["plus"])
            self._rename.setNode("")
            self._rename.setSide("C")
            renameMatrix=self._rename.rename()
            node_dict[__createNode_dict["tag"]]=renameMatrix

        __setNode_dicts=[
            {"getNode":targetObj,"getAttr":"inverseMatrix","setNode":node_dict["mumxRot"],"setAttr":"matrixIn[1]","type":"matrix"}
        ]
        for __setNode_dict in __setNode_dicts:
            value=cmds.getAttr(__setNode_dict["getNode"]+"."+__setNode_dict["getAttr"])
            cmds.setAttr(__setNode_dict["setNode"]+"."+__setNode_dict["setAttr"],value,type=__setNode_dict["type"])

        __connectNode_dicts=[
            {"sourceNode":sourceObj,"sourceAttr":"worldMatrix","targetNode":node_dict["mumxTrs"],"targetAttr":"matrixIn[0]"},
            {"sourceNode":node_dict["mumxTrs"],"sourceAttr":"matrixSum","targetNode":node_dict["mumxRot"],"targetAttr":"matrixIn[0]"},
            {"sourceNode":targetObj,"sourceAttr":"parentInverseMatrix","targetNode":node_dict["mumxTrs"],"targetAttr":"matrixIn[1]"},
            {"sourceNode":node_dict["mumxTrs"],"sourceAttr":"matrixSum","targetNode":node_dict["demxTrs"],"targetAttr":"inputMatrix"},
            {"sourceNode":node_dict["mumxRot"],"sourceAttr":"matrixSum","targetNode":node_dict["demxRot"],"targetAttr":"inputMatrix"},
            {"sourceNode":node_dict["demxTrs"],"sourceAttr":"outputTranslate","targetNode":targetObj,"targetAttr":"translate"},
            {"sourceNode":node_dict["demxTrs"],"sourceAttr":"outputScale","targetNode":targetObj,"targetAttr":"scale"},
            {"sourceNode":node_dict["demxRot"],"sourceAttr":"outputRotate","targetNode":targetObj,"targetAttr":"rotate"},
            ]
        for __connectNode_dict in __connectNode_dicts:
            cmds.connectAttr(__connectNode_dict["sourceNode"]+"."+__connectNode_dict["sourceAttr"],__connectNode_dict["targetNode"]+"."+__connectNode_dict["targetAttr"])

    def _proximityPin_create_node(self,geo):
        # get shapes
        self._rename.setChoise(geo)
        titleOnly_str=self._rename.titleHieName()

        child_mesh=cmds.listRelatives(geo,c=True,type="mesh")
        bind_shape=child_mesh[0]
        orig_shape=child_mesh[1]
        # create and settings proximityPin
        proxPinNode_str=cmds.createNode("proximityPin")

        self._rename.setSwitch("setAuto")
        self._rename.setOrderList(["title","node"])
        self._rename.setObject(proxPinNode_str)
        self._rename.setTitle(titleOnly_str)
        self._rename.setNode("")
        self._rename.setSide("C")
        renamePin=self._rename.rename()

        __proxPin_dicts=[
            {"node":renamePin,"attr":"coordMode","value":1}, # Uses UV for coordinate mode
            {"node":renamePin,"attr":"normalAxis","value":0}, # Uses X for Normal Axis
            {"node":renamePin,"attr":"tangentAxis","value":1}, # Uses Y for Tanget Axis
            {"node":renamePin,"attr":"offsetTranslation","value":1},
            {"node":renamePin,"attr":"offsetOrientation","value":1}
        ]
        for __proxPin_dict in __proxPin_dicts:
            cmds.setAttr(__proxPin_dict["node"]+"."+__proxPin_dict["attr"],__proxPin_dict["value"])
        # connections
        __connection_dicts=[
            {"sourceAttr":str(orig_shape)+".outMesh","targetAttr":renamePin+".originalGeometry"},
            {"sourceAttr":str(bind_shape)+".worldMesh[0]","targetAttr":renamePin+".deformedGeometry"}
        ]
        for __connection_dict in __connection_dicts:
            cmds.connectAttr(__connection_dict["sourceAttr"],__connection_dict["targetAttr"])
        return renamePin

    def _proximityPinMatrix_create_func(self,ctrl,proxPin,matrixIndex=0):
        parentNull=hLB.Hierarchy()
        parentNull.setObjs([ctrl])
        nulls=parentNull.addParentNull()
        ctrlNull_obj=nulls[0]
        
        self._rename.setChoise(ctrl)
        titleOnly_str=self._rename.titleHieName()
        sideOnly_str=self._rename.sideName()

        node_dict={}
        __createNode_dicts=[
            {"node":"multMatrix","tag":"mumxWdMx","plus":"WdMx"},
            {"node":"multMatrix","tag":"mumxPrIMx","plus":"PrIMx"},
            {"node":"decomposeMatrix","tag":"demx","plus":""},
            ]
        for __createNode_dict in __createNode_dicts:
            node=cmds.createNode(__createNode_dict["node"])

            self._rename.setSwitch("setAuto")
            self._rename.setOrderList(["title","node"])
            self._rename.setObject(node)
            self._rename.setTitle(titleOnly_str+__createNode_dict["plus"])
            self._rename.setSide(sideOnly_str)
            self._rename.setNode("")
            renameMatrix=self._rename.rename()
            node_dict[__createNode_dict["tag"]]=renameMatrix

        __setNode_dicts=[
            {"getNode":ctrl,"getAttr":"worldMatrix","setNode":node_dict["mumxWdMx"],"setAttr":"matrixIn[0]","type":"matrix"}
        ]
        for __setNode_dict in __setNode_dicts:
            value=cmds.getAttr(__setNode_dict["getNode"]+"."+__setNode_dict["getAttr"])
            cmds.setAttr(__setNode_dict["setNode"]+"."+__setNode_dict["setAttr"],value,type=__setNode_dict["type"])
        
        __matrixConnects=[
            {"sourceAttr":node_dict["mumxWdMx"]+".matrixSum","targetAttr":proxPin+".inputMatrix["+str(matrixIndex)+"]"},
            {"sourceAttr":proxPin+".outputMatrix["+str(matrixIndex)+"]","targetAttr":node_dict["mumxPrIMx"]+".matrixIn[0]"},
            {"sourceAttr":ctrlNull_obj+".parentInverseMatrix[0]","targetAttr":node_dict["mumxPrIMx"]+".matrixIn[1]"},
            {"sourceAttr":node_dict["mumxPrIMx"]+".matrixSum","targetAttr":node_dict["demx"]+".inputMatrix"},
            {"sourceAttr":node_dict["demx"]+".outputTranslate","targetAttr":ctrlNull_obj+".translate"},
            {"sourceAttr":node_dict["demx"]+".outputRotate","targetAttr":ctrlNull_obj+".rotate"},
            {"sourceAttr":node_dict["demx"]+".outputShear","targetAttr":ctrlNull_obj+".shear"},
        ]
        for __matrixConnect in __matrixConnects:
            cmds.connectAttr(__matrixConnect["sourceAttr"],__matrixConnect["targetAttr"])

    #Public Function
    def parentConstraint(self):
        constraint_list=cmds.parentConstraint(self._sourceNode,self._targetNode,mo=True,w=1)
        self._rename.setSwitch("fullAuto")
        self._rename.setObject(constraint_list[0])
        self._rename.rename()

    def pointConstraint(self):
        constraint_list=cmds.pointConstraint(self._sourceNode,self._targetNode,mo=True,w=1)
        self._rename.setSwitch("fullAuto")
        self._rename.setObject(constraint_list[0])
        self._rename.rename()

    def orientConstraint(self):
        constraint_list=cmds.orientConstraint(self._sourceNode,self._targetNode,mo=True,w=1)
        self._rename.setSwitch("fullAuto")
        self._rename.setObject(constraint_list[0])
        self._rename.rename()

    def scaleConstraint(self):
        constraint_list=cmds.scaleConstraint(self._sourceNode,self._targetNode,mo=True,w=1)
        self._rename.setSwitch("fullAuto")
        self._rename.setObject(constraint_list[0])
        self._rename.rename()

    def aimConstraint(self):
        constraint_list=cmds.aimConstraint(self._sourceNode,self._targetNode,mo=True,w=1)
        self._rename.setSwitch("fullAuto")
        self._rename.setObject(constraint_list[0])
        self._rename.rename()

    def ikHandleConstraint(self):
        ikHandles=cmds.ikHandle(sj=self._sourceNode,ee=self._targetNode,p=2)
        
        self._rename.setChoise(self._targetNode)
        titleOnly_str=self._rename.titleHieName()
        self._rename.setTitle(titleOnly_str)
        self._rename.setSwitch("setAuto")
        self._rename.setObject(ikHandles[0])
        ikHandle=self._rename.rename()

        self._rename.setNode("")
        self._rename.setObject(ikHandles[1])
        self._rename.rename()
        
        constraint_list=cmds.poleVectorConstraint(self._thirdNode,ikHandle,w=1)
        
        self._rename.setNode("")
        self._rename.setObject(constraint_list[0])
        self._rename.rename()

    def matrixConstraint(self):
        self._matrixConnect_create_func(self._sourceNode,self._targetNode)
    
    def matrixParent(self):
        self._matrixParent_create_func(self._sourceNode,self._targetNode)

    def proximityPin(self):
        proxPin_node=self._proximityPin_create_node(self._sourceNode)
        self._proximityPinMatrix_create_func(self._targetNode,proxPin_node)