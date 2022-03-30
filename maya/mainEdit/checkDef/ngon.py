import maya.cmds as cmds

def OKList(sel, check):
    print 'OK' + ' : ' + check + ' : ' + sel
def NGList(sel, check):
    print 'NG' + ' : ' + check + ' : ' + sel

def NgonCheck(sels):
    check = 'N-Gon'
    NGs = 0
    for sel in sels:
        allFaces = cmds.filterExpand(cmds.polyListComponentConversion(sel, tf=True), sm=34)
        for vertices in allFaces:
            allvertices = cmds.filterExpand(cmds.polyListComponentConversion(vertices, tv=True), sm=31)
            if len(allvertices)==3:
                pass
            elif len(allvertices)==4:
                pass
            elif len(allvertices)>=5:
                cmds.select(vertices, add = True)
                NGs += 1

        if NGs > 0:
            NGList(sel, check)
        else :
            OKList(sel, check)
        

def main():
    sels = cmds.ls(sl = True)
    NgonCheck(sels)

main()