# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import cgInTools as cit
from cgInTools.maya.library import checkLB as chLB
cit.reloads([chLB])

import os
import re

def fileName_check_func():
    check=chLB.Check()
    check.setMax(6)
    judge_dict=check.fileUnderCount()
    if judge_dict["bool"]:
        print("OK:"+" relation:"+str(judge_dict["relation"])+" max:"+str(judge_dict["maxLimit"]))
    else:
        print("NG:"+" relation:"+str(judge_dict["relation"])+" max:"+str(judge_dict["maxLimit"]))
    
def pathName_check_func():
    check=chLB.Check()
    check.setMax(10)
    judge_dict=check.pathUnderCount()
    if judge_dict["bool"]:
        print("OK:"+" relation:"+str(judge_dict["relation"])+" max:"+str(judge_dict["maxLimit"]))
    else:
        print("NG:"+" relation:"+str(judge_dict["relation"])+" max:"+str(judge_dict["maxLimit"]))

def samePathAndSceneName_check_func():
    file_path=cmds.file(q=True,sn=True)
    ma_file = os.path.basename(file_path)
    pathParts_list = file_path.lower().split('/')
    nameParts_list = ma_file.replace('.ma','').lower().split('_')
    same_dicts=[
        {"relation":nameParts_list[0],"same":pathParts_list[1].lower()},
        {"relation":nameParts_list[1],"same":pathParts_list[5].lower()},
        {"relation":nameParts_list[2],"same":pathParts_list[6].lower()},
        {"relation":nameParts_list[3],"same":pathParts_list[7].lower()},
    ]
    check=chLB.Check()
    for same_dict in same_dicts:
        check.setRelation(same_dict["relation"])
        check.setSame(same_dict["same"])
        judge_dict=check.sameRelation()
        if judge_dict["bool"]:
            print("OK:"+" relation:"+str(judge_dict["relation"])+" same:"+str(judge_dict["same"]))
        else:
            print("NG:"+" relation:"+str(judge_dict["relation"])+" same:"+str(judge_dict["same"]))

def sameObjName_check_func():
    check=chLB.Check()
    dagNodes=cmds.ls(dag=True)
    for dagNode in dagNodes:
        check.setNode(dagNode)
        judge_dict=check.sameObjName()
        if judge_dict["bool"]:
            print("OK:"+" node:"+str(judge_dict["node"]))
        else:
            print("NG:"+" node:"+str(judge_dict["node"]))

def graySameRigName_check_func():
    hierarchyName="rig"
    hierarchyNumber=2
    
    judge_dicts=[]
    dagNodes=cmds.ls(dag=True)
    for dagNode in dagNodes:
        evaluation_dict={"bool":False}
        if '|' in dagNode:
            evaluation_dict["node"]=dagNode
            if cmds.ls(dagNode,long=True)[0].split('|')[hierarchyNumber].lower()==hierarchyName:
                evaluation_dict["bool"]=True
                judge_dicts.append(evaluation_dict)
            else:
                evaluation_dict["bool"]=False
                judge_dicts.append(evaluation_dict)

    for judge_dict in judge_dicts:
        if judge_dict["bool"]:
            print("Gray:"+" node:"+str(judge_dict["node"]))
        else:
            print("NG:"+" node:"+str(judge_dict["node"]))

def trashReferences_check_func():
    file_path=cmds.file(q=True,sn=True)
    ma_file = os.path.basename(file_path)
    
    check=chLB.Check()
    refs=cmds.ls(type='reference')
    for ref in refs:
        check.setNode(ref)
        judge_dict=check.trashReferences()
        judge_dict["scene"]=ma_file
        if judge_dict["bool"]:
            print("OK:"+" reference:"+str(judge_dict["reference"])+" scene:"+str(judge_dict["scene"]))
        else:
            print("NG:"+" reference:"+str(judge_dict["reference"])+" scene:"+str(judge_dict["scene"]))

def nodeUnLocked_check_func():
    node="initialShadingGroup"
    check=chLB.Check()
    check.setNode(node)
    judge_dict=check.nodeUnLocked()
    judge_dict["node"]=node
    if judge_dict["bool"]:
        print("OK:"+" node:"+str(judge_dict["node"]))
    else:
        print("NG:"+" node:"+str(judge_dict["node"]))
 
def arnoldSetting_check_func():
    check=chLB.Check()
    mesh_shapes=cmds.ls(type="mesh")
    chackAttr_dicts=[
        {"attr":"aiSubdivType","same":1},
        {"attr":"aiSubdivIterations","same":1},
        {"attr":"aiSubdivUvSmoothing","same":1},
    ]
    for mesh_shape in mesh_shapes:
        for chackAttr_dict in chackAttr_dicts:
            check.setNode(mesh_shape)
            check.setAttr(chackAttr_dict["attr"])
            check.setSame(chackAttr_dict["same"])
            check.setEdit(False)
            judge_dict=check.attrSame()
            if judge_dict["bool"]:
                print("OK:"+judge_dict["node"]+"."+judge_dict["attr"]+","+str(judge_dict["relation"]))
            else:
                print("NG:"+judge_dict["node"]+"."+judge_dict["attr"]+","+str(judge_dict["relation"]))

def inheritances_check_func():
    shapes=cmds.ls(type='mesh')
    geos=cmds.ls(cmds.listRelatives(shapes,parent=True))
    check=chLB.Check()
    check.setSame(0)
    for geo in geos:
        ancestrals=cmds.ls(geo,long=True)[0].split('|')[1:-1]
        check.setRelation(len(ancestrals))
        judge_dict=check.sameRelation()
        judge_dict["node"]=geo
        if judge_dict["bool"]:
            print("NG:"+judge_dict["node"]+" relation:"+str(judge_dict["relation"]))
        else:
            print("OK:"+judge_dict["node"]+" relation:"+str(judge_dict["relation"]))

def main():
    #fileName_check_func()
    #pathName_check_func()
    #samePathAndSceneName_check_func()
    #sameObjName_check_func()
    #graySameRigName_check_func()
    #arnoldSetting_check_func()
    #inheritances_check_func()
    trashReferences_check_func()
    #nodeUnLocked_check_func()
    pass

main()