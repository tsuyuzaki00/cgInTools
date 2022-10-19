# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
from cgInTools.maya.library import cNurbs as cn
from cgInTools.maya.library import cGrouping as cgrp

def surfaceBuild_create_objs():
    poly=cn.NurbsToPoly()
    grp=cgrp.GroupIng()
    polyUnites=[]

    grp.setGrpName("surface_grp")
    grp.setSearchType("transform")
    surfaces=grp.choiseType()
    
    for surface in surfaces:
        numberV=cmds.getAttr(surface+".numberV")
        numberU=cmds.getAttr(surface+".numberU")
        poly.setObj(surface)
        poly.setName(surface.replace("_surf","_geo"))
        poly.setFormat(2)
        poly.setPolyType(1)
        poly.setUNumber(numberU)
        poly.setVNumber(numberV)
        polygon=poly.create()
        polyUnites.append(polygon)
    return polyUnites

def margePolygons_edit_obj(polyUnites,name="name_geo_C"):
    polyUnite=cmds.polyUnite(polyUnites,ch=True,mergeUVSets=0,n=name)
    cmds.delete(polyUnite,ch=True)
    return polyUnite


def main():
    polyUnites=surfaceBuild_create_objs()
    margePolygons_edit_obj(polyUnites,name="base_geo_C")

main()