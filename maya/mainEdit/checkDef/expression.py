import maya.cmds as cmds

def OKList(sel, check):
    print 'OK' + ' : ' + check + ' : ' + sel
def NGList(sel, check):
    print 'NG' + ' : ' + check + ' : ' + sel

def expressionCheck(sels):
    check = 'Expression'
    for sel in sels:
        if cmds.listConnections( sel , type = 'expression'):
            NGList(sel, check)
        else :
            OKList(sel, check)
            
def main():
    sels = cmds.ls(sl = True)
    expressionCheck(sels)

main()