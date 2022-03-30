import pymel.core as pm

def curveCircle(name):
    pm.circle( nr=(1, 0, 0), c=(0, 0, 0), sw=360, r=2, n = name)
    return name  

def curveChenge():
    sels = pm.selected()
    for sel in sels:
        selShape = createShape = pm.listRelatives(sel, type='nurbsCurve')
        pm.delete(selShape[0:])
        curveCircle(sel)
        createName = pm.selected()[0]
        createShape = pm.listRelatives(createName)
        pm.parent(createShape, sel, r = True, s = True)
        pm.delete(createName)
        