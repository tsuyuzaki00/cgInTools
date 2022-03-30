import pymel.core as pm

def main():
    trsAttr = 'translate'
    rotateAttr = 'rotate'
    blendc_inAttr1 = 'color1'
    blendc_inAttr2 = 'color2'
    blendc_outAttr = 'output'

    pm.selected()
    Prx = pm.ls(sl=True, dag=True)

    jntPrxs =[i for i in Prx if '_jntPrx' in i.name()]
    jntFKs = [jntPrx.replace('_jntPrx', '_jntFK') for jntPrx in jntPrxs]
    jntIKs = [jntPrx.replace('_jntPrx', '_jntIK') for jntPrx in jntPrxs]
    blendT = [jntPrx.replace('_jntPrx', '_translateBlend') for jntPrx in jntPrxs]
    blendR = [jntPrx.replace('_jntPrx', '_rotateBlend') for jntPrx in jntPrxs]

    for i in range(len(jntPrxs)):
        pm.connectAttr( jntIKs[i]+'.'+trsAttr, blendT[i]+'.'+blendc_inAttr1)
        pm.connectAttr( jntFKs[i]+'.'+trsAttr, blendT[i]+'.'+blendc_inAttr2)
        pm.connectAttr( blendT[i]+'.'+blendc_outAttr, jntPrxs[i]+'.'+trsAttr )
        
        pm.connectAttr( jntIKs[i]+'.'+rotateAttr, blendR[i]+'.'+blendc_inAttr1)
        pm.connectAttr( jntFKs[i]+'.'+rotateAttr, blendR[i]+'.'+blendc_inAttr2)
        pm.connectAttr( blendR[i]+'.'+blendc_outAttr, jntPrxs[i]+'.'+rotateAttr)