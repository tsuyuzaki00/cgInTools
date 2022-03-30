import pymel.core as pm

def main():
    exSel = pm.selected()[0]
    inSels = pm.selected()[1:]

    for inSel in inSels:
        nextSel = pm.duplicate(exSel)
        shapes = pm.listRelatives(nextSel, type='nurbsCurve')
        pm.rename(shapes, inSel+'Shape')
        pm.parent(shapes, inSel , r = True , s = True)
        pm.delete(nextSel)