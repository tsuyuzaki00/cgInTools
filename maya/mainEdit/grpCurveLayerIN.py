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
        
    sels = pm.ls(sl = True, dag = True)
    for sel in sels:
        if sel.nodeType() == 'transform':
            if pm.listRelatives(sel, c = True, type = 'nurbsCurve'):
                if pm.objExists( '_'.join(['selCtrl',scene,'layer'] ) ):
                    pm.editDisplayLayerMembers(ctrlLayer, sel)
                else :
                    if pm.objExists( '_'.join(['selCtrl',scene,'layer'] ) ):
                        for i in range(100):
                            ctrlLayer = pm.createDisplayLayer(n = '_'.join( ['grpCtrl' + chr(i),scene,'layer'] ))
                            if not pm.objExists( '_'.join(['selCtrl',scene,'layer'] ) ):
                                pm.editDisplayLayerMembers(ctrlLayer, sel)
                                break
                    
                    
                    