# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import cgInTools as cit
#from cgInTools.maya.library import _testPath as TP
#from cgInTools.maya.manager import equipmentSettingsMN as MN
#from cgInTools.maya.option import autoRenameOP as OP
#from cgInTools.maya.library import objectLB as oLB
#from cgInTools.maya.library import constrainLB as LB
from cgInTools.maya.execute import exportAnimPackEX as EX
cit.reloads([EX])

def main():
    #OP.main()
    #MN.main()
    EX.main()
    #TP.main()
    """
    objs=cmds.ls(sl=True)
    settings=[]
    for obj in objs:
        nm=oLB.MatrixObject(obj)
        settings=[nm]

    shot=LB.EquipmentSettings()
    for setting in settings:
        shot.addSetting(setting)
        shot.createLayout()
    
    sourceNode=cmds.ls(sl=True)[0]
    targetNode=cmds.ls(sl=True)[1]
    thirdNode=cmds.ls(sl=True)[2]

    replace=LB.Constrain()  
    replace.setSourceNode(sourceNode)
    replace.setTargetNode(targetNode)
    replace.setThirdNode(thirdNode)
    replace.ikHandleConstraint()
    """
    

main()