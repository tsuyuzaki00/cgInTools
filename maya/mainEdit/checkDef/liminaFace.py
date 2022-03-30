import maya.cmds as cmds

def OKList(sel, check):
    print 'OK' + ' : ' + check + ' : ' + sel
def NGList(sel, check):
    print 'NG' + ' : ' + check + ' : ' + sel

def liminaCheck(sels):
    check = 'LiminaFace'
    for sel in sels:
        limina = cmds.polyInfo(sel, nmv = True, nme = True, nue = True, iv = True, ie = True, lf = True)
        if limina == None:
            OKList(sel, check)
        else :
            cmds.select(limina)
            NGList(sel, check)
            
def main():
    sels = cmds.ls(sl = True)
    liminaCheck(sels)

main()