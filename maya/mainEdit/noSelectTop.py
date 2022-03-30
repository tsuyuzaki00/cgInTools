import pymel.core as pm

sels = pm.ls(sl = True, dag = True)
for sel in sels:
    part = sel.split('_')
    if part[-1] == 'LT' or part[-1] == 'CT' or part[-1] == 'RT':
        pass
    else :
        pm.select(sel, add = True)