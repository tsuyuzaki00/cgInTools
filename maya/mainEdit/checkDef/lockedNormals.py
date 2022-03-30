import maya.cmds as cmds

def OKList(sel, check):
    print 'OK' + ' : ' + check + ' : ' + sel
def NGList(sel, check):
    print 'NG' + ' : ' + check + ' : ' + sel

def lockedNormalsCheck(sels):
    check = 'lockedNormals'
    i = 0
    for sel in sels:
        vertices =  cmds.filterExpand(cmds.polyListComponentConversion(sel,tv=True),sm=31)
        for vertex in vertices:
            locked = cmds.polyNormalPerVertex(vertex, q=True, al=True)[0]
            if locked == True:
                NGList(sel, check)
            else :
                i += 1
                if i == len(vertices):
                    OKList(sel, check)
            
def main():
    sels = cmds.ls(sl = True)
    lockedNormalsCheck(sels)

main()