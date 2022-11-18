# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

def valueRelation_check_func(obj,attr,relation,edit=False):
    value=cmds.getAttr(obj+"."+attr)
    if edit:
        if value is not relation:
            cmds.setAttr(obj+"."+attr,relation)
        else:
            ok="OK:"+obj+"."+attr+":"+str(value)
            return ok
    else:
        if value is relation:
            ok="OK:"+obj+"."+attr+":"+str(value)
            return ok
        else:
            ng="NG:"+obj+"."+attr+":"+str(value)
            return ng
        
def main():
    mesh_shapes=cmds.ls(type="mesh")
    chackAttr_dicts=[
        {"attr":"aiSubdivType","relation":1},
        {"attr":"aiSubdivIterations","relation":1},
        {"attr":"aiSubdivUvSmoothing","relation":1},
    ]
    for mesh_shape in mesh_shapes:
        for chackAttr_dict in chackAttr_dicts:
            check=valueRelation_check_func(mesh_shape,chackAttr_dict["attr"],chackAttr_dict["relation"])
            print(check)

main()