import pymel.core as pm

sels = pm.ls(sl = True, dag = True)

for sel in sels:
    part = sel.split('_')
    jnt = '_'.join( ['bnd',part[1],part[2],part[3],part[4]])
    pm.connectAttr(sel + '.' + 'translate', jnt + '.' + 'translate')
    pm.connectAttr(sel + '.' + 'rotate', jnt + '.' + 'rotate')
    pm.connectAttr(sel + '.' + 'scale', jnt + '.' + 'scale')
