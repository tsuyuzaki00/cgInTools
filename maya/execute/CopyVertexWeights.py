# -*- coding: iso-8859-15 -*-
from cgInTools.maya.library import cSkin as cs

def main():
    copy_dicts=[
        {"sourceVertexID":1944,"targetVertexID":1944,"sourceJointID":0,"targetJointID":0},
        {"sourceVertexID":1952,"targetVertexID":1952,"sourceJointID":0,"targetJointID":0},
    ]
    copySkin=cs.CopyVertexSkinWeights()
    copySkin.setSourceObj("Dummy_Mesh")
    copySkin.setTargetObj("Dummy_Mesh1")
    copySkin.jointIDCheck()
    for copy_dict in copy_dicts:
        copySkin.setSourceVertexID(copy_dict["sourceVertexID"])
        copySkin.setTargetVertexID(copy_dict["targetVertexID"])
        copySkin.setSourceJointID(copy_dict["sourceJointID"])
        copySkin.setTargetJointID(copy_dict["targetJointID"])
        #copySkin.run()
        copySkin.queryGetWeights()

main()