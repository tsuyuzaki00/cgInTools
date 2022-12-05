# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from cgInTools.maya.library import setBaseLB as sbLB
cit.reloads([sbLB])

class FKIK(sbLB.BasePair):
    def __init__(self):
        self._sourceNode=""
        self._targetNode=""
        self._thirdNode=""
        self._ui=""
        self._fkCtrls=[]
        self._ikCtrls=[]

    def __loading(self):
        self.__threeJoints=[self._sourceNode,self._thirdNode,self._targetNode]
        self.__threeJoints_dict=self.getThreeJoints_create_dict(self._sourceNode,self._thirdNode,self._targetNode)

    #Single Function
    def listHierarchy_edit_obj(self,objs=[]):
        parentObj=None
        for obj in objs:
            if parentObj is not None:
                cmds.parent(obj,parentObj)
                parentObj=obj
            else:
                parentObj=obj
                firstParent=obj
        return firstParent

    def getThreeJoints_create_dict(self,startJoint,betweenJoint,endJoint):
        __joints=[startJoint,betweenJoint,endJoint]
        __renamers=["jntPrx","jntIK","jntFK"]
        __dupJoint_dict={"jntPrx":[],"jntIK":[],"jntFK":[]}

        for __joint in __joints:
            for __renamer in __renamers:
                dupName=__joint+"_"+__renamer
                __dupJoint_dict[__renamer].append(dupName)

        return __dupJoint_dict

    def duplicateThreeJoints_create_dict(self,startJoint,betweenJoint,endJoint):
        __joints=[startJoint,betweenJoint,endJoint]
        __renamers=["jntPrx","jntIK","jntFK"]
        __dupJoint_dict={"jntPrx":[],"jntIK":[],"jntFK":[]}

        for __joint in __joints:
            for __renamer in __renamers:
                dup=cmds.duplicate(__joint,n=__joint+"_"+__renamer,po=True)
                __dupJoint_dict[__renamer].append(dup[0])
                parent_list=cmds.listRelatives(dup,p=True)
                if not parent_list is None:
                    cmds.parent(dup[0],w=True)

        for __renamer in __renamers:
            self.listHierarchy_edit_obj(__dupJoint_dict[__renamer])
        return __dupJoint_dict

    def connectFKIKJoint_edit_func(self,ui,jnt,fk,ik,blendName="pbld"):
        attr="fkik"
        blend_node=cmds.createNode("pairBlend",n=blendName)
        if not cmds.attributeQuery(attr,node=ui,exists=True):
            cmds.addAttr(ui,ln=attr,nn=attr.capitalize(),at="double",min=0,max=1,dv=1)
            cmds.setAttr(ui+"."+attr,keyable=True)
        cmds.setAttr(blend_node+".rotInterpolation",1)
        cmds.connectAttr(ui+"."+attr,blend_node+".weight",f=True)
        cmds.connectAttr(ik+".rotate",blend_node+".inRotate1",f=True)
        cmds.connectAttr(fk+".rotate",blend_node+".inRotate2",f=True)
        cmds.connectAttr(blend_node+".outRotate",jnt+".rotate",f=True)

    def switchFKIKConnect_edit_func(self,ui,ctrl,switch):
        if switch == "FK":
            shapes=cmds.listRelatives(ctrl,s=True)
            for shape in shapes:
                cmds.connectAttr(ui+".fkik",shape+".visibility")
        elif switch == "IK":
            shapes=cmds.listRelatives(ctrl,s=True)
            for shape in shapes:
                reverse_node=cmds.createNode("reverse",n=ctrl.replace("ctrl","rev"))
                cmds.connectAttr(ui+".fkik",reverse_node+".input.inputX")
                cmds.connectAttr(reverse_node+".output.outputX",shape+".visibility")

    #{"startJoint":joint,"endJoint":joint,"handleCtrl":object,"poleCtrl":object},
    def IKHandle_create_func(self,startJoint,endJoint,handleCtrl,poleCtrl):
        handle_node=cmds.ikHandle(sj=startJoint,ee=endJoint,n=handleCtrl.replace("ctrl","handle"),p=2)
        cmds.rename(handle_node[1],handle_node[0].replace("handle","effe"))
        cmds.parent(handle_node[0],handleCtrl)
        cmds.orientConstraint(handleCtrl,endJoint,n=handleCtrl.replace("ctrl","orc"),mo=True,w=1)
        cmds.poleVectorConstraint(poleCtrl,handle_node[0],n=handle_node[0].replace("handle","plvct"),w=1)

    #{"dagObj":dagObject,"findName":str,"type":nodeType}
    def findNode_query_list(self,dagObj,type,findName=None):
        if findName is None or findName is "":
            node_list=cmds.listRelatives(dagObj,ad=True,f=True,type=type)
        else :
            node_list=cmds.listRelatives(dagObj,ad=True,type=type)
            newNode_list=[node for node in node_list if findName in node]
            return newNode_list

    #handle_node=cmds.ikHandle(sj='collarAIK_jnt_R',ee='wristAIK_jnt_R',sol="ikSplineSolver",scv=False,n="wristAIK_handle_R")
    def IKSpline_create_func(self,startJoint,endJoint,handleCtrl):
        handle_node=cmds.ikHandle(sj=startJoint,ee=endJoint,sol="ikSplineSolver",scv=False,n=handleCtrl.replace("ctrl","handle"))
        effector_node=cmds.rename(handle_node[1],handle_node[0].replace("handle","effe"))
        curve_node=cmds.rename(handle_node[2],handle_node[0].replace("handle","curve"))
        grp=cmds.group([handle_node,curve_node],n=handleCtrl.replace("ctrl","grp"))
        cmds.parent(grp,"spine01_ctrl_C")

    #Multi Function

    #Private Function
    def _createThreeJoints_create_func(self):
        self.duplicateThreeJoints_create_dict(self._sourceNode,self._thirdNode,self._targetNode)
        
        self.__loading()
        for num in range(len(self.__threeJoints_dict["jntPrx"])):
            self.connectFKIKJoint_edit_func(self._ui,self.__threeJoints_dict["jntPrx"][num],self.__threeJoints_dict["jntFK"][num],self.__threeJoints_dict["jntIK"][num])
            cmds.orientConstraint(self.__threeJoints_dict["jntPrx"][num],self.__threeJoints[num],mo=True,w=1)

    def _connectFKIKCtrls_edit_func(self):
        for _fkCtrl in self._fkCtrls:
            switchFKIKConnect_edit_func(self._ui,_fkCtrl,"FK")
        for _ikCtrl in self._ikCtrls:
            switchFKIKConnect_edit_func(self._ui,_ikCtrl,"IK")

    #Public Function
    def allRun(self):
        self._createThreeJoints_create_func()
        self._connectFKIKCtrls_edit_func()

    def createThreeJoints(self):
        self._createThreeJoints_create_func()

    def connectFKIKCtrls(self):
        self._connectFKIKCtrls_edit_func()