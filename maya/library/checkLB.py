# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import cgInTools as cit
from cgInTools.maya.library import setBaseLB as sbLB
cit.reloads([sbLB])

import os
import re

class Check(sbLB.BaseCheck):
    def __init__(self):
        self._same=""
        self._max=100
        self._min=0
        self._relation=""
        self._edit=False
        self._node=""
        self._attr=""
        self._evaluation_dict={"bool":False,"relation":self._relation}
    
#Public Function
    def attrSame(self):
        judge_dict=self.attrSame_check_dict(self._node,self._attr,self._same,self._edit)
        return judge_dict

    def pathUnderCount(self):
        file_path=cmds.file(q=True,sn=True)
        pathParts_list=file_path.lower().split('/')
        judge_dict=self.nameUnderCount_check_dict(pathParts_list,self._max)
        return judge_dict

    def fileUnderCount(self):
        file_path=cmds.file(q=True,sn=True)
        ma_file=os.path.basename(file_path)
        nameParts_list=ma_file.replace('.ma','').lower().split('_')
        judge_dict=self.nameUnderCount_check_dict(nameParts_list,self._max)
        return judge_dict

#Private Function

#Mulch Function
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

    def nameUnderCount_check_dict(self,relations,max):
        numRelation=len(relations)
        judge_dict=self.maxRelation_check_dict(numRelation,max)
        return judge_dict

#Single Function
    def sameRelation_check_dict(self,relation,same):
        evaluation_dict={"bool":False,"relation":relation,"same":same}
        if relation is same:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else:
            evaluation_dict["bool"]=False
            return evaluation_dict

    def minRelation_check_dict(self,relation,min):
        evaluation_dict={"bool":False,"relation":relation,"min":min}
        if relation >= min:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else:
            evaluation_dict["bool"]=False
            return evaluation_dict

    def maxRelation_check_dict(self,relation,max):
        evaluation_dict={"bool":False,"relation":relation,"max":max}
        if relation <= max:
            evaluation_dict["bool"]=True
            return evaluation_dict
        else:
            evaluation_dict["bool"]=False
            return evaluation_dict

    def minMaxRelation_check_dict(self,relation,min,max):
        evaluation_dict={"bool":False,"relation":relation,"min":min,"max":max}
        if relation >= min and relation <= max:
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

    