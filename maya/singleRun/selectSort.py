import pymel.core as pm

sels = pm.selected()

hoge = sorted(sels, key=str)
sels.sort()

for sel in sels:
    pm.(sel, back = True)