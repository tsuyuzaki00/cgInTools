import pymel.core as pm

def main():
    ctrl = pm.selected()[0]
    part = ctrl.split("_")
    
    cndIK = part[1][0].upper() + part[1][1:]
    
    offset = ctrl.replace("ctrl_",'offset_')    
    parentName = ctrl.replace("ctrl_",'offParentConstraint_')
    
    trsRoot = 'trs_root_' + part[2] + '_C'
    trsShaft = 'trs_shaft_' + part[2] + '_C'
    cndRoot = 'cnd_root' + cndIK + '_' + part[2] + '_' + part[3]
    cndShaft = 'cnd_shaft' + cndIK + '_' + part[2] + '_' + part[3]
    
    trsPelvis = 'trs_pelvis_' + part[2] + '_C'
    cndPelvis = 'cnd_pelvis' + cndIK + '_' + part[2] + '_' + part[3]
    
    trsFootIK = 'trs_footIK_' + part[2] + '_' + part[3]
    cndFootIK = 'cnd_footIK' + cndIK + '_' + part[2] + '_' + part[3]
    
    trsShoulder = 'trs_shoulder_' + part[2] + '_' + part[3]
    cndShoulder = 'cnd_shoulder' + cndIK + '_' + part[2] + '_' + part[3]
    
    trsHandIK = 'trs_handIK_' + part[2] + '_' + part[3]
    cndHandIK = 'cnd_handIK' + cndIK + '_' + part[2] + '_' + part[3]
    
    
    pm.parentConstraint(trsRoot, offset, n = parentName, mo = True, w = 1)
    pm.parentConstraint(trsShaft, offset, mo = True, w = 1)
    
    pm.parentConstraint(trsShoulder, offset, mo = True, w = 1)
    pm.parentConstraint(trsHandIK, offset, mo = True, w = 1)
    
    #pm.parentConstraint(trsPelvis, offset, mo = True, w = 1)
    #pm.parentConstraint(trsFootIK, offset, mo = True, w = 1)
    
    pm.connectAttr(cndRoot+".outColorR", parentName + "." + trsRoot + "W0")
    pm.connectAttr(cndShaft+".outColorR", parentName + "." + trsShaft + "W1")
    
    pm.connectAttr(cndShoulder+".outColorR", parentName + "." + trsShoulder + "W2")
    pm.connectAttr(cndHandIK+".outColorR", parentName + "." + trsHandIK + "W3")
    
    #pm.connectAttr(cndPelvis+".outColorR", parentName + "." + trsPelvis + "W2")
    #pm.connectAttr(cndFootIK+".outColorR", parentName + "." + trsFootIK + "W3")
    
main()