import pymel.core as pm

def main():
    sels = pm.selected()
    for sel in sels:
        matrixCreateConnect(sel)

def matrixCreateConnect(sel):
    sel_part = sel.split('_')
    #nameSetting
    cnsName = pm.createNode('transform', n = "_".join([sel_part[0],"ref",sel_part[2]]))
    mumx_name_trs = pm.createNode('multMatrix', n = "_".join([sel_part[0],"mumx",sel_part[2],"trs"]))
    mumx_name_rot = pm.createNode('multMatrix', n = "_".join([sel_part[0],"mumx",sel_part[2],"rot"]))
    demx_name_trs = pm.createNode('decomposeMatrix', n = "_".join([sel_part[0],"demx",sel_part[2],"trs"]))
    demx_name_rot = pm.createNode('decomposeMatrix', n = "_".join([sel_part[0],"demx",sel_part[2],"rot"]))
    
    #selGet>cns
    pm.parent(cnsName, sel)
    pm.move( 0, 0, 0 , ls=True)
    pm.rotate( 0, 0, 0 , os=True)
    pm.parent(cnsName , w = True)
    
    #connection
    pm.connectAttr( cnsName + '.worldMatrix', mumx_name_trs + '.matrixIn[0]')
    pm.connectAttr( mumx_name_trs + '.matrixSum', mumx_name_rot + '.matrixIn[0]')
    pm.connectAttr( sel + '.parentInverseMatrix', mumx_name_trs + '.matrixIn[1]')
    getSelImx = pm.getAttr(sel + '.inverseMatrix')
    pm.setAttr(mumx_name_rot + '.matrixIn[1]', getSelImx)
    pm.connectAttr( mumx_name_trs + '.matrixSum', demx_name_trs + '.inputMatrix')
    pm.connectAttr( mumx_name_rot + '.matrixSum', demx_name_rot + '.inputMatrix')
    pm.connectAttr( demx_name_trs + '.outputTranslate', sel + '.translate')
    pm.connectAttr( demx_name_trs + '.outputScale', sel + '.scale')
    pm.connectAttr( demx_name_rot + '.outputRotate', sel + '.rotate')
    
main()