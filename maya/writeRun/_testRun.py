# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import cgInTools as cit
from cgInTools.maya.library import checkLB as chLB
cit.reloads([chLB])

def main():
    check=chLB.Check()
    mesh_shapes=cmds.ls(type="mesh")
    chackAttr_dicts=[
        {"attr":"aiSubdivType","same":1},
        {"attr":"aiSubdivIterations","same":1},
        {"attr":"aiSubdivUvSmoothing","same":1},
    ]
    for mesh_shape in mesh_shapes:
        for chackAttr_dict in chackAttr_dicts:
            check.setObject(mesh_shape)
            check.setAttr(chackAttr_dict["attr"])
            check.setSame(chackAttr_dict["same"])
            check.setEdit(False)
            test=check.attrSame()
            if not test["bool"]:
                print("NG:"+test["object"]+"."+test["attr"]+","+str(test["relation"]))

main()