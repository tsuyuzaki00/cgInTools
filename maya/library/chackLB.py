# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

def valueRelation_check_func(obj,attr,relation,edit=False):
    value=cmds.getAttr(obj+"."+attr)
    if edit:
        if value is not relation:
            cmds.setAttr(obj+"."+attr,relation)
        else:
            print("OK:"+obj+"."+attr+":"+str(value))
    else:
        if value is relation:
            print("OK:"+obj+"."+attr+":"+str(value))
        else:
            print("NG:"+obj+"."+attr+":"+str(value))
        
def main():
    mesh_shapes=cmds.ls(type="mesh")
    chackAttr_dicts=[
        {"attr":"aiSubdivType","relation":1},
        {"attr":"aiSubdivIterations","relation":1},
        {"attr":"aiSubdivUvSmoothing","relation":1},
    ]
    for mesh_shape in mesh_shapes:
        for chackAttr_dict in chackAttr_dicts:
            valueRelation_check_func(mesh_shape,chackAttr_dict["attr"],chackAttr_dict["relation"])

main()