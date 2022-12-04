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

    def matrixConstraint(self):
        self.matrixConnect_create_func(self._sourceNode,self._targetNode)
    
    def matrixParent(self):
        self.matrixParent_create_func(self._sourceNode,self._targetNode)

    def proximityPin(self):
        proxPin_node=self.proximityPin_create_node(self._targetNode)
        self.proximityPinMatrix_create_func(self._sourceNode,proxPin_node)

    #Multi Function
    def proximityPinMatrix_create_func(self,ctrl,proxPin,matrixIndex=0):
        ctrlNull_obj=self.addParentNull_create_null(ctrl)
        worldMatrix_node=self.setNodeMultMatrix_create_node(ctrl,"worldMatrix",ctrl+"WdMx"+str(matrixIndex).zfill(2)+"_mtmx")
        parentInverseMatrix_node=cmds.createNode("multMatrix",n=ctrl+"PrIMx"+str(matrixIndex).zfill(2)+"_mtmx")
        decomposeMatirix_node=cmds.createNode("decomposeMatrix",n=ctrl+str(matrixIndex).zfill(2)+"_dcmx")
        __matrixConnects=[
            {"sourceAttr":str(worldMatrix_node)+".matrixSum","targetAttr":str(proxPin)+".inputMatrix["+str(matrixIndex)+"]"},
            {"sourceAttr":str(proxPin)+".outputMatrix["+str(matrixIndex)+"]","targetAttr":str(parentInverseMatrix_node)+".matrixIn[0]"},
            {"sourceAttr":str(ctrlNull_obj)+".parentInverseMatrix[0]","targetAttr":str(parentInverseMatrix_node)+".matrixIn[1]"},
            {"sourceAttr":str(parentInverseMatrix_node)+".matrixSum","targetAttr":str(decomposeMatirix_node)+".inputMatrix"},
            {"sourceAttr":str(decomposeMatirix_node)+".outputTranslate","targetAttr":str(ctrlNull_obj)+".translate"},
            {"sourceAttr":str(decomposeMatirix_node)+".outputRotate","targetAttr":str(ctrlNull_obj)+".rotate"},
            {"sourceAttr":str(decomposeMatirix_node)+".outputShear","targetAttr":str(ctrlNull_obj)+".shear"},
        ]
        for __matrixConnect in __matrixConnects:
            cmds.connectAttr(__matrixConnect["sourceAttr"],__matrixConnect["targetAttr"])
    
    #Single Function
    def matrixConnect_create_func(self,sourceObj,targetObj,trs=True,rot=True,scl=True,shr=True):
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
            ]
        if trs:
            __connectNode_dicts.append({"sourceNode":__createNode_dict["demx"],"sourceAttr":"outputTranslate","targetNode":targetObj,"targetAttr":"translate"})
        if rot:
            __connectNode_dicts.append({"sourceNode":__createNode_dict["demx"],"sourceAttr":"outputRotate","targetNode":targetObj,"targetAttr":"rotate"})
        if scl:
            __connectNode_dicts.append({"sourceNode":__createNode_dict["demx"],"sourceAttr":"outputScale","targetNode":targetObj,"targetAttr":"scale"})
        if shr:
            __connectNode_dicts.append({"sourceNode":__createNode_dict["demx"],"sourceAttr":"outputShear","targetNode":targetObj,"targetAttr":"shear"})
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
   
    def bindShape_check_geo(self,geo):
        child_check=cmds.listRelatives(geo,c=True)
        if len(child_check) == 2:
            return geo
        else:
            cmds.error("Bind to the "+geo+".")
            
    def proximityPin_create_node(self,geo):
        # get shapes
        child_mesh=cmds.listRelatives(geo,c=True,type="mesh")
        bind_shape=child_mesh[0]
        orig_shape=child_mesh[1]
        # create and settings proximityPin
        proxPin_node=cmds.createNode("proximityPin",n=geo+"_pxmp")
        __proxPin_dicts=[
            {"node":str(proxPin_node),"attr":"coordMode","value":1}, # Uses UV for coordinate mode
            {"node":str(proxPin_node),"attr":"normalAxis","value":0}, # Uses X for Normal Axis
            {"node":str(proxPin_node),"attr":"tangentAxis","value":1}, # Uses Y for Tanget Axis
            {"node":str(proxPin_node),"attr":"offsetTranslation","value":1},
            {"node":str(proxPin_node),"attr":"offsetOrientation","value":1}
        ]
        for __proxPin_dict in __proxPin_dicts:
            cmds.setAttr(__proxPin_dict["node"]+"."+__proxPin_dict["attr"],__proxPin_dict["value"])
        # connections
        __connection_dicts=[
            {"sourceAttr":str(orig_shape)+".outMesh","targetAttr":str(proxPin_node)+".originalGeometry"},
            {"sourceAttr":str(bind_shape)+".worldMesh[0]","targetAttr":str(proxPin_node)+".deformedGeometry"}
        ]
        for __connection_dict in __connection_dicts:
            cmds.connectAttr(__connection_dict["sourceAttr"],__connection_dict["targetAttr"])
        return proxPin_node

    def setNodeMultMatrix_create_node(self,node,matrixAttr,name="poxy_mumx"):
        multMatrix_node=cmds.createNode("multMatrix",n=name)
        getMatrix=cmds.getAttr(node+"."+matrixAttr+"[0]")
        cmds.setAttr(multMatrix_node+".matrixIn[0]",getMatrix,type="matrix")
        return multMatrix_node

    def addParentNull_create_null(self,obj):
        parent=cmds.listRelatives(obj,p=True)
        if not parent == None:
            parent=parent[0]
        null=cmds.createNode("transform",n=obj+"_null",p=parent,ss=True)
        getMatrix=cmds.xform(obj,q=True,m=True)
        cmds.xform(null,m=getMatrix)
        cmds.parent(obj,null)
        return null
    
    def addOffsetNull_create_null(self,obj):
        parent=cmds.listRelatives(obj,p=True)
        if not parent == None:
            parent=parent[0]
        null=cmds.createNode("transform",n=obj+"_null",ss=True)
        getMatrix=cmds.xform(parent,q=True,m=True,a=True)
        cmds.xform(null,m=getMatrix)
        cmds.parent(null,parent)
        cmds.parent(obj,null)
        return null