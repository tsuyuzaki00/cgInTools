import maya.cmds as cmds

def OKList(sel, check):
    print 'OK' + ' : ' + check + ' : ' + sel
def NGList(sel, check):
    print 'NG' + ' : ' + check + ' : ' + sel

def SameNameCheck(sels):
    check = 'SameName'
    for sel in sels:
        longname = sel.split("|")
        if len(longname) > 1:
            NGList(sel, check)
        else:
            OKList(sel, check)

def main():
    sels = cmds.ls(sl = True)
    SameNameCheck(sels)

main()