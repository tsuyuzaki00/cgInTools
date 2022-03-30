import pymel.core as pm

sels = pm.selected()
for sel in sels:
    part = sel.split('_')
    name = '_'.join([part[2],part[1],part[4],part[3],part[0]])
    #name = '_'.join([part[3],part[1],part[0],part[2],part[4]])
    #name = '_'.join([part[0],part[1],part[3],part[2],part[4]])
    
    pm.rename(sel, name)
    