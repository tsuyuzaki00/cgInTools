import maya.cmds as cmds

def OKList(sel, check):
    print 'OK' + ' : ' + check + ' : ' + sel
def NGList(sel, check):
    print 'NG' + ' : ' + check + ' : ' + sel

def childNullCheck(sels):
    check = 'ChildNull'
    for sel in sels:
        children = cmds.listRelatives(sel, ad = True)
        if children is None:
            NGList(sel, check)
        else :
            OKList(sel, check)

def main():
    sels = cmds.ls(sl = True)
    childNullCheck(sels)

main()