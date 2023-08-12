# -*- coding: iso-8859-15 -*-

import os
import maya.cmds as cmds
from ..library import facialCtrlExport as FCE

def main():
    _FacialCtrl = FCE.FacialCtrl()
    facialCtrl_dict3 = _FacialCtrl.facialCtrl_query_json(facialCtrl_json="facialCtrlEyebrows")
    fullPath_path = os.path.join(os.environ['MGEAR_SHIFTER_CUSTOMSTEP_PATH'],facialCtrl_dict3["path"])
    selObjs_list = selObjs_check_list(objs=facialCtrl_dict3["export_ctrls"])
    _FacialCtrl.curve_export_json(path=fullPath_path,file=facialCtrl_dict3["file"],export_ctrls=selObjs_list)

def selObjs_check_list(objs=[]):
    selObjs_list = []
    for obj in objs:
        if cmds.objExists(obj):
            selObjs_list.append(obj)
    return selObjs_list