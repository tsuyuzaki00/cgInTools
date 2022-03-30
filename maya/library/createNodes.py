import pymel.core as pm
from ..library import getNameSplits as gns
class CreateNode():
    def __init__(self, name = ''):
        self.name = name
    
    def cameraNode(self):
        sel = pm.camera(n = self.name)
        self.renameTemplate(sel = sel[0])

    def polyCubeNode(self):
        sel = pm.polyCube(n = self.name)
        self.renameTemplate(sel = sel[0])

    def polyBallNode(self):
        sel = pm.polyCube(n = self.name)
        pm.polySmooth(dv = 2)
        self.renameTemplate(sel = sel[0])

    def polyCylinderNode(self):
        sel = pm.polyCylinder(sc = 2 ,sa = 16, n = self.name)
        self.renameTemplate(sel = sel[0])

    def polyPlaneNode(self):
        sel = pm.polyPlane(w = 10, h = 10, n = self.name)
        self.renameTemplate(sel = sel[0])

    def imagePlaneNode(self):
        sel = pm.imagePlane(n = self.name)
        self.renameTemplate(sel = sel[0])

    def spotLightNode(self):
        shape = pm.spotLight(n = self.name)
        sel = pm.listRelatives(shape, p = True)
        self.renameTemplate(sel = sel[0])

    def pointLightNode(self):
        shape = pm.pointLight(n = self.name)
        sel = pm.listRelatives(shape, p = True)
        self.renameTemplate(sel = sel[0])

    def directionalLightNode(self):
        shape = pm.directionalLight(n = self.name)
        sel = pm.listRelatives(shape, p = True)
        self.renameTemplate(sel = sel[0])

    def ambientLightNode(self):
        shape = pm.ambientLight(n = self.name)
        sel = pm.listRelatives(shape, p = True)
        self.renameTemplate(sel = sel[0])

    def spaceLocatorNode(self):
        sel = pm.spaceLocator(n = self.name)
        self.renameTemplate(sel = sel[0])

    def nullNode(self):
        sel = pm.createNode('transform', n = self.name)
        self.renameTemplate(sel = sel)

    def ikHandleNode(self):
        sel = pm.selected()
        ikHand = pm.ikHandle(sj = sel[0], ee = sel[1], n = self.name)
        test = pm.rename(ikHand[1], self.name)
        self.renameTemplate(sel = ikHand[0])
        self.renameTemplate(sel = test)

    def renameTemplate(self, sel):
        getNameSplit = gns.GetNameSplit()
        scene = getNameSplit.scene()
        num = '1'.zfill(2)
        node = getNameSplit.node(sel)
        obj = getNameSplit.obj(sel)
        pos = getNameSplit.pos(sel)

        pm.rename(sel, '_'.join( [pos, obj, node, scene, num] ))
