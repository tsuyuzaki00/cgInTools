# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import cgInTools as cit
from cgInTools.maya.library import checkLB as chLB
cit.reloads([chLB])

import os

def fileUnderCount_check_func(maxLimit=6):
    check=chLB.Check()
    check.setMaxLimit(maxLimit)
    judge_dict=check.fileUnderCount()
    if judge_dict["bool"]:
        #print("OK:"+" relation:"+str(judge_dict["relation"])+" max:"+str(judge_dict["maxLimit"]))
        pass
    else:
        print("NG:"+"fileUnderCount relation:"+str(judge_dict["relation"])+" max:"+str(judge_dict["maxLimit"]))
    
def pathUnderCount_check_func(maxLimit=10):
    check=chLB.Check()
    check.setMaxLimit(maxLimit)
    judge_dict=check.pathUnderCount()
    if judge_dict["bool"]:
        #print("OK:"+" relation:"+str(judge_dict["relation"])+" max:"+str(judge_dict["maxLimit"]))
        pass
    else:
        print("NG:"+"pathUnderCount relation:"+str(judge_dict["relation"])+" max:"+str(judge_dict["maxLimit"]))

def samePathAndSceneName_check_func(same_dicts=[{"relation":"","same":""}]):
    file_path=cmds.file(q=True,sn=True)
    ma_file = os.path.basename(file_path)
    pathParts_list = file_path.lower().split('/')
    nameParts_list = ma_file.replace('.ma','').lower().split('_')
    same_dicts=same_dicts or [
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
            #print("OK:"+" relation:"+str(judge_dict["relation"])+" same:"+str(judge_dict["same"]))
            pass
        else:
            print("NG:"+"samePathAndSceneName relation:"+str(judge_dict["relation"])+" same:"+str(judge_dict["same"]))

def sameObjName_check_func():
    check=chLB.Check()
    dagNodes=cmds.ls(dag=True)
    for dagNode in dagNodes:
        check.setNode(dagNode)
        judge_dict=check.sameObjName()
        if judge_dict["bool"]:
            #print("OK:"+" node:"+str(judge_dict["node"]))
            pass
        else:
            print("NG:"+"sameObjName node:"+str(judge_dict["node"]))

def graySameRigName_check_func(hierarchyName="rig",hierarchyNumber=2):
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
            print("NG:"+"SameRigName node:"+str(judge_dict["node"]))

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
            #print("OK:"+" reference:"+str(judge_dict["reference"])+" scene:"+str(judge_dict["scene"]))
            pass
        else:
            print("NG:"+"trashReferences reference:"+str(judge_dict["reference"])+" scene:"+str(judge_dict["scene"]))

def nodeUnLocked_check_func(node="initialShadingGroup"):
    check=chLB.Check()
    check.setNode(node)
    judge_dict=check.nodeUnLocked()
    judge_dict["node"]=node
    if judge_dict["bool"]:
        #print("OK:"+" node:"+str(judge_dict["node"]))
        pass
    else:
        print("NG:"+"nodeUnLocked node:"+str(judge_dict["node"]))
 
def arnoldSetting_check_func(chackAttr_dicts=[{"attr":"","same":""}]):
    check=chLB.Check()
    mesh_shapes=cmds.ls(type="mesh")
    geos=cmds.ls(cmds.listRelatives(mesh_shapes,parent=True),l=True)
    chackAttr_dicts=[
        {"attr":"aiSubdivType","same":1},
        {"attr":"aiSubdivIterations","same":1},
        {"attr":"aiSubdivUvSmoothing","same":1},
    ] or chackAttr_dicts
    for geo in list(set(geos)):
        for chackAttr_dict in chackAttr_dicts:
            check.setNode(geo)
            check.setAttr(chackAttr_dict["attr"])
            check.setSame(chackAttr_dict["same"])
            check.setEdit(False)
            judge_dict=check.attrSame()
            if judge_dict["bool"]:
                #print("OK:"+judge_dict["node"]+"."+judge_dict["attr"]+","+str(judge_dict["relation"]))
                pass
            else:
                print("NG:"+"nodeUnLocked "+judge_dict["node"]+"."+judge_dict["attr"]+","+str(judge_dict["relation"]))

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
            print("NG:"+"inheritances node:"+judge_dict["node"]+" relation:"+str(judge_dict["relation"]))
        else:
            #print("OK:"+judge_dict["node"]+" relation:"+str(judge_dict["relation"]))
            pass

def readPath_check_func(absolute_paths=["N:\\GMR\\source\\pub\\assets\\Shd","N:/GMR/source/pub/assets/Chr/operatorMob1/Maps"]):
    file_paths=cmds.filePathEditor(q=True,listDirectories="")
    check=chLB.Check()
    normpath_paths=[]
    for absolute_path in absolute_paths:
        normpath_paths.append(os.path.normpath(absolute_path))
    check.setSameList(normpath_paths)
    for file_path in file_paths:
        file_path=os.path.normpath(file_path)
        check.setRelation(file_path)
        judge_dict=check.andSameRelation()
        if judge_dict["bool"]:
            #print("OK:"+" relation:"+str(judge_dict["relation"])+" same:"+str(judge_dict["same"]))
            pass
        else:
            print("NG:"+"readPath relation:"+str(judge_dict["relation"])+" sameList:"+str(judge_dict["sameList"]))

def readFile_check_func():
    check=chLB.Check()
    file_paths=cmds.filePathEditor(q=True,listDirectories="")
    for file_path in file_paths:
        file_names=cmds.filePathEditor(q=True,listFiles=file_path,withAttribute=True)
        twoTake=iter(file_names)
        for file,node in zip(twoTake,twoTake):
            full_path=os.path.normpath(os.path.join(file_path,file)) 
            check.setRelation(full_path)
            judge_dict=check.thePath()
            judge_dict["node"]=node
            if judge_dict["bool"]:
                #print("OK:"+" node:"+str(judge_dict["node"])+" relation:"+str(judge_dict["relation"]))
                pass
            else:
                print("NG:"+"readFile node:"+str(judge_dict["node"])+" relation:"+str(judge_dict["relation"]))

def imagesUsed_check_func(image_path="N:/GMR/source/pub/assets/Chr/operatorMob1/Maps/GMR_Chr_operatorMob1_Mdl_19170"):
    same_list=[]
    image_path=os.path.normpath(os.path.join(image_path))
    file_names=cmds.filePathEditor(q=True,listFiles=image_path)
    for file_name in file_names:
        if '<udim>' in file_name.lower():
            file_name=file_name.replace(r'<udim>',r'\d{4}').replace(r'<UDIM>',r'\d{4}')
        same_list.append(file_name)

    relations=os.listdir(image_path)
    check=chLB.Check()
    check.setSameList(same_list)
    for relation in relations:
        check.setRelation(relation)
        judge_dict=check.andMatchRelation()
        if judge_dict["bool"]:
            #print("OK:"+" relation:"+str(judge_dict["relation"]))
            pass
        else:
            if ".*png" in judge_dict["relation"]:
                print("NG:"+"imagesUsed relation:"+str(judge_dict["relation"]))
            else:
                #print("OK:"+" relation:"+str(judge_dict["relation"]))
                pass

def main():
    fileUnderCount_check_func()
    pathUnderCount_check_func()
    samePathAndSceneName_check_func()
    sameObjName_check_func()
    graySameRigName_check_func()
    arnoldSetting_check_func()
    inheritances_check_func()
    trashReferences_check_func()
    nodeUnLocked_check_func()
    readPath_check_func()
    readFile_check_func()
    imagesUsed_check_func()
    pass

main()