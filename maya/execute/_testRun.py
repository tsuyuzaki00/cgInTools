# -*- coding: iso-8859-15 -*-

from cgInTools.maya.library import cjson as cj; reload(cj);
from cgInTools.maya.library import cfiling as cf; reload(cf);
import maya.cmds as cmds

json_name="skin"
ex="CSkinPack"

_cj=cj.CJson()
_cf=cf.CFiling()

objs=cmds.ls(sl=True)
packFiles={"packFiles":objs}

path=_cf.wrkDir_create_path(wrkDir=r"D:\_test",addFolder="jsonTest")
json_file=_cj.pathSetting_create_str(path=path,json_name=json_name,extension=ex)
_cj.writeJson_create_func(json_file,dict=packFiles)