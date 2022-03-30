import pymel.core as pm

def main():
    sel = pm.selected()
    part = sel[1].split("_")
    
    ikHand = pm.ikHandle(sj = sel[0], ee = sel[1], n = '_'.join(['ikhl', part[1], part[-3], part[-2], part[-1]]) )
    pm.rename(ikHand[1], '_'.join(['efct', part[1], part[-3], part[-2], part[-1]])) 
    grp = '_'.join( ['grp','ctrl',part[-3]] )
    if pm.objExists(grp):
        pm.parent(ikHand[0], grp)