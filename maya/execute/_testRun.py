# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
from cgInTools.maya.library import cJson as cj; reload(cj);
from cgInTools.maya.library import cFiling as cf; reload(cf);

cage_file=cf.File()
cage_path=cf.Path()
root=cage_path.rootPath()
adds=[root,"polite","middle","add","cage"]
for add in adds:
    cage_path.addPath(add)
cage_file.setPath(cage_path.queryPath())
cage_file.setObjs(["cage_grp"])
cage_file.setName("cage")
cage_file.grpsExport()