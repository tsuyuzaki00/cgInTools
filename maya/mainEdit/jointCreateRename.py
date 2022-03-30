import pymel.core as pm

def main():
    jointCreate(1,'C')

def jointCreate(num,pos):
    sceneName = pm.sceneName().basename()
    part = sceneName.split("_")
    
    if part[0].endswith('.ma') or part[0].endswith('.mb'):
        scene = part[0][:-3]
    elif part[0] == '':
        scene = 'scene'
    else:
        scene = part[0]
    
    sels = pm.selected()
    rootName = '_'.join( [pos,'root','jnt',scene,'00'] )
    hiyJntName = '_'.join( [pos,'joint','jnt',scene,'00'] )
    
    if sels == []:
        jnt = pm.joint(rad= 0.5, n = rootName)
        grpJnt = '_'.join( ['grp','jnt',scene] )
        if pm.objExists(grpJnt):
            pm.parent(jnt, grpJnt)
            
    elif pm.objExists(hiyJntName):
        for i in range(1000):
            hiyJntName = '_'.join( [pos,'joint','jnt', scene, str(i).zfill(2)] )
            if not pm.objExists(hiyJntName):
                jnt = pm.joint(r = True, p = (2,0,0), rad= 0.5, n = hiyJntName)
                break
    else:
        jnt = pm.joint(r = True, p = (2,0,0), rad= 0.5, n = hiyJntName)