import pymel.core as pm

def curveMirror(setCurve, getCurve):
    sels = pm.selected()
    for sel in sels:
        CVs = pm.filterExpand(sel,sm = 28)
        for CV in CVs:
            CVPos = pm.pointPosition( CV , w = True )
            renameCV = CV.replace(setCurve, getCurve)
            pm.select(renameCV)
            pm.move(CVPos[0]*-1,CVPos[1],CVPos[2])

def main():
    curveMirror('_L','_R')