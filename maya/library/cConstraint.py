# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

class CtrlParent():
    def __init__(self):
        self._sourceObj="source_obj"
        self._targetObj="target_obj"
        self._spaceNames=["null","space"]
        self._trsName="trs"
        self._offsetObj="offset_obj"
        self._offsetJoint="offset_joint"
        self._offsetName="offset"
        self._ctrlName="ctrl"

    def setSourceObj(self,sourceObj):
        self._sourceObj=sourceObj
        return self._sourceObj
    
    def setTargetObj(self,targetObj):
        self._targetObj=targetObj
        return self._targetObj
    
    def setSpaceNames(self,spaceNames):
        self._spaceNames=spaceNames
        return self._spaceNames

    def setTrsName(self,trsName):
        self._trsName=trsName
        return self._trsName
    
    def setOffsetObj(self,offsetObj):
        self._offsetObj=offsetObj
        return self._offsetObj
    
    def setOffsetJoint(self,offsetJoint):
        self._offsetJoint=offsetJoint
        return self._offsetJoint
    
    def setOffsetName(self,offsetName):
        self._offsetName=offsetName
        return self._offsetName

    def setCtrlName(self,ctrlName):
        self._ctrlName=ctrlName
        return self._ctrlName

    def createOffsetConnect(self):
        grp=self.ctrlGrp_create_obj()
        space_list=self.trsSpace_create_list(self._targetObj,self._spaceNames)
        trs_list=self.trsSpace_create_list(self._targetObj,[self._trsName])
        offset_list=self.trsSpace_create_list(self._offsetJoint,[self._offsetName])
        ctrl=self.ctrlShape_create_obj(self._ctrlName)

        ctrl=self.posSet_edit_obj(ctrl,self._targetObj)
        trs=self.posSet_edit_obj(trs_list[0],self._targetObj)
        offset=self.posSet_edit_obj(offset_list[0],self._offsetJoint)
        for posSet in space_list:
            self.posSet_edit_obj(posSet,self._targetObj)
        
        space_list.insert(0,offset)
        space_list.append(ctrl)
        space_list.append(trs)
        hierarchy=space_list
        self.parentHierarchy_edit_func(hierarchy)
        cmds.parent(offset,grp)
        self.constraint_create_func(self._offsetJoint,self._offsetObj)
        self.constraint_create_func(self._sourceObj,self._targetObj)

    def parentHierarchy_edit_func(self,objs=[]):
        parentObj=None
        for obj in objs:
            if parentObj is not None:
                cmds.parent(obj,parentObj)
                parentObj=obj
            else:
                parentObj=obj

    def posSet_edit_obj(self,source,target):
        cmds.parent(source,target)
        cmds.setAttr(source+'.translate', 0, 0, 0, type="double3")
        cmds.setAttr(source+'.rotate', 0, 0, 0, type="double3")
        cmds.parent(source,w=True)
        return source

    def trsSpace_create_list(self,obj="",names=[]):
        trsNodes=[]
        for name in names:
            trsNode=cmds.createNode("transform",n=name)
            trsNodes.append(trsNode)
        return trsNodes

    def ctrlGrp_create_obj(self):
        if not cmds.objExists("ctrl_grp"):
            grp=cmds.createNode("transform",n="ctrl_grp")
            return grp
        else:
            grp="ctrl_grp"
            return grp
        
    def ctrlShape_create_obj(self,name=""):
        ctrlName=cmds.curve(p=[(0,1.11,0),(0,0.78,-0.78),(0,0,-1.11),(0,-0.78,-0.78),(0,-1.11,0),(0,-0.78,0.78),(0,0,1.11),(0,0.78,0.78),(0,1.11,0)])
        ctrlNode=cmds.rename(ctrlName,name)
        return ctrlNode

    def constraint_create_func(self,source,target,name=""):
        cmds.pointConstraint(source,target)
        cmds.orientConstraint(source,target)