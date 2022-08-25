import pymel.core as pm
import maya.cmds as cmds

from ..library import namingSplits as ngs
from .... import cgInTools as sf
from ..library import cJson as sj

def main():
    simple_json = sj.SimpleJson()
    get_name_split = ngs.NamingSplits()
    setting = simple_json.path_setting(sf.maya_settings_folder,"autoRename")
    read_setting = simple_json.read_json(setting)

    sels = cmds.ls(sl=True)
    for sel in sels:
        scene = get_name_split.scene()
        obj = get_name_split.obj(sel)
        node = get_name_split.node(sel)
        pos = get_name_split.pos(sel)
        num = get_name_split.num(sel)
        read_setting["naming_order"]
        lists = [pos,obj,node]
        names = [l for l in lists if l != ""]
        autoRename = '_'.join(names)
        if sel != autoRename:
            trueRename = get_name_split.same_name_check(check = autoRename)
            cmds.rename(sel, trueRename)