# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
from cgInTools.maya.library import cJson as cj
from cgInTools.maya.library import cFiling as cf

json_name="skin"
ex="CSkin"
path=cf.Path()
path.setPath()
path=cf.wrkDir_create_path(wrkDir=r"D:\_test",addFolder="jsonTest")

objs=cmds.ls(sl=True)
writePack_list=[]
for obj in objs:
    attrs=cmds.listAttr(obj,r=True,k=True,u=True)
    write_dict={"obj":obj,"attr":attrs}
    element_dict=cj.packDict_create_list(obj,ex,write_dict)
    writePack_list.append(element_dict)

cj.writePack_create_func(writePack_list,path,pack_file=json_name,extension="jsonPack")
#_cj.writeJson_create_func(json_file,dict=packFiles)
#_cj.writePack_create_func(json_file,write_dict)
