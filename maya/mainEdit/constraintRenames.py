import pymel.core as pm

def parentConstraintRename(exConstraint, inConstraint):
    part = exConstraint.split("_")
    renameConstraint = part[0] + '_' + 'prc' + '_' + part[2] + '_' + part[3]
    pm.parentConstraint(exConstraint, inConstraint, n = renameConstraint, mo = True, w = 1)

def pointConstraintRename(exConstraint, inConstraint):
    part = exConstraint.split("_")
    renameConstraint = part[0] + '_' + 'ptc' + '_' + part[2] + '_' + part[3]
    pm.pointConstraint(exConstraint, inConstraint, n = renameConstraint, mo = True, w = 1)
    
def orientConstraintRename(exConstraint, inConstraint):
    part = exConstraint.split("_")
    renameConstraint = part[0] + '_' + 'otc' + '_' + part[2] + '_' + part[3]
    pm.orientConstraint(exConstraint, inConstraint, n = renameConstraint, mo = True, w = 1)
    
def scaleConstraintRename(exConstraint, inConstraint):
    part = exConstraint.split("_")
    renameConstraint = part[0] + '_' + 'slc' + '_' + part[2] + '_' + part[3]
    pm.scaleConstraint(exConstraint, inConstraint, n = renameConstraint, mo = True, w = 1)
    
def aimConstraintRename(exConstraint, inConstraint):
    part = exConstraint.split("_")
    renameConstraint = part[0] + '_' + 'amc' + '_' + part[2] + '_' + part[3]
    pm.aimConstraint(exConstraint, inConstraint, n = renameConstraint, mo = True, w = 1)
    
def poleVectroConstraintRename(exConstraint, inConstraint):
    part = exConstraint.split("_")
    renameConstraint = part[0] + '_' + 'pvc' + '_' + part[2] + '_' + part[3]
    pm.poleVectorConstraint(exConstraint, inConstraint, n = renameConstraint, mo = True, w = 1)

sels = pm.selected()

def jointConstraint():
    for sel in sels:
        part = sel.split("_")
        jntName = part[0] + '_' + 'jnt' + '_' + part[2] + '_' + part[3]
        parentConstraintRename(sel, jntName)
        
#jointConstraint()

#parentConstraintRename(sels[0], sels[1])
#pointConstraintRename(sels[0], sels[1])
#orientConstraintRename(sels[0], sels[1])
#scaleConstraintRename(sels[0], sels[1])
#aimConstraintRename(sels[0], sels[1])
#poleVectorConstraintRename(sels[0], sels[1])