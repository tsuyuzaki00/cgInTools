import pymel.core as pm

def multiConstraint():
    sel = pm.selected()
    pm.listRelatives(sel, parent=True)
    hierarchySelection = pm.ls(sl=True, dag=True)

    for ctrl in hierarchySelection:
        jntName = ctrl.replace('_ctrl','_jnt')
        parentName = ctrl.replace('_ctrl','_prc')
        if ctrl.nodeType() == 'transform':
            if '_ctrl' in ctrl.name():
                if '_grp' not in ctrl.name():
                    pm.parentConstraint(ctrl, jntName, n = parentName, mo = True, w = 1)
                    pm.select(cl = True)