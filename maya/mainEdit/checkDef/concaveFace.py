from maya import cmds,mel

def OKList(sel, check):
    print 'OK' + ' : ' + check + ' : ' + sel
def NGList(sel, check):
    print 'NG' + ' : ' + check + ' : ' + sel

def concaveCheck(sels):
    check = 'ConcaveFace'
    concave = mel.eval('polyCleanupArgList 4 { "0","2","1","0","1","1","0","0","0","1e-05","0","1e-05","0","1e-05","0","-1","0","0" };')
    for sel in sels:
        if concave == [] :
            OKList(sel, check)
        else :
            for i in concave :
                cmds.select(concave, add = True)
                NGList(i, check)
                
            
def main():
    sels = cmds.ls(sl = True)
    concaveCheck(sels)

main()