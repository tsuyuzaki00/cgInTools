import pymel.core as pm

sels = pm.ls(sl=True, dag=True)
multMatrixs = [i.replace("_jnt","_multMatrix") for i in sels]
decomposeMatrixs = [i.replace("_jnt","_decomposeMatrix") for i in sels]
    
for i in range(len(sels)):
   pm.createNode( 'multMatrix', n = multMatrixs[i])
   pm.createNode( 'decomposeMatrix', n = decomposeMatrixs[i])

import pymel.core as pm

matrixAttr = 'matrix'
    
matrix_inAttr = 'matrix in[0]'
matrix_sumAttr = 'matrix sum'
    
input_matrixAttr = 'inputMatrix'
translate_outAttr = 'output translate'
rotate_outAttr = 'output rotate'
scale_outAttr = 'output scale'
shear_outAttr = 'output shear'
    
translateAttr = 'translate'
rotateAttr = 'rotate'
scaleAttr = 'scale'
shearAttr = 'shear'
    
sel = pm.ls(sl=True, dag=True)
    
jnts =[i for i in sel if '_jnt' in i.name()]
jntPrxs = [jnt.replace('_jnt', '_jntPrx') for jnt in jnts]
multMatrixs = [jnt.replace('_jnt', '_multMatrix') for jnt in jnts]
decomposeMatrixs = [jnt.replace('_jnt', '_decomposeMatrix') for jnt in jnts]

print jntPrxs

        
for i in range(len(jnts)):
    pm.connectAttr( jnts[i]+'.'+matrixAttr, multMatrixs[i]+'.'+matrix_inAttr)
    pm.connectAttr( multMatrixs[i]+'.'+matrix_sumAttr, decomposeMatrixs[i]+'.'+input_matrixAttr)
        
    pm.connectAttr( decomposeMatrixs[i]+'.'+translate_outAttr, jntPrxs[i]+'.'+translateAttr )
    pm.connectAttr( decomposeMatrixs[i]+'.'+rotate_outAttr, jntPrxs[i]+'.'+rotateAttr)
    pm.connectAttr( decomposeMatrixs[i]+'.'+scale_outAttr, jntPrxs[i]+'.'+scaleAttr)
    #pm.connectAttr( decomposeMatrixs[i]+'.'+shear_outAttr, jntPrxs[i]+'.'+shearAttr)