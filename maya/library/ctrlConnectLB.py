# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2
from cgInTools.maya.library import setBaseLB as sbLB

class CtrlParent(sbLB.SetObject):
    def __init__(self):
        """
        self.object=""
        self.parent=""
        """
        self.vector_dict={
            "+x":[1,0,0],
            "+X":[1,0,0],
            "+y":[0,1,0],
            "+Y":[0,1,0],
            "+z":[0,0,1],
            "+Z":[0,0,1],
            "-x":[-1,0,0],
            "-X":[-1,0,0],
            "-y":[0,-1,0],
            "-Y":[0,-1,0],
            "-z":[0,0,-1],
            "-Z":[0,0,-1],
        }
        self.name="object"
        self.position="C"
        self.spaceNodeNames=["null","space"]
        self.trsNodeName="trs"
        self.offsetNodeName="offset"
        self.ctrlNodeName="ctrl"
        self.upNodeName="up"
        self.aimVector="+X"
        self.upVector="+Y"
    
    def update(self):
        self.name=self.object.split("_")[0]
        self.position="C"
        self.spaceNodeNames=["null","space"]
        self.trsNodeName="trs"
        self.offsetNodeName="offset"
        self.ctrlNodeName="ctrl"
        self.upNodeName="up"
        self.aimVector="+X"
        self.upVector="+Y"
        self.repeatName="_".join([self.name,"node",self.position])
        self.attrName="pointConstraintSwitch"

    def __createSettingSpaces(self,spaceNodeNames,target):
        self.update()
        spaceNames=[]
        for spaceNodeName in spaceNodeNames:
            spaceName=self.repeatName.replace("node",spaceNodeName)
            spaceNames.append(spaceName)
        space_list=self.transSpace_create_list(spaceNames)
        for space in space_list:
            self.transSet_edit_obj(space,target)
        return space_list
    
    def __createSettingCtrl(self,ctrlNodeName,target):
        self.update()
        ctrlName=self.repeatName.replace("node",ctrlNodeName)
        ctrl_obj=self.ctrlShape_create_obj(ctrlName)
        self.transSet_edit_obj(ctrl_obj,target)
        return ctrl_obj

    def __createNodes(self):
        self.parent=self.getParent_query_obj(self.object)  # select joint
        offset_list=self.__createSettingSpaces([self.offsetNodeName],self.parent)
        space_list=self.__createSettingSpaces(self.spaceNodeNames,self.object)
        ctrl_obj=self.__createSettingCtrl(self.ctrlNodeName,self.object)
        trs_list=self.__createSettingSpaces([self.trsNodeName],self.object)

        self.addAttrIntLimit_create_attrName(trs_list[0],self.attrName,min=0,max=1,defaultValue=1)
        self.addAttrIntLimit_create_attrName(ctrl_obj,self.attrName,min=0,max=1,defaultValue=1)
        cmds.connectAttr(ctrl_obj+"."+self.attrName,trs_list[0]+"."+self.attrName)

        # create hierarchy list
        space_list.insert(0,offset_list[0])
        space_list.append(ctrl_obj)
        space_list.append(trs_list[0])
        hierarchy=space_list # Variables are changed because roles have changed.

        # create hierarchy
        firstParent=self.listHierarchy_edit_obj(hierarchy)
        grp=self.ctrlGrp_create_obj()
        cmds.parent(firstParent,grp)

        return offset_list[0],trs_list[0]

    def offsetCtrlRoot(self):
        offset,trs=self.__createNodes()
        # connect pointConstraint and orientConstraint
        self.posConstraint_create_func(trs,self.object)

    def offsetCtrl(self):
        offset,trs=self.__createNodes()
        self.posConstraint_create_func(trs,self.object)
        self.posConstraint_create_func(self.parent,offset)

    def aimsetCtrlRoot(self):
        offset,trs=self.__createNodes()
        self.psConstraint_create_func(trs,self.object)
        if self.parent != self.object:
            cmds.pointConstraint(self.parent,offset)
    
    def aimsetCtrl(self):
        offset,trs=self.__createNodes()
        up_obj=self.__createSettingCtrl(self.upNodeName,self.parent)
        cmds.parent(up_obj,offset)
        cmds.select(up_obj)
        cmds.move(self.vector_dict[self.upVector][0],self.vector_dict[self.upVector][1],self.vector_dict[self.upVector][2],r=True,os=True,wd=True)

        # connect pointConstraint and aimConstraint
        self.psConstraint_create_func(trs,self.object)
        cmds.pointConstraint(self.parent,offset)
        cmds.aimConstraint(trs,self.parent,aim=self.vector_dict[self.aimVector],u=self.vector_dict[self.upVector],wut="object",wuo=up_obj,w=1)

    def getParent_query_obj(self,obj):
        parent=cmds.listRelatives(obj,p=True)
        if parent == None:
            return obj
        else:
            return parent[0]

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

    def transSet_edit_obj(self,source,target):
        cmds.parent(source,target)
        cmds.setAttr(source+".translate",0,0,0,type="double3")
        cmds.setAttr(source+".rotate",0,0,0,type="double3")
        cmds.parent(source,w=True)
        return source

    def ctrlGrp_create_obj(self):
        if not cmds.objExists("ctrl_grp"):
            grp=cmds.createNode("transform",n="ctrl_grp")
            return grp
        else:
            grp="ctrl_grp"
            return grp

    def transSpace_create_list(self,names=[]):
        trsNodes=[]
        for name in names:
            trsNode=cmds.createNode("transform",n=name)
            trsNodes.append(trsNode)
        return trsNodes
    
    # Plans to create classes in the future
    def ctrlShape_create_obj(self,name=""):
        ctrlName=cmds.curve(p=[(0,1.11,0),(0,0.78,-0.78),(0,0,-1.11),(0,-0.78,-0.78),(0,-1.11,0),(0,-0.78,0.78),(0,0,1.11),(0,0.78,0.78),(0,1.11,0)])
        ctrlNode=cmds.rename(ctrlName,name)
        return ctrlNode
    
    # Plans to create classes in the future
    def ctrlShape_create_obj(self,name=""):
        ctrlName=cmds.curve(p=[(0,1.11,0),(0,0.78,-0.78),(0,0,-1.11),(0,-0.78,-0.78),(0,-1.11,0),(0,-0.78,0.78),(0,0,1.11),(0,0.78,0.78),(0,1.11,0)])
        ctrlNode=cmds.rename(ctrlName,name)
        return ctrlNode
    
    # Plans to create classes in the future
    def ctrlShape_create_obj(self,name=""):
        ctrlName=cmds.curve(p=[(0,1.11,0),(0,0.78,-0.78),(0,0,-1.11),(0,-0.78,-0.78),(0,-1.11,0),(0,-0.78,0.78),(0,0,1.11),(0,0.78,0.78),(0,1.11,0)])
        ctrlNode=cmds.rename(ctrlName,name)
        return ctrlNode

    def posConstraint_create_func(self,source,target):
        cmds.pointConstraint(source,target)
        cmds.orientConstraint(source,target)
        #cmds.scaleConstraint(source,target)

    def psConstraint_create_func(self,source,target):
        pointC=cmds.pointConstraint(source,target)[0]
        attrName="pointConstraintSwitch"
        cmds.connectAttr(source+"."+attrName,pointC+"."+source+"W0")
        #cmds.scaleConstraint(source,target)

    def addAttr_check_bool(self,node,attr):
        attr_bool=cmds.attributeQuery(attr,node=node,exists=True)
        return attr_bool

    def addAttrIntLimit_create_attrName(self,obj,name,niceName=None,min=0,max=1,defaultValue=0):
        attr_bool=self.addAttr_check_bool(obj,name)
        if attr_bool:
            cmds.setAttr(obj+"."+name,keyable=True)
        else:
            cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="long",min=min,max=max,dv=defaultValue)
            cmds.setAttr(obj+"."+name,keyable=True)
        return name
        
class OldCtrlParent():
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

        """ aimCtrl
        cmds.pointConstraint(parent,offset)
        cmds.pointConstraint(bendCtrl,obj)
        cmds.aimConstraint(bendCtrl,parent,aim=[0,-1,0],u=[0,0,1],wut="object",wuo="up",w=1)
        """

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

    def aimConstraint_create_func(self,sourceCtrl,targetJoint,parentJoint,offsetTrs):
        cmds.pointConstraint(parentJoint,offsetTrs)
        cmds.pointConstraint(sourceCtrl,targetJoint)
        cmds.aimConstraint(sourceCtrl,parentJoint,aim=[0,-1,0],u=[0,0,1],wut="object",wuo="up",w=1)