import maya.cmds as cmds

def OKList(sel, check):
    print 'OK' + ' : ' + check + ' : ' + sel
def NGList(sel, check):
    print 'NG' + ' : ' + check + ' : ' + sel

def layerCheck(sels):
    check = 'Layer'
    for sel in sels:
        layer = cmds.listConnections(sel, type = "displayLayer")
        if layer == None:
            OKList(sel, check)
        else :
            NGList(sel, check)


def main():
    sels = cmds.ls(sl = True)
    layerCheck(sels)

main()