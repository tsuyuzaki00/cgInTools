# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import cgInTools as cit
#from cgInTools.maya.library import _testPath as TP
from cgInTools.maya.manager import selectSetCtrlMN as MN
#from cgInTools.maya.option import autoRenameOP as OP
#from cgInTools.maya.library import objectLB as oLB
#from cgInTools.maya.library import renderLB as LB
#from cgInTools.maya.execute import infJntRemoveEditEX as EX
cit.reloads([MN])

def main():
    #OP.main()
    MN.main()
    #EX.main()
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
    """
    
    """
    fkik=LB.FKIK()
    fkik.setSourceNode("joint1")
    fkik.setTargetNode("joint3")
    fkik.setThirdNode("joint2")
    fkik.setUI("UIsan")
    fkik.createThreeJoints()
    replace=LB.Constrain()
    replace.setSourceNode(sourceNode)
    replace.setTargetNode(targetNode)
    replace.proximityPin()
    """

main()