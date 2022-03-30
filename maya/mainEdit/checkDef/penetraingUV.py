import maya.cmds as cmds

def OKList(sel, check):
    print 'OK' + ' : ' + check + ' : ' + sel
def NGList(sel, check):
    print 'NG' + ' : ' + check + ' : ' + sel

def penetratingUVCheck(sels):
    check = 'PenetratingUV'
    for sel in sels:
        shape = cmds.listRelatives(sel, shapes = True, fullPath = True)
        convertToFaces = cmds.ls(cmds.polyListComponentConversion(shape, tf=True), fl=True)
        overlapping = (cmds.polyUVOverlap(convertToFaces, oc=True ))
        if overlapping is not None:
            for obj in overlapping:
                cmds.select(obj, add = True)
                NGList(obj, check)
        else :
            OKList(sel, check)
            
            
def main():
    sels = cmds.ls(sl = True)
    penetratingUVCheck(sels)

main()