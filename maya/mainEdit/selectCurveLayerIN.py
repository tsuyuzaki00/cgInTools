import pymel.core as pm

def main():
    sceneName = pm.sceneName().basename()
    part = sceneName.split("_")
    
    if pm.objExists(part[0]) or pm.objExists('scene'):
        pm.error('Group scene already exists')
    
    if part[0].endswith('.ma') or part[0].endswith('.mb'):
        scene = part[0][:-3]
    elif part[0] == '':
        scene = 'scene'
    else:
        scene = part[0]
        
    sels = pm.selected()
    for sel in sels:
        curve = pm.listRelatives(sel, c = True, type = 'nurbsCurve')
        if pm.objExists( '_'.join(['selCtrl',scene,'layer'] ) ):
            pm.editDisplayLayerMembers(ctrlLayer, curve)
        else :
            ctrlLayer = pm.createDisplayLayer(n = '_'.join( ['selCtrl',scene,'layer'] ))
            pm.editDisplayLayerMembers(ctrlLayer, curve)