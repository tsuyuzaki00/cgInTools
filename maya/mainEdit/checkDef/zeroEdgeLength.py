from maya import cmds,mel

def OKList(sel, check):
    print 'OK' + ' : ' + check + ' : ' + sel
def NGList(sel, check):
    print 'NG' + ' : ' + check + ' : ' + sel

def zeroEdgeLengthCheck(sels):
    check = 'ZeroEdgeLength'
    zeroEdge = mel.eval('polyCleanupArgList 4 { "0","2","0","0","0","0","0","0","0","1e-005","1","1e-005","0","1e-005","0","-1","0" };')
    for sel in sels:
        if zeroEdge == []:
            OKList(sel, check)
        else :
            for i in zeroEdge:
                cmds.select(zeroEdge)
                NGList(i, check)
            
def main():
    sels = cmds.ls(sl = True)
    zeroEdgeLengthCheck(sels)

main()