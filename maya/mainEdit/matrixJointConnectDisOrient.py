import pymel.core as pm

def main():
    sels = pm.selected()
    for sel in sels:
        matrixCreateConnect(sel)

def matrixCreateConnect(sel):
    selPart = sel.split('_')
    #nameSetting
    cnsName = pm.createNode('transform', n = 'cns_' + selPart[1] + '_' + selPart[-2] + '_' + selPart[-1])
    cnsPart = cnsName.split('_')
    trsMmxName = pm.createNode('multMatrix', n = 'mmx_' + selPart[1] + '_Trs' + '_' + cnsPart[0] + selPart[0] + '_' + selPart[-2] + '_' + selPart[-1])
    rotMmxName = pm.createNode('multMatrix', n = 'mmx_' + selPart[1] + '_Rot' + '_' + cnsPart[0] + selPart[0] + '_' + selPart[-2] + '_' + selPart[-1])
    trsDmxName = pm.createNode('decomposeMatrix', n = 'dmx_' + selPart[1] + '_Trs' + '_' + cnsPart[0] + selPart[0] + '_' + selPart[-2] + '_' + selPart[-1])
    rotDmxName = pm.createNode('decomposeMatrix', n = 'dmx_' + selPart[1] + '_Rot' + '_' + cnsPart[0] + selPart[0] + '_' + selPart[-2] + '_' + selPart[-1])
    
    #selGet>cns
    pm.parent(cnsName, sel)
    pm.move( 0, 0, 0 , ls=True)
    pm.rotate( 0, 0, 0 , os=True)
    pm.parent(cnsName , w = True)
    
    #jointReset
    if sel.type() == 'joint':
        getOrient = pm.getAttr(sel + '.jointOrient')
        if getOrient != [0,0,0]:
            pm.setAttr(sel + '.jointOrient',0,0,0)
            pm.setAttr(sel + '.rotate',getOrient)
            
    #connection
    pm.connectAttr( cnsName + '.worldMatrix', trsMmxName + '.matrixIn[0]')
    pm.connectAttr( trsMmxName + '.matrixSum', rotMmxName + '.matrixIn[0]')
    pm.connectAttr( sel + '.parentInverseMatrix', trsMmxName + '.matrixIn[1]')
    pm.connectAttr( trsMmxName + '.matrixSum', trsDmxName + '.inputMatrix')
    pm.connectAttr( rotMmxName + '.matrixSum', rotDmxName + '.inputMatrix')
    pm.connectAttr( trsDmxName + '.outputTranslate', sel + '.translate')
    pm.connectAttr( trsDmxName + '.outputScale', sel + '.scale')
    pm.connectAttr( rotDmxName + '.outputRotate', sel + '.rotate')
    
main()