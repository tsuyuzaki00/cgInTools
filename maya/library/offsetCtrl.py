# -*- coding: iso-8859-15 -*-

import maya.cmds as cmds

class COffsetCtrl():
    def __init__(self,joint):
        self.joint = joint
        self.parentJnt = cmds.listRelatives(self.joint, parent=True)
        self.offsetName = self.joint.replace("jnt","offset")
        self.aimName = self.joint.replace("jnt","aim")
        self.spaceName = self.joint.replace("jnt","space")
        self.ctrlName = self.joint.replace("jnt","ctrl")
        self.trsName = self.joint.replace("jnt","trs")

    def run(self):
        self.orientCtrl_create_func(self)

    def aimCtrl_create_func(self):
        self.setNodes_create_func()
        self.aimNode = cmds.createNode("transform",n=self.aimName)

        posSetting_list=[
            {"copyObj":self.parentJnt,"pasteObj":self.offsetNode},
            {"copyObj":self.joint,"pasteObj":self.aimNode},
            {"copyObj":self.joint,"pasteObj":self.spaceNode},
            {"copyObj":self.joint,"pasteObj":self.ctrlNode},
            {"copyObj":self.joint,"pasteObj":self.trsNode},
        ]
        for posSetting in posSetting_list:
            self.copyPasteMatrix_edit_func(posSetting["copyObj"],posSetting["pasteObj"])

        parentDicts_list=[
            {"parent":self.ctrlNode,"child":self.trsNode},
            {"parent":self.spaceNode,"child":self.ctrlNode},
            {"parent":self.aimNode,"child":self.spaceNode},
            {"parent":self.offsetNode,"child":self.aimNode},
            {"parent":self.grpNode,"child":self.offsetNode},
        ]
        for parentDicts in parentDicts_list:
            cmds.parent(parentDicts["child"],parentDicts["parent"])
        
        attrs=["rotateY","rotateZ"]

        if self.parentJnt == None:
            self.trsNodeConnect_create_func()
            for attr in attrs:
                cmds.setAttr(self.ctrlNode+"."+attr,l=True,k=False,cb=False)
        elif type(self.parentJnt) is list:
            self.trsNodeConnect_create_func()
            for attr in attrs:
                cmds.setAttr(self.ctrlNode+"."+attr,l=True,k=False,cb=False)

    def orientCtrl_create_func(self):
        self.setNodes_create_func()
        posSetting_list=[
            {"copyObj":self.parentJnt,"pasteObj":self.offsetNode},
            {"copyObj":self.joint,"pasteObj":self.spaceNode},
            {"copyObj":self.joint,"pasteObj":self.ctrlNode},
            {"copyObj":self.joint,"pasteObj":self.trsNode},
        ]
        for posSetting in posSetting_list:
            self.copyPasteMatrix_edit_func(posSetting["copyObj"],posSetting["pasteObj"])

        parentDicts_list=[
            {"parent":self.ctrlNode,"child":self.trsNode},
            {"parent":self.spaceNode,"child":self.ctrlNode},
            {"parent":self.offsetNode,"child":self.spaceNode},
            {"parent":self.grpNode,"child":self.offsetNode},
        ]
        for parentDicts in parentDicts_list:
            cmds.parent(parentDicts["child"],parentDicts["parent"])
        
        if self.parentJnt == None:
            self.trsNodeConnect_create_func()
        elif type(self.parentJnt) is list:
            self.trsNodeConnect_create_func()
            self.offsetNodeConnect_create_func()

    def offsetNodeConnect_create_func(self,offsetNode="",joint=""):
        offsetNode = self.offsetNode or offsetNode
        joint = self.parentJnt or joint
        #cmds.parentConstraint(self.offsetNode,self.joint)
        cmds.pointConstraint(joint,offsetNode)
        cmds.orientConstraint(joint,offsetNode)

    def trsNodeConnect_create_func(self,trsNode="",joint=""):
        trsNode = self.trsNode or trsNode
        joint = self.joint or joint
        #cmds.parentConstraint(self.trsNode,self.joint)
        cmds.pointConstraint(trsNode,joint)
        cmds.orientConstraint(trsNode,joint)
        cmds.scaleConstraint(trsNode,joint)

    def setNodes_create_func(self):
        self.grpNode = self.grpNode_check_string()
        self.offsetNode = cmds.createNode("transform",n=self.offsetName)
        self.spaceNode = cmds.createNode("transform",n=self.spaceName)
        self.trsNode = cmds.createNode("transform",n=self.trsName)
        ctrlNode = cmds.curve(p=[(0, 1.11, 0), (0, 0.78, -0.78), (0, 0, -1.11), (0, -0.78, -0.78), (0, -1.11, 0), (0, -0.78, 0.78), (0, 0, 1.11), (0, 0.78, 0.78), (0, 1.11, 0)] )
        self.ctrlNode = cmds.rename(ctrlNode ,self.ctrlName)
        return self.grpNode,self.offsetNode,self.spaceNode,self.trsNode,self.ctrlNode

    def copyPasteMatrix_edit_func(self,copyObj,pasteObj):
        matrix = cmds.xform(copyObj,q=True,ws=True,m=True)
        cmds.xform(pasteObj,ws=True,m=matrix)
        
    def grpNode_check_string(self):
        grpName_str="ctrls_grp"
        if cmds.objExists(grpName_str):
            grp_node = cmds.ls(grpName_str)[0]
            return grp_node
        else:
            grp_node = cmds.createNode("transform", n=grpName_str)
            return grp_node