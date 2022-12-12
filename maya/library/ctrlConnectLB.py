# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

import cgInTools as cit
from cgInTools.maya.library import setBaseLB as sbLB
from cgInTools.maya.library import namingLB as nLB
from cgInTools.maya.library import curveLB as cLB
cit.reloads([sbLB,nLB,cLB])

class CtrlParent(sbLB.BaseObject):
    def __init__(self):
        self._object=""
        self._parent=""
        self._aimVector="+X"
        self._upVector="+Y"
        self.__vector_dict={
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
    
    def __loading(self):
        self._spaceNodeNames=["null","space"]
        self._offsetNodeName="offset"
        self._trsNodeName="trs"
        self._ctrlNodeName="ctrl"
        self._holdNodeName="hold"
        self._upNodeName="up"
        self._pointSwitchName="pointConstraintSwitch"
        self._offsetSwitchName="childConstraintSwitch"

    def __createNodes(self):
        self.__loading()
        # createNames
        offsetName=self.getRename_edit_func(self._object,self._offsetNodeName)
        spaceNames=[]
        for _spaceNodeName in self._spaceNodeNames:
            spaceName=self.getRename_edit_func(self._object,_spaceNodeName)
            spaceNames.append(spaceName)
        ctrlName=self.getRename_edit_func(self._object,self._ctrlNodeName)
        trsName=self.getRename_edit_func(self._object,self._trsNodeName)

        # createNodes
        self._parent=self.getParent_query_obj(self._object)  # select joint
        offset_obj=cmds.createNode("transform",n=offsetName)
        self.transSet_edit_obj(offset_obj,self._parent)
        
        space_objs=[]
        for spaceName in spaceNames:
            space_obj=cmds.createNode("transform",n=spaceName)
            self.transSet_edit_obj(space_obj,self._object)
            space_objs.append(space_obj)

        ctrl_obj=self.ctrlShape_create_obj(ctrlName)
        self.transSet_edit_obj(ctrl_obj,self._object)
        
        trs_obj=cmds.createNode("transform",n=trsName)
        self.transSet_edit_obj(trs_obj,self._object)

        self.addAttrIntLimit_create_pointSwitchName(trs_obj,self._pointSwitchName,min=0,max=1,defaultValue=1)
        self.addAttrIntLimit_create_pointSwitchName(ctrl_obj,self._pointSwitchName,min=0,max=1,defaultValue=1)
        cmds.connectAttr(ctrl_obj+"."+self._pointSwitchName,trs_obj+"."+self._pointSwitchName)

        # create hierarchy list
        hierarchy=[]
        hierarchy.append(offset_obj)
        for space_obj in space_objs:
            hierarchy.append(space_obj)
        hierarchy.append(ctrl_obj)
        hierarchy.append(trs_obj)

        # create hierarchy
        firstParent=self.listHierarchy_edit_obj(hierarchy)
        self._grp=self.ctrlGrp_create_obj("ctrl_grp")
        cmds.parent(firstParent,self._grp)
        return offset_obj,trs_obj

    #Public Function
    def offsetCtrlRoot(self):
        offset_obj,trs_obj=self.__createNodes()
        # connect pointConstraint and orientConstraint
        self.posConstraint_create_func(trs_obj,self._object)

    def offsetCtrl(self):
        offset_obj,trs_obj=self.__createNodes()
        self.posConstraint_create_func(trs_obj,self._object)
        self.posConstraint_create_func(self._parent,offset_obj)

    def aimsetCtrlRoot(self):
        offset_obj,trs_obj=self.__createNodes()
        grp=self.ctrlGrp_create_obj("up_grp")
        cmds.parent(grp,self._grp)
        self.psConstraint_create_func(trs_obj,self._object,trs_obj,self._pointSwitchName)
        if self._parent != self._object:
            cmds.pointConstraint(self._parent,offset_obj)
    
    def aimsetCtrl(self):
        offset_obj,trs_obj=self.__createNodes()

        grp=self.ctrlGrp_create_obj("up_grp")

        holdName=self.getRename_edit_func(self._parent,self._holdNodeName)
        hold_obj=cmds.createNode("transform",n=holdName)
        self.transSet_edit_obj(hold_obj,self._parent)
        
        upName=self.getRename_edit_func(self._parent,self._upNodeName)
        up_obj=self.ctrlUp_create_obj(upName)
        self.transSet_edit_obj(up_obj,self._parent)

        self.addAttrIntLimit_create_pointSwitchName(offset_obj,self._offsetSwitchName,min=0,max=1,defaultValue=1)
        self.addAttrIntLimit_create_pointSwitchName(up_obj,self._offsetSwitchName,min=0,max=1,defaultValue=1)

        hierarchy=[grp,hold_obj,up_obj]
        self.listHierarchy_edit_obj(hierarchy)
        
        cmds.select(up_obj)
        cmds.move(self.__vector_dict[self._upVector][0],self.__vector_dict[self._upVector][1],self.__vector_dict[self._upVector][2],r=True,os=True,wd=True)

        # connect pointConstraint and aimConstraint
        self.psConstraint_create_func(trs_obj,self._object,trs_obj,self._pointSwitchName)
        self.psConstraint_create_func(self._parent,offset_obj,offset_obj,self._offsetSwitchName)
        cmds.pointConstraint(self._parent,hold_obj)
        cmds.aimConstraint(trs_obj,self._parent,aim=self.__vector_dict[self._aimVector],u=self.__vector_dict[self._upVector],wut="object",wuo=up_obj,w=1)
        cmds.connectAttr(up_obj+"."+self._offsetSwitchName,offset_obj+"."+self._offsetSwitchName)

    #Private Function
    def _createNames(self):
        spaceNames=[]
        for _spaceNodeName in self._spaceNodeNames:
            spaceName=self.getRename_edit_func(self._object,_spaceNodeName)
            spaceNames.append(spaceName)
        offsetName=self.getRename_edit_func(self._object,self._offsetNodeName)
        ctrlName=self.getRename_edit_func(self._object,self._ctrlNodeName)
        trsName=self.getRename_edit_func(self._object,self._trsNodeName)

    #Single Function
    def getRename_edit_func(self,object,node):
        name=nLB.Naming()
        name.setSwitch("setAuto")
        name.setOrders(["title","node","side"])
        name.setObject(object)
        name.setTitle(name._titleName_query_str(object,False))
        name.setSide(name.sideName_query_str(object))
        name.setNode(node)
        rename=name.getRename()
        return rename

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

    def ctrlGrp_create_obj(self,grpName):
        if not cmds.objExists(grpName):
            grp_obj=cmds.createNode("transform",n=grpName)
            return grp_obj
        else:
            grp_obj=grpName
            return grp_obj

    def transSpace_create_list(self,names=[]):
        trsNodes=[]
        for name in names:
            trsNode=cmds.createNode("transform",n=name)
            trsNodes.append(trsNode)
        return trsNodes
    
    # Plans to create classes in the future
    def ctrlUp_create_obj(self,name=""):
        xu=(1,0,0)
        xd=(-1,0,0)
        yu=(0,1,0)
        yd=(0,-1,0)
        zu=(0,0,1)
        zd=(0,0,-1)
        points=[xu,zd,xd,zu,xu,yu,xd,yd,xu,zd,yu,zu,yd,zd,xu]
        ctrlName=cmds.curve(d=1,p=points)
        ctrlNode=cmds.rename(ctrlName,name)
        return ctrlNode
    
    # Plans to create classes in the future
    def ctrlShape_create_obj(self,name=""):
        a01=(1,1,1)
        a02=(1,1,-1)
        a03=(-1,1,-1)
        a04=(-1,1,1)
        b01=(1,-1,1)
        b02=(1,-1,-1)
        b03=(-1,-1,-1)
        b04=(-1,-1,1)
        points=[a01,a02,a03,a04,a01,b01,b02,a02,b02,b03,a03,b03,b04,a04,b04,b01,a01]
        ctrlName=cmds.curve(d=1,p=points)
        ctrlNode=cmds.rename(ctrlName,name)
        return ctrlNode

    def posConstraint_create_func(self,source,target):
        cmds.pointConstraint(source,target)
        cmds.orientConstraint(source,target)
        cmds.scaleConstraint(source,target)

    def psConstraint_create_func(self,source,target,connect,attrName):
        pointC=cmds.pointConstraint(source,target)[0]
        cmds.connectAttr(connect+"."+attrName,pointC+"."+source+"W0")
        cmds.scaleConstraint(source,target)

    def addAttr_check_bool(self,node,attr):
        attr_bool=cmds.attributeQuery(attr,node=node,exists=True)
        return attr_bool

    def addAttrIntLimit_create_pointSwitchName(self,obj,name,niceName=None,min=0,max=1,defaultValue=0):
        attr_bool=self.addAttr_check_bool(obj,name)
        if not attr_bool:
            cmds.addAttr(obj,ln=name,nn=name.capitalize() or niceName,at="long",min=min,max=max,dv=defaultValue)
        cmds.setAttr(obj+"."+name,keyable=True)
        return name
 