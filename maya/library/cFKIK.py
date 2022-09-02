# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

def threeBoneFKIK_edit_func(start,middle,end):
    pass

def worldParent_check_object(obj):
    try:
        cmds.parent(obj,w=True)
        return obj
    except RuntimeError:
        return obj

def duplicateSolo_create_func(obj,names):
    duplicate_list=[]
    for name in names:
        dup=cmds.duplicate(obj,n=name or obj,po=True)
        dup=worldParent_check_object(dup)
        duplicate_list.append(dup[0])
    duplicate_list.append(obj)
    return duplicate_list

#{"FK":FK_joint,"IK":FK_joint,"jnt":joint,"UI":object,"blend":str(node_pbld_pos)}
def connectFKIKJoint_edit_func(UI,FK,IK,jnt,blend_name="pbld"):
    blend_node=cmds.createNode("pairBlend",n=blend_name)
    cmds.setAttr(blend_node+".rotInterpolation",1)
    cmds.connectAttr(UI+".fkik",blend_node+".weight",f=True)
    cmds.connectAttr(IK+".rotate",blend_node+".inRotate1",f=True)
    cmds.connectAttr(FK+".rotate",blend_node+".inRotate2",f=True)
    cmds.connectAttr(blend_node+".outRotate",jnt+".rotate",f=True)

#{"UI":object,"ctrl":object,"switch":"FK"or"IK"}
def switchFKIKConnect_edit_func(ui,ctrl,switch):
    if switch == "FK":
        shapes=cmds.listRelatives(ctrl,s=True)
        for shape in shapes:
            cmds.connectAttr(ui+".fkik",shape+".visibility")
    elif switch == "IK":
        shapes=cmds.listRelatives(ctrl,s=True)
        for shape in shapes:
            reverse_node=cmds.createNode("reverse",n=ctrl.replace("ctrl","rev"))
            cmds.connectAttr(ui+".fkik",reverse_node+".input.inputX")
            cmds.connectAttr(reverse_node+".output.outputX",shape+".visibility")

#{"startJoint":joint,"endJoint":joint,"handleCtrl":object,"poleCtrl":object},
def IKHandle_create_func(startJoint,endJoint,handleCtrl,poleCtrl):
    handle_node=cmds.ikHandle(sj=startJoint,ee=endJoint,n=handleCtrl.replace("ctrl","handle"),p=2)
    cmds.rename(handle_node[1],handle_node[0].replace("handle","effe"))
    cmds.parent(handle_node[0],handleCtrl)
    cmds.orientConstraint(handleCtrl,endJoint,n=handleCtrl.replace("ctrl","orc"),mo=True,w=1)
    cmds.poleVectorConstraint(poleCtrl,handle_node[0],n=handle_node[0].replace("handle","plvct"),w=1)

#{"dagObj":dagObject,"findName":str,"type":nodeType}
def findNode_query_list(dagObj,type,findName=None):
    if findName is None or findName is "":
        node_list=cmds.listRelatives(dagObj,ad=True,f=True,type=type)
    else :
        node_list=cmds.listRelatives(dagObj,ad=True,type=type)
        newNode_list=[node for node in node_list if findName in node]
        return newNode_list

#handle_node=cmds.ikHandle(sj='collarAIK_jnt_R',ee='wristAIK_jnt_R',sol="ikSplineSolver",scv=False,n="wristAIK_handle_R")
def IKSpline_create_func(startJoint,endJoint,handleCtrl):
    handle_node=cmds.ikHandle(sj=startJoint,ee=endJoint,sol="ikSplineSolver",scv=False,n=handleCtrl.replace("ctrl","handle"))
    effector_node=cmds.rename(handle_node[1],handle_node[0].replace("handle","effe"))
    curve_node=cmds.rename(handle_node[2],handle_node[0].replace("handle","curve"))
    grp=cmds.group([handle_node,curve_node],n=handleCtrl.replace("ctrl","grp"))
    cmds.parent(grp,"spine01_ctrl_C")

splines=[
{"startJoint":"collarAIK_jnt_L","endJoint":"wristAIK_jnt_L","handleCtrl":"collarAIK_ctrl_L"},
{"startJoint":"collarBIK_jnt_L","endJoint":"wristBIK_jnt_L","handleCtrl":"collarBIK_ctrl_L"},
{"startJoint":"collarAIK_jnt_R","endJoint":"wristAIK_jnt_R","handleCtrl":"collarAIK_ctrl_R"},
{"startJoint":"collarBIK_jnt_R","endJoint":"wristBIK_jnt_R","handleCtrl":"collarBIK_ctrl_R"},
]

for spline in splines:
    IKSpline_create_func(spline["startJoint"],spline["endJoint"],spline["handleCtrl"])