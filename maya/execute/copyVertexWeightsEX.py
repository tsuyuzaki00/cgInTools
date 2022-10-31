# -*- coding: iso-8859-15 -*-
import cgInTools as cit
from cgInTools.maya.library import skinLB as cs
cit.verReload(cs)

def main():
    copy_dicts=[
        {"sourceVertexID":255,"targetVertexID":2293},
        {"sourceVertexID":256,"targetVertexID":2294},
        {"sourceVertexID":386,"targetVertexID":2938},
        {"sourceVertexID":385,"targetVertexID":2937},
        {"sourceVertexID":182,"targetVertexID":2120},
        {"sourceVertexID":11,"targetVertexID":12},
        {"sourceVertexID":30,"targetVertexID":31},
        {"sourceVertexID":230,"targetVertexID":2268},
    ]
    copySkin=cs.CopyVertexSkinWeights()
    copySkin.setSourceObj("DTN_CH_HeraCasual_geo_bodyA_H_008")
    copySkin.setTargetObj("DTN_CH_HERCalw_Geo_bodyA_H_004")
    copySkin.setSourceJoint("DTN_CH_HeraCasual_Skl_Neck1")
    copySkin.setTargetJoint("DTN_CH_HERCalw_Skl_Neck1")
    for copy_dict in copy_dicts:
        copySkin.setSourceVertexID(copy_dict["sourceVertexID"])
        copySkin.setTargetVertexID(copy_dict["targetVertexID"])
        copySkin.run()

    copySkin.setSourceJoint("DTN_CH_HeraCasual_Skl_Head")
    copySkin.setTargetJoint("DTN_CH_HERCalw_Skl_Head")
    for copy_dict in copy_dicts:
        copySkin.setSourceVertexID(copy_dict["sourceVertexID"])
        copySkin.setTargetVertexID(copy_dict["targetVertexID"])
        copySkin.run()

main()