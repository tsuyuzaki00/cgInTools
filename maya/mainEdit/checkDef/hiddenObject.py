import maya.cmds as cmds

def OKList(sel, check):
    print 'OK' + ' : ' + check + ' : ' + sel
def NGList(sel, check):
    print 'NG' + ' : ' + check + ' : ' + sel

def hiddenObjectCheck(sels):
    check = 'HiddenObject'
    for sel in sels:
        if cmds.getAttr(sel + '.v') == 1:
            OKList(sel, check)
        else :
            NGList(sel, check)
            
def main():
    sels = cmds.ls(sl = True)
    hiddenObjectCheck(sels)

main()