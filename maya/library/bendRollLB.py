# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
from . import namingLB as nLB
from . import setBaseLB as sbLB

#mel.eval('GoToBindPose;')

class BendRollCtrl(sbLB.BasePair):
    def __init__(self):
        self._sourceNode=""
        self._targetNode=""

    def __loading(self):
        getName=nLB.Naming()
        sourceTitle=getName._titleName_query_str(self._sourceNode)
        targetTitle=getName._titleName_query_str(self._targetNode)
        rotate_comx="_".join(["rotate","comx",sourceTitle,targetTitle])
        aimVector_comx="_".join(["aimVector","comx",sourceTitle,targetTitle])
        upVector_comx="_".join(["upVector","comx",sourceTitle,targetTitle])
        aimVector_mumx="_".join(["aimVector","mumx",sourceTitle,targetTitle])
        upVector_mumx="_".join(["upVector","mumx",sourceTitle,targetTitle])
        aimVector_demx="_".join(["aimVector","demx",sourceTitle,targetTitle])
        upVector_demx="_".join(["upVector","demx",sourceTitle,targetTitle])
        aimVectorRevers_fltm="_".join(["aimVectorRevers","fltm",sourceTitle,targetTitle])
        upVectorRevers_fltm="_".join(["upVectorRevers","fltm",sourceTitle,targetTitle])
        self.getBendAxisAngle_agbw="_".join(["getBendAxisAngle","agbw",sourceTitle,targetTitle])
        getRollAxisAngle_agbw="_".join(["getRollAxisAngle","agbw",sourceTitle,targetTitle])
        getBendQuat_atoq="_".join(["getBendQuat","atoq",sourceTitle,targetTitle])
        getRollQuat_atoq="_".join(["getRollQuat","atoq",sourceTitle,targetTitle])
        getBend_comx="_".join(["getBend","comx",sourceTitle,targetTitle])
        getUpVectorBendedOrg_mumx="_".join(["getUpVectorBendedOrg","mumx",sourceTitle,targetTitle])
        upVectorBended_demx="_".join(["upVectorBended","demx",sourceTitle,targetTitle])
        quatCul_qprd="_".join(["quatCul","qprd",sourceTitle,targetTitle])
        quatToEuler_qtoe="_".join(["quatToEuler","qtoe",sourceTitle,targetTitle])
        translateRevers_fltm="_".join(["translateRevers","fltm",sourceTitle,targetTitle])

        self.createNode_list=[
            {"nodeType":"composeMatrix","name":rotate_comx},
            {"nodeType":"composeMatrix","name":aimVector_comx},
            {"nodeType":"composeMatrix","name":upVector_comx},
            {"nodeType":"multMatrix","name":aimVector_mumx},
            {"nodeType":"multMatrix","name":upVector_mumx},
            {"nodeType":"decomposeMatrix","name":aimVector_demx},
            {"nodeType":"decomposeMatrix","name":upVector_demx},
            {"nodeType":"floatMath","name":aimVectorRevers_fltm},
            {"nodeType":"floatMath","name":upVectorRevers_fltm},
            {"nodeType":"angleBetween","name":self.getBendAxisAngle_agbw},
            {"nodeType":"angleBetween","name":getRollAxisAngle_agbw},
            {"nodeType":"axisAngleToQuat","name":getBendQuat_atoq},
            {"nodeType":"axisAngleToQuat","name":getRollQuat_atoq},
            {"nodeType":"composeMatrix","name":getBend_comx},
            {"nodeType":"multMatrix","name":getUpVectorBendedOrg_mumx},
            {"nodeType":"decomposeMatrix","name":upVectorBended_demx},
            {"nodeType":"quatProd","name":quatCul_qprd},
            {"nodeType":"quatToEuler","name":quatToEuler_qtoe},
            {"nodeType":"floatMath","name":translateRevers_fltm},
        ]
        self.setAttr_list=[
            {"nodeAttr":aimVector_comx+".inputTranslateX","value":1.0},
            {"nodeAttr":aimVector_comx+".inputTranslateY","value":0.0},
            {"nodeAttr":aimVector_comx+".inputTranslateZ","value":0.0},
            {"nodeAttr":upVector_comx+".inputTranslateX","value":0.0},
            {"nodeAttr":upVector_comx+".inputTranslateY","value":1.0},
            {"nodeAttr":upVector_comx+".inputTranslateZ","value":0.0},
            {"nodeAttr":aimVectorRevers_fltm+".floatB","value":-1.0},
            {"nodeAttr":aimVectorRevers_fltm+".operation","value":2},
            {"nodeAttr":upVectorRevers_fltm+".floatB","value":-1.0},
            {"nodeAttr":upVectorRevers_fltm+".operation","value":2},
            {"nodeAttr":translateRevers_fltm+".floatB","value":-1.0},
            {"nodeAttr":translateRevers_fltm+".operation","value":2},
            {"nodeAttr":getBend_comx+".useEulerRotation","value":0}
        ]
        self.connectAttr_list=[
            {"source":self._sourceNode+".rotate","target":rotate_comx+".inputRotate"},
            {"source":aimVector_comx+".outputMatrix","target":aimVector_mumx+".matrixIn[0]"},
            {"source":upVector_comx+".outputMatrix","target":upVector_mumx+".matrixIn[0]"},
            {"source":rotate_comx+".outputMatrix","target":aimVector_mumx+".matrixIn[1]"},
            {"source":rotate_comx+".outputMatrix","target":upVector_mumx+".matrixIn[1]"},
            {"source":aimVector_mumx+".matrixSum","target":aimVector_demx+".inputMatrix"},
            {"source":upVector_mumx+".matrixSum","target":upVector_demx+".inputMatrix"},
            {"source":aimVector_demx+".outputTranslateX","target":aimVectorRevers_fltm+".floatA"},
            {"source":aimVectorRevers_fltm+".outFloat","target":self.getBendAxisAngle_agbw+".vector2X"},
            {"source":aimVector_demx+".outputTranslateY","target":self.getBendAxisAngle_agbw+".vector2Y"},
            {"source":aimVector_demx+".outputTranslateZ","target":self.getBendAxisAngle_agbw+".vector2Z"},
            {"source":self.getBendAxisAngle_agbw+".vector2","target":self.getBendAxisAngle_agbw+".vector1"},
            {"source":self.getBendAxisAngle_agbw+".axis","target":getBendQuat_atoq+".inputAxis"},
            {"source":self.getBendAxisAngle_agbw+".angle","target":getBendQuat_atoq+".inputAngle"},
            {"source":getBendQuat_atoq+".outputQuat","target":getBend_comx+".inputQuat"},
            {"source":upVector_comx+".outputMatrix","target":getUpVectorBendedOrg_mumx+".matrixIn[0]"},
            {"source":getBend_comx+".outputMatrix","target":getUpVectorBendedOrg_mumx+".matrixIn[1]"},
            {"source":getUpVectorBendedOrg_mumx+".matrixSum","target":upVectorBended_demx+".inputMatrix"},
            {"source":upVectorBended_demx+".outputTranslate","target":getRollAxisAngle_agbw+".vector1"},
            {"source":upVector_demx+".outputTranslateX","target":upVectorRevers_fltm+".floatA"},
            {"source":upVectorRevers_fltm+".outFloat","target":getRollAxisAngle_agbw+".vector2X"},
            {"source":upVector_demx+".outputTranslateY","target":getRollAxisAngle_agbw+".vector2Y"},
            {"source":upVector_demx+".outputTranslateZ","target":getRollAxisAngle_agbw+".vector2Z"},
            {"source":getRollAxisAngle_agbw+".axis","target":getRollQuat_atoq+".inputAxis"},
            {"source":getRollAxisAngle_agbw+".angle","target":getRollQuat_atoq+".inputAngle"},
            {"source":getBendQuat_atoq+".outputQuat","target":quatCul_qprd+".input1Quat"},
            {"source":getRollQuat_atoq+".outputQuat","target":quatCul_qprd+".input2Quat"},
            {"source":quatCul_qprd+".outputQuat","target":quatToEuler_qtoe+".inputQuat"},
            {"source":quatToEuler_qtoe+".outputRotate","target":self._targetNode+".rotate"},
            {"source":self._sourceNode+".translateX","target":translateRevers_fltm+".floatA"},
            {"source":translateRevers_fltm+".outFloat","target":self._targetNode+".translateX"},
            {"source":self._sourceNode+".translateY","target":self._targetNode+".translateY"},
            {"source":self._sourceNode+".translateZ","target":self._targetNode+".translateZ"}
        ]
    
    #Public Function
    def run(self):
        self.__loading()
        self.createNodes_create_list(self.createNode_list)
        self.setAttrs_edit_func(self.setAttr_list)
        self.connectAttrs_edit_func(self.connectAttr_list)
        cmds.disconnectAttr(self.getBendAxisAngle_agbw+".vector2",self.getBendAxisAngle_agbw+".vector1")

    #Single Function
    def createNodes_create_list(self,createNode_list):
        culNodeList=[]
        for createNode in createNode_list:
            newNode=cmds.createNode(createNode["nodeType"],n=createNode["name"])
            culNodeList.append(newNode)
        return culNodeList

    def setAttrs_edit_func(self,setAttr_list):
        for setAttr in setAttr_list:
            cmds.setAttr(setAttr["nodeAttr"],setAttr["value"])

    def connectAttrs_edit_func(self,connectAttr_list):
        for connectAttr in connectAttr_list:
            cmds.connectAttr(connectAttr["source"],connectAttr["target"])


def getReverseJoint_create_list(joint_list):
    inputLoc_list=[]
    #各ジョイントごとの処理
    for j in joint_list:
        #あらかじめ反転対象のジョイントを探しておく
        mirrorJoint = j 
        if "Left" in j:
            mirrorJoint = j.replace("Left","Right") 
        elif "Right" in j:
            mirrorJoint = j.replace("Right","Left") 
        elif "_L" in j:
            mirrorJoint = j.replace("_L","_R") 
        elif "_R" in j:
            mirrorJoint = j.replace("_R","_L") 
        if not mirrorJoint in joint_list:
            #ミラー対象が見当たらなければ処理をスキップ
            continue
        #各ジョイントごとにTransformノードを作り、コンストレインで接続
        loc = cmds.createNode("transform",n=j.replace("jnt","loc"))
        inputLoc_list.append(loc)
    
        #移動・回転に0.0をセットすることで初期位置に戻れるようにoffsetノードを用意
        cmds.pointConstraint(j,loc,n=j.replace("jnt","poic")) 
        cmds.orientConstraint(j,loc,mo=True,n=j.replace("jnt","oric"))
    return inputLoc_list