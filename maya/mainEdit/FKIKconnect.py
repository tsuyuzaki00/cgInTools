import pymel.core as pm
    
def createSwitch(radio):
    if radio == 0:
        pm.error("select radio")
    elif radio == 1:
        parts = 'Arm'
    elif radio == 2:
        parts = 'Leg'
    elif radio == 3:
        parts = 'Hear'
    elif radio == 4:
        parts = 'Tail'
    
    sels = pm.selected()
    
    part = sels[0].split("_")
    reverseName = parts + '_' + 'IKFKReverse' + '_' + part[2] + '_' + part[3]
    IKFKSwitchName = parts + '_' + 'IKFKSwitch' + '_' + part[2] + '_' + part[3]
        
    reverse = pm.createNode('reverse', n = reverseName)
    IKFKSwitch = pm.createNode('nurbsSurface', n = IKFKSwitchName)
    pm.addAttr(ln = 'IKFK', nn = 'IKFK', at = 'enum', en = 'IK:FK')
    pm.setAttr(IKFKSwitch + '.IKFK', k = True)
    pm.connectAttr(IKFKSwitch + '.IKFK', reverse + ".inputX")   
    
    for sel in sels:
        part = sel.split("_")
        IKName = part[0] + '_' + 'jntIK' + '_' + part[2] + '_' + part[3]
        FKName = part[0] + '_' + 'jntFK' + '_' + part[2] + '_' + part[3]
        prcName = part[0] + '_' + 'prc' + '_' + part[2] + '_' + part[3]
          
        pm.parentConstraint(IKName, sel, n = prcName, mo = True, w = 1)
        pm.parentConstraint(FKName, sel , mo = True, w = 0)
        
        pm.connectAttr(reverse + ".outputX", prcName + "." + IKName + "W0")
        pm.connectAttr(IKFKSwitch + ".IKFK", prcName + "." + FKName + "W1")

with pm.window( title = '', ret = True):
    with pm.columnLayout( adjustableColumn = True ):
        pm.text( label = 'please parts name ' )
        partsName = pm.radioButtonGrp( numberOfRadioButtons = 4,
                                    label = 'partsName',
                                    labelArray4 = [ 'Arm','Leg','Hear','Tail'])
        pm.text( label = 'Remember to select joints...' )
        pm.button( label = 'createChild', c = 'createSwitch(partsName.getSelect())')