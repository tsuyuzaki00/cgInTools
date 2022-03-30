import pymel.core as pm

def main():
    ctrl = pm.selected()[0]
    part = ctrl.split("_")
    grpName = 'grp' + '_' + part[0] + '_' + part[2]
    pm.select(grpName)
    selects = pm.ls(sl=True, dag=True)

    for allKey in selects:
        if allKey.nodeType() == 'transform':
            if 'ctrl_' in allKey.name():
                if 'grp_' not in allKey.name():
                    pm.setKeyframe(allKey)
                    pm.select(cl = True)