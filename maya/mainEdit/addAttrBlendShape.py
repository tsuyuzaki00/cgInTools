import maya.cmds as cmds

def curveStar(name='star',s=1):
    a00 = (s*0, s*2, 0)
    a01 = (s*-1.2, s*-1.75, 0)
    a02 = (s*2,  s*0.5, 0)
    a03 = (s*-2, s*0.5, 0)
    a04 = (s*1.2, s*-1.75, 0)
    tName = cmds.curve( d=1,p=[a00,a01,a02,a03,a04,a00],n=name)

    return tName


def createBlendShapeCtl(BSName):
    targetNum = cmds.blendShape(BSName, q=True, wc=True)

    targetNames = []
    posGrpList = []


    ctl = curveStar(name=BSName+'_ctl',s=3)
    offset = cmds.group(ctl,n='offset_'+ctl.capitalize())
    position = cmds.group(offset,n='position_'+ctl.capitalize())

    for i in range(2*targetNum):
        targetName = cmds.aliasAttr(BSName+'.weight['+str(i)+']',q=1)
        if targetName == '' or targetName in targetNames:
            pass

        else:
            cmds.addAttr(ctl,ln = targetName, k = True, at = 'float')
            cmds.connectAttr(ctl+'.'+targetName,BSName+'.weight['+str(i)+']')
            targetNames.append(targetName)

createBlendShapeCtl('facialBlendShape')