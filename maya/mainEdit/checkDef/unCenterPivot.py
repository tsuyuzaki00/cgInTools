import maya.cmds as cmds

def OKList(sel, check):
    print 'OK' + ' : ' + check + ' : ' + sel
def NGList(sel, check):
    print 'NG' + ' : ' + check + ' : ' + sel

def unCenterPivotCheck(sels):
    check = 'UnCenterPivot'
    for sel in sels:
        if cmds.xform(sel,q=1,ws=1,rp=1) == [0,0,0]:
            OKList(sel, check)
        else :
            NGList(sel, check)
            
def main():
    sels = cmds.ls(sl = True)
    unCenterPivotCheck(sels)

main()