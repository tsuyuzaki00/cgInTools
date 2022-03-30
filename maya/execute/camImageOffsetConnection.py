import maya.cmds as cmds

def main():
    camImageOffsetConnection()

def camImageOffsetConnection():
    cam = cmds.ls(sl = True, dag = True, typ = 'camera')
    connection = cmds.listConnections(cam, t = 'imagePlane')

    imageP = connection[0].replace( cam[0] + '->', '' )

    cmds.connectAttr(cam[0] + '.filmOffset', imageP + '.offset')