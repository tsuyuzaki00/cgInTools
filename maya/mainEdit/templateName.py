import pymel.core as pm

def scene(sel):
    sceneName = pm.sceneName().basename()
    part = sceneName.split("_")
    if part[0].endswith('.ma') or part[0].endswith('.mb'):
        scene = part[0][:-3]
    elif part[0] == '':
        scene = 'scene'
    else:
        scene = part[0]
    return scene

