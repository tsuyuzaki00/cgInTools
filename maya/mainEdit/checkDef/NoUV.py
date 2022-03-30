import maya.cmds as cmds

def OKList(sel, check):
    print 'OK' + ' : ' + check + ' : ' + sel
def NGList(sel, check):
    print 'NG' + ' : ' + check + ' : ' + sel

def NoUVCheck(sels):
    check = 'No UV'
    for sel in sels:
        try:
            objectUVs = cmds.filterExpand(cmds.polyListComponentConversion(sel, tuv=True), sm=35)
            for j in objectUVs:
                uvPos = cmds.polyEditUV(j, q=True, v=True, u=True)
                for k in uvPos:
                    if float(k) < 0.0 or float(k) > 0.0:
                        OKList(sel, check)
                        return
        except:
            NGList(sel, check)
            
def main():
    sels = cmds.ls(sl = True)
    NoUVCheck(sels)

main()