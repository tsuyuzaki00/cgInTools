import pymel.core as pm

def main():
    sceneName = pm.sceneName().basename()
    part = sceneName.split("_")
    if part[0].endswith('.ma') or part[0].endswith('.mb'):
        scene = part[0][:-3]
    elif part[0] == '':
        scene = 'scene'
    else:
        scene = part[0]

    sels = pm.selected()
    sel = tuple(sels)
    pm.polyUnite( sel, n = sels[0])
    pm.delete(ch = True)
    grpIN = pm.selected()
    if pm.objExists( '_'.join(['grp','geo',scene]) ):
        pm.parent(grpIN, '_'.join(['grp','geo',scene]) )