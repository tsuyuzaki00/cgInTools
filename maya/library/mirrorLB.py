# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

class MatrixMirror():
    def __init__(self):
        self.sourceNode=""
        self.targetNode=""
        self.mirrorX=True
        self.mirrorY=False
        self.mirrorZ=False
        self.duplicate=False
    def setSourceNode(self,variable):
        self.sourceNode=variable
        return self.sourceNode
    def setTargetNode(self,variable):
        self.targetNode=variable
        return self.targetNode
    def setMirrorX(self,variable):
        self.mirrorX=variable
        return self.mirrorX
    def setMirrorY(self,variable):
        self.mirrorY=variable
        return self.mirrorY
    def setMirrorZ(self,variable):
        self.mirrorZ=variable
        return self.mirrorZ
    def setDuplicate(self,variable):
        self.duplicate=variable
        return self.duplicate
    def translateOnly(self):
        if self.duplicate:
            targetName=self.reversedLeftRight_edit_string(self.sourceNode)
            self.targetNode=cmds.duplicate(self.sourceNode,n=targetName)
        self.translateMirror_edit_func(self.sourceNode,self.targetNode,self.mirrorX,self.mirrorY,self.mirrorZ)
    def rotateOnly(self):
        if self.duplicate:
            targetName=self.reversedLeftRight_edit_string(self.sourceNode)
            self.targetNode=cmds.duplicate(self.sourceNode,n=targetName)
        self.rotateMirror_edit_func(self.sourceNode,self.targetNode,self.mirrorX,self.mirrorY,self.mirrorZ)
    def run(self):
        if self.duplicate:
            targetName=self.reversedLeftRight_edit_string(self.sourceNode)
            self.targetNode=cmds.duplicate(self.sourceNode,n=targetName)
        self.rotateMirror_edit_func(self.sourceNode,self.targetNode,self.mirrorX,self.mirrorY,self.mirrorZ)
        self.translateMirror_edit_func(self.sourceNode,self.targetNode,self.mirrorX,self.mirrorY,self.mirrorZ)


    def reversedLeftRight_edit_string(self,name):
        LRs=[
            ["_Left","_Right"],
            ["Left_","Right_"],
            ["_Right","_Left"],
            ["Right_","Left_"],
            ["_left","_right"],
            ["left_","right_"],
            ["_right","_left"],
            ["right_","left_"],
            ["_L","_R"],
            ["L_","R_"],
            ["_R","_L"],
            ["R_","L_"],
            ]
        for lr in LRs:
            if lr[0] in name:
                newName=name.replace(lr[0],lr[1])
                return newName    
        cmds.error("left or Right or L or R is not in the name")

    def reverseLocatorDict_edit_dict(self,locator_dicts):
        new_list=[]
        new_dict={}
        reverse_list=[]
        for locator in locator_dicts:
            new_dict["name"]=locator["name"]
            reverse_list.append(locator["locators"][1])
            reverse_list.append(locator["locators"][0])
            reverse_list.append(locator["locators"][3])
            reverse_list.append(locator["locators"][2])
            new_dict["locators"]=reverse_list
            new_list.append(new_dict)
            reverse_list=[]
        return new_list

    def mirrorAxis_edit_tuple(self,mirrorX=True,mirrorY=False,mirrorZ=False):
        mirror_list=[1,1,1]
        if mirrorX:
            mirror_list[0]=-1
        if mirrorY:
            mirror_list[1]=-1
        if mirrorZ:
            mirror_list[2]=-1
        return tuple(mirror_list)

    def getNodeMatrix_query_mMatrix(self,node):
        node_mSelectionList=om2.MSelectionList().add(node)
        node_mDagPath=node_mSelectionList.getDagPath(0)
        node_mMatrix=node_mDagPath.inclusiveMatrix()
        return node_mMatrix

    def translateMirror_edit_func(self,sourceNode,targetNode,mirrorX=True,mirrorY=False,mirrorZ=False):
        mirror=self.mirrorAxis_edit_tuple(mirrorX,mirrorY,mirrorZ)
        sourceNode_mMatrix=self.getNodeMatrix_query_mMatrix(sourceNode)
        trans_mTransformationMatrix = om2.MTransformationMatrix(sourceNode_mMatrix)
        trans_mVector=trans_mTransformationMatrix.translation(om2.MSpace.kWorld)
        cmds.xform(targetNode,ws=True,t=(trans_mVector[0]*mirror[0],trans_mVector[1]*mirror[1],trans_mVector[2]*mirror[2]))

    def rotateMirror_edit_func(self,sourceNode,targetNode,mirrorX=True,mirrorY=False,mirrorZ=False):
        mirror=self.mirrorAxis_edit_tuple(mirrorX,mirrorY,mirrorZ)
        sourceNode_mMatrix=self.getNodeMatrix_query_mMatrix(sourceNode)
        mirror_mMatrix=om2.MMatrix((mirror[0],0,0,0, 0,mirror[1],0,0, 0,0,mirror[2],0, 0,0,0,1))
        mirror_mMatrix=sourceNode_mMatrix*mirror_mMatrix
        cmds.xform(targetNode,m=mirror_mMatrix)

    def bendRollMirror_edit_func(self,sourceNode,targetNode,mirrorX=True,mirrorY=False,mirrorZ=False):
        mirror=self.mirrorAxis_edit_tuple(mirrorX,mirrorY,mirrorZ)
        sourceNode_mMatrix=self.getNodeMatrix_query_mMatrix(sourceNode)
        aimVector_mMatrix=om2.MMatrix((1,0,0,0, 0,1,0,0, 0,0,1,0, 1,0,0,1))
        upVector_mMatrix=om2.MMatrix((1,0,0,0, 0,1,0,0, 0,0,1,0, 0,1,0,1))
        aimVector_mMatrix=sourceNode_mMatrix*aimVector_mMatrix
        upVector_mMatrix=sourceNode_mMatrix*upVector_mMatrix

        trans_mTransformationMatrix = om2.MTransformationMatrix(sourceNode_mMatrix)
        trans_mVector=trans_mTransformationMatrix.translation(om2.MSpace.kWorld)
        trans_mVector[0]*mirror[0],
        trans_mVector[1]*mirror[1],
        trans_mVector[2]*mirror[2]

        mirror_mMatrix=()
        cmds.xform(targetNode,m=mirror_mMatrix)

