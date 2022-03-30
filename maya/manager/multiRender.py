# -*- coding: iso-8859-15 -*-

import maya.cmds as cmds
from ..library import mayaRender as MR

# demo
test_json = {
    "shotImage":
    [
        {"file":"test/image","camera":"persp","width":1024,"height":1024,"imageFormat":32,"isRenderer":"arnold"}
    ],
    "sequence":
    [
        {"file":"test/sequence","camera":"persp","width":1920,"height":1080,"imageFormat":32,"isRenderer":"arnold","start":5,"end":10}
    ],
    "playblast":
    [
        {"file":"playblast","camera":"persp","width":1920,"height":1080,"start":0,"end":10}
    ]
}

def main():
    _mayaRender = MR.MayaRender()
    for cameras in test_json["shotImage"]:
        _mayaRender.shotImage_create_func(fileName=cameras["file"],camera=cameras["camera"],width=cameras["width"],height=cameras["height"],imageFormat=cameras["imageFormat"],isRenderer=cameras["isRenderer"])
    for cameras in test_json["sequence"]:
        _mayaRender.sequence_create_func(fileName=cameras["file"],camera=cameras["camera"],width=cameras["width"],height=cameras["height"],imageFormat=cameras["imageFormat"],isRenderer=cameras["isRenderer"],startFrame=cameras["start"],endFrame=cameras["end"])
    for cameras in test_json["playblast"]:
        _mayaRender.playblast_create_func(fileName=cameras["file"],camera=cameras["camera"],width=cameras["width"],height=cameras["height"],startFrame=cameras["start"],endFrame=cameras["end"])