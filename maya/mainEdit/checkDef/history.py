import maya.cmds as cmds

def OKList(sel, check):
    print 'OK' + ' : ' + check + ' : ' + sel
def NGList(sel, check):
    print 'NG' + ' : ' + check + ' : ' + sel

def historyCheck(sels):
    check = 'History'
    for sel in sels:
        shape = cmds.listRelatives(sel, shapes = True, typ = 'mesh')
        historySize = len(cmds.listHistory(shape))
        if historySize < 2:
            OKList(sel, check)
        else :
            NGList(sel, check)
            
def main():
    sels = cmds.ls(sl = True)
    historyCheck(sels)
    
main()