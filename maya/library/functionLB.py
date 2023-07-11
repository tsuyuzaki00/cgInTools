# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import maya.api.OpenMayaAnim as oma2
import sys,math

import cgInTools as cit
from ...library import jsonLB as jLB
cit.reloads([jLB])

def childTypes_query_strs(obj,nodeType):
    childs=cmds.ls(obj,sl=True,dag=True,type=nodeType)
    if nodeType == "nurbsCurve" or nodeType == "mesh" or nodeType == "nurbsSurface":
        transforms=[cmds.listRelatives(child,p=True,type="transform")[0] for child in childs]
        childs=transforms
    return childs
    
def removeIncludedNames_query_strs(names,removes=[]):
    newNames=[item for item in names if not any(substring in item for substring in removes)]
    return newNames

def _childSelections_query_strs(nodeType="transform",removes=[]):
    objs=cmds.ls(sl=True)
    selects=[]
    for obj in objs:
        childs=childTypes_query_strs(obj,nodeType)
        newChilds=removeIncludedNames_query_strs(childs,removes)
        cmds.select(newChilds,add=True)
        for newChild in newChilds:
            selects.append(newChild)
    return selects

def splineIKJoints_create_dict(self,joints,renameType="jnt"):
        splineIK_dict={}
        jointPosition_lists=[cmds.xform(joint,q=True,ws=True,t=True) for joint in joints]
        
        crv=cmds.curve(ep=jointPosition_lists,n=joints[0].replace(renameType,"crv"))
        shape=cmds.listRelatives(crv,s=True)[0]
        cmds.rename(shape,crv+"Shape")
        ikHandleName_str=crv.replace("crv","ikhl")
        ikEffectorName_str=crv.replace("crv","ikef")
        
        hdl,eff=cmds.ikHandle(sol='ikSplineSolver',ccv=False,pcv=False,sj=joints[0],ee=joints[-1],curve=crv,n=ikHandleName_str)
        eff=cmds.rename(eff,ikEffectorName_str)
        
        splineIK_dict["curve"]=crv
        splineIK_dict["ikHandle"]=hdl
        splineIK_dict["ikEffector"]=eff
        return splineIK_dict

def setMultMatrix(node,matrixAttr,mumx,num):
    node_matrix=cmds.getAttr(node+"."+matrixAttr)
    cmds.setAttr(mumx+".matrixIn["+str(num)+"]",node_matrix,type="matrix")
