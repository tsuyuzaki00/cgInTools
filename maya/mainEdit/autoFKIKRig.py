import pymel.core as pm

def duplicateLeg():
    selLeg = pm.ls(sl=True, dag=True)
    pm.duplicate(selLeg[0], rc = True)
    bnds = pm.ls(sl=True, dag=True)
    jntRenames = [jnt.replace("_bnd",'_jnt') for jnt in bnds]
    for i in range(len(bnds)):
        a = jntRenames[i]
        jntRename = a[:-1]
        pm.rename(bnds[i],jntRename)
    parentName = pm.ls(sl=True, dag=True)
        
def duplicateLegFK():        
    selLeg = pm.ls(sl=True, dag=True)
    pm.duplicate(selLeg[0], rc = True)
    bnds = pm.ls(sl=True, dag=True)
    jntRenames = [jnt.replace("_jnt",'_jntFK') for jnt in bnds]
    for i in range(len(bnds)):
        a = jntRenames[i]
        jntRename = a[:-1]
        pm.rename(bnds[i],jntRename)
    parentName = pm.ls(sl=True, dag=True)
        
def duplicateLegIK():        
    selLeg = pm.ls(sl=True, dag=True)
    pm.duplicate(selLeg[0], rc = True)
    bnds = pm.ls(sl=True, dag=True)
    jntRenames = [jnt.replace("_jntFK",'_jntIK') for jnt in bnds]
    for i in range(len(bnds)):
        a = jntRenames[i]
        jntRename = a[:-1]
        pm.rename(bnds[i],jntRename)
    parentName = pm.ls(sl=True, dag=True)
    pm.ikHandle( sj=parentName[0], ee=parentName[2])


def connection():

    for i in range(len(bnds)):
        pm.orientConstraint( jnt , IK ,  n = name + '_orientConstraint_' + ctrl[-1])
        pm.orientConstraint( jnt , FK ,  n = name + '_orientConstraint_' + ctrl[-1])
        
duplicateLeg()
duplicateLegFK()
duplicateLegIK()
#connection()