import pymel.core as pm

def main():
    sels = pm.selected()
    aimConstraintRename(sels)

def aimConstraintRename(sels):
    if len(sels) >= 3 or len(sels) <= 1:
        pm.error('Please select two')
        
    part = sels[1].split("_")
    
    renameConstraint = '_'.join( ['amc',part[1],part[2],part[3]] )
    pm.aimConstraint(sels[0], sels[1], n = renameConstraint, mo = True, w = 1)