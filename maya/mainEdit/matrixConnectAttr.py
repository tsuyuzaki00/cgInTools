import pymel.core as pm

obj = 'mouthC'
pos = 'RU'

ctrl = obj + '_ctrl_' + pos
space = obj + '_space_' + pos
multi = obj + '_multiMatrix_' + pos
decompose = obj + '_decomposeMatrix_' + pos
jntPrx = obj + '_jntPrx_' + pos

pm.connectAttr(ctrl + '.matrix',multi + '.matrixIn[0]')
pm.connectAttr(space + '.matrix',multi + '.matrixIn[1]')

pm.connectAttr(multi + '.matrixSum', decompose + '.inputMatrix')

pm.connectAttr(decompose + '.outputTranslate',jntPrx + '.translate')
pm.connectAttr(decompose + '.outputRotate',jntPrx + '.rotate')
pm.connectAttr(decompose + '.outputScale',jntPrx + '.scale')