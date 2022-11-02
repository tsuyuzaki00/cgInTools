# -*- coding: iso-8859-15 -*-
import cgInTools as cit
from cgInTools.maya.library import skinLB as cs
cit.verReload(cs)

def main():
    vertexID_dicts=[
        {"sourceVertexID":1,"targetVertexID":1},
        {"sourceVertexID":3,"targetVertexID":3},
        {"sourceVertexID":5,"targetVertexID":5},
        {"sourceVertexID":7,"targetVertexID":7},
        {"sourceVertexID":8,"targetVertexID":0},
        {"sourceVertexID":11,"targetVertexID":2},
        {"sourceVertexID":10,"targetVertexID":4},
        {"sourceVertexID":9,"targetVertexID":6},
        {"sourceVertexID":0,"targetVertexID":9},
        {"sourceVertexID":2,"targetVertexID":10},
        {"sourceVertexID":4,"targetVertexID":11},
        {"sourceVertexID":6,"targetVertexID":8},
    ]
    joint_dicts=[
        {"sourceJoint":"sourceA_jnt_C","targetJoint":"targetA_jnt_C"},
        {"sourceJoint":"sourceB_jnt_C","targetJoint":"targetB_jnt_C"},
        {"sourceJoint":"sourceC_jnt_C","targetJoint":"targetC_jnt_C"},
    ]
    copySkin=cs.CopyVertexSkinWeights()
    copySkin.setSourceNode("source_geo_C")
    copySkin.setTargetNode("target_geo_C")
    for vertexID_dict in vertexID_dicts:
        copySkin.setSourceComponent(vertexID_dict["sourceVertexID"])
        copySkin.setTargetComponent(vertexID_dict["targetVertexID"])
        #print(copySkin.querySourceWeights())
        print(copySkin.querySourceWeightsDict())
        #print(copySkin.queryTargetWeights())
        print(copySkin.queryTargetWeightsDict())
        for joint_dict in joint_dicts:
            copySkin.setSourceJoint(joint_dict["sourceJoint"])
            copySkin.setTargetJoint(joint_dict["targetJoint"])
            copySkin.run()

main()