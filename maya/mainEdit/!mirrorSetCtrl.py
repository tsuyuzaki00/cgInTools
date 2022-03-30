import pymel.core as pm

def curveMirror(setName, getName):
    sels = pm.selected()
    for sel in sels:
        selTrs = pm.getAttr(sel + '.translate')
        selRot = pm.getAttr(sel + '.rotate')
        selScl = pm.getAttr(sel + '.scale')
        renameMove = sel.replace(setName, getName)
        pm.setAttr(renameMove + '.translate', selTrs[0] * -1, selTrs[1], selTrs[2], type ='double3')
        pm.setAttr(renameMove + '.rotate', selRot[0], selRot[1] * -1, selRot[2] * -1, type ='double3')
        pm.setAttr(renameMove + '.scale', selScl[0], selScl[1], selScl[2], type ='double3')

def main():
    curveMirror('_L','_R')

main()