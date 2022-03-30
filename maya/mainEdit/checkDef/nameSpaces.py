import maya.cmds as cmds

def OKList(sel, check):
    print 'OK' + ' : ' + check + ' : ' + sel
def NGList(sel, check):
    print 'NG' + ' : ' + check + ' : ' + sel

def nameSpacesCheck(sels):
    check = 'NameSpaces'
    for sel in sels:
        if ':' in sel:
            NGList(sel, check)
        else:
            OKList(sel, check)

def main():
    sels = cmds.ls(sl = True)
    nameSpacesCheck(sels)

main()