import pymel.core as pm

def main():
    pm.selected()
    jnts = pm.ls(sl=True, dag=True)
    
    for jnt in jnts:
        trsName = jnt.replace("jnt_",'trs_')
        node = pm.createNode( 'transform', n= trsName)
        
        pm.parent(node , jnt)
        pm.move( 0, 0, 0 ,ls=True)
        pm.rotate( 0, 0, 0 , os=True)
        pm.parent(node ,w = True)
        
main()