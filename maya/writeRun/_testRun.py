# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from cgInTools.maya.library import objectLB as oLB
cit.reloads([oLB])

camera=oLB.RenderCamera()
camera.setObject("camera1")
camera.addAnimDicts({"matrix":[],"time":-1,"in":"","out":""})
camera.addLightDicts({"light":"","name":"","matrix":[]})

def main():
    pass

main()