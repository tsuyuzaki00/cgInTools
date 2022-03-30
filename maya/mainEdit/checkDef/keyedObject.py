import maya.cmds as cmds

def OKList(sel, check):
    print 'OK' + ' : ' + check + ' : ' + sel
def NGList(sel, check):
    for i in sel:
        print 'NG' + ' : ' + check + ' : ' + i

def keyedObjectCheck(sels):
    check = 'KeyedObject'
    OKs = []
    NGs = []
    for sel in sels:
        listKeys = cmds.listAttr(v = True, k = True)
        for listKey in listKeys:
            checkKey = cmds.keyframe(sel, query=True, at=listKey, timeChange=True)
            if checkKey == None:
                OKs.append(listKey)
            else :
                NGs.append(listKey)

        print 'OK :' + str(OKs)
        print 'NG :' + str(NGs)
    
            
def main():
    sels = cmds.ls(sl = True)
    keyedObjectCheck(sels)

main()