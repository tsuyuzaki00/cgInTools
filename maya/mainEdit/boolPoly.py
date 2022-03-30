import pymel.core as pm

def boolpoly():
    sel = pm.selected()
    pm.polyExtrudeFacet(sel[0], kft=True, ltz=500)
    pm.polyExtrudeFacet(sel[1], kft=True, ltz=500)
    pm.polyCBoolOp(sel[0],sel[1], op = 3, n = 'geo_body_name')
    pm.delete(ch = True)