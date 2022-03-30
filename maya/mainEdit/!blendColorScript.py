import pymel.core as pm

sels = pm.selected()

for sel in sels:
    part = sel.split("_")

    changeParts = 'arm'
    changeLR = 'R'
    
    switchName = 'ctrl_'+ changeParts +'Switch_00_ribbonRig_' + changeLR
    switchAttr = changeParts + 'IKFK' + changeLR
    trsAttr = 'translate'
    rotAttr = 'rotate'
    sclAttr = 'scale'

    if pm.objExists(switchName):
        pass
    else :
        pm.circle( nr = (1, 0, 0), c = (0, 0, 0), sw = 360, r = 2 , ch = False, n = switchName)
        pm.addAttr(sn = switchAttr, k = True, at = 'enum', en = 'IK:FK')

    blendTrs = pm.createNode('blendColors', n = '_'.join( ['bdcTrs',part[1],part[2],part[3],part[4]])) #bdcTrs_obj_num_secne_pos
    blendRot = pm.createNode('blendColors', n = '_'.join( ['bdcRot',part[1],part[2],part[3],part[4]])) #bdcRot_obj_num_secne_pos
    blendScl = pm.createNode('blendColors', n = '_'.join( ['bdcScl',part[1],part[2],part[3],part[4]])) #bdcScl_obj_num_secne_pos
    jntFK = '_'.join( [part[0]+'FK',part[1],part[2],part[3],part[4]]) #jntFK_obj_num_secne_pos
    jntIK = '_'.join( [part[0]+'IK',part[1],part[2],part[3],part[4]]) #jntIK_obj_num_secne_pos

    #translate connectAttr
    pm.connectAttr(jntFK + '.'+ trsAttr, blendTrs +'.color1')
    pm.connectAttr(jntIK + '.' + trsAttr, blendTrs+'.color2')
    pm.connectAttr(blendTrs + '.output', sel +'.'+ trsAttr)
    pm.connectAttr(switchName + '.' + switchAttr , blendTrs +'.blender')

    #rotate connectAttr
    pm.connectAttr(jntFK + '.'+ rotAttr, blendRot +'.color1')
    pm.connectAttr(jntIK + '.' + rotAttr, blendRot+'.color2')
    pm.connectAttr(blendRot + '.output', sel +'.'+ rotAttr)
    pm.connectAttr(switchName + '.' + switchAttr , blendRot +'.blender')

    #scale connectAttr
    pm.connectAttr(jntFK + '.'+ sclAttr, blendScl +'.color1')
    pm.connectAttr(jntIK + '.' + sclAttr, blendScl+'.color2')
    pm.connectAttr(blendScl + '.output', sel +'.'+ sclAttr)
    pm.connectAttr(switchName + '.' + switchAttr , blendScl +'.blender')