import maya.cmds as cmds
from mainEdit import qt
from PySide2 import QtGui, QtCore, QtWidgets

class IKFKMatchingWindow(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(IKFKMatchingWindow, self).__init__(*args, **kwargs)
        mainLayout = QtWidgets.QFormLayout(self)

        buttonLegIKL = QtWidgets.QPushButton('LegIKMatching')
        buttonLegFKL = QtWidgets.QPushButton('LegFKMatching')
        #buttonArmIKL = QtWidgets.QPushButton('ArmIKMatching')
        #buttonArmFKL = QtWidgets.QPushButton('ArmFKMatching')
        
        widthLayout = QtWidgets.QVBoxLayout(self)
        widthLayout.addWidget(buttonLegIKL, True)
        widthLayout.addWidget(buttonLegFKL, True)
        #widthLayout.addWidget(buttonArmIKL, True)
        #widthLayout.addWidget(buttonArmFKL, True)
        mainLayout.addRow(widthLayout)
        
        buttonLegIKL.clicked.connect(self._legIKMatchingL)
        buttonLegFKL.clicked.connect(self._legFKMatchingL)

    def _legFKMatchingL(self):
        legFKMatchingL()

    def _legIKMatchingL(self):
        legIKMatchingL()

def legIKMatchingL():
    rotHandIKL = cmds.xform('L_leg_jnt_IKFKRig_02', q = True, ws = True, ro = True)
    trsHandIKL = cmds.xform('L_leg_jnt_IKFKRig_02', q = True, ws = True, t = True)
    trsElbowIKL = cmds.xform('L_leg_jnt_IKFKRig_01', q = True, ws = True, t = True)

    cmds.xform('L_legIK_ctrl_IKFKRig_00', ws = True, ro = (rotHandIKL[0], rotHandIKL[1], rotHandIKL[2]))
    cmds.xform('L_legIK_ctrl_IKFKRig_00', ws = True, t = (trsHandIKL[0], trsHandIKL[1], trsHandIKL[2]))
    cmds.xform('L_legVector_ctrl_IKFKRig_00', ws = True, t = (trsElbowIKL[0], trsElbowIKL[1], trsElbowIKL[2]))

    cmds.setAttr('L_legSwitch_ctrl_IKFKRig_00.legIKFKL', 0)
    cmds.select(cl = True)

def legFKMatchingL():
    rotLegFK00L = cmds.xform('L_leg_jnt_IKFKRig_00', q = True, ws = True, ro = True)
    rotLegFK01L = cmds.xform('L_leg_jnt_IKFKRig_01', q = True, ws = True, ro = True)
    rotLegFK02L = cmds.xform('L_leg_jnt_IKFKRig_02', q = True, ws = True, ro = True)

    cmds.setAttr('L_legFK_ctrl_IKFKRig_00.rotate', 0,0,0)
    cmds.xform('L_legFK_ctrl_IKFKRig_00', ws = True, ro = (rotLegFK00L[0], rotLegFK00L[1], rotLegFK00L[2]))
    cmds.xform('L_legFK_ctrl_IKFKRig_01', ws = True, ro = (rotLegFK01L[0], rotLegFK01L[1], rotLegFK01L[2]))
    cmds.xform('L_legFK_ctrl_IKFKRig_02', ws = True, ro = (rotLegFK02L[0], rotLegFK02L[1], rotLegFK02L[2]))

    cmds.setAttr('L_legSwitch_ctrl_IKFKRig_00.legIKFKL', 1)
    cmds.select(cl = True)

def IKMatchingR():
    rotHandIKR = cmds.xform('rightArm_IK_snap_GRP', q = True, ws = True, ro = True)
    trsHandIKR = cmds.xform('rightArm_IK_snap_GRP', q = True, ws = True, t = True)
    trsElbowIKR = cmds.xform('rightForeArm_result_JNT', q = True, ws = True, t = True)

    cmds.xform('rightArm_CTRL', ws = True, ro = (rotHandIKR[0], rotHandIKR[1], rotHandIKR[2]))
    cmds.xform('rightArm_CTRL', ws = True, t = (trsHandIKR[0], trsHandIKR[1], trsHandIKR[2]))
    cmds.xform('rightElbow_CTRL', ws = True, t = (trsElbowIKR[0], trsElbowIKR[1], trsElbowIKR[2]))

    cmds.setAttr('rightArm_settings_CTRL.FK_IK_blend', 1)

def FKMatchingR():
    rotUpperArmFKR = cmds.xform('rightUpperArm_FK_snap_JNT', q = True, ws = True, ro = True)
    rotForeArmFKR = cmds.xform('rightForeArm_FK_snap_JNT', q = True, ws = True, ro = True)
    rotHandFKR = cmds.xform('rightHand_FK_snap_JNT', q = True, ws = True, ro = True)

    cmds.setAttr('rightArm_gimbal_corr_CTRL.rotate', 0,0,0)
    cmds.xform('rightUpperArm_FK_CTRL', ws = True, ro = (rotUpperArmFKR[0], rotUpperArmFKR[1], rotUpperArmFKR[2]))
    cmds.xform('rightForeArm_FK_CTRL', ws = True, ro = (rotForeArmFKR[0], rotForeArmFKR[1], rotForeArmFKR[2]))
    cmds.xform('rightHand_FK_CTRL', ws = True, ro = (rotHandFKR[0], rotHandFKR[1], rotHandFKR[2]))

    cmds.setAttr('rightArm_settings_CTRL.FK_IK_blend', 0)

def main():
    window = IKFKMatchingWindow(qt.getMayaWindow())
    window.setWindowFlags(QtCore.Qt.Window)
    window.show()

main()