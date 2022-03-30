import maya.cmds as cmds

def conpornent_pos(get_obj,pos="center"):
    bbox = cmds.xform(get_obj, query=True, boundingBox=True, ws=True)
    up = [(bbox[0]+bbox[3])/2,bbox[4],(bbox[2]+bbox[5])/2]
    down = [(bbox[0]+bbox[3])/2,bbox[1],(bbox[2]+bbox[5])/2]
    right = [bbox[3],(bbox[1]+bbox[4])/2,(bbox[2]+bbox[5])/2]
    left = [bbox[0],(bbox[1]+bbox[4])/2,(bbox[2]+bbox[5])/2]
    front = [(bbox[0]+bbox[3])/2,(bbox[1]+bbox[4])/2,bbox[5]] 
    back = [(bbox[0]+bbox[3])/2,(bbox[1]+bbox[4])/2,bbox[2]]
    center = [(bbox[0]+bbox[3])/2,(bbox[1]+bbox[4])/2,(bbox[2]+bbox[5])/2]
    return center

def main():
    sel = cmds.ls(sl = True)
    center = conpornent_pos(sel[0])
    cmds.move(center[0],center[1],center[2],sel[1:],a=True)

main()