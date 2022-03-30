import maya.cmds as cmds

def OKList(sel, check):
    print 'OK' + ' : ' + check + ' : ' + sel
def NGList(sel, check):
    print 'NG' + ' : ' + check + ' : ' + sel

def parentGeometryCheck(sels):
    check = 'ParentGeometry'
    for sel in sels:
        shapeNode = False
        parents = cmds.listRelatives(sel, p = True, fullPath = True)
        if parents is not None:
            for i in parents:
                parentsChildren = cmds.listRelatives(i, fullPath = True)
                for l in parentsChildren:
                    if cmds.nodeType(l) == 'mesh':
                        shapeNode = True
        if shapeNode == True:
            NGList(sel, check)
        else :
            OKList(sel, check)


def main():
    sels = cmds.ls(sl = True)
    parentGeometryCheck(sels)

main()