import os
from maya import cmds
from ..MayaLibrary import mayaJsons as mjs

def main():
    jsonName = "mayaJsons_animJson"
    mayaJsonMake = mjs.MayaJsonMake(jsonName = jsonName)
    mayaJsonMake.animJsonExport(attrs = ["tx","ty","tz","rx","ry","rz"])