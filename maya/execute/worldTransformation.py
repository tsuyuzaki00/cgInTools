#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import maya.api.OpenMaya as om
import maya.cmds as cmds

#vector = om.MVector(10,10,10)
#matrix = om.MMatrix()

#print(vector[0])

def fix_hand(ctl):
    # コントローラの値を取得
    npo = cmds.listRelatives(ctl,p=True)
    get_npo = cmds.getAttr(npo[0] + ".rotate")
    # リセットして通常のポーズを取得
    cmds.setAttr(npo[0] + ".rotate", 0,0,0 , type = "double3")
    
    # ロケーターを作成して元の位置を取得
    locator = cmds.createNode("locator")
    locator = cmds.listRelatives(locator,p=True)
    pccl = cmds.parentConstraint(ctl, locator, w = 1)
    #
    
    # keyframeが打たれているtimeを取得
    ctl_keys = cmds.keyframe(ctl, q = True, tc = True)
    ctl_keys = set(ctl_keys)

    # keyフレームをセット
    cmds.currentTime(0)
    cmds.setKeyframe(locator[0], bd = 0, pcs = 0, hi = "none", cp = 0, s = 0)
    cmds.setAttr(locator[0] + ".blendParent1", 1)

    for ctl_key in ctl_keys:
        cmds.currentTime(ctl_key)
        cmds.setKeyframe(locator[0], bd = 0, pcs = 0, hi = "none", cp = 0, s = 0)
    
    # ロケーターペアレント解除
    cmds.delete(pccl)
    #

    # 初期位置にnpoを戻す
    cmds.setAttr(npo[0] + ".rotate", get_npo[0][0], get_npo[0][1], get_npo[0][2], type = "float3")
    #

    # ロケーターにコントローラをコンストレイントする
    cmds.parentConstraint(locator[0], ctl, w = 1)
    #

    # keyフレームをセット
    for ctl_key in ctl_keys:
        cmds.currentTime(ctl_key)
        cmds.setKeyframe(ctl, bd = 0, pcs = 0, hi = "none", cp = 0, s = 0)

    # 不要なロケーターを削除
    cmds.delete(locator[0])
    #

def main():
    objs = cmds.ls(sl=True)
    for obj in objs:
        fix_hand(obj)