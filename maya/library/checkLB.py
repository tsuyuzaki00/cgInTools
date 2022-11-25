# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import cgInTools as cit
from cgInTools.maya.library import setBaseLB as sbLB
cit.reloads([sbLB])

import os
import re

class Check(sbLB.BaseCheck):
    def __init__(self):
        self._relation=""
        self._same=""
        self._same_list=[]
        self._maxLimit=100
        self._minLimit=0
        self._highLimit=100
        self._lowLimit=0
        self._edit=False
        self._node=""
        self._attr=""
        self._evaluation_dict={"bool":False}
    
#Public Function
    def attrSame(self):
        judge_dict=self.attrSame_check_dict(self._node,self._attr,self._same,self._edit)
        return judge_dict

    def sameRelation(self):
        judge_dict=self.sameRelation_check_dict(self._relation,self._same)
        return judge_dict

    def relationIsSame(self):
        judge_dict=self.relationIsSame_check_dict(self._relation,self._same)
        return judge_dict

    def includedString(self):
        judge_dict=self.includedString_check_dict(self._relation,self._same)
        return judge_dict

    def thePath(self):
        judge_dict=self.thePath_check_dict(self._relation)
        return judge_dict

    def minRelation(self):
        judge_dict=self.minRelation_check_dict(self._relation,self._minLimit)
        return judge_dict

    def maxRelation(self):
        judge_dict=self.maxRelation_check_dict(self._relation,self._maxLimit)
        return judge_dict

    def minMaxRelation(self):
        judge_dict=self.minMaxRelation_check_dict(self._relation,self._minLimit,self._maxLimit)
        return judge_dict

    def lowRelation(self):
        judge_dict=self.minRelation_check_dict(self._relation,self._lowLimit)
        return judge_dict

    def highRelation(self):
        judge_dict=self.maxRelation_check_dict(self._relation,self._highLimit)
        return judge_dict

    def pathUnderCount(self):
        judge_dict=self.pathUnderCount_check_dict(self._maxLimit)
        return judge_dict

    def fileUnderCount(self):
        judge_dict=self.fileUnderCount_check_dict(self._maxLimit)
        return judge_dict

    def nodeUnLocked(self):
        judge_dict=self.nodeUnLocked_check_dict(self._node)
        return judge_dict

    def sameObjName(self):
        judge_dict=self.sameObjName_check_dict(self._node)
        return judge_dict

    def trashReferences(self):
        judge_dict=self.trashReferences_check_dict(self._node)
        return judge_dict
    
    def andSameRelation(self):
        judge_dict=self.andSameRelation_check_dict(self._relation,self._same_list)
        return judge_dict
    
    def andMatchRelation(self):
        judge_dict=self.andMatchRelation_check_dict(self._relation,self._same_list)
        return judge_dict

#Private Function

#Mulch Function
    def pathUnderCount_check_dict(self,maxLimit):
        file_path=cmds.file(q=True,sn=True)
        pathParts_list=file_path.lower().split('/')
        judge_dict=self.nameUnderCount_check_dict(pathParts_list,maxLimit)
        return judge_dict

    def fileUnderCount_check_dict(self,maxLimit):
        file_path=cmds.file(q=True,sn=True)
        ma_file=os.path.basename(file_path)
        nameParts_list=ma_file.replace('.ma','').lower().split('_')
        judge_dict=self.nameUnderCount_check_dict(nameParts_list,maxLimit)
        return judge_dict

    def attrSame_check_dict(self,node,attr,same,edit=False):
        relation=cmds.getAttr(node+"."+attr)
        judge_dict=self.sameRelation_check_dict(relation,same)
        judge_dict["node"]=node
        judge_dict["attr"]=attr
        if edit:
            if judge_dict["bool"]:
                return judge_dict
            else:
                cmds.setAttr(node+"."+attr,same)
                return judge_dict
        else:
            return judge_dict

    def nameUnderCount_check_dict(self,relations,maxLimit):
        numRelation=len(relations)
        judge_dict=self.maxRelation_check_dict(numRelation,maxLimit)
        return judge_dict

#Single Function
    def sameRelation_check_dict(self,relation,same):
        evaluation_dict={"bool":False,"relation":relation,"same":same}
        if relation == same:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else:
            evaluation_dict["bool"]=False
            return evaluation_dict

    def relationIsSame_check_dict(self,relation,same):
        evaluation_dict={"bool":False,"relation":relation,"same":same}
        if relation is same:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else:
            evaluation_dict["bool"]=False
            return evaluation_dict

    def includedString_check_dict(self,relation,same):
        evaluation_dict={"bool":False,"relation":relation,"same":same}
        if same in relation:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else:
            evaluation_dict["bool"]=False
            return evaluation_dict

    def thePath_check_dict(self,relation):
        evaluation_dict={"bool":False,"relation":relation}
        if os.path.isdir(os.path.dirname(relation)):
            evaluation_dict["bool"]=True
            return evaluation_dict
        else:
            evaluation_dict["bool"]=False
            return evaluation_dict

    def minRelation_check_dict(self,relation,minLimit):
        evaluation_dict={"bool":False,"relation":relation,"minLimit":minLimit}
        if minLimit <= relation:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else:
            evaluation_dict["bool"]=False
            return evaluation_dict

    def maxRelation_check_dict(self,relation,maxLimit):
        evaluation_dict={"bool":False,"relation":relation,"maxLimit":maxLimit}
        if relation <= maxLimit:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else:
            evaluation_dict["bool"]=False
            return evaluation_dict

    def minMaxRelation_check_dict(self,relation,minLimit,maxLimit):
        evaluation_dict={"bool":False,"relation":relation,"minLimit":minLimit,"maxLimit":maxLimit}
        if minLimit <= relation and relation <= maxLimit:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else:
            evaluation_dict["bool"]=False
            return evaluation_dict

    def lowRelation_check_dict(self,relation,lowLimit):
        evaluation_dict={"bool":False,"relation":relation,"lowLimit":lowLimit}
        if relation < lowLimit:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else:
            evaluation_dict["bool"]=False
            return evaluation_dict

    def highRelation_check_dict(self,relation,highLimit):
        evaluation_dict={"bool":False,"relation":relation,"highLimit":highLimit}
        if highLimit < relation:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else:
            evaluation_dict["bool"]=False
            return evaluation_dict

    def nodeUnLocked_check_dict(self,node):
        evaluation_dict={"bool":False,"node":node}
        if cmds.lockNode(node,q=True)[0]:
            evaluation_dict["bool"]=False
            return evaluation_dict
        else:
            evaluation_dict["bool"]=True
            return evaluation_dict

    def sameObjName_check_dict(self,node):
        evaluation_dict={"bool":False,"node":node}
        if ':' in node:
            pass
        if '|' in node:
            evaluation_dict["bool"]=False
            return evaluation_dict
        else:
            evaluation_dict["bool"]=True
            return evaluation_dict

    def trashReferences_check_dict(self,node):
        evaluation_dict={"bool":False,"reference":node}
        try:
            cmds.referenceQuery(node,filename=True)
            evaluation_dict["bool"]=True
            return evaluation_dict
        except RuntimeError:
            evaluation_dict["bool"]=False
            return evaluation_dict

    def andSameRelation_check_dict(self,relation,same_list):
        judge_bools=[]
        judge_dict={"bool":False,"relation":relation,"sameList":same_list}
        for same in same_list:
            if same in relation:
                judge_bools.append(True)
        if True in judge_bools:
            judge_dict["bool"]=True
            return judge_dict
        else:
            judge_dict["bool"]=False
            return judge_dict

    def andMatchRelation_check_dict(self,relation,same_list):
        judge_bools=[]
        judge_dict={"bool":False,"relation":relation,"sameList":same_list}
        for same in same_list:
            if re.match(same,relation):
                judge_bools.append(True)
        if True in judge_bools:
            judge_dict["bool"]=True
            return judge_dict
        else:
            judge_dict["bool"]=False
            return judge_dict