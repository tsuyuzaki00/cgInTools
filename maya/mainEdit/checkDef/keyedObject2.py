import maya.cmds as cmds

def OKList(sel, check):
    print 'OK' + ' : ' + check + ' : ' + sel
def NGList(sel, check):
    print 'NG' + ' : ' + check + ' : ' + sel

def keyedObjectCheck(sels):
    check = 'KeyedObject'

    for sel in sels:
        if cmds.listConnections( sel , type = 'animCurveTU'):
            NGList(sel, check)
        else :
            OKList(sel, check)

    '''
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

    '''
            
def main():
    sels = cmds.ls(sl = True)
    keyedObjectCheck(sels)

main()