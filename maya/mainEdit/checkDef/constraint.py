import maya.cmds as cmds

def OKList(sel, check):
    print 'OK' + ' : ' + check + ' : ' + sel
def NGList(sel, check):
    print 'NG' + ' : ' + check + ' : ' + sel

def constraintCheck(sels):
    check = 'Constrain'
    for sel in sels:
        if cmds.listConnections( sel , type = 'parentConstraint'):
            NGList(sel, check)
        elif cmds.listConnections( sel , type = 'pointConstraint'):
            NGList(sel, check)
        elif cmds.listConnections( sel , type = 'orientConstraint'):
            NGList(sel, check)
        elif cmds.listConnections( sel , type = 'scaleConstraint'):
            NGList(sel, check)
        elif cmds.listConnections( sel , type = 'aimConstraint'):
            NGList(sel, check)
        elif cmds.listConnections( sel , type = 'poleVectorConstraint'):
            NGList(sel, check)
        else :
            OKList(sel, check)
            
def main():
    sels = cmds.ls(sl = True)
    constraintCheck(sels)

main()