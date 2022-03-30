import maya.cmds as cmds

def createPhotographSet(name = 'camera', trs = (0, 0, 5), rot = (0,0,0)):
    cam = cmds.camera(name = 'shotCam_' + name)
    litShape = cmds.spotLight()
    litParent = cmds.listRelatives(litShape, p = True)
    lit = cmds.rename(litParent, "shotLit_" + name)
    cmds.setAttr(cam[0] + ".translate", trs[0], trs[1], trs[2], type = "double3")
    cmds.setAttr(cam[0] + ".rotate", rot[0], rot[1], rot[2], type = "double3")
    cmds.setAttr(lit + ".translate", trs[0], trs[1], trs[2], type = "double3")
    cmds.setAttr(lit + ".rotate", rot[0], rot[1], rot[2], type = "double3")
    cmds.parent(lit, cam[0])
    return cam

def shotImages(cameraShape = [], imageName = '', width = 1920, height = 1080, imageFormat = 32, isRenderer = "mayaHardware2"):
    cmds.setAttr("perspShape" + ".renderable", 0)
    cmds.setAttr("defaultRenderGlobals.animation", 0)
    cmds.setAttr("defaultRenderGlobals.currentRenderer", isRenderer, type = "string")
    cmds.setAttr("defaultRenderGlobals.imageFilePrefix", imageName, type = "string")
    cmds.setAttr("defaultResolution.width", width)
    cmds.setAttr("defaultResolution.height", height)
    cmds.setAttr("defaultRenderGlobals.imageFormat", imageFormat)
    cmds.setAttr(cameraShape[1] + ".renderable", 1)
    cmds.render(b = True, rep = True)
    cmds.delete(cameraShape[0])

def secenece(cameraShape = [], imageName = '', width = 1920, height = 1080, imageFormat = 32, isRenderer = "mayaHardware2", startFrame = 0, endFrame = 1):
    cmds.setAttr("perspShape" + ".renderable", 0)
    cmds.setAttr("defaultRenderGlobals.currentRenderer", isRenderer, type = "string")
    cmds.setAttr("defaultRenderGlobals.imageFilePrefix", imageName, type = "string")
    cmds.setAttr("defaultResolution.width", width)
    cmds.setAttr("defaultResolution.height", height)
    cmds.setAttr("defaultRenderGlobals.imageFormat", imageFormat)
    cmds.setAttr(cameraShape[1] + ".renderable", 1)
    cmds.setAttr("defaultRenderGlobals.outFormatControl", 0)
    cmds.setAttr("defaultRenderGlobals.animation", 1)
    cmds.setAttr("defaultRenderGlobals.animationRange", 0)
    cmds.setAttr("defaultRenderGlobals.extensionPadding", 3)
    cmds.setAttr("defaultRenderGlobals.startFrame", startFrame)
    cmds.setAttr("defaultRenderGlobals.endFrame", endFrame)
    cmds.setAttr("defaultRenderGlobals.putFrameBeforeExt", 1)
    cmds.setAttr("defaultRenderGlobals.periodInExt", 2)
    cmds.render(b = True, rep = True)

def playblast():
    pass

def wireFrameImage():
    pass

'''
def main():
    cam = createPhotographSet(trs = (5.987, 3.484, 6.591), rot = (-16.311, 43.027, 0.0))
    start = cmds.getAttr("defaultRenderGlobals.startFrame")
    end = cmds.getAttr("defaultRenderGlobals.endFrame")
    secenece(cameraShape = cam, imageName = cam[0], startFrame = start, endFrame = end)

'''

def main():
    cam1 = createPhotographSet(name = 'front', trs = (2.883, 76.78, 335.096), rot = (0.0, 0.0, 0.0))
    cam2 = createPhotographSet(name = 'side', trs = (342.247, 78.456, 1.291), rot = (0.0, 90.0, 0.0))
    cam3 = createPhotographSet(name = 'persp', trs = (213.072, 216.63, 205.637,), rot = (-25.01, 44.044, -0.0))
    cams = [cam1, cam2, cam3]
    for cam in cams:
        shotImages(cameraShape = cam, imageName = cam[0])

  