from maya import cmds,mel

def OKList(sel, check):
    print 'OK' + ' : ' + check + ' : ' + sel
def NGList(sel, check):
    print 'NG' + ' : ' + check + ' : ' + sel

def holesCheck(sels):
    check = 'Holes'
    holes = mel.eval('polyCleanupArgList 4 { "0","2","1","0","0","0","1","0","0","1e-05","0","1e-05","0","1e-05","0","-1","0","0" };')
    for sel in sels:
        if holes == []:
            OKList(sel, check)
        else :
            for i in holes:
                cmds.select(holes)
                NGList(i, check)
            
def main():
    sels = cmds.ls(sl = True)
    holesCheck(sels)

main()