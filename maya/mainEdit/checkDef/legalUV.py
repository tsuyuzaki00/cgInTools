import maya.cmds as cmds

def OKList(sel, check):
    print 'OK' + ' : ' + check + ' : ' + sel
def NGList(sel, check):
    print 'NG' + ' : ' + check + ' : ' + sel

def NoUVCheck(sels):
    check = 'Legal UV'
    i = 0
    for sel in sels:
        objectUVs = cmds.filterExpand(cmds.polyListComponentConversion(sel, tuv=True), sm=35)
        for j in objectUVs:
            uvPos = cmds.polyEditUV(j, q=True, v=True, u=True)
            for k in uvPos:
                if float(k) < 0.0 or float(k) > 1.0:
                    cmds.select(j, add = True)
                    NGList(j, check)
                else :
                    i += 1
                    if i == len(j):
                        OKList(sel, check)
            
def main():
    sels = cmds.ls(sl = True)
    NoUVCheck(sels)

main()