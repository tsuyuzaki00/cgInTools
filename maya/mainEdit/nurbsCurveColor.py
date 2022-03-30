import pymel.core as pm

def main():
    selects = pm.ls(sl=True, dag=True)

    for ctrl in selects:
        if ctrl.nodeType() == 'nurbsCurve':
            pm.setAttr( ctrl+'.overrideEnabled', 1)
            if '_LShape' in ctrl.name():
                pm.setAttr( ctrl+'.overrideColor', 6)#Left
            if '_RShape' in ctrl.name():
                pm.setAttr( ctrl+'.overrideColor', 14)#Right
            else :
                pm.setAttr( ctrl+'.overrideEnabled', 0)