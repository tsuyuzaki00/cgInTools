import pymel.core as pm

def main():
    node = pm.selected()
    pm.listRelatives(node, parent=True)
    selects = pm.ls(sl=True, dag=True)

    for allKey in selects:
        if allKey.nodeType() == 'transform':
            if 'ctrl_' in allKey.name():
                if 'grp_' not in allKey.name():
                    pm.setKeyframe(allKey)
                    pm.select(cl = True)