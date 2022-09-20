# -*- coding: iso-8859-15 -*-

import os
import maya.cmds as cmds
from mgear.core import curve

from ..library import simpleJson as sj
from ..library import pyNodeEdit as pne
import cgInTools as cit

class FacialCtrl():
    def set_cstp_path(wrk_dir='',folder_name=''):
        wrk_dir = wrk_dir or cmds.workspace(q=True,rd=True)
        folder_name = folder_name or 'mgear_build'
        os.environ['MGEAR_SHIFTER_CUSTOMSTEP_PATH'] = os.path.join(wrk_dir,folder_name)

    def setCurve_create_path(self,path,file=""):
        file = file or "curve_shapes"
        get_path = os.path.join(path,file + ".crv")#r"D:/../date/lips/curve_shapes.crv"
        new_path = get_path.replace("\\","/")
        return new_path

    def facialCtrl_query_json(self,facialCtrl_json=""):
        _SimpleJson = sj.SimpleJson()
        facialCtrl_path = _SimpleJson.path_setting(cit.mgear_settings_path,facialCtrl_json)
        facialCtrl_dict3 = _SimpleJson.read_json(facialCtrl_path)
        return facialCtrl_dict3

    def curve_export_json(self,path="",file="",export_ctrls=[]):
        curve_path = self.setCurve_create_path(path,file)
        _PyNodes = pne.PyNodes()
        objs = _PyNodes.change_pyNode(export_ctrls)
        curve.export_curve(curve_path,objs)