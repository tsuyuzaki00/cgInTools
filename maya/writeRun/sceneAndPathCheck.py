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
    geos=cmds.ls(cmds.listRelatives(mesh_shapes,parent=True),l=True)
    chackAttr_dicts=[
        {"attr":"aiSubdivType","same":1},
        {"attr":"aiSubdivIterations","same":1},
        {"attr":"aiSubdivUvSmoothing","same":1},
    ]
    for geo in list(set(geos)):
        for chackAttr_dict in chackAttr_dicts:
            check.setNode(geo)
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

def readPath_check_func():
    file_paths=cmds.filePathEditor(q=True,listDirectories="")
    check=chLB.Check()
    check.setSame(os.path.normpath("N:/GMR/source/pub/assets"))
    for file_path in file_paths:
        file_path=os.path.normpath(file_path)
        check.setRelation(file_path)
        judge_dict=check.includedString()
        if judge_dict["bool"]:
            print("OK:"+" relation:"+str(judge_dict["relation"])+" same:"+str(judge_dict["same"]))
        else:
            print("NG:"+" relation:"+str(judge_dict["relation"])+" same:"+str(judge_dict["same"]))

def readFile_check_func():
    #----------------------------------------------------------
    file_paths=cmds.filePathEditor(q=True,listDirectories="")
    same_dicts=[]
    check=chLB.Check()
    check.setSame(os.path.normpath("N:/GMR/source/pub/assets"))
    for file_path in file_paths:
        file_path=os.path.normpath(file_path)
        check.setRelation(file_path)
        judge_dict=check.includedString()
        if judge_dict["bool"]:
            same_dicts.append(judge_dict)
    #----------------------------------------------------------
    check=chLB.Check()
    for same_dict in same_dicts:
        file_names=cmds.filePathEditor(q=True,listFiles=same_dict["relation"],withAttribute=True)
        twoTake=iter(file_names)
        for file,node in zip(twoTake,twoTake):
            full_path=os.path.normpath(os.path.join(same_dict["relation"],file)) 
            check.setRelation(full_path)
            judge_dict=check.thePath()
            judge_dict["node"]=node
            if judge_dict["bool"]:
                print("OK:"+" node:"+str(judge_dict["node"])+" relation:"+str(judge_dict["relation"]))
            else:
                print("NG:"+" node:"+str(judge_dict["node"])+" relation:"+str(judge_dict["relation"]))


def UDIM_check_func():
    #----------------------------------------------------------
    file_paths=cmds.filePathEditor(q=True,listDirectories="")
    same_dicts=[]
    check=chLB.Check()
    check.setSame(os.path.normpath("N:/GMR/source/pub/assets"))
    for file_path in file_paths:
        file_path=os.path.normpath(file_path)
        check.setRelation(file_path)
        judge_dict=check.includedString()
        if judge_dict["bool"]:
            same_dicts.append(judge_dict)
    #----------------------------------------------------------
    """
    check=chLB.Check()
    file_dicts=[]
    for same_dict in same_dicts:
        file_names=cmds.filePathEditor(q=True,listFiles=same_dict["relation"],withAttribute=True)
        twoTake=iter(file_names)
        for file,obj in zip(twoTake,twoTake):
            full_path=os.path.normpath(os.path.join(same_dict["relation"],file))
            check.setRelation(full_path)
            judge_dict=check.thePath()
            judge_dict["object"]=obj
            if judge_dict["bool"]:
                file_dicts.append(judge_dict)
    #----------------------------------------------------------
    check=chLB.Check()
    for file_dict in file_dicts:
        full_path=os.path.normpath(file_dict["relation"])
        file=os.path.basename(full_path)
        if '<udim>' in file.lower():
            regex = file.replace(r'<udim>', r'\d{4}').replace(r'<UDIM>', r'\d{4}')
            for f in os.listdir(filedir):
                if re.match(regex, f):
                    for udim_file in udim_files:
                        udimfullpath = os.path.join(filedir,udim_file)
                        if not os.path.isfile(udimfullpath):
                            print(udimfullpath)
    """
    #----------------------------------------------------------
    check=chLB.Check()
    file_dicts=[]
    for same_dict in same_dicts:

        file_names=cmds.filePathEditor(q=True,listFiles=same_dict["relation"],withAttribute=True)
        image_path=os.path.normpath(os.path.join(same_dict["relation"]))
        twoTake=iter(file_names)
        for file,obj in zip(twoTake,twoTake):
            if '<udim>' in file.lower():
                regex=file.replace(r'<udim>',r'\d{4}').replace(r'<UDIM>',r'\d{4}')
                try:
                    for image in os.listdir(image_path):
                        if re.match(regex,image):
                            print("OK:"+regex,obj)
                        else:
                            print("NG:"+regex,obj)
                except:
                    pass
def test():
    image_path=os.path.normpath(os.path.join("N:/GMR/source/pub/assets/Chr/operatorMob1/Maps/GMR_Chr_operatorMob1_Mdl_19170"))
    file_names=cmds.filePathEditor(q=True,listFiles=image_path,withAttribute=True)
    OK_nodes=[]
    NG_nodes=[]
    judge_dicts=[]
    twoTake=iter(file_names)
    for file,node in zip(twoTake,twoTake):
        if '<udim>' in file.lower():
            file=file.replace(r'<udim>',r'\d{4}').replace(r'<UDIM>',r'\d{4}')
        for image in os.listdir(image_path):
            if re.match(file,image):
                OK_nodes.append(node)
                judge_dict={"bool":True,"node":node,"relation":file,"same":image}
                judge_dicts.append(judge_dict)
            else:
                judge_dict={"bool":False,"node":node,"relation":file,"same":image}
                judge_dicts.append(judge_dict)
    
    for judge_dict in judge_dicts:
        if judge_dict["bool"]:
            #print("OK:"+" node:"+str(judge_dict["node"])+" same:"+str(judge_dict["same"]))
            pass
        else:
            NG_nodes.append(judge_dict["bool"])
            
    print(set(OK_nodes)-set(NG_nodes))
            


    #difference=list(set(ok_dicts["node"])-set(ng_dicts["node"]))
    #if difference==[]:
        #print("OK")
    #else:
        #print("NG")


def main():
    #fileName_check_func()
    #pathName_check_func()
    #samePathAndSceneName_check_func()
    #sameObjName_check_func()
    #graySameRigName_check_func()
    #arnoldSetting_check_func()
    #inheritances_check_func()
    #trashReferences_check_func()
    #nodeUnLocked_check_func()
    #readPath_check_func()
    #readFile_check_func()
    #UDIM_check_func()
    test()
    pass

main()