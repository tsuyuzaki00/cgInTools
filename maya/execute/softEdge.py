import pymel.core as pm

def main():
    sels = pm.selected()
    for sel in sels:
        pm.polySoftEdge(sel, a = 180)
        pm.delete(ch = True)