# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import mgear.rigbits as rb
import pymel.core as pm

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
        proxPin_node=self.proximityPinNode_create_func(self._targetNode)
        self.proximityPinMatrix_create_func(self._sourceNode,proxPin_node)

    #Multi Function
    def proximityPinNode_create_func(self,geo):
        geo=self.bindShape_check_geo(geo)
        bind_shape,orig_shape=self.getBindShapes_query_bindMesh_origMesh(geo)
        proxPin_node=self.proximityPin_create_node(geo)
        self.connectMeshAndProxPin_edit_func(orig_shape,bind_shape,proxPin_node)
        return proxPin_node
    
    def proximityPinMatrix_create_func(self,ctrl,proxPin,matrixIndex=0):

        ctrl_npo=rb.addNPO(objs=pm.PyNode(ctrl))
        worldMatrix_node=self.multMatrix_create_node(ctrl,"worldMatrix",ctrl+"WdMx"+str(matrixIndex).zfill(2)+"_mtmx")
        parentInverseMatrix_node=cmds.createNode("multMatrix",n=ctrl+"PrIMx"+str(matrixIndex).zfill(2)+"_mtmx")
        decomposeMatirix_node=cmds.createNode("decomposeMatrix",n=ctrl+str(matrixIndex).zfill(2)+"_dcmx")
        __matrixConnects=[
            {"sourceAttr":str(worldMatrix_node)+".matrixSum","targetAttr":str(proxPin)+".inputMatrix["+str(matrixIndex)+"]"},
            {"sourceAttr":str(proxPin)+".outputMatrix["+str(matrixIndex)+"]","targetAttr":str(parentInverseMatrix_node)+".matrixIn[0]"},
            {"sourceAttr":str(ctrl_npo[0])+".parentInverseMatrix[0]","targetAttr":str(parentInverseMatrix_node)+".matrixIn[1]"},
            {"sourceAttr":str(parentInverseMatrix_node)+".matrixSum","targetAttr":str(decomposeMatirix_node)+".inputMatrix"},
            {"sourceAttr":str(decomposeMatirix_node)+".outputTranslate","targetAttr":str(ctrl_npo[0])+".translate"},
            {"sourceAttr":str(decomposeMatirix_node)+".outputRotate","targetAttr":str(ctrl_npo[0])+".rotate"},
            {"sourceAttr":str(decomposeMatirix_node)+".outputShear","targetAttr":str(ctrl_npo[0])+".shear"},
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

    def getBindShapes_query_bindMesh_origMesh(self,geo):
        child_mesh=cmds.listRelatives(geo,c=True,type="mesh")
        bind_shape=child_mesh[0]
        orig_shape=child_mesh[1]
        return bind_shape,orig_shape
            
    def proximityPin_create_node(self,node):
        proxPin_node=cmds.createNode("proximityPin",n=node+"_pxmp")
        __proxPin_dicts=[
            {"node":str(proxPin_node),"attr":"coordMode","value":1}, # Uses UV for coordinate mode
            {"node":str(proxPin_node),"attr":"normalAxis","value":0}, # Uses X for Normal Axis
            {"node":str(proxPin_node),"attr":"tangentAxis","value":1}, # Uses Y for Tanget Axis
            {"node":str(proxPin_node),"attr":"offsetTranslation","value":1},
            {"node":str(proxPin_node),"attr":"offsetOrientation","value":1}
        ]
        for __proxPin_dict in __proxPin_dicts:
            cmds.setAttr(__proxPin_dict["node"]+"."+__proxPin_dict["attr"],__proxPin_dict["value"])
        return proxPin_node

    def multMatrix_create_node(self,node,matrixAttr,name="poxy_mumx",setIndex=0):
        multMatrix_node=cmds.createNode("multMatrix",n=name)
        get_matrix=cmds.getAttr(node+"."+matrixAttr+"[0]")
        cmds.setAttr(multMatrix_node+".matrixIn["+str(setIndex)+"]",get_matrix,type="matrix")
        return multMatrix_node

    def connectMeshAndProxPin_edit_func(self,orig_shape,bind_shape,proxPin_node):
        __connection_dicts=[
            {"sourceAttr":str(orig_shape)+".outMesh","targetAttr":str(proxPin_node)+".originalGeometry"},
            {"sourceAttr":str(bind_shape)+".worldMesh[0]","targetAttr":str(proxPin_node)+".deformedGeometry"}
        ]
        for __connection_dict in __connection_dicts:
            cmds.connectAttr(__connection_dict["sourceAttr"],__connection_dict["targetAttr"])

    def ctrlConnectNodes_create_dict(ctrl):
        ctrl_npo=rb.addNPO(objs=pm.PyNode(ctrl))
        worldMatrix_node=self.multMatrix_create_node(ctrl,"worldMatrix",ctrl+"WdMx"+str(matrixIndex).zfill(2)+"_mtmx")
        parentInverseMatrix_node=cmds.createNode("multMatrix",n=ctrl+"PrIMx"+str(matrixIndex).zfill(2)+"_mtmx")
        decomposeMatirix_node=cmds.createNode("decomposeMatrix",n=ctrl+str(matrixIndex).zfill(2)+"_dcmx")
        ctrlConnectNodes_dict={"worldMatrix":worldMatrix_node,"parentInverseMatrix":parentInverseMatrix_node,"decomposeMatirix":decomposeMatirix_node,}
        return ctrlConnectNodes_dict

    def connectProxPinAndMatrix_edit_func(self,proxPin,ctrl_npo,matrixIndex,worldMatrix_node,parentInverseMatrix_node,decomposeMatirix_node):
        __matrixConnects=[
            {"sourceAttr":str(worldMatrix_node)+".matrixSum","targetAttr":str(proxPin)+".inputMatrix["+str(matrixIndex)+"]"},
            {"sourceAttr":str(proxPin)+".outputMatrix["+str(matrixIndex)+"]","targetAttr":str(parentInverseMatrix_node)+".matrixIn[0]"},
            {"sourceAttr":str(ctrl_npo[0])+".parentInverseMatrix[0]","targetAttr":str(parentInverseMatrix_node)+".matrixIn[1]"},
            {"sourceAttr":str(parentInverseMatrix_node)+".matrixSum","targetAttr":str(decomposeMatirix_node)+".inputMatrix"},
            {"sourceAttr":str(decomposeMatirix_node)+".outputTranslate","targetAttr":str(ctrl_npo[0])+".translate"},
            {"sourceAttr":str(decomposeMatirix_node)+".outputRotate","targetAttr":str(ctrl_npo[0])+".rotate"},
            {"sourceAttr":str(decomposeMatirix_node)+".outputShear","targetAttr":str(ctrl_npo[0])+".shear"},
        ]
        for __matrixConnect in __matrixConnects:
            cmds.connectAttr(__matrixConnect["sourceAttr"],__matrixConnect["targetAttr"])