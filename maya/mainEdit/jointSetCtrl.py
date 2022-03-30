import pymel.core as pm

def curveCube(name):
    a1 = (1,1,1)
    a2 = (1,1,-1)
    a3 = (-1,1,-1)
    a4 = (-1,1,1)
    b1 = (1,-1,1)
    b2 = (1,-1,-1)
    b3 = (-1,-1,-1)
    b4 = (-1,-1,1)

    tmpCurve = pm.curve( d=1,p=[a1,a2,a3,a4,a1,b1,b2,a2,b2,b3,a3,b3,b4,a4,b4,b1], n= name)
    return name

def jointSetCtrl():
    pm.selected()
    jnts = pm.ls(sl=True, dag=True)
    
    for jnt in jnts:
        trsName = jnt.replace('jnt_','trs_')
        ctrlName = jnt.replace('jnt_','ctrl_')
        trs = pm.createNode( 'transform', n= trsName)

        ctrl = curveCube(ctrlName)

        pm.parent(ctrl, trs)
        pm.parent(trs, jnt)
        
        pm.move( 0, 0, 0 ,ls=True)
        pm.rotate( 0, 0, 0 , os=True)
        pm.parent(trs ,w = True)
