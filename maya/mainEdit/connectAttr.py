import pymel.core as pm

def main():
    pm.selected()
    bnds = pm.ls(sl=True, dag=True)

    for bnd in bnds:
        jnt = bnd.replace("bnd_",'jnt_')
        pm.connectAttr( jnt +'.'+ 'translate', bnd +'.'+'translate',f=True )
        pm.connectAttr( jnt +'.'+ 'rotate', bnd +'.'+'rotate',f=True )
        pm.connectAttr( jnt +'.'+ 'scale', bnd +'.'+'scale',f=True )