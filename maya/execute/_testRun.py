# -*- coding: iso-8859-15 -*-

from cgInTools.maya.library import cjson as cj; reload(cj);
from cgInTools.maya.library import cfiling as cf; reload(cf);
import maya.cmds as cmds

_cj=cj.CJson()
_cf=cf.CFiling()

json_name="skin"
ex="CSkin"
path=_cf.wrkDir_create_path(wrkDir=r"D:\_test",addFolder="jsonTest")

objs=cmds.ls(sl=True)
writePack_list=[]
for obj in objs:
    attrs=cmds.listAttr(obj,r=True,k=True,u=True)
    write_dict={"obj":obj,"attr":attrs}
    element_dict=_cj.packDict_create_list(obj,ex,write_dict)
    writePack_list.append(element_dict)

_cj.writePack_create_func(writePack_list,path,pack_file=json_name)
#_cj.writeJson_create_func(json_file,dict=packFiles)
#_cj.writePack_create_func(json_file,write_dict)