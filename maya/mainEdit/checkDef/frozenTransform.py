import maya.cmds as cmds

def OKList(sel, check):
    print 'OK' + ' : ' + check + ' : ' + sel
def NGList(sel, check):
    print 'NG' + ' : ' + check + ' : ' + sel

def frozenTransformCheck(sels):
    check = 'FrozenTransform'
    for sel in sels:
        translation = cmds.xform(sel, q=True, worldSpace = True, translation = True)
        rotation = cmds.xform(sel, q=True, worldSpace = True, rotation = True)
        scale = cmds.xform(sel, q=True, worldSpace = True, scale = True)
        if translation == [0.0,0.0,0.0] and rotation == [0.0,0.0,0.0] and scale == [1.0,1.0,1.0]:
            OKList(sel, check)
        elif not translation == [0.0,0.0,0.0] or not rotation == [0.0,0.0,0.0] or not scale == [1.0,1.0,1.0]:
            NGList(sel, check)
            
def main():
    sels = cmds.ls(sl = True)
    frozenTransformCheck(sels)

main()