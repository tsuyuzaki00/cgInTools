# -*- coding: iso-8859-15 -*-

import maya.cmds as cmds

class COffsetCtrl():
    def __init__(self,joint):
        self.joint = joint

    def run(self):
        parentJnt = cmds.listRelatives(self.joint, parent=True)
        offsetName = self.joint.replace("jnt","offset")
        spaceName = self.joint.replace("jnt","space")
        ctrlName = self.joint.replace("jnt","ctrl")
        trsName = self.joint.replace("jnt","trs")
        grpNode = self.grpNode_check_string(self)
        
        parent_list= [
            {"parent":ctrlName,"child":trsName,},
            {"parent":spaceName,"child":ctrlName},
            {"parent":grpNode,"child":spaceName}
        ]
        spaceNode = cmds.createNode("transform",n=spaceName)
        trsNode = cmds.createNode("transform",n=trsName)
        ctrlNode = cmds.curve(p=[(0, 1.11, 0), (0, 0.78, -0.78), (0, 0, -1.11), (0, -0.78, -0.78), (0, -1.11, 0), (0, -0.78, 0.78), (0, 0, 1.11), (0, 0.78, 0.78), (0, 1.11, 0)] )
        cmds.rename(ctrlNode ,ctrlName)

    def aimCtrl_create_func(self):
        
        return 

    def orientCtrl_create_func(self):
        if parentSel == []:
            cmds.parent(spaceNode, 'grp_ctrl_'+ name_ctrl_grp[2])
            cmds.pointConstraint(trsNode,sel[0])
            cmds.orientConstraint(trsNode,sel[0])
        else :
            offsetName = sel[0].replace("jnt_",'offset_')
            offsetNode = cmds.createNode("transform", n=offsetName)
            cmds.parent(offsetNode,parentSel[0])
            cmds.setAttr(offsetNode+'.translate', 0, 0, 0, type="double3")
            cmds.setAttr(offsetNode+'.rotate', 0, 0, 0, type="double3")
            
            cmds.parent(offsetNode, 'grp_ctrl_'+ name_ctrl_grp[2])
            cmds.parent(spaceNode,offsetNode)
            
            cmds.pointConstraint(parentSel[0],offsetNode)
            cmds.orientConstraint(parentSel[0],offsetNode)
            cmds.pointConstraint(trsNode,sel[0])
            cmds.orientConstraint(trsNode,sel[0])

    def parentReset_create_func(self,parent,child):
        cmds.parent(child,parent)
        cmds.setAttr(child+'.translate', 0, 0, 0, type="double3")
        cmds.setAttr(child+'.rotate', 0, 0, 0, type="double3")
        
    def grpNode_check_string(self):
        if "grp_ctrl_"+"":
            grp_node = cmds.createNode("transform", n="grp_ctrl_"+"")
            return grp_node
        else :
            grp_node = "grp_ctrl_"+""
            return grp_node