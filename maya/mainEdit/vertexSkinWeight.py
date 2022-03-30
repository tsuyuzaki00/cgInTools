import pymel.core as pm

def twoJointSkinWeight(geo = '', firstSelJoint = '', secondSelJoint = '', firstValueJoint = 1, secondValueJoint = 0):
    vtxSels = pm.selected()
    pm.skinPercent('skinCluster11', vtxSels, transformValue = [('tail_C0_5_jnt', 0.3550), ('tail_C0_6_jnt', 0.6550)])

def main():
    sels = pm.selected()
    twoJointSkinWeight(geo = sels[0], firstSelJoint = sels[1], secondSelJoint = sels[2], firstValueJoint = 1, secondValueJoint = 0)

main() 