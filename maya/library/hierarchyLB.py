# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from . import setBaseLB as sbLB
from . import namingLB as nLB
cit.reloads([sbLB,nLB])

class Hierarchy(sbLB.BaseHierarchy):
    def __init__(self):
        super(Hierarchy,self).__init__()
        self._rename=nLB.Naming()
        self._rename.setOrderList(["title","node","side"])
        self._rename.setSwitch("fullAuto")

    #Single Function
    def grpNodeChoise_query_list(self,grpNodes,choisNames):
        choiseNodes=[]
        for node in grpNodes:
            for choisName in choisNames:
                if choisName in node:
                    choiseNodes.append(node)
        return choiseNodes
        
    def objSence_check_string(self,objName):
        if cmds.objExists(objName):
            return objName
        else:
            cmds.error("There is no name for the group "+"'"+objName+"'")

    def addParentNull_create_null(self,obj,nodeName="move"):
        parent=cmds.listRelatives(obj,p=True)
        if not parent == None:
            parent=parent[0]
        null=cmds.createNode("transform",n=obj,p=parent,ss=True)
        getMatrix=cmds.xform(obj,q=True,m=True)
        cmds.xform(null,m=getMatrix)
        cmds.parent(obj,null)

        self._rename.setChoise(null)
        titleOnly_str=self._rename.titleHieName()

        self._rename.setSwitch("setAuto")
        self._rename.setObject(null)
        self._rename.setTitle(titleOnly_str)
        self._rename.setNode(nodeName)
        self._rename.setSide("")
        null=self._rename.rename()
        return null
    
    def addOffsetNull_create_null(self,obj,nodeName="offset"):
        parent=cmds.listRelatives(obj,p=True)
        if not parent == None:
            parent=parent[0]
        null=cmds.createNode("transform",n=obj,ss=True)
        getMatrix=cmds.xform(parent,q=True,m=True,a=True)
        cmds.xform(null,m=getMatrix)
        cmds.parent(null,parent)
        cmds.parent(obj,null)

        self._rename.setChoise(null)
        titleOnly_str=self._rename.titleHieName()

        self._rename.setSwitch("setAuto")
        self._rename.setObject(null)
        self._rename.setTitle(titleOnly_str)
        self._rename.setNode(nodeName)
        self._rename.setSide("")
        null=self._rename.rename()
        return null

    def deleteOnlyObj_edit_func(self,obj):
        parent_list=cmds.listRelatives(obj,p=True,pa=True)
        childs=cmds.listRelatives(obj,c=True,pa=True,typ="transform")
        if not childs == None:
            if not parent_list == None:
                parent=parent_list[0]
                cmds.parent(childs,parent)
            else:
                cmds.parent(childs,w=True)
        cmds.delete(obj)

    def listHierarchy_edit_str(self,objs=[]):
        parentObj=None
        for obj in objs:
            if parentObj is not None:
                cmds.parent(obj,parentObj)
                parentObj=obj
            else:
                parentObj=obj
                firstParent=obj
        return firstParent
    
    #Public Function
    def getObjsChoiseName(self):
        return self.grpNodeChoise_query_list(self,self._objs,self._choiseNames)

    def getObjsChoiseType(self):
        return cmds.ls(self._objs,type=self._choiseType)

    def group(self):
        grpName=cmds.group(self._objs,n=self._name)
        return grpName

    def groupChoiseName(self):
        choiseNodes=self.grpNodeChoise_query_list(self._objs,self._choiseNames)
        grpName=cmds.group(choiseNodes,n=self._name)
        return grpName

    def groupChoiseType(self):
        choiseNodes=cmds.ls(self._objs,type=self._choiseType)
        grpName=cmds.group(choiseNodes,n=self._name)
        return grpName

    def groupHierarchy(self):
        parent=self.listHierarchy_edit_str(self._objs)
        grpName=cmds.group(parent,n=self._name)
        return grpName

    def parent(self):
        parentName=self.objSence_check_string(self._name)
        cmds.parent(self._objs,parentName)
        return parentName

    def parentChoiseName(self):
        choiseNodes=self.grpNodeChoise_query_list(self._objs,self._choiseNames)
        parentName=self.objSence_check_string(self._name)
        cmds.parent(choiseNodes,parentName)
        return parentName

    def parentChoiseType(self):
        choiseNodes=cmds.ls(self._objs,type=self._choiseType)
        parentName=self.objSence_check_string(self._name)
        cmds.parent(choiseNodes,parentName)
        return parentName

    def parentHierarchy(self):
        parentName=self.objSence_check_string(self._name)
        parent=self.listHierarchy_edit_str(self._objs)
        cmds.parent(parent,parentName)
        return parentName

    def deleteOnlyObjs(self):
        for _obj in self._objs:
            self.deleteOnlyObj_edit_func(_obj)
    
    def addParentNull(self):
        nulls=[]
        for _obj in self._objs:
            null=self.addParentNull_create_null(_obj)
            nulls.append(null)
        return nulls
    
    def addOffsetNull(self):
        for _obj in self._objs:
            null=self.addOffsetNull_create_null(_obj)
            nulls.append(null)
        return nulls
