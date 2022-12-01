from maya import cmds,mel

def OKList(sel, check):
    print ('OK' + ' : ' + check + ' : ' + sel)
def NGList(sel, check):
    print ('NG' + ' : ' + check + ' : ' + sel)

def inversUVCheck(sels):
    check = 'Invers UV'
    for sel in sels:
        cmds.hilite(sel)
        invers = mel.eval('selectUVFaceOrientationComponents {} 1 2 1')
        if invers == []:
            OKList(sel, check)
        else :
            for i in invers:
                cmds.select(invers)
                NGList(i, check)
            
def main():
    sels = cmds.ls(sl = True)
    inversUVCheck(sels)

main()