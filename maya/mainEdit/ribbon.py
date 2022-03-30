import pymel.core as pm
import maya.mel as mel

class RibbonClass:
    def __init__(self):
        self.sels = pm.selected()
        self.pos = 'C'
        self.scene = 'scene'
        self.obj = 'ribbon'
        self.num = 00

    def settingRibbon(self, width = 16, joint = 5, length = 1.5):
        Ucount = joint - 1
        pm.nurbsPlane( ax = [0, 1, 0], d = 1, w = width, u = Ucount, v = 1, lr = length * 0.1, ch = False, n = '_'.join( [self.pos, self.obj, 'nurb', self.scene, '00']))
        mel.eval('string $Ucount = "%s";' % joint)
        #createHair(name Ucount,Vcount,PointPerHair,CreateRestCurves,PassiveFill,EdgeBounded,Equalize,Length,Randomization,Output,Dynamic||Static,PlaceHairsInto)
        mel.eval('createHair $Ucount 1 10 0 0 1 0 5 0 2 1 1')
        hairParents = pm.rename('hairSystem1Follicles', '_'.join( [self.pos, self.obj, 'grp', self.scene, '00']))
        pm.delete('nucleus1', 'hairSystem1OutputCurves','hairSystem1')
        parentFollicle = pm.listRelatives(hairParents, c = True)
        for i in range(len(parentFollicle)):
            deleteCurve = pm.listRelatives(parentFollicle[i] , c = True, typ = 'transform')
            pm.delete(deleteCurve[0])
            pm.select(parentFollicle[i])
            pm.rename(parentFollicle[i], '_'.join( [self.pos, self.obj, 'foll', self.scene, str(i).zfill(2)]))
            pm.joint(r = True, rad= 0.1, n = '_'.join( [self.pos, self.obj, 'jntRib', self.scene, str(i).zfill(2)]))

    def jointSelectRibbon(self):
        pass

    def nurbsCVSelectRibbon(self):
        for sel in self.sels:
            print sel[-1][-1]

ribbonClass = RibbonClass()
ribbonClass.settingRibbon(joint = 10)