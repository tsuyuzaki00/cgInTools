import pymel.core as pm

def constraintRename():
    to = 'trs'
    sels = pm.selected()[0:]
    for sel in sels:
        selb = sel[:-1]
        part = selb.split("_")
        trsoff = to + part[-1][0].upper() + part[-1][1:]
        name = trsoff + '_' + part[1] + '_' + part[2] + '_' + part[3]
        pm.rename ( sel, name )

def changeRename():
    sels = pm.selected()[0:]
    for sel in sels:
        part = sel.split("_")
        num = len(part)
        if num == 3:
            name = part[2] + '_' + part[1] + '_' + part[0]
            pm.rename ( sel, name )
        elif num == 4:
            name = part[2] + '_' + part[1] + '_' + part[0] + '_' + part[3]
            pm.rename ( sel, name )

constraintRename()
changeRename()