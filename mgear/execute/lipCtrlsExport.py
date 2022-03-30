# -*- coding: iso-8859-15 -*-

import os
import maya.cmds as cmds
from ..library import facialCtrlExport as FCE

def main():
    _FacialCtrl = FCE.FacialCtrl()
    facialCtrl_dict3 = _FacialCtrl.facialCtrl_query_json(facialCtrl_json="facialCtrlLips")
    fullPath_path = os.path.join(os.environ['MGEAR_SHIFTER_CUSTOMSTEP_PATH'],facialCtrl_dict3["path"])
    _FacialCtrl.curve_export_json(path=fullPath_path,file=facialCtrl_dict3["file"],export_ctrls=facialCtrl_dict3["export_ctrls"])