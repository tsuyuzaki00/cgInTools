import pymel.core as pm

def main():
    select1 = pm.selected() [0]
    select2 = pm.selected() [1]

    ctrl = select1.split("_")
    jnt = select2.split("_")

    name = ctrl[0] + '_' + ctrl[1]

    pm.pointConstraint( select1 , select2 , n = name + '_pointConstraint_' + ctrl[-1])
    pm.orientConstraint( select1 , select2 ,  n = name + '_orientConstraint_' + ctrl[-1])