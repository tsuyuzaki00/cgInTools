import pymel.core as pm

def main():
    sels = pm.selected()
    matrixParent(sels)
    
def matrixParent(sels):
    if len(sels) >= 3 or len(sels) <= 1:
        pm.error('Please select two')
    
    exSel = sels[0]
    inSel = sels[1]
    exSelPart = exSel.split('_')
    inSelPart = inSel.split('_')
    
    prcMmxName = pm.createNode('multMatrix', n = 'mmx_' + exSelPart[1] + '_Trs' + '_' + exSelPart[0] + inSelPart[0] + '_' + exSelPart[-3] + '_' + exSelPart[-2] + '_' + exSelPart[-1])
    prcDmxName = pm.createNode('decomposeMatrix', n = 'dmx_' + exSelPart[1] + '_Trs' + '_' + exSelPart[0] + inSelPart[0] + '_' + exSelPart[-3] + '_' + exSelPart[-2] + '_' + exSelPart[-1])
    
    pm.connectAttr( exSel + '.matrix', prcMmxName + '.matrixIn[0]')
    pm.connectAttr( exSel + '.parentMatrix', prcMmxName + '.matrixIn[1]')
    pm.connectAttr( inSel + '.parentInverseMatrix', prcMmxName + '.matrixIn[2]')
    pm.connectAttr( prcMmxName + '.matrixSum', prcDmxName + '.inputMatrix')
    pm.connectAttr( prcDmxName + '.outputTranslate', inSel + '.translate')
    pm.connectAttr( prcDmxName + '.outputScale', inSel + '.scale')
    pm.connectAttr( prcDmxName + '.outputRotate', inSel + '.rotate')
    pm.connectAttr( prcDmxName + '.outputShear', inSel + '.shear')
    
main()