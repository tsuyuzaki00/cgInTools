import maya.cmds as cmds
from ..Library import mayaRender as mr

cameras = [
    ['C_joe_bodyPersp_00_cam', 'joe_bodyPersp_00', 0, 360],
    ['C_joe_bodyPersp_01_cam', 'joe_bodyPersp_01', 0, 360],
    ['C_joe_bodyFront_00_cam', 'joe_bodyFront', 0, 360],
    ['C_joe_bodySide_00_cam', 'joe_bodySide', 234, 360],
    ['C_joe_handFront_00_cam', 'joe_handFront', 9, 89],
	['C_joe_handSide_00_cam', 'joe_handSide', 9, 89],
    ['C_joe_arm_00_cam', 'joe_arm', 9, 129],
    ['C_joe_facialFront_00_cam', 'joe_facialFront', 360, 940],
    ['C_joe_facialSide_00_cam', 'joe_facialSide', 360, 940],
    ['C_joe_facialPersp_00_cam', 'joe_facialPersp_00', 360, 940],
    ]

def main():
    for cam in cameras:
        _maya_render = mr.MayaRender()
        _maya_render.run_playblast(cam = cam[0], width = 1024, height = 1024, fileName = cam[1], workSpacePath="D:/GMR/cjoe", startFrame = cam[2], endFrame = cam[3])
    cmds.lookThru('persp')

main()