import pymel.core as pm

def main():
    sels = pm.selected()
    poleVectorConstraintRename(sels)

def poleVectorConstraintRename(sels):
    if len(sels) >= 3 or len(sels) <= 1:
        pm.error('Please select two')
        
    part = sels[1].split("_")
    
    renameConstraint = '_'.join( ['pvc',part[1],part[2],part[3]] )
    pm.poleVectorConstraint(sels[0], sels[1], n = renameConstraint, w = 1)