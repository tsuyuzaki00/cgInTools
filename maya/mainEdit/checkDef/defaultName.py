import maya.cmds as cmds

def OKList(sel, check):
    print 'OK' + ' : ' + check + ' : ' + sel
def NGList(sel, check, text):
    print 'NG' + ' : ' + check + ' : ' + sel + " Rename:"+ text

def expressionCheck(sels):
    check = 'DefaultName'
    sceneName = pm.sceneName().basename()
    part = sceneName.split("_")
    
    if part[0].endswith('.ma') or part[0].endswith('.mb'):
        name = part[0][:-3]
    elif part[0] == '':
        name = 'scene'
    else:
        name = part[0]
    
    for sel in sels:
        i=sel.split('|')[-1]
        if '_model_' in i:
            NGList(sel, check, 'fix is _model_')
        elif 'pCube' in i or 'polySurface' in i or 'pCylinder' in i or 'pSphere' in i or 'pCone' in i or 'pPlane' in i or 'pTorus' in i or 'pPyramid' in i or 'pPipe' in i or '__Pasted' in i:
            NGList(sel, check, 'defaultName')
        elif not 'geo' in i:
            NGList(sel, check, 'add lower geo')
        elif not name in i:
            NGList(sel, check, 'scene name is different')
        else :
            OKList(sel, check)
            
def main():
    sels = cmds.ls(sl = True)
    expressionCheck(sels)

main()