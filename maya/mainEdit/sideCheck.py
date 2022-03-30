import maya.cmds as cmds

objs = cmds.ls(sl=True)

def auto_side(obj,dist=0):
    left = []
    right = []
    center = []
    for obj in objs:
        boundingBox = cmds.xform(obj,q=True,boundingBox=True,ws=True)
        minX = round(boundingBox[0],3)
        maxX = round(boundingBox[3],3)
        if minX > dist and maxX > dist:
            left.append(obj)
        elif minX < -dist and maxX < -dist:
            right.append(obj)
        else:
            center.append(obj)

    return left,right,center