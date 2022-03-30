import pymel.core as pm

jnts = pm.selected()

ctrlScale = pm.createNode('nurbsSurface', n = 'allScale')
pm.addAttr(ln = 'scale', nn = 'Scale', at = 'float', dv = 1)
pm.setAttr(ctrlScale + '.scale', k = True)

pm.connectAttr(ctrlScale + '.scale', jnts[0] + '.scaleX')
pm.connectAttr(ctrlScale + '.scale', jnts[0] + '.scaleY')
pm.connectAttr(ctrlScale + '.scale', jnts[0] + '.scaleZ')

for jnt in jnts:
    pm.setAttr(jnt + '.segmentScaleCompensate', 0)
    nullName = jnt.replace('JNT_','NLL_')
    ctrlName = jnt.replace('JNT_','CTL_')
    pm.connectAttr(jnt + '.scale', nullName + '.scale')
    pm.parent('surface1|allScale', ctrlName , add = True, s = True)

pm.delete('surface1')
        
        